---
type: entity
title: "robosuite"
date: 2026-04-15
updated: 2026-04-15
tags:
  - simulation
  - open-source
  - mujoco
  - reinforcement-learning
entity_type: tool
aliases:
  - "robosuite"
  - "Robosuite"
  - "ARISE robosuite"
---

# robosuite

## Description

基于 MuJoCo 的机器人学习仿真框架（v1.5），由斯坦福 SVL（2017年创建）、UT RPL 和 NVIDIA GEAR 共同维护。GitHub：`ARISE-Initiative/robosuite`。提供标准化操作任务库（19种）、10种机器人模型（含人形 GR1ArmsOnly）、高质量控制器实现，支持强化学习和模仿学习，兼容 OpenAI Gym API。

## Key Contributions

- 19种标准化操作任务：门开关、升降机、螺母组装、拾取放置、堆叠、双臂协作、擦拭等，覆盖主流机器人操作场景
- 10种机器人支持：包括人形机器人（GR1ArmsOnly）、移动机器狗（SpotWithArmFloating）、主流机械臂（Panda/UR5e/Sawyer等）
- v1.5 新特性：全身控制器（WBC）、人形机器人支持、自定义机器人组合、照片级渲染
- `pip install robosuite` 一键安装，API 与 OpenAI Gym 兼容，极低入门门槛

## Related Concepts

- [[robot-simulation-framework]]
- [[reinforcement-learning-locomotion]]
- [[embodied-ai]]

## Sources

- [[sources/robosuite-quickstart]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为 robosuite 快速入门教程
