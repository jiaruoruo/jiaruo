---
title: 聊一聊MCULess, 10BASE-T1S以及RCP
slug: mculess-10baset1s-rcp-discussion
source_url: https://mp.weixin.qq.com/s/onQ1uh9YFboECVcYTmbWFA
author: AlvinY
published: 2026-04-28
ingested: 2026-04-28
sha256: 304dbdfa
tags: [mculess, 10base-t1s, rcp, plca, ieee802-3cg, someip, ieee1722, automotive]
concepts: [mculess-architecture, eea-architecture, can-eth-protocol-conversion, zonal-gateway]
entities: []
---

# 聊一聊MCULess, 10BASE-T1S以及RCP

## 核心摘要

技术深度探讨文，覆盖 MCU-less 双重解耦本质、10BASE-T1S 标准细节（IEEE 802.3cg 2020）、RCP 起源历史（宝马 2023 TC14 提案 → 2024 TC18 标准化），以及 RCP 封装协议选项对比（SOME/IP vs IEEE 1722）。

## MCU-less 双重解耦

1. **软硬解耦**：硬件标准化，功能由软件定义，支持 OTA 升级而无需硬件改版
2. **软软解耦**：应用逻辑与通信协议栈分离，微服务化部署在 ZCU，通过标准接口调用边缘 IO

## 10BASE-T1S 技术标准

- **标准号**：IEEE 802.3cg，2020 年发布
- **速率**：10 Mbps，半双工
- **物理介质**：单对非屏蔽双绞线（UTP），传输距离至少 25 m
- **拓扑**：Multi-drop（多节点挂接同一总线，最多 8 节点，可扩展至 255）

### PLCA 机制详解

PLCA（Physical Layer Collision Avoidance，物理层碰撞避免）：

- **时分复用**：每个节点分配唯一 Node ID（0–255），按 ID 轮询发送机会
- **BEACON 信号**：协调器（ID=0）周期性广播 BEACON 帧，同步所有节点的发送时隙
- **TO（Transmit Opportunity）**：每轮 BEACON 后，各节点按序获得发送窗口
- **突发模式**：节点在单次 TO 内可发送多帧（Burst Count 可配）
- **主冗余**：协调器约 13ms 内未发出 BEACON，网络自动降级至 CSMA/CD 模式

## RCP 起源与标准化进程

| 时间 | 事件 |
|---|---|
| 2023 年 5 月 | 宝马在 IEEE TC14 工作组提出 RCP 概念 |
| 2024 年 7 月 | IEEE TC18 工作组成立，专项推进 RCP 标准化 |
| 当前 | Draft 0.2 版本，标准仍在制定中 |

## RCP 工作原理

- ZCU 生成 SPI/I2C/GPIO 等**原生总线指令**（而非封装成应用层消息）
- 将指令封装进 RCP 消息体，通过 10BASE-T1S 传输至边缘节点
- 边缘节点 RCP CORE（硬件状态机）直接解包执行，无需软件介入
- 延迟路径：ZCU 应用层 → RCP 封装 → 10BASE-T1S 传输（PLCA 确定性）→ 硬件执行

## RCP 封装协议选项对比

| 封装方式 | 特点 | 适用性 |
|---|---|---|
| SOME/IP | 成熟，广泛应用于 AUTOSAR，但开销较大 | 可用，非最优 |
| **IEEE 1722（AVTP）** | 低延迟，时间敏感，帧头开销小，原生支持 TSN | **更优选** |
| Protocol Buffers | 紧凑序列化，语言中立，已被 Onsemi 采用 | 实现层选项 |

作者观点：**IEEE 1722 更适合 RCP 封装**，因为其低延迟特性与 RCP 确定性控制目标更契合。

## MCU-less 三种部署方式

1. **端节点部署**：仅边缘节点使用 RCP 芯片，ZCU 保持传统 ECU 形态
2. **ZCU 部署**：ZCU 内运行 RCP 客户端软件，统一管理下挂所有 RCP 节点
3. **全链路部署**：从中央计算平台到边缘节点全链路 RCP 化，最大化软件定义能力

## 实际挑战

- **成本对比**：10BASE-T1S MAC+PHY 约十几元（RMB）vs CAN 收发器仅几毛钱
- **生态成熟度**：CAN 生态极其成熟，10BASE-T1S 工具链/调试手段仍在建立中
- **标准完整性**：RCP Draft 0.2，标准尚未最终确定，厂商实现存在差异

## 结论

MCU-less + 10BASE-T1S + RCP 是汽车 EEA 演进的重要技术路径，但与 CAN 的成本差距和生态成熟度问题需要时间解决。预计 2026–2028 年随量产项目落地逐步主流化。
