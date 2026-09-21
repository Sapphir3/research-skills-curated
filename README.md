# research-skills-curated

为本地 **Codex 和 OpenCode** 工作流挑选、保存和分发 skills 的中转缓冲仓库。这里保留经过选择的固定上游副本，便于追溯来源、检查更新和恢复已采用版本，避免本地安装直接跟随上游变化或依赖上游持续可用。

默认保留上游的方法、脚本、参考资料和输出能力；只有实际宿主接入确有必要时才作最小修改并记录。`-curated` 后缀用于区分本仓库分发副本，不表示 OpenCode 专用版或效果提升。

## 当前使用与分发的技能

当前仅收录以下 **1 项**。本表列出本仓库采用的技能，不是本机全部安装项或运行验证清单。

| 本仓库技能 | 分类 | 简要作用 | 原技能与官方仓库 | 采用的上游版本 | 上游最新版本（核查时） |
| --- | --- | --- | --- | --- | --- |
| [scientific-writing-curated](scientific-writing-curated/) | 科研写作 | 论文与报告起草、修订；证据追溯、报告规范、署名声明及本地一致性检查 | `scientific-writing` · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-writing) | `2.1` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/scientific-writing) | `2.1` · 同一提交，技能内容一致 |

版本核查时间：**2026-09-21 12:00（北京时间，UTC+8）**。“最新”是该时点的查询结果，不会自动刷新。

- 采用及本次最新的上游 `main` 提交：`330c8e764435a731eff571e3efdda70b363d0792`。
- 上游技能路径：`skills/scientific-writing`；采用及本次最新的目录 Git tree：`ae5fac6462c292e31e8f75337ad4735c127146b4`。
- 本仓库分发版本：[`scientific-writing-curated-v2.1.0`](https://github.com/Sapphir3/research-skills-curated/releases/tag/scientific-writing-curated-v2.1.0)。保留全部 31 个上游技能文件，仅修改 `SKILL.md` 的名称，并补充原许可证及[来源说明](scientific-writing-curated/UPSTREAM_SOURCE.md)，共 33 个文件。

## 使用与更新

在 CC Switch 中添加本仓库 `https://github.com/Sapphir3/research-skills-curated`，选择 `main` 分支下的 `scientific-writing-curated`，按需安装到 Codex 和 OpenCode。依赖和使用方法见该技能的 [SKILL.md](scientific-writing-curated/SKILL.md)。

1. 检查表中的官方仓库及技能路径，将当前上游 `main` 与已采用提交比较。版本号可能不变，仓库新提交也可能只涉及其他技能；以该技能目录的 tree 或文件差异判断是否更新，并核对相关许可和依赖变化。
2. 确认变更适合当前用途后，手动更新本仓库副本、必要的来源说明及本表版本和核查时间，保留可恢复的已采用版本。不自动跟随或合并上游。
3. 从本仓库通过 CC Switch 更新本地安装。仓库更新与本地安装是两个独立步骤。

技能内来源说明提及的旧 `manifest` 保存在[固定发布版本](https://github.com/Sapphir3/research-skills-curated/blob/scientific-writing-curated-v2.1.0/manifest.json)中；当前收录清单以本 README 为准。Git 历史与既有发布保留用于追溯，旧发布所含的其他技能不属于当前收录范围。

## 许可

仓库维护文档采用 [MIT License](LICENSE)。上游技能的版权归原作者所有，原 MIT 声明完整保留于 [scientific-writing-curated/LICENSE.md](scientific-writing-curated/LICENSE.md)；本仓库不改变其授权条件。
