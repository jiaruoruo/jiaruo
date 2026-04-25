---
type: concept
title: "机器人软件架构"
date: 2026-04-25
updated: 2026-04-25
tags:
  - robot
  - software-architecture
  - ros
  - real-time
  - embodied-ai
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-04-25
aliases:
  - "机器人软件架构"
  - "Robot Software Architecture"
  - "robot-software-architecture"
  - "机器人软件栈"
---

# 机器人软件架构（Robot Software Architecture）

## Definition

机器人软件架构是机器人系统的神经中枢与运行骨架，决定机器人功能上限、控制精度、智能化水平与安全可靠性。目前行业主流采用**标准 5 层架构**，从底层到顶层依次为：HAL 硬件抽象层 → 驱动执行层 → 实时控制层 → 决策规划层 → 应用层，两大主流技术路线为 ROS/ROS2 分布式 与 自研全栈硬实时一体化架构。

## Key Points

- **标准 5 层架构**：
  - **HAL（硬件抽象层）**：屏蔽异构硬件差异，统一封装 GPIO/ADC/PWM/SPI/I2C/CAN/EtherCAT 等接口，是软硬件之间的"翻译官"
  - **驱动执行层（超高速硬实时）**：三环闭环控制（电流环 10-50kHz，控制抖动 <1μs），直接驱动电机；主流硬件：TI C2000/STM32G4H7/Xilinx Artix-7；控制算法：FOC/SMO/自适应PID
  - **实时控制层（硬实时）**：多轴协同插补、全维度动力学控制，控制周期 1-10kHz；与驱动层通过 EtherCAT/CAN 实现 μs 级同步；RTOS：FreeRTOS/QNX/VxWorks/Xenomai；框架：TwinCAT3/ROS2 Control；动力学库：RBDL/Pinocchio
  - **决策规划层（软实时）**：环境感知+全局规划+轨迹生成；ROS/ROS2 + MoveIt!/Navigation2；边缘计算平台：Jetson Orin/RK3588
  - **应用层（非实时）**：人机交互、编程开发、任务管理、状态监控；示教器/上位机PC/工控机
- **两大路线对比**：ROS 路线生态完善、开发快、跨场景复用；自研路线全链路硬实时、安全性强（ISO 13849/IEC 61508）、成本高；ABB/KUKA/FANUC/安川/特斯拉Optimus/宇树科技用自研，多数协作机器人/科研机构用 ROS
- **不同机器人类型适配**：工业机械臂→驱动+实时层极致；移动机器人→决策层 SLAM/导航；协作机器人→5 层均衡；**人形机器人→全栈极致优化，最高难度形态，硬实时+具身智能深度融合**
- **四大演进趋势**：①大小脑融合一体化（端到端延迟从百ms降至1ms）；②端侧 VLA 大模型赋能决策层；③云边端协同（端侧实时控制，云端训练+多机协同）；④软硬协同全栈优化（专用芯片+指令集）

## My Position

## Contradictions

## Sources

- [[sources/robot-software-architecture-intro]]

## Evolution Log

- 2026-04-25（1 sources）：概念初建，来源为具身智能研发基础入门文章；建立5层架构+两大路线+人形机器人适配的完整认知框架
