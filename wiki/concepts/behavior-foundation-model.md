---
type: concept
title: "行为基础模型"
date: 2026-06-27
updated: 2026-06-27
tags:
  - embodied-ai
  - humanoid-robot
  - behavior-foundation-model
  - motion-control
source_count: 2
confidence: low
domain_volatility: high
last_reviewed: 2026-06-27
aliases:
  - "行为基础模型"
  - "运控基座"
  - "运控基座模型"
  - "Behavior Foundation Model"
  - "BFM"
---

# 行为基础模型（Behavior Foundation Model / BFM）

## Definition

行为基础模型（Behavior Foundation Model，BFM，业界又称「运控基座」「运控基座模型」）是人形机器人运动控制的基础模型范式：把机器人的「动作能力」沉淀为可被上层智能（VLA、世界模型、语言模型）复用、适配、调用的「身体接口」底座。其核心转变是把人形机器人运动控制从「针对单一任务的技能训练」推向「身体接口工程」——让身体成为通用、可调用的能力层。智元、众擎、逐际动力、地平线等厂商均在押注该路线。

## Key Points

- **核心论点**：BFM 把「动作能力」往「身体接口」层推，让机器人身体成为上层智能可复用/适配/调用的底座（见 [[embodied-ai]]、[[humanoid-robot]]）。
- **五类问题组织**：Forward-backward 表征（把任务压进可调用身体潜空间）、Goal-conditioned 学习、Intrinsic reward 预训练、Adaptation（迁移到新任务/动力学/机器人）、Hierarchical control（语言/VLA/扩散/规划器调用底层身体）。
- **代表工作**：BFM-Zero（无监督 RL 做 promptable 身体基座）；HoloMotion-1（地平线，野外视频+MoCap+自建数据混训零样本运动基座）。
- **产业映射**：智元明牌把 BFM-2 推成「运控基座模型」并预告 BFM-3；众擎 demo（多动作拼接/长时程稳定/倒地起身/抗扰恢复）落在同类身体能力；逐际推进 BFM 综述与全身运控基础模型。
- **与既有方法关系**：是强化学习运动控制（见 [[reinforcement-learning-locomotion]]）向 foundation model 化的延伸，强调大覆盖面与可迁移性。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂未发现来源间分歧 -->

## Sources

- [[sources/behavior-foundation-model-bfm-survey]]
- [[sources/embodied-ai-weekly-papers-2026-06-06]]

## Evolution Log

- 2026-06-27（2 sources）：概念初建（补全 stub 时从 BFM 综述与具身智能周报提炼）。涵盖「身体接口工程」核心论点、五类问题组织、BFM-Zero/HoloMotion-1 代表工作、智元/众擎/逐际产业映射；confidence 设为 low（2 源、快速演进）。
