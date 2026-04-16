---
type: concept
title: "准直驱电机"
date: 2026-04-15
updated: 2026-04-15
tags:
  - motor
  - actuator
  - robotics
  - hardware
source_count: 2
confidence: low
domain_volatility: medium
last_reviewed: 2026-04-15
aliases:
  - "准直驱电机"
  - "Quasi-Direct Drive Motor"
  - "quasi-direct-drive-motor"
  - "准直驱"
  - "QDD 电机"
---

# 准直驱电机（Quasi-Direct Drive Motor）

## Definition

准直驱电机（Quasi-Direct Drive，QDD）是一种采用低减速比（1:6~1:9）行星减速器配合大直径无框电机的关节驱动方案。相比谐波减速器（减速比1:50~1:160），准直驱保留了直驱电机的高力控带宽和高透明度（backdrivability），同时通过低比减速器在不牺牲过多动态响应的前提下提升输出扭矩，是新一代人形机器人和四足机器人的主流驱动方案。

## Key Points

- **与谐波减速器对比**：
  - 准直驱：减速比1:6~1:9，力矩密度8-15 Nm/kg，控制带宽>100Hz，背隙极小，成本中等
  - 谐波减速器：减速比1:50~1:160，力矩密度5-10 Nm/kg，控制带宽10-30Hz，零背隙，成本高（¥2000-5000/个）
- **代表产品**：
  - **小米 Cybergear**：扭矩密度0.29 Nm/g（业界领先），额定12Nm/峰值27Nm，重量92g，减速比1:8，力控带宽>100Hz；N52高磁能积永磁体 + FOC 精确控制
  - **宇树关节模组**：额定35Nm/峰值80Nm，重量约500g，减速比1:6，开源控制协议，支持力矩控制
- **控制技术**：FOC（磁场定向控制）实现高效率（>90%）精确力矩输出；阻抗控制 `τ = K(θ_d - θ) + B(θ̇_d - θ̇)` 实现柔顺交互
- **成本**：准直驱关节约¥300-800/个，远低于谐波方案（¥2000-5000/个），且更适合国产化（谐波减速器被日本 Harmonic Drive 垄断）
- **适用场景**：强化学习训练（需要高力控带宽）、动态运动（跑跳）、快速迭代开发；精密装配场景仍推荐谐波减速器
- **技术趋势**：宇树、小米、1X Technologies 均已采用，正成为新一代机器人主流选择

## My Position

## Contradictions

## Sources

- [[sources/robot-sensor-actuator-communication]]
- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：概念初建，来源为人形机器人技术研究及快速原型建设报告
- 2026-04-15（2 sources）：强化——传感器沙盘补充伺服驱动视角：FOC 控制频率数十kHz、相位延迟极低、自适应/前馈补偿等与现有准直驱内容一致
