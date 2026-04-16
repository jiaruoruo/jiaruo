---
type: concept
title: "强化学习运动控制"
date: 2026-04-15
updated: 2026-04-15
tags:
  - reinforcement-learning
  - locomotion
  - robotics
  - ppo
source_count: 1
confidence: low
domain_volatility: high
last_reviewed: 2026-04-15
aliases:
  - "强化学习运动控制"
  - "RL Locomotion"
  - "reinforcement-learning-locomotion"
  - "强化学习步态控制"
---

# 强化学习运动控制（RL Locomotion）

## Definition

强化学习运动控制是指利用深度强化学习算法（主要为 PPO/SAC）训练机器人运动策略，使其能够在复杂地形下稳定行走、跑步、跳跃的技术范式。相比传统模型预测控制（MPC）和全身控制（WBC），强化学习无需精确的机器人动力学模型，通过大量仿真交互自动发现鲁棒策略，并通过 Sim-to-Real 技术迁移至真实机器人。

## Key Points

- **主流算法**：PPO（Proximal Policy Optimization）因稳定性高、样本效率好成为首选；宇树 H1、ANYmal 等均采用 PPO；SAC 适合连续动作空间
- **大规模并行仿真**：NVIDIA Isaac Gym 在单张 A100 GPU 上并行16,000+环境，训练时间从数周缩短至数小时（约4-24小时/任务）
- **域随机化**：随机化摩擦系数（0.3-1.2）、质量（±20%）、时延（0-50ms）等参数，提升策略对真实世界不确定性的鲁棒性
- **Privileged Learning**：仿真中使用额外特权信息（地形高度图、接触状态），真机部署时移除，通过蒸馏保留策略能力
- **Sim-to-Real 成功率**：宇树 H1 等案例验证成功率>90%，无需真机微调即可稳定行走
- **控制频率**：策略推理50-100Hz，底层力控1kHz；级联控制：位置外环100Hz → 速度中环1kHz → 电流内环10kHz
- **对比传统方法**：MPC（100-500Hz，可处理约束但计算量大）、WBC（1kHz，多任务优先级但需精确模型）；RL 适应性最强但训练成本高

## My Position

## Contradictions

## Sources

- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：概念初建，来源为人形机器人技术研究及快速原型建设报告
