---
type: concept
title: "Sim-to-Real 迁移"
date: 2026-04-15
updated: 2026-04-15
tags:
  - sim-to-real
  - reinforcement-learning
  - robotics
  - domain-randomization
source_count: 2
confidence: low
domain_volatility: high
last_reviewed: 2026-04-15
aliases:
  - "Sim-to-Real 迁移"
  - "Sim-to-Real Transfer"
  - "sim-to-real-transfer"
  - "仿真到真实迁移"
  - "仿真迁移"
---

# Sim-to-Real 迁移（Sim-to-Real Transfer）

## Definition

Sim-to-Real 迁移是指将在仿真环境中训练的机器人策略（神经网络）直接部署到真实机器人上，无需或仅需少量真机数据微调的技术方法。核心挑战是「仿真-真实差距」（Reality Gap）——仿真中的物理参数（摩擦、惯性、延迟等）与真实世界存在偏差，导致策略在真机上失效。

## Key Points

- **主要技术手段**：
  - **域随机化（Domain Randomization）**：仿真训练时随机化物理参数（摩擦系数0.3-1.2、质量±20%、时延0-50ms），迫使策略学习对参数变化鲁棒的行为
  - **特权学习（Privileged Learning）**：仿真中提供额外信息（地形高度图、接触状态）辅助训练，真机部署时移除；通过师生蒸馏保留能力
  - **系统辨识（System Identification）**：测量真实机器人物理参数，调整仿真模型以缩小差距
  - **自适应策略**：引入在线估计模块，推断真实环境参数并调整策略
- **成功案例**：宇树 H1（PPO + Isaac Gym，直接部署成功率>90%）、ANYmal（复杂地形行走）、OpenAI Dactyl（灵巧手魔方）
- **关键仿真工具**：Isaac Gym（16,000+并行环境，GPU加速，10,000-20,000x 提速）；MuJoCo（高精度接触建模，适合操作任务）
- **仍存在的差距**：高精度接触力（抓取细小物体）、材料形变（柔性物体）、传感器噪声模型的仿真精度仍有局限
- **部署流程**：Isaac Gym训练 → ONNX导出 → 真机加载策略 → 参数微调（可选）

## My Position

## Contradictions

## Sources

- [[sources/openclaw-simulation-rl-agent]]
- [[sources/humanoid-robot-research-rapid-prototyping]]

## Evolution Log

- 2026-04-15（1 sources）：概念初建，来源为人形机器人技术研究及快速原型建设报告
- 2026-04-15（2 sources）：强化——OpenClaw 文章补充 Sim-to-Real 的工程本质：接口一致性（action/obs schema）+ 行为可回放（case_id），而非仅靠域随机化
