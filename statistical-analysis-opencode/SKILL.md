---
name: statistical-analysis-opencode
description: Analyze measured data with a declared estimand, units and independent-unit hierarchy; preserve originals, diagnose fits and quantify uncertainty. Prefer an existing Python analysis and request scientific decisions when metadata or assumptions are unresolved. ImageJ and ParaView outputs need their calibration and processing provenance.
license: MIT
metadata:
  version: "1.0.0-r16.1"
  upstream: "K-Dense-AI/scientific-agent-skills@330c8e764435a731eff571e3efdda70b363d0792/skills/statistical-analysis"
---

# Statistical analysis of measurements

## Bounded OpenCode R13 use

This narrowed guidance replaces the upstream automatic test-selection workflow.
No new controller, mandatory software stack or writing format is introduced.
Existing permissions prevail: researcher settles scientific design/method, analyst
owns derived analysis/diagnostics/error, engineer handles complex implementation,
worker runs settled mechanical steps, document reads sources, explorer only locates
unknown inputs, and critic questions a method when needed. Primary coordinates.

1. Identify the actual outcome/estimand and read the project guidance. Inspect exact
   input paths, types, versions and hashes, units/calibration, independent-unit and
   batch relationships, paired/time structure, missing codes and existing masks or
   exclusions as needed by the requested output. Check authorized materials first;
   ask only about unknowns that block current correctness, interpretation, permissions
   or a consequential action. Name that step, continue independent work, and do not
   repeatedly request known-unavailable inputs. Never fabricate data, scales or n.
2. Before processing, fix the model and error assumptions, inclusion rules, minimal
   outputs and known-reference/error/pass criteria. Preserve raw files and metadata;
   derived tables/masks retain original row/object/frame mapping and reasons.
3. Reuse a suitable existing Python runtime and script. Record the actual interpreter
   and package versions. Add only required dependencies in a bounded environment;
   do not replace the user's default runtime or install a full Bayesian/DOE stack.
4. Fit the declared quantity, then examine residual patterns, heteroscedasticity,
   time dependence, leverage/influence and identifiability as applicable. A normality
   p-value alone does not authorize changing the model, using a rank test, deleting
   points, or asserting assumptions are satisfied. Flag influence; retain observations.
5. Match uncertainty to the source: repeatability, calibration/shared systematic
   error, parameter covariance and independent-unit variation are different. Preserve
   covariance. In weighted fitting, justify weights and covariance scaling; if x has
   meaningful measurement error, ordinary y-on-x least squares may be inadequate.
6. Report estimates and warranted uncertainty in their units, observations versus
   independent units, actual diagnostics and unresolved limitations. Statistical
   significance does not prove existence or importance; a non-significant result
   does not establish no effect. Use multiplicity handling only for a defined family.
   Do not choose models, subgroups, priors or exclusions to obtain a desired result.

The user currently uses ImageJ/ParaView for image/geometry work and prefers Python
for future data analysis in place of prior MATLAB/OriginPro use. This is a routing
preference, not an already-tested replacement of all functions or formats:

- Excel: retain workbook/sheet/cell origins, units, IDs, formulas and cached values.
  Reading a formula cache does not recalculate it; missing caches are not zero.
  Do not run macros or overwrite the workbook. Confirm the actual Excel format.
- Images: preserve originals, calibrated pixel/voxel spacing, channels/axes, time,
  ROIs/masks, and ImageJ macro/settings or other processing record. Do not use visual
  estimates or enhanced display intensities as original quantitative measurements.
- STL: surface geometry is not a raw microscopy image. Establish coordinate units,
  source/segmentation/scale history and mesh quality before length/area/volume claims.
  Open boundaries, inconsistent normals and non-manifold geometry require explicit
  treatment; do not silently repair, smooth, decimate or fill holes. Facets are not n.
- PIV only if actual tracer image pairs and timing/calibration support it. Preserve
  raw displacement, s2n, masks/invalid flags and an optional separate interpolation
  copy. Default demo scales and interpolated vectors are not measurements.

For an explicitly bounded software/workflow check, reuse a suitable labeled local
synthetic or known-reference example; report only the tested behavior. Missing
physical units, calibration, timing or independent-unit metadata stay unknown and
block dependent scientific claims, not unrelated work. Real-data analysis is
conditional on an actual commissioned task and available inputs; a real sample
may support descriptive method checking without supporting population inference.
Do not claim empirical validation or general format/interface support from a fixture.
Unselected future formats and tools are not prerequisites or required adapters.

Any method/unit/exclusion/hierarchy change returns to primary and researcher. Each
output path has one writer; transfer path/version/hash after stopping the old writer.
Preserve R07 necessary/optional boundaries, exact-final-version review and model
independence through authorized_review_chain. Do not claim host execution was an
OpenCode scientific-role run. Do not launch later rounds or global adoption.

Sources: pinned upstream Statistical Integrity/diagnostic guidance, with the above
corrections; [SciPy fitting covariance](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html),
[openpyxl formula/cache reading](https://openpyxl.readthedocs.io/en/stable/api/openpyxl.reader.excel.html).
ImageJ/ParaView and format-specific details are task-dependent methods, not blanket
claims that every associated Python interface is connected.
