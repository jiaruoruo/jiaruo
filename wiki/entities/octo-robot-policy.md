---
type: entity
title: "Octo"
date: 2026-04-15
updated: 2026-04-15
tags:
  - open-source
  - embodied-ai
  - robot-policy
  - pretrained-model
entity_type: tool
aliases:
  - "Octo"
  - "octo-robot-policy"
  - "Octo Robot Policy"
  - "octo-models"
---

# Octo

## Description

UC Berkeley 与 Stanford 联合开发的通用机器人策略模型（2024年，arXiv:2405.12213，GitHub 2.8k stars）。核心创新：跨具身迁移能力——一个模型适配22种机器人平台。93M 参数，在 Open X-Embodiment 数据集（80万轨迹）上预训练，推理速度10Hz，开源权重（Apache 2.0），迁移至新机器人仅需50-200条演示数据。

## Key Contributions

- 跨具身迁移：Embodiment Embedding（每种机器人专属嵌入）+ Adapter Layers（<5%参数微调），零样本成功率52%，微调50条演示后78%
- 预训练效率：8×A100 GPU 训练约7天；相比从头训练（1000条演示，24小时），微调版本（50条演示，2小时）成功率反而更高
- 开源生态：完整预训练权重、微调示例（`02_finetune_new_robot.py`）、评估脚本，适合快速原型验证
- 快速原型推荐方案：`octo-small` 或 `octo-base` + 自采集50-200条演示 → 2-5天完成微调部署

## Related Concepts

- [[embodied-ai]]
- [[sim-to-real-transfer]]

## Sources

- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为人形机器人技术研究及快速原型建设报告
