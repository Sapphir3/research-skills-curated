---
name: experimental-design-opencode
description: Define measurement goals, experimental units, biological subsampling, technical repeats, batches, controls and predeclared inclusion criteria. Use for planning a study or checking its actual design before analysis; do not invent missing replication or retrospectively randomize collected data.
license: MIT
metadata:
  version: "1.0.0-r16.1"
  upstream: "K-Dense-AI/scientific-agent-skills@330c8e764435a731eff571e3efdda70b363d0792/skills/experimental-design"
---

# Experimental design

## Bounded OpenCode R13 use

This is a narrowed guidance adaptation of the pinned upstream skill. It includes
no allocation generator or new controller. Existing role permissions prevail.
The primary/researcher settles scientific design; analyst owns derived analysis;
worker only executes a settled mechanical step. A read-only role does not write,
run scripts, or delegate. Do not change model bindings or the review route.

Start with the user's actual measurement objective and available materials.
Previous examples and file extensions do not determine a new research topic.
If data are missing, ask once for the material facts and continue useful local
checks. Do not substitute paper-fit parameters or synthetic data for a real sample.

Record only what the task needs:

- What is estimated or compared, in which units, and over what population or object.
- The entity to which treatment is independently assigned/applied; biological
  source, specimen, chip, batch and acquisition order; paired or nested relations.
- Which observations are biological subsamples, repeated measurements or technical
  repeats. Pixels, frames, objects and files are not automatically independent n.
- Existing controls, randomization and blinding, or their absence. Do not claim
  randomization balances every finite sample or by itself proves a causal effect.
- Instrument calibration and its uncertainty; image scale, axes and frame interval
  when relevant. Unknown metadata remain unknown, never inferred from a filename.
- Existing missing-value, mask/bad-point and exclusion rules, fixed before analysis.

For a future experiment, block or randomize only at justified levels and retain
the seed/schedule if generated. Do not require new DOE software or a sample-size
calculation for every descriptive task. A power calculation needs an estimand,
design, meaningful effect and defensible variance assumptions.

For existing data, preserve the recorded design. If enough independent units and
identifiers exist, appropriate aggregation or a justified hierarchical model may
correct a pseudoreplicated analysis. It cannot create absent replication or undo
complete treatment/batch confounding. Measurements below a treatment unit may be
biological subsamples, not necessarily technical repeats. Inference levels must
match the intended question; a single sample can support a descriptive pilot only.

Before processing, hand analyst the exact input paths/version/hash, unit hierarchy,
approved method and exclusions, required derived outputs and reference/error/pass
criteria. Changes to calibration, experimental hierarchy, exclusion or scientific
model return through primary to researcher; never select them to favor results.
Each output path has one writer; a handoff stops the former writer and records
path, version and hash. Preserve originals, keep derived masks/results separate.

Use the existing R07 necessary/optional review boundary and authorized_review_chain;
do not add a second homogeneous full review. Successful parsing or a numeric
reference does not demonstrate experimental, physical or scientific validation.

Source: the pinned upstream design overview and design-types reference, narrowed
for OpenCode; [NC3Rs experimental-unit guidance](https://eda.nc3rs.org.uk/experimental-design-unit).
The R13 source/difference/hash receipt is maintained by the configuration project,
not copied into every research deliverable. Stable global adoption remains R18.
