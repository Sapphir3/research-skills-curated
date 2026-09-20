"""Static identity and packaging checks; never execute candidate code."""
from pathlib import Path
import ast
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
names = [s['name'] for s in manifest['skills']]
assert len(names) == len(set(names))
assert {p.parent.name for p in ROOT.rglob('SKILL.md') if '.git' not in p.parts} == set(names)
files_checked = 0
for skill in manifest['skills']:
    name = skill['name']
    assert re.fullmatch(r'[a-z0-9-]+-opencode', name)
    assert skill['path'] == name and skill['targetApp'] == 'opencode'
    directory = ROOT / name
    files = {p.relative_to(directory).as_posix(): p for p in directory.rglob('*') if p.is_file()}
    assert set(files) == set(skill['files']), f'{name}: extra or missing runtime file'
    for relative, path in files.items():
        assert not path.is_symlink(), f'No runtime link: {path}'
        assert '..' not in Path(relative).parts
        assert hashlib.sha256(path.read_bytes()).hexdigest() == skill['files'][relative], path
        assert not any(part in {'tests','.git','node_modules','__pycache__'} for part in path.relative_to(directory).parts)
        text = path.read_text(encoding='utf-8')
        assert not re.search(r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:ghp_|gho_|github_pat_)[A-Za-z0-9_]{20,}', text), path
        if path.suffix == '.py': ast.parse(text,filename=str(path))
        if path.suffix == '.md':
            for link in re.findall(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)', text):
                if re.match(r'^(https?://|mailto:|#)',link): continue
                target = link.split('#',1)[0]
                assert (path.parent/target).is_file(), f'{path}: missing relative resource {target}'
        files_checked += 1
    text = files['SKILL.md'].read_text(encoding='utf-8')
    frontmatter = text.split('---',2)[1]
    assert re.search(r'^name:\s*'+re.escape(name)+r'\s*$',frontmatter,re.M)
    assert re.search(r'^  version:\s*"'+re.escape(skill['version'])+r'"\s*$',frontmatter,re.M)
    assert 'LICENSE' in files or 'LICENSE.md' in files
    assert skill['upstream']['commit'] and skill['acceptedAdapter']['skillSha256']
print(json.dumps({'passed':True,'skills':len(names),'runtimeFiles':files_checked,'candidateCodeExecuted':False}))
