"""Small OpenCode adapter: explicit bounded plan -> raw evidence, normalized JSON, RIS.

No service, MCP, library writes, global configuration, paid API or credential discovery.
Reuse the pinned paper-lookup parsers. Run only through an authorized execution owner.
"""
from __future__ import annotations
import argparse, datetime as dt, email.utils, hashlib, html, json, pathlib, re
import os, time, unicodedata, urllib.error, urllib.parse as U, urllib.request as H
import xml.etree.ElementTree as ET
import paginate, arxiv_atom, openalex_abstract

CHANNELS = ['crossref','openalex','semantic-scholar','pubmed','europepmc','arxiv']
DELAY = {'crossref':1.0,'openalex':1.0,'semantic-scholar':1.1,'pubmed':0.4,'europepmc':0.5,'arxiv':3.1}
S2_FIELDS = 'title,year,authors,externalIds,abstract,venue,publicationDate,publicationTypes,openAccessPdf,url'
BASE = 'https://www.ebi.ac.uk/europepmc/webservices/rest/'
def now(): return dt.datetime.now(dt.timezone.utc).isoformat()
def sha(b): return hashlib.sha256(b).hexdigest()
def text(s): return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',str(s or '')))).strip()
def titlekey(s): return ''.join(c for c in unicodedata.normalize('NFKC',text(s)).casefold() if c.isalnum())
def doi(s):
    s = U.unquote(str(s or '').strip())
    return re.sub(r'^(https?://(dx\.)?doi\.org/|doi:\s*)','',s,flags=re.I).strip().lower() or None
def doi_syntax(s): return bool(re.fullmatch(r'10\.\d{4,9}/\S+',doi(s) or ''))
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def url(base,params): return base+'?'+U.urlencode(params)
def retry_delay(value):
    try: return max(0,float(value))
    except (TypeError,ValueError):
        try: return max(0,(email.utils.parsedate_to_datetime(value)-dt.datetime.now(dt.timezone.utc)).total_seconds())
        except (TypeError,ValueError): return 3.0

class FetchError(RuntimeError): pass
class NoRedirect(H.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl): return None

class Client:
    def __init__(self,out,max_requests=50,max_seconds=480,s2_key=None):
        self.out=out; self.logs=[]; self.last={}; self.started=time.monotonic()
        self.max_requests=max_requests; self.max_seconds=max_seconds
        self.s2_key=s2_key
        (out/'raw').mkdir(parents=True)
    def get(self,channel,target,job):
        for attempt in range(2):
            if len(self.logs)>=self.max_requests or time.monotonic()-self.started>self.max_seconds:
                raise FetchError('request/time bound reached')
            time.sleep(max(0,DELAY[channel]-(time.monotonic()-self.last.get(channel,0))))
            entry={'requestId':len(self.logs)+1,'job':job,'channel':channel,'url':target,'at':now(),'attempt':attempt+1}
            started=time.monotonic(); data=b''; headers={}; status=None
            try:
                headers_out={'User-Agent':'paper-lookup-opencode/2.2.1-r09 (bounded research metadata)'}
                if self.s2_key and channel=='semantic-scholar':
                    if U.urlparse(target).scheme!='https' or U.urlparse(target).netloc!='api.semanticscholar.org':
                        raise FetchError('Refuse key outside the Semantic Scholar HTTPS API')
                    headers_out['x-api-key']=self.s2_key
                req=H.Request(target,headers=headers_out)
                # Do not redirect a private authentication header to another host.
                open_request=H.build_opener(NoRedirect).open if 'x-api-key' in headers_out else H.urlopen
                with open_request(req,timeout=25) as response:
                    status=response.status; headers=dict(response.headers); data=response.read(8*1024*1024+1)
                if len(data)>8*1024*1024: raise FetchError('response exceeds 8 MiB bound')
            except urllib.error.HTTPError as e:
                status=e.code; headers=dict(e.headers); data=e.read(1024*1024)
            except Exception as e:
                entry['transportError']=type(e).__name__
            self.last[channel]=time.monotonic()
            entry.update(status=status,elapsedSeconds=round(time.monotonic()-started,3),bytes=len(data))
            entry['headers']={k:v for k,v in headers.items() if k.lower() in ['retry-after','content-type'] or 'ratelimit' in k.lower()}
            if data:
                path=f'raw/{entry["requestId"]:03}-{channel}.bin'
                (self.out/path).write_bytes(data); entry.update(raw=path,sha256=sha(data))
            self.logs.append(entry)
            with (self.out/'requests.jsonl').open('a',encoding='utf-8') as f: f.write(json.dumps(entry,ensure_ascii=False)+'\n')
            if status==200 and not entry.get('transportError'): return data,entry
            if status in [429,503] and not attempt:
                wait=retry_delay(next((v for k,v in headers.items() if k.lower()=='retry-after'),None))
                if wait<=30 and time.monotonic()-self.started+wait<self.max_seconds:
                    time.sleep(wait); continue
            # 404 means absent at this endpoint, never a DOI validity decision.
            raise FetchError(f'HTTP {status}' if status else entry.get('transportError','transport failure'))

