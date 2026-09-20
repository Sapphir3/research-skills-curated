---
name: scientific-slides-opencode
description: Produce a bounded editable scientific PPTX from accepted evidence, using an existing template and local native objects; verify data, Chinese, formulas, citations and a native PowerPoint render without changing scientific conclusions.
license: MIT
metadata:
  version: "1.0.0-r16.1"
  upstream: "K-Dense-AI/scientific-agent-skills"
  upstream-commit: "330c8e764435a731eff571e3efdda70b363d0792"
---

# Scientific slides — editable local delivery

Bounded OpenCode R15 adaptation. This is the sole presentation-production entry for
the accepted evidence package. It is not another writing, analysis, retrieval or
review workflow. Preserve the existing author responsibility and role permissions.
The upstream image/PDF generation defaults are replaced for editable PPTX delivery.

## Inputs and ownership

- Read the requested audience, page limit, exact approved source/result paths and
  claim limits. Use a supplied template or authorized existing assets; preserve the
  originals. If none is supplied, a simple consistent style is sufficient.
- Label a public or synthetic example accurately. Do not invent affiliations,
  speaker names, measurements, units, experimental counts, references or study results.
- Author owns content and the final academic artifact. If its runtime forbids shell
  execution, it sends a bounded production package through the primary to the existing
  worker. Author must stop writing that path before the primary assigns it to worker;
  hand over the exact file/version/hash and reclaim it only after worker stops.
  Neither this skill nor the handoff expands permissions or creates a role.
- Missing sources return through the primary to document; changed results to analyst;
  scientific meaning/methods to the primary/researcher. Continue independent work.

## One production path

1. Fix a small outline from accepted text and results. Keep one point per slide,
   consistent terminology, generous margins and readable titles/body/citations.
   Do not reopen the approved writing workflow, run fresh analysis, or retrieve an
   arbitrary quota of papers. Notes can hold exact source anchors and long URLs.
2. Use the already available `python-pptx` implementation for this verified path.
   Templates remain input copies; edit native text, tables and charts. Match the
   supplied template's design where applicable. No template was tested in R15.
3. Bind chart series and table values directly to approved derived files. Native XY
   charts must contain their workbook data. Preserve source-row identity when
   sorting solely for a display line; never silently filter or recalculate results.
4. Use installed Chinese fonts explicitly, including East Asian run properties.
   For simple equations, native rich text with real subscript/superscript is acceptable
   and must be described as such. A textbox is not an Office equation-editor object.
   Complex structured equations require a separate task-specific decision/check.
5. Reuse figures without altering scientific content. Do not rasterize the entire
   slide or substitute generated images for data, chart values, formulas or citations.
   No paid image service, default external upload, mandatory decoration or default
   upstream-brand attribution is needed for this local delivery.
6. Write a derived PPTX in the agreed output directory. Word/PDF are optional only
   for a real requested use; do not create them as proof of editable PPTX capability.

## Acceptance and handoff

- Inspect saved OOXML: slide count, text, equations, chart caches plus embedded
  workbooks, native tables, citation hyperlinks, source values and package integrity.
- Open the actual PPTX in installed Microsoft PowerPoint, inspect its objects and
  render every slide with its native exporter. Inspect the resulting page images;
  repair actual clipping, overlap, illegible Chinese/math or inaccurate labels.
  A PDF or library preview alone is not native-PPTX acceptance.
- On a derived test copy, change representative native text/formula, a table cell and
  chart data, save and reopen to verify persistence. Do not mutate source inputs or
  the accepted final deck. Record exactly which objects and software were checked.
- After chart-data edits, compare the embedded workbook and native series cache.
  R15's PowerPoint build retained its old cache after a workbook-only COM change;
  the verified mechanical edit updates workbook and native series together before
  saving. Do not assume refresh/close alone synchronizes every chart representation.
- Keep a concise source/hash, environment, execution and limitations record. Distinguish
  host production, OpenCode discovery/loading, actual role/model calls and independent
  review. None implies scientific validity or tested template/Word/PDF support.
- Follow existing HumanReview and `authorized_review_chain` triggers; this skill
  neither grants publication approval nor adds a compulsory duplicate full review.

## Verified scope and recovery

R15 covers a four-page public Norris example, simple editable text equations,
Chinese, two native XY charts and native tables, using local Python and PowerPoint.
Use the exact runtime paths/version record of the current task; a Codex-bundled path
is not an OpenCode dependency installer or portability guarantee.

The candidate is only in the R15 directory. One child-process configuration overlay
is sufficient for discovery checks; normal discovery must be checked after it ends.
Do not edit shared skills, role permissions, model selection or global configuration.
Stop explicitly referencing this candidate to withdraw it. Before restoring a task
state or output, compare final hashes and preserve/merge later user modifications.

Upstream source and MIT notice are retained in the R15 provenance bundle. Technical
chart behavior is based on the MIT `python-pptx` library and its official chart API;
native open/export behavior uses Microsoft's installed PowerPoint object model.
