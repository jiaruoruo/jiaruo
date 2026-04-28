---
type: source
title: "售前方案——理想汽车 GPAN 座椅控制器（v1.1）"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "恒润科技（Hirain）"
tags:
  - gpan
  - seat-controller
  - li-auto
  - presales
  - automotive
processed: true
raw_file: "raw/pdfs/售前方案-理想GPAN座椅v1.1.pdf"
raw_sha256: "05afd97b7ca2ba70217569c82da8284146db084d54dc4f247da5cc54fc901ce7"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 售前方案——理想汽车 GPAN 座椅控制器（v1.1）

## Summary

本文档为恒润科技（Hirain）针对理想汽车 GPAN 座椅控制器项目的售前技术方案（v1.1），详细描述了基于 BGA144 封装 GE1101 GPAN 芯片的座椅控制器硬件架构、电机 Hall 控制方案、多种唤醒方式的响应时间，以及 10ms 周期内的通信数据量规格。

## Key Points

- **方案背景**：理想汽车采用 GPAN 网络替代传统 LIN 总线实现座椅控制器通信，恒润科技作为 Tier-1 供应商提供完整座椅控制器方案
- **核心芯片**：GE1101，采用 **BGA144** 封装，集成 GPAN 网络物理层 + 以太网 MAC + 多路 CAN/LIN/GPIO/TDM 接口
- **硬件架构**：
  - 1 个 GE1101（BGA144）作为主控通信芯片，直接挂接 GPAN 网络
  - 多路 HSD 驱动芯片控制座椅加热/通风
  - H-Bridge 驱动芯片控制座椅调节电机（前后/靠背/高低调节）
  - Hall 传感器接口用于电机位置检测
  - 无独立主机 MCU（完整 MCULess 方案）
- **座椅电机 Hall 控制**：
  - 采用无刷直流电机（BLDC）+ 内置 Hall 传感器方案
  - Hall 脉冲信号直接连接 GE1101 GPIO 中断引脚，由 GPAN 芯片计数并上报位置
  - 电机换向指令由域控通过 GPAN 帧下发，芯片硬件转发给 H-Bridge
- **唤醒方案与响应时间**：
  - **CAN 总线唤醒**：收到 CAN wake pattern 后系统唤醒，响应时间 **115ms**
  - **AD 模拟量唤醒**：压力传感器或重量传感器超阈值（如有人坐下检测），响应时间 **112.5ms**
  - **IO 数字量唤醒**：按键/微动开关边沿触发唤醒，响应时间 **111ms**
- **通信数据量规格**（10ms 周期帧）：
  - **上行（座椅→域控）**：每帧 **149 字节**，包含 Hall 计数/电机状态/传感器 ADC 值/故障码
  - **下行（域控→座椅）**：每帧 **164 字节**，包含电机使能/方向/PWM 占空比/加热等级/通风档位
  - 10ms 周期对应 100Hz 控制频率，满足座椅舒适功能实时性要求

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/zonal-gateway]]

## Entities Extracted

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Contradictions

<!-- 暂无 -->

## My Notes

本文档是 GPAN MCULess 方案在具体车型（理想汽车）具体零件（座椅控制器）上的实际应用案例，说明方案已经进入 Tier-1 售前阶段。恒润科技作为 Tier-1 参与，也说明 GPAN 生态正在向下游零部件厂商延伸。149/164 字节的 10ms 帧数据量较传统 LIN 总线（最大 8 字节/帧）大幅增加，体现了 GPAN 高带宽的优势。
