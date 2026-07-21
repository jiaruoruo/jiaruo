---
type: system-overview
graph-excluded: true
---

# Knowledge Base Health Dashboard

_最后更新：2026-07-21_

## 健康状态总览

| 指标 | 数值 | 说明 |
|---|---|---|
| 总来源数（Sources） | 233 | wiki/sources/ 下的页面总数（+1 PDF: yeasy《Harness》技术书） |
| 总 Concept 页数 | 74 | wiki/concepts/ 下的页面总数（不变） |
| 总 Entity 页数 | 31 | wiki/entities/ 下的页面总数（不变） |
| 总 Synthesis 页数 | 9 | wiki/synthesis/ 下的页面总数（不变） |
| 来源/综合比 | 26:1 | 233/9，**低于阈值（30）** |
| 高置信度概念数（High Confidence） | 2 | confidence: high 的 concept 页数 |
| 中置信度概念数（Medium Confidence） | 16 | confidence: medium 的 concept 页数 |
| 低置信度概念数（Low Confidence） | 56 | confidence: low 的 concept 页数 |
| 开放问题数（Open Questions） | 5 | QUESTIONS.md 中未解决的问题数 |
| Stale 页面数 | 0 | 超过 domain_volatility 时效阈值的页面数 |
| 近重复概念对数 | 0 | lint Check5 已加白名单豁免同族概念误报 |

## 最近 Lint 报告

- 2026-07-13 `wiki/outputs/lint-2026-07-13.md`（**9/9 项通过，0 问题**；clippings + notes 两批次 ingest 后复检，已刷新）
- 2026-06-29 `wiki/outputs/lint-2026-06-29.md`（**9/9 项通过，0 问题**；定时任务运行）
- 2026-06-27 `wiki/outputs/lint-2026-06-27.md`（**9/9 项通过，0 问题**；近重复白名单已豁免同族概念误报）

## 最近修复（2026-07-13 两批次 ingest 复检）

- **断链清零（clippings 批次）**：初检 Check2 断链 10 处 + Check8 跨语言重复 1 处；修正 MCP 实体 wikilink、未建实体来源改为纯文本标注、移除 human-in-the-loop 重复别名 slug、补建 langgraph / claude-opus-4 / automotive-ethernet-10base-t1s 3 页
- **notes 批次（59 源）**：技术笔记 9 个建新概念 robot-safety / vehicle-domain-controller 并挂接；简报/报告 50 个统一 low confidence、关键词挂接已有概念、不新建概念，无断链/重复；复检 9/9 通过

## 最近 Synthesis

- 2026-07-13 `wiki/synthesis/agent-theme-synthesis.md`（Agent 主题综合：6层架构×Harness×安全治理三层抽象栈，含 MCP 连接层，confidence: low）
- 2026-07-13 `wiki/synthesis/vehicle-comms-protocols-synthesis.md`（车载实时通信 GPAN/EtherCAT/10BASE-T1S/ZCU 三路线互补共存，confidence: medium）
- 2026-07-13 `wiki/synthesis/sdv-vla-agent-convergence-synthesis.md`（端到端自动驾驶×具身智能×域控架构收敛，方法论同构，confidence: low）
- 2026-06-27 `wiki/synthesis/embodied-ai-humanoid-robot-synthesis.md`（人形机器人约束下移到「身体层」三大瓶颈：BFM 接口/真机数据/灵巧手供应链，confidence: medium）
- 2026-06-27 `wiki/synthesis/edge-ai-on-device-inference-synthesis.md`（边缘AI：推理下沉设备端、重塑 MCU 角色、不可能三角，confidence: medium）
- 2026-06-27 `wiki/synthesis/chip-design-manufacturing-flow-synthesis.md`（芯片设计制造全流程地图 + 与前沿簇割裂的孤岛诊断，confidence: medium）
- 2026-06-27 `wiki/synthesis/mculess-eea-architecture-synthesis.md`（MCULess 与汽车 EEA 架构演进，硬件路由 vs 软件路由，confidence: medium）
- 2026-04-25 `wiki/synthesis/robot-semiconductor-competitive-synthesis.md`（机器人半导体竞争格局，confidence: medium）
- 2026-04-25 `wiki/synthesis/agent-architecture-landscape-synthesis.md`（Agent 框架三条路线，confidence: low）

## 最近 Reflect 报告

- 2026-07-13 `wiki/outputs/gap-report-2026-07-13.md`（REFLECT 新增 2 篇 synthesis，比 34:1→26:1；孤立概念 16 个待深化；GPAN/SDV 收敛均标回音室风险）
- 2026-06-29 `wiki/outputs/gap-report-2026-06-29.md`（上轮 P0 已消除；新盲区：ota-update 14 源无页 / thermal-management 9 源 / cybersecurity-automotive 4 源；单源积压 32）
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
| 2026-07-13（ingest 3 文件） | 146 | 73 | 31 | 6 |
| 2026-07-13（ingest notes 59 文件） | 205 | 74 | 31 | 6 |
| 2026-07-13（reflect 2 synthesis） | 205 | 74 | 31 | 8 |
| 2026-07-13（agent 主题综合 +1 synthesis） | 205 | 74 | 31 | 9 |
| 2026-07-14（ingest articles 23 文件） | 228 | 74 | 31 | 9 |
| 2026-07-21（ingest pdf 1 文件） | 233 | 74 | 31 | 9 |

## 待办（下一步建议）

- **补充 Synthesis（已完成本轮）**：来源/综合比从 34:1 拉回 **23:1**（低于 30 阈值）。本轮 REFLECT 新增 2 篇 synthesis；随后按用户指示把 gap-report 第六节的「Agent 主题归一」落地为 `agent-theme-synthesis.md`（6层架构×Harness×安全治理三层抽象栈，low），闭环该建议。下一步可针对「芯片设计全流程深化」「人形机器人供应链」补综合（见 gap-report-2026-07-13.md 第六节）。
- **横向连通补桥**：芯片簇仍是相对孤岛（concept↔concept 链接稀疏），后续 ingest 现代芯片内容时应优先连到 advanced-packaging / gan-power-devices / mobile-soc / functional-safety 四个桥接点（见 chip-design-manufacturing-flow-synthesis）。
- **单源概念深化**：仍有大量 `source_count=1` 概念（如 agent-architecture / soft-robotics / neuromorphic-computing / vision-language-action-model / robot-safety / vehicle-domain-controller 等），可在后续摄入中强化定义、补充矛盾点。
- **简报类质量**：50 个 daily-tech-digest / weekly / monthly 均标记 low confidence 且仅挂接已有概念，是「宽而浅」的来源层；其价值在于趋势追踪，不宜据此单独下结论。
- **raw 待清理**：`raw/clippings/MCU-LESS.md` 已于本次作为独立内部笔记摄入（slug: mculess-tech-industry-current-state），与 `raw/articles/MCU-LESS.md`（已建 mculess-tech-comparison-analysis）确认为不同文件，非逐字节重复；原 overview 中"待清理"标记作废。
- **跟进开放问题**：QUESTIONS.md 已播种 5 个开放问题，后续 ingest 时留意是否被回答。
