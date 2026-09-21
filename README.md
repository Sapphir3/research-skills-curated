# research-skills-curated

为本地 **Codex 和 OpenCode** 工作流挑选、保存和分发 skills 的中转缓冲仓库。这里保留经过选择的固定上游副本，便于追溯来源、检查更新和恢复已采用版本，避免本地安装直接跟随上游变化或依赖上游持续可用。

默认保留上游的方法、脚本、参考资料和输出能力；只有实际宿主接入确有必要时才作最小修改并记录。`-curated` 后缀用于区分本仓库分发副本，不表示 OpenCode 专用版或效果提升。

## 当前使用与分发的技能

当前收录以下 **3 项**。本表列出本仓库采用的技能，不是本机全部安装项或运行验证清单。

| 本仓库技能 | 分类 | 简要作用 | 原技能与官方仓库 | 采用的上游版本 | 上游最新版本（核查时） |
| --- | --- | --- | --- | --- | --- |
| [scientific-writing-curated](scientific-writing-curated/) | 科研写作 | 论文与报告起草、修订；证据追溯、报告规范、署名声明及本地一致性检查 | `scientific-writing` · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-writing) | `2.1` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/scientific-writing) | `2.1` · 同一提交，技能内容一致 |
| [peer-review-curated](peer-review-curated/) | 科研审稿 | 稿件、方案及提案评估；论断与证据核对、方法统计与复现审查、作者/编辑双通道意见 | `peer-review` · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/peer-review) | `2.2` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/peer-review) | `2.2` · 同一提交，技能内容一致 |
| [paper-lookup-curated](paper-lookup-curated/) | 文献检索 | 18 个学术 API 的检索与标识符查询、开放获取定位、分页和原始响应解析、来源记录 | `paper-lookup` · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/paper-lookup) | `2.2` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/paper-lookup) | `2.2` · 同一提交，技能内容一致 |

版本核查时间（北京时间，UTC+8）：scientific-writing 为 **2026-09-21 12:00**；peer-review 为 **2026-09-21 12:23**；paper-lookup 为 **2026-09-21 13:27**。“最新”是该时点的查询结果，不会自动刷新。

- 采用及本次最新的上游 `main` 提交：`330c8e764435a731eff571e3efdda70b363d0792`。
- scientific-writing 上游路径：`skills/scientific-writing`；采用及本次最新的目录 Git tree：`ae5fac6462c292e31e8f75337ad4735c127146b4`。
- scientific-writing 分发版本：[`scientific-writing-curated-v2.1.0`](https://github.com/Sapphir3/research-skills-curated/releases/tag/scientific-writing-curated-v2.1.0)。保留全部 31 个上游技能文件，仅修改 `SKILL.md` 的名称，并补充原许可证及[来源说明](scientific-writing-curated/UPSTREAM_SOURCE.md)，共 33 个文件。
- peer-review 上游路径：`skills/peer-review`；采用及本次最新的目录 Git tree：`5521fbe04d1868847f76765c08edfc9d7632f7f7`。
- peer-review 分发版本：[`peer-review-curated-v2.2.0`](https://github.com/Sapphir3/research-skills-curated/releases/tag/peer-review-curated-v2.2.0)。保留全部 24 个上游技能文件，仅修改 `SKILL.md` 的名称，并补充原许可证及[来源说明](peer-review-curated/UPSTREAM_SOURCE.md)，共 26 个文件。

- paper-lookup 上游路径：`skills/paper-lookup`；采用及本次最新的目录 Git tree：`b7790a25f1f5428e8d631df35fe3344fac8a5008`。
- paper-lookup 分发版本：[`paper-lookup-curated-v2.2.0`](https://github.com/Sapphir3/research-skills-curated/releases/tag/paper-lookup-curated-v2.2.0)。保留全部 24 个上游技能文件，仅改名称，加原许可、[来源说明](paper-lookup-curated/UPSTREAM_SOURCE.md)及简短[问题发现记录](paper-lookup-curated/KNOWN_ISSUES.md)，共 27 个文件；上游问题未修复。

## 使用与更新

在 CC Switch 中添加本仓库 `https://github.com/Sapphir3/research-skills-curated`，在 `main` 分支下选择表中的技能，按需安装到 Codex 和 OpenCode。依赖和使用方法见各技能目录中的 `SKILL.md`。

1. 检查表中的官方仓库及技能路径，将当前上游 `main` 与已采用提交比较。版本号可能不变，仓库新提交也可能只涉及其他技能；以该技能目录的 tree 或文件差异判断是否更新，并核对相关许可和依赖变化。
2. 确认变更适合当前用途后，手动更新本仓库副本、必要的来源说明及本表版本和核查时间，保留可恢复的已采用版本。不自动跟随或合并上游。
3. 从本仓库通过 CC Switch 更新本地安装。仓库更新与本地安装是两个独立步骤。

scientific-writing 来源说明提及的旧 `manifest` 保存在[固定发布版本](https://github.com/Sapphir3/research-skills-curated/blob/scientific-writing-curated-v2.1.0/manifest.json)中；当前收录清单以本 README 为准。Git 历史与既有发布保留用于追溯，旧发布所含的其他技能不属于当前收录范围。

## 许可

仓库维护文档采用 [MIT License](LICENSE)。上游技能的版权归原作者所有，原 MIT 声明完整保留于 [scientific-writing](scientific-writing-curated/LICENSE.md)、[peer-review](peer-review-curated/LICENSE.md) 和 [paper-lookup](paper-lookup-curated/LICENSE.md) 各自目录；本仓库不改变其授权条件。
