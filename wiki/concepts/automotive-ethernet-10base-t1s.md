---
type: concept
title: "10BASE-T1S 车载以太网"
date: 2026-07-13
updated: 2026-07-14
tags:
  - automotive-ethernet
  - 10base-t1s
  - ieee-802-3cg
  - plca
  - mculess
  - rcp
  - automotive-eea
source_count: 7
confidence: medium
domain_volatility: medium
last_reviewed: 2026-07-14
aliases:
  - "10BASE-T1S 车载以太网"
  - "10BASE-T1S"
  - "automotive-ethernet-10base-t1s"
  - "IEEE 802.3cg"
  - "车载以太网"
---

# 10BASE-T1S 车载以太网（10BASE-T1S Automotive Ethernet）

## Definition

10BASE-T1S（IEEE 802.3cg-2019）是一种基于单对双绞线（SPE）的 10Mbps 半双工车载以太网物理层标准，支持多点拓扑（Multidrop）和物理层冲突避免（PLCA）机制，在单根非屏蔽双绞线上实现确定性以太网通信。它是汽车 MCU-less 架构（RCP 路线）的首选物理层。

## Key Points

- **核心机制**：PLCA（物理层冲突避免）——由 Node ID=0 协调器周期发 BEACON 启动传输周期，各节点按 ID 顺序获传输机会（TO），无数据自动跳过，避免总线空闲；TSN 802.1AS/IEEE1588 时间同步
- **物理特性**：单对双绞线，10Mbps 半双工，多点拓扑支持≥8 节点，最长 25m（Pt-Pt 全双工 15m），分支 <0.1m
- **两大应用路线**：
  - **RCP 路线**（10Base-T1S）：ADI AD330x MACPHY、NXP TJA1415；最小调度周期 1ms，可用带宽有限，适用实时性/数据量同 CAN/CANFD 场景；ADI/NXP/TI/ON 下一代暂未规划
  - 与 **GPAN**（100M 全双工，类 EtherCAT 私有协议）并列对比，详见 [[mculess-architecture]]、[[gpan-communication]]、[[rcp-remote-control-protocol]]
- **价值**：替代传统 CAN/CANFD 的关键使能技术，降低布线复杂度与系统成本，支撑区域架构（Zonal）与 SDV

## My Position

- 与 [[rcp-remote-control-protocol]]（依赖 10BASE-T1S 作物理层）、[[mculess-architecture]]、[[gpan-communication]] 共同构成车载 MCU-less 通信底座。10BASE-T1S 标准化程度高但带宽受限，GPAN 带宽高但私有协议，二者互补而非替代。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/mculess-tech-industry-current-state]]
- [[sources/10baset1s-automotive-ethernet-technical-analysis]]
- [[sources/mculess-technology-insight-full-2026-05]]
- [[sources/gpan-mculess-distributed-audio-v1-8]]
- [[sources/gpan-mculess-application-analysis-v0-8]]
- [[sources/gpan-spec-introduction-v0-2]]
- [[sources/mcu-less-auto-robot-insight]]

## Evolution Log

- 2026-07-13（2 sources）：概念初建，融合内部笔记「MCU-LESS 技术行业现状」（RCP/10Base-T1S 路线：ADI AD330x、NXP TJA1415，PLCA 确定性调度，最小周期 1ms，TSN 802.1AS/IEEE1588）与 10BASE-T1S 技术深度解析文章（IEEE 802.3cg 标准、PLCA、总线 25m/分支<0.1m、≥255 从节点）

- 2026-07-14（7 sources）：强化——[MCU-less 技术洞察（详尽版）：机会分析 · 技术方案 · 执行策略] 与现有定义一致
- 2026-07-14（7 sources）：强化——[GPAN 车载 MCU-less 和分布式音频介绍（V1.8）] 与现有定义一致
- 2026-07-14（7 sources）：强化——[GPAN 车载通信应用场景价值分析（V0.8）] 与现有定义一致
- 2026-07-14（7 sources）：强化——[GPAN 芯片规格介绍文档（V0.2）] 与现有定义一致
- 2026-07-14（7 sources）：强化——[MCU-less 技术在汽车和机器人领域的应用洞察] 与现有定义一致
- 2026-07-21（7 sources）：REFLECT 补齐主域标签：automotive-eea
