# research-skills-curated

为本地 **Codex 和 OpenCode** 工作流挑选、保存和分发 skills 的中转缓冲仓库。保存固定上游副本，便于追溯、检查更新和恢复，避免本地安装直接跟随上游变化或依赖上游持续可用。

默认保留完整上游方法、脚本、参考资料和输出能力；`-curated` 仅区分分发名称，不表示 OpenCode 专用适配或效果提升。各技能的 `UPSTREAM_SOURCE.md` 记录原仓库、完整提交、目录 tree、取得时间、许可及分发版本；`KNOWN_ISSUES.md`（若有）仅记录问题，不表示已修复或全面验证。

## 当前收录

共 **7 项**；本表是仓库分发清单，不是本机安装或运行验收清单。

| 本仓库技能 | 分类 | 简要作用 | 原技能与官方仓库 | 采用的上游版本 | 上游最新版本（核查时） |
| --- | --- | --- | --- | --- | --- |
| [scientific-writing-curated](scientific-writing-curated/) | 科研写作 | 论文与报告起草、修订；证据追溯、报告规范、署名声明及本地一致性检查 | `scientific-writing` · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-writing) | `2.1` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/scientific-writing) | `2.1` · 同一提交，技能内容一致 |
| [peer-review-curated](peer-review-curated/) | 科研审稿 | 稿件、方案及提案评估；论断与证据核对、方法统计与复现审查、作者/编辑双通道意见 | `peer-review` · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/peer-review) | `2.2` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/peer-review) | `2.2` · 同一提交，技能内容一致 |
| [paper-lookup-curated](paper-lookup-curated/) | 文献检索 | 18 个学术 API 的检索与标识符查询、开放获取定位、分页和原始响应解析、来源记录 | `paper-lookup` · [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/paper-lookup) | `2.2` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/paper-lookup) | `2.2` · 同一提交，技能内容一致 |
| [experimental-design-curated](experimental-design-curated/) | 实验设计 | 研究设计、随机分配、区组/分层/聚类及 DOE 组合生成 | `experimental-design` · [官方目录](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/experimental-design) | `1.2` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/experimental-design) | `1.2` · 同一提交，技能内容一致 |
| [statistical-analysis-curated](statistical-analysis-curated/) | 统计分析 | 检验选择、假设诊断、效应量/功效、贝叶斯方法与统计报告 | `statistical-analysis` · [官方目录](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/statistical-analysis) | `1.2` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/statistical-analysis) | `1.2` · 同一提交，技能内容一致 |
| [sympy-curated](sympy-curated/) | 符号计算 | 代数、微积分、方程、矩阵、物理/力学及代码生成 | `sympy` · [官方目录](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/sympy) | `1.3` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/sympy) | `1.3` · 同一提交，技能内容一致 |
| [uncertainty-and-units-curated](uncertainty-and-units-curated/) | 单位与测量不确定度 | 单位/温标换算、GUM 与蒙特卡洛传播、预算、有效数字和量纲审计 | `uncertainty-and-units` · [官方目录](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/uncertainty-and-units) | `1.1` · [`330c8e7`](https://github.com/K-Dense-AI/scientific-agent-skills/tree/330c8e764435a731eff571e3efdda70b363d0792/skills/uncertainty-and-units) | `1.1` · 同一提交，技能内容一致 |

“最新”仅指以下查询时点，不会自动刷新；完整提交、tree 和更新比较入口见对应来源说明。

- [scientific-writing-curated](scientific-writing-curated/UPSTREAM_SOURCE.md)：2026-09-21T02:59:48.221Z（UTC）。
- [peer-review-curated](peer-review-curated/UPSTREAM_SOURCE.md)：2026-09-21T04:23:41.048943+00:00（UTC）。
- [paper-lookup-curated](paper-lookup-curated/UPSTREAM_SOURCE.md)：2026-09-21T05:27:57.837643+00:00（UTC）。
- [experimental-design-curated](experimental-design-curated/UPSTREAM_SOURCE.md)：2026-09-21T06:22:28.849077+00:00（UTC）。
- [statistical-analysis-curated](statistical-analysis-curated/UPSTREAM_SOURCE.md)：2026-09-21T06:29:05.674249+00:00（UTC）。
- [sympy-curated](sympy-curated/UPSTREAM_SOURCE.md)：2026-09-21T06:33:14.625944+00:00（UTC）。
- [uncertainty-and-units-curated](uncertainty-and-units-curated/UPSTREAM_SOURCE.md)：2026-09-21T06:37:39.482276+00:00（UTC）。

## 使用与更新

在 CC Switch 中使用 `https://github.com/Sapphir3/research-skills-curated`，分支 `main`，选择表中技能，按需安装到 Codex/OpenCode。名称改变不等于旧 `-opencode` 安装会自动迁移；运行依赖和用法见各技能 SKILL.md。

1. 根据各技能来源说明比较上游 main 与固定提交，重点检查该技能目录 tree/文件、依赖及许可差异。版本号不变不代表内容未变，仓库新提交也可能只涉及其他技能。
2. 审阅后手动更新副本、来源说明、本表与问题记录；不自动跟随上游。Git 历史、固定 tags/releases 和单技能 ZIP 保留已采用版本。
3. 再通过 CC Switch 手动更新本地安装。仓库发布与宿主实际加载/科研效果是不同步骤。

历史发布中的旧技能和管理文件不代表当前收录范围；当前仓库不维护重复 manifest、CI 或自动测试框架。scientific-writing 来源说明提及的旧 manifest 见其固定发布版本。

## 许可

仓库维护文档采用 [MIT License](LICENSE)。每个技能目录的 LICENSE.md 完整保留上游仓库 MIT 声明；原版权归原作者。SKILL 中指向的第三方软件许可仍适用于相应软件，本仓库未打包这些软件，也不改变其授权条件。
