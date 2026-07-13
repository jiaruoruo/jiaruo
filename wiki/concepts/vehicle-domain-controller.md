---
type: concept
title: "车载域控制器"
date: 2026-07-13
updated: 2026-07-13
tags:
  - vehicle-domain-controller
  - eea-architecture
  - autonomous-driving
  - automotive
source_count: 2
confidence: low
domain_volatility: high
last_reviewed: 2026-07-13
aliases:
  - "车载域控"
  - "域控制器"
  - "Domain Controller"
  - "Vehicle DC"
  - "CCU-ZCU"
---

# 车载域控制器（Vehicle Domain Controller）

## Definition

车载域控制器（Vehicle Domain Controller）是汽车电子电气架构（见 [[eea-architecture]]）中的高算力计算中枢，按功能域（智驾/座舱/车身/底盘等）或区域（Zonal，见 [[zonal-gateway]]）聚合控制与计算任务。在 MCULess 趋势（见 [[mculess-architecture]]）下，域控制器承担更多原分散在末端 MCU 的逻辑。其设计受 [[functional-safety]]（ISO 26262）、AUTOSAR、SOTIF 等标准强约束。

## Key Points

- **域划分**：智驾域（自动驾驶/感知融合）、座舱域（IVI/人机）、车身域、底盘/动力域；高阶方案走向中央计算（CCU）+ 区域控制器（ZCU）拓扑（用户所在组织采用 CCU-ZCU）
- **关键标准**：ISO 26262（功能安全）、AUTOSAR Classic/Adaptive（软件架构）、ISO/PAS 21448（SOTIF，预期功能安全）、ASPICE（流程）、UN ECE R155（网络安全）/R156（软件更新）、GB/T 国标
- **开源生态**：Apollo（百度）、Autoware、openPilot（Comma.ai）、CARLA（仿真）、nuScenes（数据集）；Apex.OS（功能安全实时 ROS）
- **信息获取四维矩阵**（来自内部数据源推荐文档）：学术论文（arXiv/Papers With Code/顶会）+ 产业研报（佐思/IDC/Gartner/IFR）+ 开源社区（GitHub/ROS/HuggingFace）+ 媒体公号（机器之心/车东西），强调交叉验证、标准优先于技术创新
- **跨域功能安全**（与 [[robot-safety]] 同源方法学）：CCU-ZCU 项目需关注跨域通信安全、安全目标协调、共享资源隔离、共因故障、端到端追溯

## My Position

车载域控是「软件定义汽车」的物理落点，但安全（功能安全+预期功能安全）是不可逾越的硬约束——任何算力/架构创新都必须让位于 ISO 26262 与 SOTIF。这与 MCULess 降本叙事的边界一致：安全关键域禁止去 MCU。

## Contradictions

<!-- 暂无来源间分歧；域控方案在具体芯片选型/拓扑上随项目而异，但标准约束一致 -->

## Sources

- [[sources/ai-robot-vehicle-dc-data-sources]]
- [[sources/ai-robot-vehicle-dc-tech-quick-reference]]

## Evolution Log

- 2026-07-13（2 sources）：概念初建，来源为 AI·机器人·车载域控前瞻技术数据源推荐 + 速查表（内部参考文档，2026-05），提炼域控定义、关键标准、开源生态、四维信息矩阵与跨域功能安全关注点；confidence 设为 low（来源为数据源清单而非深度技术文档）
