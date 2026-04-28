---
type: source
title: 硬件极简化革命：从传统ECU到MCU-less边缘节点的设计变革
slug: mculess-hardware-simplification-revolution
date: 2026-04-28
source_url: https://mp.weixin.qq.com/s/zEl1EF_5e21-igpDJ5hkvg
author: 汽车电子老登
published: 2026-04-28
ingested: 2026-04-28
sha256: 9c17ce58
tags: [mculess, rcp, 10base-t1s, can-fd-light, gpan, automotive, bom-cost, asil]
concepts: [mculess-architecture, eea-architecture, can-eth-protocol-conversion]
entities: [goodix-technology]
---

# 硬件极简化革命：从传统ECU到MCU-less边缘节点的设计变革

## 核心摘要

从传统 ECU 硬件结构出发，量化分析 MCU-less 方案的成本节省，并提供详细的 RCP 芯片选型对比表（ADI / Onsemi / Microchip / 汇顶 / ST）。

## 传统 ECU 六大硬件模块（BOM $15–25）

1. MCU 主控芯片
2. 晶振（时钟源）
3. 复位电路
4. 存储器（Flash/EEPROM）
5. 电源管理电路
6. 通信接口（CAN/LIN 收发器）

MCU-less 方案删除上述 1–4 项，PCB 面积从 25×35mm 缩减至 15×20mm，BOM 降至 $8–12，节省约 40%。

## RCP 芯片选型对比表

| 厂商 | 型号 | 封装 | IO 数量 | 物理层速率 | 延迟 | 价格（参考）| 状态 |
|---|---|---|---|---|---|---|---|
| ADI | AD3301 | QFN | 12 | 10 Mbps | <1ms | ~$1.3 | 量产 |
| ADI | AD3304 | QFN | 12 | 10 Mbps | <1ms | ~$1.3 | 量产（宝马采用）|
| ADI | AD3305 | QFN | 12 | 10 Mbps | <1ms | ~$1.3 | 量产 |
| Onsemi | T30HM1TS3600 | — | 10 | 10 Mbps | <1ms | — | 样片 |
| Onsemi | T30HM1TS3610 | — | 20 | 10 Mbps | <1ms | — | 样片 |
| Microchip | LAN8660 | — | 16 | 10 Mbps | — | — | — |
| 汇顶科技 | GE1101 | BGA144 | 120/45 IO | 100 Mbps | ~50 μs | ~14 RMB | 预计 2026Q3 |
| ST | 1991dlh32 | — | — | 500K–2 Mbps（CAN FD）| 低 | — | — |

## RCP 芯片内部架构

RCP 芯片核心是**硬件状态机**（非 MCU 软件），实现：
- 接收 ZCU 通过 10BASE-T1S 发来的 RCP 指令
- 硬件直接执行 GPIO/PWM/SPI/I2C/UART 操作
- 无需操作系统，无需软件开发，极低延迟

## 电源管理集成优化

- 传统 ECU：独立电源管理 IC + LDO + 多路电源轨
- MCU-less 方案：RCP 芯片集成内部 LDO（如 T30HM1TS3600 的 1.2V LDO），减少外部器件
- 支持 PoDL（以太网供电），可通过 10BASE-T1S 单对线同时传输数据和供电

## 成本与尺寸量化对比

| 指标 | 传统 ECU | MCU-less 方案 | 节省 |
|---|---|---|---|
| 节点 BOM | $15–25 | $8–12 | ~40% |
| PCB 面积 | 25×35 mm | 15×20 mm | ~51% |
| 线束减重 | 基准 | — | 50–60% |

## 功能安全

- 目标等级：ASIL-B
- 通过集中化错误处理和 ZCU 侧冗余逻辑实现
- 边缘节点硬件状态机确定性行为，降低随机硬件故障率（PMHF）
