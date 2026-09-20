# Research skills curated for OpenCode

Personal, reviewed distribution of eight bounded OpenCode adapters derived from [K-Dense scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792). This repository is separate from [homemade skills](https://github.com/Sapphir3/codex-skills-homemade). It is a selected distribution, not a mirror of the entire upstream library.

The initial release preserves the accepted scientific guidance, scripts, references and licenses. Only the installable names and package version metadata change. `-opencode` distinguishes these adapters from existing shared/Codex installations. R16 foundation verification does not establish R17 real-task quality or R18 stable multi-device adoption.

## Available skills

| Category | Installable name | Relevant workflow roles |
| --- | --- | --- |
| Literature | paper-lookup-opencode | document; worker executes bounded retrieval |
| Theory and methods | sympy-opencode | researcher, analyst, engineer |
| Theory and methods | uncertainty-and-units-opencode | researcher, analyst, critic, engineer |
| Design and analysis | experimental-design-opencode | researcher, analyst, critic |
| Design and analysis | statistical-analysis-opencode | researcher, analyst, critic |
| Writing and review | scientific-writing-opencode | author |
| Writing and review | peer-review-opencode | critic |
| Presentation | scientific-slides-opencode | author; worker handles mechanical production |

Each skill has one top-level directory; categories and roles are metadata, not duplicate copies. [manifest.json](manifest.json) fixes each package version, upstream commit, accepted adapter identity, dependencies and SHA-256 of every runtime file. The role assignments require the user's existing workflow configuration; installing a skill does not create agents or grant permissions. Main controllers retain their existing routing rules. The built-in `customize-opencode` entry follows the OpenCode host version and is not published here.

## Install and update

1. In CC Switch, add `https://github.com/Sapphir3/research-skills-curated`, branch `main`.
2. Install the selected `-opencode` skills for OpenCode only. Retain existing differently named shared installations and their Codex settings.
3. Confirm the installed files match the manifest, the matching role configuration has arrived through the existing configuration channel, and the local dependencies needed by the actual task are present.
4. Restart OpenCode completely, check actual discovery and role loading, and keep the previous working state until these checks pass.

CC Switch app switches are not a discovery sandbox: shared `.agents/skills`, `.claude/skills` and explicit host paths can expose another entry. Inspect actual paths. Do not place these OpenCode variants in a shared host-scanned source directory unless that behavior has been explicitly accepted.

The reviewed `main` branch is the update channel. Release tags, manifest hashes and single-skill ZIP assets identify fixed content. A ZIP import is useful for offline recovery but does not retain GitHub update tracking. No upstream download, execution, update schedule or automatic adoption is enabled by this repository.

## Maintenance and recovery

Use one leading plan and responsible owner; combine complementary methods when needed. Skills do not change models, scientific ownership, write permissions or the authorized audit chain. Consider new candidates when a concrete quality, effort or maintenance benefit is plausible; current acceptance is not a claim of global optimality.

For an update, inspect changes to selected skills and their actual dependencies, retain licenses, review candidate instructions/scripts before execution, run targeted checks, and bind approval to exact content. Run `python -B tests/validate_release.py` before publication. CI performs that same static integrity check; it does not execute downloaded candidate scripts or certify scientific correctness. Method or script changes also require the relevant behavioral evidence. Do not switch versions in an active research task.

After the main computer verifies the combined skills/configuration/environment, it may upload a new CC Switch WebDAV snapshot. WebDAV includes database configuration as well as skills. Other computers protect unmerged changes before downloading and verify their local paths, authentication, dependencies and fresh host loading. Keep existing device-local authentication management.

On failure, stop further distribution, preserve evidence and return the affected files/configuration to the last accepted content. Correct the published branch with a normal corrective/revert commit so later installs cannot reintroduce the bad version; retain immutable tags. Recheck only affected behavior, then upload a newly verified snapshot. Do not restore an old whole database blindly or rewrite published history.

The editing source, device-local Git checkout and CC Switch installation are distinct locations. Keep `.git` outside cloud-synchronized source trees. Detailed local rollout evidence belongs to the user's workflow project, not this public repository.

## License

Preserve the MIT notices in each package. Upstream software libraries and external services retain their own licenses and access conditions. This repository contains no credentials or research inputs.
