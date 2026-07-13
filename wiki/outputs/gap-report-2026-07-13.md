---
type: gap-report
title: "知识库 Gap 分析报告 2026-07-13"
date: 2026-07-13
graph-excluded: true
tags:
  - reflect
  - gap-analysis
  - knowledge-base-health
---

# 知识库 Gap 分析报告（2026-07-13）

> REFLECT 触发：Sources/Synthesis 比 = 205/6 ≈ **34.2**，超过 30 阈值；孤立概念积压；出现成熟但未综合簇。本报告对应 CLAUDE.md 五、REFLECT Stage 3。

## 一、综合覆盖状态

- 概念总数：**74**；Synthesis 数：**6 → 8**（本次新增 2 篇）。
- Sources/Synthesis 比：**34.2 → 25.6**（新增 2 篇 synthesis 后）。
- 已综合概念 31 个中，本次新增覆盖：**gpan-communication、ethercat-realtime-communication、automotive-ethernet-10base-t1s、zonal-gateway**（通信簇综合）；autonomous-driving / vision-language-action-model / agent-architecture / vehicle-domain-controller 进入「SDV/具身收敛」综合的论证范围。

## 二、成熟但未综合簇（已处理）

| 簇 | 代表概念（source_count） | 状态 |
|---|---|---|
| 车载实时通信 | gpan-communication(24)、ethercat-realtime-communication(9)、automotive-ethernet-10base-t1s(2)、zonal-gateway(3) | ✅ 已建 `vehicle-comms-protocols-synthesis` |
| SDV×具身收敛 | vehicle-domain-controller(2)、vision-language-action-model(1)、agent-architecture(1)、autonomous-driving(1) | ✅ 已建 `sdv-vla-agent-convergence-synthesis`（low confidence） |

> 注：`mculess-architecture`(28)、`humanoid-robot`(12)、`chip-design`(10)、`functional-safety`(10) 等大头已在此前综合中覆盖。

## 三、孤立概念积压（source_count=1 且创建 >30 天）

触发阈值：≥10 个即预警。当前命中 **16 个**：

- agent-security-governance（2026-04-25）
- automotive-sensor（2026-05-17）
- autosar-configuration-toolchain（2026-05-14）
- can-eth-protocol-conversion（2026-04-16）
- claude-code-workflow（2026-05-14）
- eea-architecture（2026-04-16）
- humanoid-robot-supply-chain（2026-05-17）
- llm-benchmark-evaluation（2026-04-27）
- llm-knowledge-management（2026-04-25）
- multimodal-api（2026-04-15）
- reinforcement-learning-locomotion（2026-04-15）
- robot-software-architecture（2026-04-25）
- tensor-mathematics（2026-04-28）
- text-to-speech（2026-04-15）
- time-sensitive-networking（2026-04-16）
- video-generation（2026-04-15）

**建议**：这批多为早期单来源摄入，长期未强化。两种处置——① 若主题已无新增价值，标记为 `low` 并保留为「种子概念」；② 若仍有相关性（如 `can-eth-protocol-conversion`、`time-sensitive-networking` 对 ZCU/通信综合很重要），下次 INGEST 优先补充来源以提升置信度。

## 四、隐性盲区 / 薄覆盖

- **端到端自动驾驶深度缺失**：`autonomous-driving` 仅 1 源且停留在「多传感器融合」层面，BEV/占用网络/世界模型等真正收敛焦点未摄入。这是 SDV 收敛综合的最大证据短板。
- **TSN（时间敏感网络）仅 1 源**：`time-sensitive-networking` 是车载以太网确定性调度的关键，却被严重低估覆盖，与 GPAN/EtherCAT 的时钟同步论证强相关，建议补源。
- **CAN-ETH 协议转换仅 1 源**：`can-eth-protocol-conversion` 是 ZCU 四大功能之首，覆盖过薄。
- **RCP 协议**：`rcp-remote-control-protocol`(6) 已综合，但其与 10BASE-T1S 的物理层耦合在 `automotive-ethernet-10base-t1s`(2) 中仍偏弱。

## 五、矛盾 / 回音室风险

- **GPAN 单一方来源偏向（强）**：GPAN 全部性能优势来自汇顶阵营+内部笔记，缺第三方复测；已在其综合的 Counter-evidence 节显式标注。
- **SDV/具身收敛（强）**：四核心概念均单来源+低置信简报共现，综合置信度定为 low，并标注回音室风险。
- EtherCAT 时钟同步精度（<1μs vs <100ns）此前已在概念页 Contradictions 节消解（采用瑞萨官方 <100ns）。

## 六、后续 REFLECT 候选

1. **芯片设计全流程深化**：`chip-design`(10)/`semiconductor-manufacturing`(5)/`vlsi-design`(4)/`ic-packaging`(7)/`ic-testing`(3) 已散落综合，可再做一篇「从 EDA 到封测的国产替代全景」。
2. **人形机器人供应链**：`humanoid-robot`(12) 已综合，但 `humanoid-robot-supply-chain`(1) 孤立，可补源后并入。
3. **Agent 主题归一**：`agent-architecture`/`agent-harness`/`agent-security-governance` 三个概念提议统一挂到 Agent 主题，待用户确认后 MERGE 或建主题综合。

---

_生成方式：脚本 `_reflect_scan.py` 提取概念/synthesis 统计与共现矩阵，结合人工研读概念页完成。_
