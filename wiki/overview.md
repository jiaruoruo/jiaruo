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
| 总 Synthesis 页数 | 6 | wiki/synthesis/ 下的页面总数 |
| 来源/综合比 | 24:1 | 143/6，已从 47:1 降至阈值（30）以下 |
| 高置信度概念数（High Confidence） | 2 | confidence: high 的 concept 页数 |
| 中置信度概念数（Medium Confidence） | 15 | confidence: medium 的 concept 页数 |
| 低置信度概念数（Low Confidence） | 44 | confidence: low 的 concept 页数 |
| 开放问题数（Open Questions） | 5 | QUESTIONS.md 中未解决的问题数（2026-06-27 从 gap 分析播种） |
| Stale 页面数 | 0 | 超过 domain_volatility 时效阈值的页面数 |
| 近重复概念对数 | 0 | lint Check5 已加白名单豁免同族概念误报，达 9/9 |

## 最近 Lint 报告

- 2026-06-27 `wiki/outputs/lint-2026-06-27.md`（**9/9 项通过，0 问题**；近重复白名单已豁免同族概念误报）

## 最近修复（2026-06-27 健康整治）

- **SHA-256 完整性**：修正 71 个假阳性「SOURCE MODIFIED」（26 个截断哈希 + 45 个 CRLF/LF 行尾漂移），补 14 个缺失哈希字段，修正 3 个 raw 路径；新增 `.gitattributes`（`raw/** -text`）防行尾再漂移
- **断链清零**：补建 24 个芯片设计/制造概念页 + 4 个实体页（高通/联发科/博通/Cadence），消除全部 63 个 broken wikilink
- **lint 修 bug**：`check_broken_wikilinks` 的 `lstrip("wiki/")` 误把 `kpmg`→`pmg`，改为前缀剥除
- **清理**：删除 6 个测试 source 页 + 5 个根目录垃圾文件；修复 2 个非法 frontmatter

## 最近 Synthesis

- 2026-06-27 `wiki/synthesis/embodied-ai-humanoid-robot-synthesis.md`（人形机器人约束下移到「身体层」三大瓶颈：BFM 接口/真机数据/灵巧手供应链，confidence: medium）
- 2026-06-27 `wiki/synthesis/edge-ai-on-device-inference-synthesis.md`（边缘AI：推理下沉设备端、重塑 MCU 角色、不可能三角，confidence: medium）
- 2026-06-27 `wiki/synthesis/chip-design-manufacturing-flow-synthesis.md`（芯片设计制造全流程地图 + 与前沿簇割裂的孤岛诊断，confidence: medium）
- 2026-06-27 `wiki/synthesis/mculess-eea-architecture-synthesis.md`（MCULess 与汽车 EEA 架构演进，硬件路由 vs 软件路由，confidence: medium）
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
| 2026-06-27（三簇 REFLECT） | 143 | 61 | 29 | 6 |

## 待办（下一步建议）

- **横向连通补桥**：芯片簇仍是相对孤岛（concept↔concept 链接稀疏），后续 ingest 现代芯片内容时应优先连到 advanced-packaging / gan-power-devices / mobile-soc / functional-safety 四个桥接点（见 chip-design-manufacturing-flow-synthesis）。
- **单源概念深化**：仍有 32 个 `source_count=1` 概念，可在后续摄入中强化定义、补充矛盾点。
- **raw 待清理**：`raw/clippings/MCU-LESS.md` 是已摄入 `raw/articles/MCU-LESS.md` 的逐字节重复；`全球机器人思考路线图 2025–2035.md` 为空文件（raw 属人类层，待你处理）。
- **跟进开放问题**：QUESTIONS.md 已播种 5 个开放问题，后续 ingest 时留意是否被回答。
