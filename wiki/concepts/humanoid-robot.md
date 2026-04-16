---
type: concept
title: "人形机器人"
date: 2026-04-15
updated: 2026-04-15
tags:
  - humanoid-robot
  - robotics
  - embodied-ai
source_count: 3
confidence: low
domain_volatility: high
last_reviewed: 2026-04-15
aliases:
  - "人形机器人"
  - "Humanoid Robot"
  - "humanoid-robot"
  - "仿人机器人"
---

# 人形机器人（Humanoid Robot）

## Definition

人形机器人（Humanoid Robot）是具有接近人类形态（双足、双臂、头部）的机器人，能够在为人类设计的环境中工作并执行多样化任务。当前主流人形机器人身高173-180cm，重量47-70kg，21-28个关节自由度（DOF），续航1-2小时，集成大脑模型（高层决策）和小脑模型（运动控制）的分层架构。

## Key Points

- **技术架构**：大脑（多模态大模型/具身智能框架，10Hz）+ 小脑（强化学习/MPC，1kHz）+ 混合架构为当前最佳实践
- **主流厂商技术路线**：
  - 宇树 H1（TRL 7）：RL + 准直驱电机 + 开源生态，行走速度3.3m/s
  - 特斯拉 Optimus Gen2（TRL 6）：端到端神经网络 + 数据飞轮 + 11 DOF 灵巧手，57kg
  - 小米 CyberOne（TRL 5-6）：Cybergear 电机（0.29 Nm/g）+ IoT 生态，21 DOF
  - 小鹏 PX5（TRL 4-5）：汽车工程跨界 + 制造优势，约70kg
  - 智元 Agibot（TRL 5-6）：清华学术工程化 + 灵巧操作见长
- **硬件关键指标**（2025年数据）：重量47-70kg，身高173-180cm，DOF 21-28，灵巧手11-24 DOF，续航1-2小时，准直驱力矩密度0.29 Nm/g（最高）
- **市场规模**：2025年约53亿美元，预计2030年380亿美元（IDC）
- **快速原型方案**：Isaac Gym + Octo + ROS 2 + EtherCAT，约53万元、2.5人团队、12-18周可完成功能原型
- **技术发展阶段**：2000-2010机械本体阶段 → 2015-2020控制算法突破 → 2021-2023 AI 赋能爆发 → 2024-2025产业化加速 → 2026+通用化与规模量产
- **核心挑战**：端到端黑盒安全性、长尾场景泛化、电池续航（1-2小时）、灵巧操作精度（精细任务成功率<70%）

## My Position

## Contradictions

## Sources

- [[sources/robot-sensor-actuator-communication]]
- [[sources/renesas-robot-servo-ethercat-application]]
- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：概念初建，来源为人形机器人技术研究及快速原型建设报告
- 2026-04-15（2 sources）：强化——瑞萨官方文档与现有定义一致；补充芯片级方案视角：RA8T2/RZ/T2L 关节驱动（FOC+EtherCAT），RZ/V2H 作为 AI 控制器实现大脑+小脑架构
- 2026-04-15（3 sources）：强化——传感器沙盘补充状态感知融合需求（状态估计延迟<5ms、频率>500Hz）与现有定义一致