def parse_json(data):
    x=json.loads(data)
    if not isinstance(x,dict) or x.get('error') or x.get('errCode') or x.get('status')=='failed':
        raise ValueError('API error or invalid envelope in response')
    return x

def arxiv_page(data):
    if data.strip().startswith(b'Rate exceeded'): raise ValueError('arXiv throttle body')
    root=ET.fromstring(data)
    if root.tag!='{http://www.w3.org/2005/Atom}feed': raise ValueError('not an Atom feed')
    entries=root.findall('atom:entry',arxiv_atom.NS)
    if any(text(e.findtext('atom:title',namespaces=arxiv_atom.NS))=='Error' for e in entries): raise ValueError('arXiv Error entry')
    return [arxiv_atom.parse_entry(e) for e in entries],int(root.findtext('opensearch:totalResults',namespaces=arxiv_atom.NS)),root.findtext('atom:title',namespaces=arxiv_atom.NS)

def record(channel,r,origin):
    ids={}; dates={}; authors=[]; locations=[]; relations=[]; abstract=None; kind=None; venue=None; year=None; title=None
    if channel=='crossref':
        ids={'doi':doi(r.get('DOI'))}; title=(r.get('title') or [None])[0]; kind=r.get('type')
        authors=[text(' '.join([a.get('given',''),a.get('family','')])) for a in r.get('author',[])]
        dates={k:r[k] for k in ['published','published-online','published-print','issued'] if k in r}
        y=(r.get('published') or r.get('issued') or {}).get('date-parts',[[None]])
        year=y[0][0]; venue=(r.get('container-title') or [None])[0]; abstract=r.get('abstract')
        for rel,values in (r.get('relation') or {}).items():
            relations += [{'type':rel,'target':v,'assertedBy':'Crossref deposit','evidence':origin} for v in values]
        relations += [{'type':'update-to','target':v,'assertedBy':'Crossref deposit','evidence':origin} for v in r.get('update-to',[])]
        locations=[{'url':v.get('URL'),'version':v.get('content-version'),'license':r.get('license'), 'availability':'publisher link; access unverified'} for v in r.get('link',[])]
    elif channel=='europepmc':
        ids={'doi':doi(r.get('doi')),'europepmc':str(r.get('source'))+':'+str(r.get('id')),'pmid':r.get('pmid'),'pmcid':r.get('pmcid')}
        if r.get('source')=='MED': ids['pmid']=str(r['id'])
        title=r.get('title'); year=r.get('pubYear'); abstract=r.get('abstractText'); kind=r.get('pubTypeList')
        authors=[a.get('fullName') or a.get('collectiveName') for a in r.get('authorList',{}).get('author',[])] or [r.get('authorString')]
        ji=r.get('journalInfo') or {}; venue=(ji.get('journal') or {}).get('title') or r.get('journalTitle')
        dates={k:r[k] for k in ['firstPublicationDate','electronicPublicationDate','firstIndexDate'] if k in r}
        dates['journalIssue']=ji.get('dateOfPublication')
        locations=[{'url':v.get('url'),'version':None,'license':r.get('license'),'availability':v.get('availability'),'documentStyle':v.get('documentStyle')} for v in r.get('fullTextUrlList',{}).get('fullTextUrl',[])]
        if r.get('pmcid') and r.get('isOpenAccess')=='Y': locations.append({'url':BASE+r['pmcid']+'/fullTextXML','version':'repository JATS','license':r.get('license'),'availability':'API-declared OA; acquisition untested'})
        if r.get('commentCorrectionList'): relations.append({'type':'commentCorrectionList','target':r['commentCorrectionList'],'assertedBy':'Europe PMC','evidence':origin})
    elif channel=='openalex':
        ids={'doi':doi(r.get('doi')),'openalex':r.get('id'),'pmid':(r.get('ids',{}).get('pmid') or '').rstrip('/').split('/')[-1] or None}
        title=r.get('title'); year=r.get('publication_year'); dates={'publication_date':r.get('publication_date')}; kind=r.get('type')
        authors=[a.get('author',{}).get('display_name') for a in r.get('authorships',[])]
        abstract=openalex_abstract.summarize(r).get('abstract')
        venue=((r.get('primary_location') or {}).get('source') or {}).get('display_name')
        locations=[{'url':l.get('pdf_url') or l.get('landing_page_url'),'version':l.get('version'),'license':l.get('license'),'availability':'API-declared OA' if l.get('is_oa') else 'access unverified'} for l in r.get('locations',[])]
    elif channel=='semantic-scholar':
        ext=r.get('externalIds') or {}; ids={'doi':doi(ext.get('DOI')),'pmid':ext.get('PubMed'),'pmcid':ext.get('PubMedCentral'),'semanticScholar':r.get('paperId')}
        title=r.get('title'); year=r.get('year'); abstract=r.get('abstract'); venue=r.get('venue'); kind=r.get('publicationTypes'); dates={'publicationDate':r.get('publicationDate')}
        authors=[a.get('name') for a in r.get('authors',[])]
        if ext.get('ArXiv'): relations.append({'type':'associated-arxiv','target':ext['ArXiv'],'assertedBy':'Semantic Scholar externalIds; version identity needs review','evidence':origin})
        if r.get('openAccessPdf'): locations=[{'url':r['openAccessPdf'].get('url'),'license':r['openAccessPdf'].get('license'),'version':None,'availability':r['openAccessPdf'].get('status')}]
    elif channel=='pubmed':
        ids={'pmid':str(r['uid'])}
        for a in r.get('articleids',[]):
            if a['idtype'] in ['doi','pmc']: ids[{'doi':'doi','pmc':'pmcid'}[a['idtype']]]=doi(a['value']) if a['idtype']=='doi' else a['value']
        title=r.get('title'); authors=[a.get('name') for a in r.get('authors',[])]; venue=r.get('fulljournalname'); kind=r.get('pubtype')
        dates={k:r.get(k) for k in ['pubdate','epubdate','sortpubdate','history']}; m=re.search(r'\d{4}',r.get('pubdate','')); year=m.group() if m else None
    elif channel=='arxiv':
        ids={'arxiv':r['arxiv_id']}; title=r['title']; authors=r['authors']; year=(r.get('published') or '')[:4] or None
        dates={k:r.get(k) for k in ['published','updated']}; abstract=r.get('abstract'); kind='preprint'; venue='arXiv'
        if r.get('doi'): relations.append({'type':'published-doi','target':doi(r['doi']),'assertedBy':'arXiv submitted journal DOI; not an identical publication version','evidence':origin})
        locations=[{'url':r.get('pdf_url'),'version':r.get('arxiv_id_versioned'),'license':None,'availability':'repository link; not acquired'}]
    ids={k:str(v) for k,v in ids.items() if v}
    key=next((k+':'+ids[k] for k in ['doi','arxiv','pmid','pmcid','openalex','semanticScholar','europepmc'] if ids.get(k)),None)
    if not key or not title: raise ValueError('record missing identity/title')
    return {'recordId':origin['job']+':'+str(origin['requestId'])+':'+str(origin['index']),'workId':key,'identifiers':ids,'title':text(title),'authors':[text(a) for a in authors if a],'year':str(year) if year else None,'dates':dates,'venue':text(venue) or None,'type':kind,'abstract':text(abstract) or None,'discovery':origin,'metadata':{'status':'single-source-unverified'},'fullText':{'status':'located-only' if any(x.get('url') for x in locations) else 'not-attempted','locations':[x for x in locations if x.get('url')]},'reading':{'status':'unread','fullTextRead':False},'relations':relations,'visualCheck':'not-performed','supplementStatus':'not-read'}

