---
type: concept
title: "整车EEA架构"
date: 2026-04-16
updated: 2026-07-14
tags:
  - automotive
  - eea
  - electrical-architecture
  - zonal
  - centralized-computing
source_count: 10
confidence: low
domain_volatility: medium
last_reviewed: 2026-07-14
aliases:
  - "整车EEA架构"
  - "电子电气架构"
  - "EEA Architecture"
  - "eea-architecture"
  - "Electrical Electronic Architecture"
  - "整车电子电气架构"
---

# 整车EEA架构（Electrical/Electronic Architecture）

## Definition

整车EEA架构（Electrical/Electronic Architecture）是定义整车控制单元部署方式、通信骨干网拓扑及功能分配的顶层架构体系。从历史演进看，EEA 经历了"分布式 ECU → 域集中式 → 中央计算+区域控制（Zonal）"三个阶段，每个阶段对应不同的网关形态和通信骨干网协议。EEA 架构演进是智能汽车软件能力跃升和成本优化的根本驱动力。

## Key Points

- **EEA 1.0（分布式架构）**：每项功能由独立 ECU 实现，CAN/LIN 总线连接，中央 CAN 网关（CGW）负责网段路由；以太网仅承担 OTA 和数据上传
- **EEA 2.0（域集中式架构）**：功能划分为动力、底盘、车身、座舱、ADAS 五大域；域内 CAN 通信，域间由以太网承担（无功能部署）；域网关（XCU/FBCM/RBCM）管理各域
- **EEA 3.0（中央计算+区域控制）**：CCU（中央计算单元）+ZCU（区域网关）架构；以太网开始承担车身控制等低实时性功能；物理区域划分取代功能域划分（LZCU/RZCU/BZCU）
- **EEA 4.0（目标架构）**：同为 CCU+ZCU，但以太网扩展至底盘/动力/高实时性功能全覆盖；软件功能灵活部署，ZCU 趋向纯执行驱动，CCU 承载全部算法逻辑
- **架构演进的核心驱动力**：①L4 自动驾驶算力集中化需求；②SOA 软件架构支持需要高带宽 ETH；③CAN 总线负载瓶颈（部分网段已达 69.88%）；④线束减重降本；⑤软件平台化降低开发成本
- **通信骨干网演进**：CAN（2Mbps）→ CANFD（5Mbps）→ 100M ETH → 千兆 ETH；主流新势力均已规划或落地 ETH 主干网
- **典型案例（理想汽车 EEA 3.0）**：CCU（中央算力+自动驾驶）+ HU（车载娱乐）+ LZCU（左区域）+ RZCU（右区域）+ BZCU（后区域）；各 ZCU 通过百兆以太网上联 CCU，管理数十个 CAN/LIN 节点
- **竞争格局**：特斯拉 HW4.0 已实现 ETH 环网主干网（含 SDN 控制器）；华为 2021 年实现 CAN-ETH 路由部署；小米下一代 EEA 规划 ETH 主干网（快速跟随策略）

## My Position

## Contradictions

## Sources

- [[sources/distributed-gateway-communication-tdt]]
- [[sources/mculess-technology-insight-full-2026-05]]
- [[sources/gpan-mculess-distributed-audio-v1-8]]
- [[sources/gpan-mculess-application-analysis-v0-8]]
- [[sources/gpan-application-scenario-vsdx]]
- [[sources/mcu-less-technology-insight-core]]
- [[sources/mcu-less-application-opportunities]]
- [[sources/mcu-less-technology-overview]]
- [[sources/mcu-less-auto-robot-insight]]
- [[sources/cost-analysis-public-v0-4]]

## Evolution Log

- 2026-04-16（1 sources）：概念初建，来源为分布式网关通信TDT内部预研立项文档

- 2026-07-14（10 sources）：强化——[MCU-less 技术洞察（详尽版）：机会分析 · 技术方案 · 执行策略] 与现有定义一致
- 2026-07-14（10 sources）：强化——[GPAN 车载 MCU-less 和分布式音频介绍（V1.8）] 与现有定义一致
- 2026-07-14（10 sources）：强化——[GPAN 车载通信应用场景价值分析（V0.8）] 与现有定义一致
- 2026-07-14（10 sources）：强化——[GPAN 应用场景架构图（Visio）] 与现有定义一致
- 2026-07-14（10 sources）：强化——[MCU-less 技术应用洞察-核心观点解读] 与现有定义一致
- 2026-07-14（10 sources）：强化——[MCU-less 应用机会点汇总] 与现有定义一致
- 2026-07-14（10 sources）：强化——[MCU-less 技术概述] 与现有定义一致
- 2026-07-14（10 sources）：强化——[MCU-less 技术在汽车和机器人领域的应用洞察] 与现有定义一致
- 2026-07-14（10 sources）：强化——[成本核算（V0.4 公共版）] 与现有定义一致