---
type: concept
title: "GPAN 通信协议"
date: 2026-04-15
updated: 2026-04-20
tags:
  - gpan
  - industrial-network
  - real-time-communication
  - robotics
source_count: 3
confidence: low
domain_volatility: medium
last_reviewed: 2026-04-15
aliases:
  - "GPAN 通信协议"
  - "GPAN"
  - "gpan-communication"
  - "通用精密自动化网络"
  - "General Precision Automation Network"
---

# GPAN 通信协议（GPAN Communication）

## Definition

GPAN（通用精密自动化网络，General Precision Automation Network）是面向下一代工业自动化与车载网络需求的高性能通信协议，采用时间触发/事件驱动混合机制，具备确定性实时传输、灵活拓扑和强时间同步能力。GPAN 芯片支持以太网、CAN/LIN、音频数据的混合传输，MCULess 方案通过硬件路由实现边缘节点无 MCU 化，简化系统架构。

## Key Points

- **核心性能指标**（GPAN 芯片实测）：节点交换时延 **1.4μs**；典型远程控制时延<100μs；全双工100Mbps带宽；最多60个子节点；传输距离100米
- **混合传输能力**：单芯片同时支持以太网数据 + CAN/LIN + 音频数据，替代传统多总线架构，是 GPAN 相对 EtherCAT 的重要差异化优势
- **MCULess 方案**：边缘节点直接通过 GPAN 芯片硬件路由转发，无需独立主机 MCU，降低 BOM 成本和延迟
- **拓扑结构**：支持环网、菊花链，灵活多拓扑，与 EtherCAT 线型/树型互有侧重
- **时间同步**：精密时间协议扩展，时钟同步目标≤2μs（验证方案目标值，低于 EtherCAT DC 的<100ns）
- **与 EtherCAT 对比**：

  | 维度 | EtherCAT | GPAN |
  |---|---|---|
  | 时钟同步精度 | <100ns（DC，IEEE 1588增强） | ≤2μs（目标） |
  | 通信机制 | 飞读飞写，主从架构 | 时间触发/事件驱动混合 |
  | 数据传输 | 仅以太网 | 以太网+CAN+LIN+音频混合 |
  | 驱动生态 | 丰富（CoE/SoE） | 专用驱动层，生态较新 |
  | 节点交换时延 | 飞行处理，微秒级 | 1.4μs |

- **应用方向**：车载网络（替代多总线）、工业机器人分布式控制、人形机器人关节网络（MCULess 简化设计）

## My Position

## Contradictions

## Sources

- [[sources/ethercat-gpan-servo-validation]]
- [[sources/gpan-mculess-validation]]
- [[sources/gpan-robot-application-introduction]]

## Evolution Log

- 2026-04-15（2 sources）：概念初建，来源为 EtherCAT & GPAN 技术验证方案和 GPAN MCULess 验证报告
- 2026-04-20（3 sources）：新增《GPAN 机器人应用介绍》PDF 来源，补充 100Base-T1 环形拓扑、>80% 带宽利用率、20μs 控制周期、≤40ns 时钟同步、MCULess 远程外设控制、<100μA 低功耗等机器人场景核心指标
