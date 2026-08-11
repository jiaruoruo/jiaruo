---
type: source
title: "灵巧手处理器选型详细设计"
date: 2026-07-13
source_url: ""
domain: "robotics"
author: "internal-note"
tags: ["dexterous-hand", "mcu", "soc", "motor-control"]
processed: true
raw_file: raw/工作/notes/机器人/灵巧手处理器选型详细设计.md
raw_sha256: 85c4b600e57f9c657de0bfb2513f5b4f5da56fb37a04e1f1dd81bb86e90fa1f5
last_verified: 2026-07-13
possibly_outdated: false
language: "zh"
canonical_source: ""
---
# 灵巧手处理器选型详细设计

## Summary

灵巧手处理器选型详细设计（2026-07-01），基于需求规格约束(闭环<2ms、>1kHz、EtherCAT、48V/250W)做计算量估算，给出异构双核(实时MCU+非实时MPU)选型对比与最终三方案。

## Key Points

- 计算量：实时控制~737 MFLOPs(FOC+PID+反射库+融合)，非实时~396 MFLOPs(MPC+手势库)，合计~1.1 GFLOPs；实时部分MCU可承担
- 异构双核架构：实时域 Cortex-M(FOC/位置环/反射库/EtherCAT从栈/安全看门狗)+非实时域 Cortex-A(MPC/手势库/OTA/ROS2桥接)
- 实时MCU推荐 STM32H753(M7 480MHz,4MB Flash,1MB SRAM,FPU,16 PWM,生态⭐⭐⭐⭐⭐)
- 非实时MPU推荐 STM32MP157(双核A7+M4 A-Sync,0.5-2W,小尺寸6×6mm)
- 三最终方案：A双芯片(H753+MP157,~$24)性能最优 / B单芯片MP157 A-Sync(~$14)成本空间最优 / C单MCU H753(~$12)最简
- 引脚分配：TIM1/8/3/4 PWM驱动各指电机；ADC1/2/3循环DMA采样编码器+相电流+六维力/触觉≥1kHz；ETH+ESC主通信、SPI MCU↔MPU、CAN预留

## Concepts Extracted

- [[dexterous-hand]]
- [[embedded-system]]
- [[soc-design]]

## Entities Extracted


## Contradictions


## My Notes


<!-- source_type: technical-note; raw_sha256 已校验 -->