def merge(records):
    groups=[]; decisions=[]
    for r in records:
        matches=[g for g in groups if any(v==g['identifiers'].get(k) for k,v in r['identifiers'].items())]
        g=matches[0] if len(matches)==1 else None
        conflicting_doi=bool(g and r['identifiers'].get('doi') and g['identifiers'].get('doi') and r['identifiers']['doi']!=g['identifiers']['doi'])
        if g and not conflicting_doi and titlekey(r['title'])==titlekey(g['title']):
            g['recordIds'].append(r['recordId']); g['identifiers'].update(r['identifiers'])
            decisions.append({'action':'merge-metadata','record':r['recordId'],'into':g['workId'],'basis':'shared exact identifier + normalized title','datesAndAllValues':'retained in records; no overwrite of raw sources'})
        else:
            work=r['workId']
            if any(x['workId']==work for x in groups): work+=':unresolved:'+sha(r['recordId'].encode())[:8]
            groups.append({'workId':work,'identifiers':dict(r['identifiers']),'title':r['title'],'recordIds':[r['recordId']]})
            if matches: decisions.append({'action':'keep-separate-identity-conflict','record':r['recordId'],'candidates':[x['workId'] for x in matches]})
    # Title alone never merges publications. Preprint/correction links remain edges.
    return groups,decisions

