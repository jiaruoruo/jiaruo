---
type: source
title: "MCULess Based ZCU 验证——BZCU 硬件 IO 需求规格"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "内部硬件验证团队"
tags:
  - mculess
  - bzcu
  - hardware
  - io-spec
  - automotive
processed: true
raw_file: "raw/pdfs/MCULess Based ZCU验证.pdf"
raw_sha256: "bb0459e51ca4a486d58970c633dc3adb5c74c6b45f44602631633c0062317c0c"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCULess Based ZCU 验证——BZCU 硬件 IO 需求规格

## Summary

本文档详细列出了 MCULess BZCU（Body Zone Control Unit）验证板的硬件 IO 需求规格，涵盖 HSD（高边驱动）、H-Bridge（桥式驱动）、EFUSE（电子熔断器）、传感器输入、Hall 传感器等超过 40 类驱动芯片类型，为 GPAN 方案替代传统 ZCU MCU 的硬件可行性提供了完整的外设需求清单。

## Key Points

- **BZCU 定位**：BZCU（Body Zone Control Unit）为理想汽车 EEA 3.0 架构中负责后备箱/后排车身控制的区域控制器，在 MCULess 方案中作为第一阶段验证目标
- **HSD（High Side Driver）需求**：
  - 多路 HSD 输出（典型 8/16/24 路），控制电动门锁、继电器、LED 灯组等负载
  - 要求支持短路/过热保护，故障反馈到 GPAN 主控
  - 典型驱动芯片：Infineon TLE6220、NXP MC33810 等系列
- **H-Bridge（桥式驱动）需求**：
  - 用于座椅调节电机、车窗电机、后备箱电动撑杆等双向运动负载
  - 要求峰值电流 ≥5A，支持 PWM 调速，具备过流锁定和热保护
  - 典型驱动芯片：Infineon BTN8982、TI DRV8876 系列
- **EFUSE（电子熔断器）需求**：
  - 替代传统保险丝，可编程限流，支持远程复位
  - 典型驱动芯片：Infineon BTS71811、NXP NCFS1100 系列
- **传感器输入需求**：
  - 模拟信号：NTC 温度传感器、电位计（线性霍尔）→ 需 12-bit ADC 精度
  - 数字信号：按键/微动开关输入，需 ESD 保护和滤波
  - 电流检测：低边电流检测（分流电阻 + 运放），用于负载状态监测
- **Hall 传感器需求**：
  - 用于座椅位置检测和电机换向，输出为脉冲信号
  - 要求 GPAN 节点具备脉冲计数功能（通过 GPIO 中断计数实现）
- **40+ 驱动芯片类型**：文档枚举超过 40 种外设驱动芯片类型，覆盖照明/电机/继电器/传感器/保护电路等完整车身域 IO 需求

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/zonal-gateway]]
- [[concepts/eea-architecture]]

## Entities Extracted

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Contradictions

<!-- 暂无 -->

## My Notes

BZCU 的 IO 需求种类繁多（40+ 类驱动芯片），说明 MCULess 方案要替代传统 ZCU MCU，GPAN 芯片的 GPIO 扩展能力和实时性必须满足严苛要求。相比软件 MCU 可通过编程灵活适配，GPAN 硬件路由方式对预先配置的正确性要求更高。
