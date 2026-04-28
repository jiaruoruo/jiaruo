---
title: 汽车ECU的MCU-less变革：从分布式走向中央计算的关键路径
slug: mculess-ecu-central-computing-path
source_url: https://mp.weixin.qq.com/s/hr61klU7pMRb7TIZyrMY8w
author: 汽车电子工程笔记
published: 2026-04-28
ingested: 2026-04-28
sha256: b6697bab
tags: [mculess, 10base-t1s, rcp, can-fd-light, automotive, eea]
concepts: [mculess-architecture, eea-architecture, can-eth-protocol-conversion]
entities: []
---

# 汽车ECU的MCU-less变革：从分布式走向中央计算的关键路径

## 核心摘要

从定义、驱动力、技术流派三个维度系统解析 MCU-less 变革。明确指出 MCU-less 并非 MCU 消亡，而是 MCU 职责的重新分配：边缘做减法，中央做加法。

## MCU-less 定义

MCU-less 边缘节点：边缘 ECU 去掉通用 MCU，仅保留专用 IO 扩展/控制芯片，控制逻辑迁移至区域控制器（ZCU）或中央计算平台。

## 三大驱动力

1. **降本**：MCU + 外围器件 BOM $15–25 → RCP 芯片方案 $8–12，降幅约 40%
2. **软硬解耦**：硬件标准化，功能通过软件OTA升级，无需硬件改版
3. **EEA 演进**：分布式→集中式→区域化，MCU-less 是区域化的最后一公里

## 三大技术流派

### 流派一：UART over CAN（软硬混合）
- 代表：TI、Infineon 方案
- 原理：保留 CAN 总线物理层，上层协议替换为简化串行指令
- 适用：改造成本低，兼容现有 CAN 网络

### 流派二：10BASE-T1S + RCP（以太网路线）
- 代表：ADI E2B（宝马量产）、Onsemi RCP、Microchip LAN8660
- 原理：10BASE-T1S 单对以太网 + RCP 协议远程控制 IO
- 适用：新平台，高带宽需求，追求确定性延迟

### 流派三：CAN FD Light（简化 CAN）
- 代表：ST（1991dlh32）
- 原理：简化 CAN FD 帧格式，专为 LED/简单执行器设计
- 适用：超低成本场景，车灯/简单传感器

## "MCU+" 趋势

边缘节点从 MCU 做减法 → 中央/区域控制器做加法（高算力 SoC），形成"MCU+" 生态：
- 边缘：最小化硬件，专用 IO 芯片
- 区域：高集成 SoC（NXP S32G/S32K5、瑞萨 R-Car 系列）
- 中央：AI 加速，整车级软件调度

## 核心洞察

**MCU-less 不是 MCU 消亡，而是 MCU 职责重新分配。** 边缘节点的控制职责上移，中央/区域控制器承担更多智能化工作，整体系统向软件定义汽车（SDV）演进。
