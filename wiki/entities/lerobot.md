---
type: entity
title: "LeRobot"
date: 2026-04-15
updated: 2026-04-15
tags:
  - open-source
  - robotics
  - framework
  - huggingface
entity_type: tool
aliases:
  - "LeRobot"
  - "lerobot"
  - "Hugging Face LeRobot"
---

# LeRobot

## Description

Hugging Face 开发的机器人学习统一框架（2024年启动，GitHub 4.1k stars），类似 Hugging Face Transformers 在 NLP 的地位。集成 ACT（50Hz）、Diffusion Policy（10-30Hz）、TDMPC（20Hz）等多种 SOTA 算法，提供统一 API 和预训练模型库，支持自定义数据集。核心价值：几十行代码即可训练机器人操作策略，大幅降低入门门槛。

## Key Contributions

- 统一 API：不同算法使用相同接口，降低学习成本；模块化设计（数据加载/训练/评估分离）
- 预训练模型库：`lerobot/act_aloha_mobile`、`lerobot/diffusion_pusht` 等可直接使用
- ACT（Action Chunking Transformer）：22M 参数，50-200条演示，50Hz 推理，适合双臂精细操作
- 标准化数据格式：HDF5 episode 文件，兼容 RLDS/TFDS/RoboMimic，支持 Hugging Face Hub 共享

## Related Concepts

- [[embodied-ai]]
- [[sim-to-real-transfer]]

## Sources

- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为人形机器人技术研究及快速原型建设报告
