# Research skills curated

Personal distribution of selected research skills from [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills), separate from [homemade skills](https://github.com/Sapphir3/codex-skills-homemade).

`scientific-writing-curated` contains the complete upstream scientific-writing 2.1 skill for Codex and OpenCode. Its methods, scripts, templates and references are unchanged; only the installable name differs, and the package adds the original license and [source/update information](scientific-writing-curated/UPSTREAM_SOURCE.md). It replaces the removed, shortened `scientific-writing-opencode` package. The other seven packages retain their previous contents; this release makes no new compatibility or scientific-quality claim for them.

## Available skills

| Category | Installable name | Distribution scope |
| --- | --- | --- |
| Writing and review | scientific-writing-curated | Complete upstream; Codex and OpenCode |
| Literature | paper-lookup-opencode | Existing OpenCode package |
| Theory and methods | sympy-opencode | Existing OpenCode package |
| Theory and methods | uncertainty-and-units-opencode | Existing OpenCode package |
| Design and analysis | experimental-design-opencode | Existing OpenCode package |
| Design and analysis | statistical-analysis-opencode | Existing OpenCode package |
| Writing and review | peer-review-opencode | Existing OpenCode package |
| Presentation | scientific-slides-opencode | Existing OpenCode package |

Each installable skill has one top-level directory. [manifest.json](manifest.json) records its upstream identity, dependencies and exact file hashes. The scientific-writing upstream version remains `2.1`; its first complete curated distribution is `2.1.0`. Skills provide resources; they do not define fixed role assignments, grant tool permissions or change models.

## Install and update

1. In CC Switch, use `https://github.com/Sapphir3/research-skills-curated`, branch `main`.
2. For scientific writing, remove the old `scientific-writing-opencode` installation and install `scientific-writing-curated` from the repository listing. The name and repository path changed, so do not assume that updating the old entry will migrate it. Enable the new entry for Codex and/or OpenCode as needed. Other differently named skills are not removed by this release.
3. Follow the host's normal reload procedure at a suitable task boundary and verify the actual discovered path. Any custom name-based permissions or pinned skill paths must refer to `scientific-writing-curated`; the package does not edit host configuration. CC Switch app switches alone do not prove discovery isolation.

The reviewed `main` branch is the update channel. A release ZIP is an offline snapshot; importing it alone does not retain GitHub source tracking. No automatic update, dependency installation or upstream execution is enabled. Use the actual discovered skill root and an existing compatible interpreter when running optional scripts; outputs belong in the authorized task project.

## Maintenance and provenance

Use [scientific-writing-curated/UPSTREAM_SOURCE.md](scientific-writing-curated/UPSTREAM_SOURCE.md) to compare the upstream main directory with the fixed commit and skill tree. Review changes before adoption; preserve the upstream methods and resources. Make a host compatibility change only when an actual execution obstacle requires it, preserving the original methods and output capability. Optional improvements require separate task evidence and a maintenance decision.

Run `python -B tests/validate_release.py` before publication. CI uses the same static content, Python syntax and resource-link checks; it does not execute skill code or certify scientific correctness. Retain applicable execution evidence when files and assumptions are unchanged. Tags and single-skill ZIPs identify immutable versions; old release records are history, not current installation recommendations. Correct or revert the main branch with normal commits rather than rewriting that history.

The synchronized editing source, device-local Git checkout and CC Switch installation remain distinct. Keep `.git` outside synchronized source trees. This release does not operate CC Switch, WebDAV, other computers, workflow models or permissions.

## License

Preserve the MIT notices in each package. External libraries and services retain their own licenses and access conditions. This repository contains no credentials or research inputs.
