---
type: system-overview
graph-excluded: true
---

# Knowledge Base Health Dashboard

_最后更新：2026-06-27_

## 健康状态总览

| 指标 | 数值 | 说明 |
|---|---|---|
| 总来源数（Sources） | 143 | wiki/sources/ 下的页面总数 |
| 总 Concept 页数 | 61 | wiki/concepts/ 下的页面总数 |
| 总 Entity 页数 | 29 | wiki/entities/ 下的页面总数 |
| 总 Synthesis 页数 | 3 | wiki/synthesis/ 下的页面总数 |
| 高置信度概念数（High Confidence） | 2 | confidence: high 的 concept 页数 |
| 中置信度概念数（Medium Confidence） | 15 | confidence: medium 的 concept 页数 |
| 低置信度概念数（Low Confidence） | 44 | confidence: low 的 concept 页数 |
| 开放问题数（Open Questions） | 0 | QUESTIONS.md 中未解决的问题数 |
| Stale 页面数 | 0 | 超过 domain_volatility 时效阈值的页面数 |
| 近重复概念对数 | 2 | Jaccard>0.7 的概念名对（同族概念误报，已核实非重复） |

## 最近 Lint 报告

- 2026-06-27 `wiki/outputs/lint-2026-06-27.md`（**8/9 项通过**；仅余 2 个近重复启发式误报）
- 2026-04-28 `wiki/outputs/lint-2026-04-28.md`
- 2026-04-25 `wiki/outputs/lint-2026-04-25.md`（0 个问题，9/9 项通过）

## 最近修复（2026-06-27 健康整治）

- **SHA-256 完整性**：修正 71 个假阳性「SOURCE MODIFIED」（26 个截断哈希 + 45 个 CRLF/LF 行尾漂移），补 14 个缺失哈希字段，修正 3 个 raw 路径；新增 `.gitattributes`（`raw/** -text`）防行尾再漂移
- **断链清零**：补建 24 个芯片设计/制造概念页 + 4 个实体页（高通/联发科/博通/Cadence），消除全部 63 个 broken wikilink
- **lint 修 bug**：`check_broken_wikilinks` 的 `lstrip("wiki/")` 误把 `kpmg`→`pmg`，改为前缀剥除
- **清理**：删除 6 个测试 source 页 + 5 个根目录垃圾文件；修复 2 个非法 frontmatter

## 最近 Synthesis

- 2026-06-27 `wiki/synthesis/mculess-eea-architecture-synthesis.md`（MCULess 与汽车 EEA 架构演进，硬件路由 vs 软件路由的过渡范式，confidence: medium）
- 2026-04-25 `wiki/synthesis/robot-semiconductor-competitive-synthesis.md`（机器人半导体竞争格局，confidence: medium）
- 2026-04-25 `wiki/synthesis/agent-architecture-landscape-synthesis.md`（Agent 框架三条路线，confidence: low）

## 最近 Reflect 报告

- 2026-06-27 `wiki/outputs/gap-report-2026-06-27.md`（P0 盲区：functional-safety 23 源无页 / gan-power-devices 11 源无页；eea-architecture 顶层框架单源失衡）

## 知识增长趋势

| 日期 | Sources | Concepts | Entities | Synthesis |
|------|---------|---------|---------|---------|
| 2026-04-13 | 1 | 5 | 1 | 0 |
| 2026-04-15 | 19 | 14 | 12 | 0 |
| 2026-04-20 | 41 | 19 | 14 | 0 |
| 2026-04-25 | 55 | 24 | 16 | 2 |
| 2026-06-27 | 126 | 57 | 29 | 2 |
| 2026-06-27（整合远端+补全） | 143 | 61 | 29 | 3 |

## 待办（下一步建议）

- **提炼滞后**：126 来源仅 2 篇 synthesis、42/57 概念为 low 置信度。建议对成熟主题（芯片制造流程、MCULess、机器人半导体、Agent 路线）执行 REFLECT，将孤立概念升格为综合。
- **芯片新概念待深化**：本次新建的 24 个芯片概念多为 source_count 1–10 的初版，可在后续摄入中强化定义、补充矛盾点。
