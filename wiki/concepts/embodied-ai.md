---
type: concept
title: "具身智能"
date: 2026-04-15
updated: 2026-04-15
tags:
  - embodied-ai
  - robotics
  - llm
  - end-to-end
source_count: 2
confidence: low
domain_volatility: high
last_reviewed: 2026-04-15
aliases:
  - "具身智能"
  - "Embodied AI"
  - "embodied-ai"
  - "具身人工智能"
---

# 具身智能（Embodied AI）

## Definition

具身智能（Embodied AI）是指将感知、认知与物理行动统一在一个智能体中，使 AI 系统能够通过与物理环境的实时交互来学习和执行任务的研究范式。区别于纯语言或视觉 AI，具身智能强调「身体」对智能的重要性——智能不仅存在于模型权重中，也体现在与环境的感知-动作闭环中。在机器人领域，具身智能框架将视觉、语言与动作统一表征，实现端到端的感知-决策-执行。

## Key Points

- **核心框架**：将视觉（Vision）、语言（Language）、动作（Action）统一为 token 序列，代表性架构包括 RT-2（55B，Google DeepMind）、Octo（93M，UC Berkeley/Stanford）、OpenVLA（7B）
- **端到端学习**：从像素到关节指令的直接映射，无需显式物体检测/分割等中间模块；特斯拉 Optimus 借鉴 FSD 架构实践这一路线
- **跨具身迁移**：Octo 通过 Embodiment Embedding + Adapter Layers，一个模型适配22种机器人平台；微调仅需50-200条演示数据（<5%参数更新）
- **数据基础**：Open X-Embodiment 数据集（80万轨迹，22种机器人平台）是当前通用策略训练的核心数据源
- **开源生态**：LeRobot（Hugging Face）集成 ACT、Diffusion Policy、TDMPC 等算法，统一 API 降低使用门槛
- **技术成熟度**：端到端大模型（RT-2）推理仅3Hz，实时性不足；Octo 达10Hz，ACT 达50Hz；商业化方案仍以混合架构为主
- **当前局限**：大模型可解释性差，安全性验证困难；数据需求量大（数万-数十万轨迹）；训练成本高（A100 GPU，数天至数周）

## My Position

## Contradictions

## Sources

- [[sources/embodied-ai-os-whitepaper-2026]]
- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：概念初建，来源为人形机器人技术研究及快速原型建设报告
- 2026-04-15（2 sources）：强化——具身智能OS白皮书补充 EAIOS 四层架构（任务/技能/服务/原语层）视角，VLA→H-VLA→世界模型演进路线与现有定义一致