def fetch_job(client,j):
    c=j['channel']; kind=j.get('kind','search'); n=j.get('page_size',5); state='*' if c in ['crossref','openalex','europepmc'] else 0
    result={'id':j['id'],'channel':c,'kind':kind,'query':j.get('query'),'params':j.get('params',{}),'started':now(),'status':'unqueried','reportedTotal':None,'returned':None,'pages':[],'stop':None}
    records=[]
    try:
        for page_no in range(j.get('max_pages',1)):
            p=dict(j.get('params',{})); q=j.get('query',''); nxt=None; echoed=None
            if kind=='fulltext':
                ident=j['identifier']; assert re.fullmatch(r'PMC\d+',ident)
                data,req=client.get(c,BASE+ident+'/fullTextXML',j['id']); root=ET.fromstring(data)
                if root.find('.//body') is None or not ''.join(root.find('.//body').itertext()).strip(): raise ValueError('JATS metadata-only; no readable body')
                doi_ids=[doi(e.text) for e in root.findall('.//article-id') if e.get('pub-id-type')=='doi']
                if j.get('expected_doi') and doi(j['expected_doi']) not in doi_ids: raise ValueError('fulltext DOI identity mismatch')
                result.update(status='obtained-not-read',returned=1,reportedTotal=None,raw=req['raw'],sha256=req['sha256'],doi=doi_ids,license=[text(''.join(e.itertext())) for e in root.findall('.//license')],bodyPresent=True,stop='single authorized fulltext')
                break
            if c=='crossref':
                if kind=='lookup':
                    if not doi_syntax(j['identifier']): raise ValueError('DOI syntax-invalid; no network lookup')
                    target='https://api.crossref.org/works/'+U.quote(doi(j['identifier']),safe='')
                elif kind=='agency': target='https://api.crossref.org/works/'+U.quote(doi(j['identifier']),safe='')+'/agency'
                else: target=url('https://api.crossref.org/works',{**p,'query.bibliographic':q,'cursor':state,'rows':n})
            elif c=='openalex': target=url('https://api.openalex.org/works',{**p,**({'search':q} if q else {}),'cursor':state,'per_page':n})
            elif c=='europepmc': target=url(BASE+'search',{**p,'query':q,'format':'json','resultType':'core','cursorMark':state,'pageSize':n})
            elif c=='semantic-scholar':
                target=('https://api.semanticscholar.org/graph/v1/paper/'+U.quote(j['identifier'],safe='')+'?'+U.urlencode({'fields':S2_FIELDS})) if kind=='lookup' else url('https://api.semanticscholar.org/graph/v1/paper/search',{**p,'query':q,'fields':S2_FIELDS,'offset':state,'limit':n})
            elif c=='pubmed': target=url('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi',{**p,'db':'pubmed','retmode':'json','term':q,'retstart':state,'retmax':n,'tool':'opencode_r09'})
            elif c=='arxiv': target=url('https://export.arxiv.org/api/query',{**p,**({'id_list':j['identifier']} if kind=='lookup' else {'search_query':q}),'start':state,'max_results':n})
            else: raise ValueError('unsupported channel')
            data,req=client.get(c,target,j['id'])
            if c=='arxiv':
                rows,total,echoed=arxiv_page(data); nxt=state+len(rows) if rows and state+len(rows)<total else None
            else:
                payload=parse_json(data)
                if c=='crossref' and kind=='agency':
                    result.update(status='registration-agency-reported',agency=payload['message'],returned=1,stop='single lookup',requestId=req['requestId']); break
                if c=='crossref' and kind=='lookup':
                    rows=[payload['message']]; total=1
                    if doi(rows[0].get('DOI'))!=doi(j['identifier']): raise ValueError('returned DOI mismatch')
                elif c in ['crossref','openalex','europepmc']:
                    required={'crossref':('message','items'),'openalex':('meta','results'),'europepmc':('hitCount','resultList')}[c]
                    if required[0] not in payload or (c=='crossref' and 'items' not in payload['message']) or (c!='crossref' and required[1] not in payload): raise ValueError('missing list envelope')
                    parsed=paginate.APIS[c].parse(payload,state); rows,total,nxt=parsed.records,parsed.total,parsed.next_state
                    echoed=payload.get('request'); result.setdefault('costReportedByAPI',[]).append(payload.get('meta',{}).get('cost_usd'))
                elif c=='semantic-scholar':
                    if kind=='lookup': rows=[payload]; total=1
                    else:
                        if 'data' not in payload or 'total' not in payload: raise ValueError('missing S2 search envelope')
                        rows=payload['data']; total=payload['total']; nxt=payload.get('next')
                elif c=='pubmed':
                    x=payload['esearchresult']
                    if x.get('errorlist'): raise ValueError('PubMed query error; inspect raw errorlist')
                    total=int(x['count']); ids=x['idlist']; echoed=x.get('querytranslation'); nxt=state+len(ids) if ids and state+len(ids)<total else None
                    if ids:
                        data2,req2=client.get(c,url('https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi',{'db':'pubmed','retmode':'json','id':','.join(ids),'tool':'opencode_r09'}),j['id'])
                        summ=parse_json(data2)['result']; rows=[summ[i] for i in ids]; req=req2
                    else: rows=[]
            if result['reportedTotal'] is None: result['reportedTotal']=total
            result['pages'].append({'page':page_no+1,'requestId':req['requestId'],'raw':req['raw'],'returned':len(rows),'reportedTotal':total,'queryAsReturned':echoed,'next':nxt})
            for index,r in enumerate(rows):
                records.append(record(c,r,{'channel':c,'job':j['id'],'kind':kind,'query':q,'at':req['at'],'requestId':req['requestId'],'raw':req['raw'],'index':index}))
            result.update(status='ok',returned=len(records))
            if nxt is None or not rows: result['stop']='endpoint exhausted'; break
            if nxt==state: result['stop']='cursor repeated; incomplete unless count reconciles'; break
            state=nxt
        if result['stop'] is None: result['stop']='explicit page bound; incomplete'
        if result['status']=='ok' and result['stop']=='endpoint exhausted' and result['reportedTotal']!=len(records):
            result['status']='incomplete-count-mismatch'
    except (FetchError,ValueError,KeyError,TypeError,ET.ParseError,AssertionError) as e:
        result.update(status='partial-failed' if records else 'failed',error=str(e),returned=len(records) if records else None,stop='error; no fabricated zero')
        if c=='crossref' and kind=='lookup' and str(e)=='HTTP 404':
            result.update(status='not-found-at-endpoint',doiState='not-indexed-by-crossref; registration/resolution not decided',stop='endpoint-specific absence; not invalid DOI')
        elif str(e)=='DOI syntax-invalid; no network lookup':
            result.update(status='invalid-identifier-syntax',doiState='syntax-invalid; registration not queried')
    result['requestIds']=[q['requestId'] for q in client.logs if q['job']==j['id']]
    result['finished']=now()
    return result,records

