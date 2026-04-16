---
type: entity
title: "Isaac Gym"
date: 2026-04-15
updated: 2026-04-15
tags:
  - simulation
  - reinforcement-learning
  - nvidia
  - tool
entity_type: tool
aliases:
  - "Isaac Gym"
  - "isaac-gym"
  - "NVIDIA Isaac Gym"
  - "Isaac Lab"
---

# Isaac Gym

## Description

NVIDIA 开发的 GPU 加速物理仿真器，专为强化学习训练设计（非商业许可）。核心创新：单张 A100 GPU 并行16,000+仿真环境，基于 PhysX 5 GPU 加速，实现10,000-20,000x 吞吐提速（相比 PyBullet/MuJoCo CPU 方案）。后继产品为 Isaac Lab（2.1k stars，模块化 RL 框架）。是人形机器人和四足机器人强化学习训练的事实标准工具。

## Key Contributions

- 大规模并行仿真：16,000+环境单 GPU，零拷贝（物理状态全程留存 GPU 内存），训练时间从数周缩至数小时
- Sim-to-Real 基础设施：内置域随机化支持（摩擦/质量/延迟参数化），宇树 H1 等多个成功案例验证
- 人形机器人任务模板：内置 Humanoid、Quadruped、Manipulation 等任务，快速启动
- 典型训练周期：四足步态约12小时（A100），人形行走12-24小时；策略导出 ONNX 后直接部署真机

## Related Concepts

- [[reinforcement-learning-locomotion]]
- [[sim-to-real-transfer]]
- [[humanoid-robot]]

## Sources

- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为人形机器人技术研究及快速原型建设报告
