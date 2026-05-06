---
type: source
title: "MCULess 半导体厂商调研报告"
date: 2026-04-28
raw_file: raw/clippings/MCULess调研报告.md
raw_sha256: 270332ab2338f56597765016a28a064d2082e2bb5be9a6f86239aa363e43ea9e
source_url: ""
author: ""
tags:
  - mculess
  - automotive
  - semiconductor
  - adi
  - ti
  - nxp
  - st-microelectronics
  - infineon
  - goodix
concepts:
  - "[[concepts/mculess-architecture]]"
  - "[[concepts/gpan-communication]]"
  - "[[concepts/can-eth-protocol-conversion]]"
entities:
  - "[[entities/goodix-technology]]"
  - "[[entities/infineon-technologies]]"
  - "[[entities/st-microelectronics]]"
last_verified: 2026-04-28
---

# MCULess 半导体厂商调研报告

## Summary

内部调研报告，全面梳理当前 MCU-less 芯片生态：仅 ADI 和 TI 有通用 MCU-less 芯片量产（IO 数量少、价格偏高）；ST/Infineon 有 LED 驱动领域的量产芯片；汇顶科技 GE1101 以 64 路 IO + 100BaseT1 在规格上最全，计划 2026 年 Q2 量产。各厂商均在与 OEM 联合探讨 MCU-less 方案布局。

## Key Points

- **MCU-less 核心价值**：去除外围节点 MCU，实现"计算中心化、外围简化"；降低 MCU 数量 / 软件复杂度 / OTA 成本，提升 E/E 架构灵活性
- **各厂商方案对比**：

  | 厂商 | 代表器件 | IO 数量 | 通信方式 | 单价 | Roadmap |
  |---|---|---|---|---|---|
  | ADI | AD3300/3301/3304/3305 | 12 路 SAIF | 10BASE-T1S（E²B） | $1.3 | 2028 年量产 40 路 IO |
  | TI | PTCAN5102DGQRQ1 | 13 路（无 ADC） | CAN FD Light / 10BASE-T1S | $0.487 | 2025 Q3：20 路；2026 Q4：32 路 |
  | NXP | SJA1124（LIN 桥接） | 16/24 路（LED） | LIN / CAN FD Light（在研）| - | 仍在设计规划 |
  | ST | L99LDLH32/L99LDLL16 | 32/16 路 LED | CAN FD Light | - | 2028 年量产 96 路 |
  | Infineon | TLD7002-16ES | 16 路 LED | CAN FD Light（主推）| - | 2025 年前发布首代 |
  | 汇顶科技 | GE1101 | **64 路** | **100BaseT1，环网/菊花链** | ~14 RMB | 2026 Q2 量产 |

- **ADI E²B 方案细节**：
  - 支持 SPI/I²C/UART/PWM/GPIO/LIN 多种 IO 配置
  - 集成 MAC/PHY，使用低复杂度 E²B 协议栈
  - 2024 年发布首批芯片，已支持 BMW 灯光系统量产
- **TI 方案细节**：
  - SPI 传感器 + 集成 PHY，实现通信协议硬件桥接
  - 价格优势明显（$0.487 vs ADI $1.3），但 IO 无 ADC
- **NXP 方案细节**：已有 SJA1124 LIN 桥接器量产；多通道 CAN FD Light LED 驱动器在研
- **ST 方案细节**：L99LDLH32 每通道电流 1–15mA 可编程 PWM；已支持量产（2022 年首款），2028 年扩展至 96 路
- **Infineon 方案方向**：LITIX™ LED 驱动升级集成 CAN FD Light；MOTIX™ 电机驱动集成 CAN FD Light，实现门窗/座椅控制器 MCU-less 化
- **汇顶科技 GE1101 竞争优势**：
  - 64 路 IO（远超其他厂商）
  - 支持 SPI/I²C/UART/PWM/GPIO/LIN/CAN/TDM 全类型 IO
  - 100BaseT1（vs 竞品 10BaseT1S），速率领先 10 倍
  - 环网/菊花链组网，支持更复杂拓扑
  - 价格约 14 RMB，与 MCU S32K144（~14 RMB）持平
- **汽车应用场景**：
  - 区域控制器（ZCU）：小 MCU + MCU-less 组合，防夹等快速闭环留在小 MCU，锁驱动/照明/电机等中低速任务由 MCU-less 执行
  - 终端执行控制器：车灯系统（ST/NXP 驱动器，中央直接发动画命令）、电动座椅（CAN FD Light 多电机控制）、传感器网络（直接上报中央 ECU）
- **成本结构对比**：MCU-less 方案无需 Flash/SRAM，芯片面积更小；单芯片集成减少 PCB 面积；但当前单芯片价格仍偏高，IO 数量有限
- **现状总结**：MCU-less 有利于软硬件解耦、整车软件集中化、降本增效（MCU 成本 + OTA 效率）；但当前处于起步阶段——IO 少、价格高，尚无明显成本优势

## Quotes

> "当前只有 ADI/TI 有通用 MCU-less 芯片量产，但 IO 数量很少，价格较高"

> "MCU-less 有利于实现软硬件解耦，实现整车软件集中化，从而实现降本（MCU 成本）增效（功能迭代，OTA）"

> "当前 MCU-less 芯片 IO 数量比较少，不符合区域控制器的应用需求；MCU-less 单芯片价格比较高，和同等 IO 数量 MCU 相比还没有成本优势"