def export(out,records,jobs,channels):
    for job in jobs:
        if job['status']=='obtained-not-read':
            for r in records:
                if r['identifiers'].get('doi') in job.get('doi',[]):
                    r['fullText'].update(status='obtained',path=job['raw'],sha256=job['sha256'],version='Europe PMC JATS; DOI matched; visual/SI unverified',license=job['license'],acquisitionJob=job['id'])
    groups,decisions=merge(records)
    result={'schemaVersion':1,'generated':now(),'channels':channels,'jobs':jobs,'records':records,'works':groups,'mergeDecisions':decisions,'relations':[{'recordId':r['recordId'],**x} for r in records for x in r['relations']], 'meaning':'Metadata records and related publication versions; counts are not independent studies or experiments.'}
    dump(out/'results.json',result)
    lookup={r['recordId']:r for r in records}; lines=[]
    for g in groups:
        r=lookup[g['recordIds'][0]]
        types=r['type']; types=types.get('pubType',[]) if isinstance(types,dict) else types
        types=[types] if isinstance(types,str) else (types or [])
        journal=any(str(t).lower() in ['article','journal-article','journal article','journalarticle'] for t in types)
        lines+=['TY  - JOUR' if journal else 'TY  - GEN','ID  - '+g['workId'],'TI  - '+text(r['title'])]
        lines+=['AU  - '+text(a) for a in r['authors']]
        for k,v in [('PY',r['year']),('JO',r['venue']),('DO',g['identifiers'].get('doi')),('UR',('https://doi.org/'+g['identifiers']['doi']) if g['identifiers'].get('doi') else None)]:
            if v: lines.append(k+'  - '+text(v))
        lines+=['N1  - Metadata export only. See results.json and requests.jsonl for provenance, conflicts, versions and reading state.','ER  - ','']
    (out/'results.ris').write_text('\n'.join(lines),encoding='utf-8')
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--plan',required=True); ap.add_argument('--out',required=True)
    ap.add_argument('--use-s2-key',action='store_true',help='Explicitly read S2_API_KEY from this process environment; never log its value')
    args=ap.parse_args(); plan=json.loads(pathlib.Path(args.plan).read_text(encoding='utf-8-sig')); out=pathlib.Path(args.out).resolve()
    s2_key=os.environ.get('S2_API_KEY') if args.use_s2_key else None
    if args.use_s2_key and not s2_key: raise SystemExit('S2_API_KEY unavailable to this process; configure locally and start a new process.')
    if out.exists(): raise SystemExit('Output already exists; use a fresh explicit run directory to preserve evidence.')
    jobs=plan['jobs']; assert len(jobs)<=30 and len({j['id'] for j in jobs})==len(jobs)
    assert sum(j.get('page_size',5)*j.get('max_pages',1) for j in jobs)<=1000, 'Plan exceeds 1000 metadata record bound'
    for j in jobs:
        assert j['channel'] in CHANNELS and j.get('kind','search') in ['search','lookup','agency','fulltext']
        assert 1<=j.get('page_size',5)<=100 and 1<=j.get('max_pages',1)<=5
        assert not any(k.lower() in ['api_key','email','mailto','token'] for k in j.get('params',{}))
        if j.get('kind')=='fulltext': assert j['channel']=='europepmc' and doi_syntax(j.get('expected_doi'))
    requests=plan.get('max_requests',50); seconds=plan.get('max_seconds',480)
    assert 1<=requests<=50 and 1<=seconds<=900
    out.mkdir(parents=True); dump(out/'plan.json',plan)
    client=Client(out,requests,seconds,s2_key=s2_key); all_records=[]; results=[]
    channels={c:{'status':'not-queried','returned':None} for c in CHANNELS+['zotero-live','third-party','institutional','scholar','core','unpaywall']}
    for job in jobs:
        result,rows=fetch_job(client,job); results.append(result); all_records+=rows
        export(out,all_records,results,channels)
        print(json.dumps({k:result[k] for k in ['id','status','reportedTotal','returned','stop']},ensure_ascii=False),flush=True)
    for c in CHANNELS:
        js=[j for j in results if j['channel']==c]
        if js:
            good=[j for j in js if j['status'] in ['ok','obtained-not-read','registration-agency-reported','not-found-at-endpoint']]
            channels[c]={'status':'tested' if len(good)==len(js) else ('partial' if good else 'failed'),'returned':sum(1 for r in all_records if r['discovery']['channel']==c) if good else None,'fullTextAcquired':sum(j['status']=='obtained-not-read' for j in js),'jobs':[j['id'] for j in js]}
    result=export(out,all_records,results,channels)
    dump(out/'run.json',{'finished':now(),'requests':len(client.logs),'records':len(all_records),'works':len(result['works']),'credentialsUsed':bool(s2_key and any(x['channel']=='semantic-scholar' for x in client.logs)),'scriptSha256':sha(pathlib.Path(__file__).read_bytes()),'planSha256':sha(pathlib.Path(args.plan).read_bytes()),'fullTextRead':False,'failures':[r['id'] for r in results if r['status'] in ['failed','partial-failed','incomplete-count-mismatch','invalid-identifier-syntax']]})

if __name__=='__main__': main()
