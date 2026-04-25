---
type: source
title: "机器人软件架构介绍——具身智能研发基础"
date: 2026-04-24
source_url: "https://mp.weixin.qq.com/s/WYGjsy3vHAR134HODtYn4Q"
domain: "mp.weixin.qq.com"
author: "学长就业辅导"
tags:
  - robot
  - software-architecture
  - ros
  - real-time
  - embodied-ai
  - humanoid
processed: true
raw_file: "raw/clippings/2026-04-24机器人软件架构介绍——具身智能研发基础.md"
raw_sha256: "aff7a32c7aaaaa07daac374c97080317c68113ff715efa3dd004bf12184ab8bb"
last_verified: 2026-04-25
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 机器人软件架构介绍——具身智能研发基础

## Summary

本文系统介绍机器人软件架构的核心知识，包括标准 5 层架构、两大技术路线（ROS/ROS2 分布式 vs 自研全栈硬实时）、不同机器人类型的架构适配，以及演进趋势（大小脑融合、端侧 VLA、云边端协同）。定位为具身智能研发基础入门材料。

## Key Points

- **标准 5 层架构**（从底到顶）：HAL 硬件抽象层 → 驱动执行层（超高速硬实时，电流环 10-50kHz）→ 实时控制层（硬实时，1-10kHz）→ 决策规划层（软实时）→ 应用层（非实时）
- **HAL 层**：屏蔽异构硬件差异（GPIO/ADC/PWM/SPI/I2C/CAN/EtherCAT 统一封装），上层无需修改即可适配不同品牌执行器
- **驱动执行层**：三环闭环（电流环/速度环/位置环），硬件级安全保护（纳秒级响应），主流硬件：TI C2000/STM32G4H7/Xilinx Artix-7；控制算法：FOC/SMO/自适应PID
- **实时控制层**：多轴协同插补（直线/圆弧/NURBS样条），全维度动力学控制，与驱动层通过 EtherCAT/CAN μs 级同步；RTOS：FreeRTOS/QNX/VxWorks/Xenomai；框架：倍福 TwinCAT3/ROS2 Control；动力学库：RBDL/Pinocchio/KDL
- **决策规划层**：ROS/ROS2 + MoveIt!/Navigation2；多模态感知（OpenCV/PCL/OMPL）；边缘计算：NVIDIA Jetson Orin/RK3588
- **两大路线对比**：ROS 路线生态完善但实时性有上限；自研路线全链路硬实时但成本高；ABB/KUKA/FANUC/安川/特斯拉Optimus/宇树用自研，大多数协作机器人用ROS
- **人形机器人**：最高难度形态，需全身动力学控制 + 具身智能深度融合，硬实时与 AI 双重要求
- **演进四趋势**：大小脑融合一体化（延迟从百ms降至1ms）、端侧VLA赋能决策层、云边端协同、软硬协同全栈优化（专用芯片+指令集）

## Concepts Extracted

- [[robot-software-architecture]]
- [[ethercat-realtime-communication]]
- [[humanoid-robot]]
- [[embodied-ai]]

## Entities Extracted

- [[entities/unitree-robotics]]

## Contradictions

## My Notes

这篇文章填补了知识库中"机器人软件系统工程层"的空白——之前的来源主要关注具体通信协议（EtherCAT/GPAN）或芯片方案，缺少完整的软件分层架构视图。5 层架构 + 实时性要求梯度是理解机器人系统工程的核心框架。
