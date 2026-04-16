---
type: entity
title: "瑞萨电子"
date: 2026-04-15
updated: 2026-04-15
tags:
  - company
  - semiconductor
  - mcu
  - japan
entity_type: institution
aliases:
  - "瑞萨电子"
  - "Renesas Electronics"
  - "renesas-electronics"
  - "Renesas"
  - "瑞萨"
---

# 瑞萨电子（Renesas Electronics）

## Description

日本半导体厂商，全球微控制器（MCU）和微处理器（MPU）主要供应商之一。在机器人领域提供面向伺服控制与 EtherCAT 实时通信的芯片产品线，覆盖工业机器人（关节伺服驱动）和人形机器人（关节驱动、灵巧手、AI 视觉控制器）全场景解决方案。

## Key Contributions

- **工业机器人芯片矩阵**：
  - RZ/T2H：4×A55（1.2GHz）+2×R52（1.0GHz）异构 SoC，9轴电机控制+多协议工业以太网，单芯片驱控一体
  - RZ/T2M：双核 Cortex-R52（800MHz），双轴电机控制+EtherCAT/PROFINET/EtherNet-IP，高性能伺服首选
  - RZ/T2L：单核 Cortex-R52（800MHz），双轴电机控制+EtherCAT 从站，高性价比
  - RZ/N2L：Cortex-R52（200-400MHz），多协议工业网络 MCU，适合现有系统网络化升级
  - RX72M：Cortex-RXv3（240MHz），双精度 FPU，EtherCAT 从站，工业机器人经典方案
- **人形机器人芯片**：
  - RA8T2（2025年9月上市）：1GHz Cortex-M85+250MHz M33，22nm，16bit ADC，FOC 40kHz PWM，EtherCAT 从站；面向关节驱动和灵巧手主控
  - RZ/V2H：8TOPS DRP-AI+4×A55（1.8GHz）+2×R8（800MHz），支持 ROS2/Ubuntu 24.04；机器人 AI 视觉控制器（大脑+小脑架构）
- **灵巧手方案**：RA8T2 一主（手掌中枢，EtherCAT+CAN-FD）+ RA6/RA4 多从（手指微电机，多 DOF 控制），支持 micro-ROS
- **机器人开发套件**：电机解决方案套件（控制板+逆变板+BLDC电机+软件+文档），提供 CN032 参考设计，加速客户开发

## Related Concepts

- [[ethercat-realtime-communication]]
- [[dexterous-hand]]
- [[humanoid-robot]]

## Sources

- [[sources/renesas-robot-servo-ethercat-application]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为瑞萨电子机器人伺服控制与EtherCAT应用技术文档
