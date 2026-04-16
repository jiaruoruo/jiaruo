---
type: entity
title: "RoboCasa"
date: 2026-04-15
updated: 2026-04-15
tags:
  - simulation
  - imitation-learning
  - open-source
  - kitchen-manipulation
entity_type: tool
aliases:
  - "RoboCasa"
  - "robocasa"
  - "RoboCasa 仿真平台"
---

# RoboCasa

## Description

MIT/Stanford 联合开发的厨房日常操作仿真平台，提供丰富的家庭场景资产和任务库，专注于构建大规模轨迹数据集（论文版本指向100K量级轨迹规模）。是模仿学习（IL）起步阶段的重要数据来源，也是机器人泛化训练的基础平台之一。

## Key Contributions

- 厨房场景任务库：覆盖日常家务操作（开关门、放置物品、整理等），贴近家庭服务机器人应用场景
- 大规模轨迹数据集构建路径：100K量级轨迹，支持模仿学习快速启动策略
- 与 Isaac Lab 等训练框架配合，支持"IL 起步 → RL 微调"工程路线

## Related Concepts

- [[robot-simulation-framework]]
- [[embodied-ai]]
- [[sim-to-real-transfer]]

## Sources

- [[sources/openclaw-simulation-rl-agent]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为 OpenClaw × Simulation × RL 文章
