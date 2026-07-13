---
type: concept
title: "视觉-语言-动作模型"
date: 2026-07-13
updated: 2026-07-13
tags:
  - vla
  - embodied-ai
  - robotics
  - foundation-model
source_count: 1
confidence: low
domain_volatility: high
last_reviewed: 2026-07-13
aliases:
  - "视觉-语言-动作模型"
  - "Vision-Language-Action Model"
  - "vision-language-action-model"
  - "VLA"
  - "VLA 模型"
---

# 视觉-语言-动作模型（Vision-Language-Action Model, VLA）

## Definition

视觉-语言-动作模型（VLA）将视觉观察、自然语言任务指令和本体感觉状态联合编码，输出连续电机控制信号，是具身 AI 的核心范式。路线图（Christensen 2026）将其列为 Layer1 算法与 AI 的基石，并判断机器人 Scaling Law 已获实证确认。

## Key Points

- **代表性系统**：Open X-Embodiment (RT-X)（ICRA 2024 最佳论文，20+ 机构数据，跨本体零样本泛化）、π0（Physical Intelligence，流匹配 VLA，验证机器人策略 Scaling Law）、OpenVLA（开源 70 亿参数）、Octo（RSS 2024，多模态输入+扩散动作输出）、RDT-1B（10 亿参数扩散模型，双手操作）、GEN-0（70 亿参数处出现能力相变，提"Harmonic Reasoning"解决物理延迟-动作同步）
- **开放问题**：长程任务推理是否需要世界模型而非直接动作模型
- **路线图里程碑**：VLA 基础模型 2025 TRL6 → 2028 TRL8 → 2035 TRL9；2027 可靠单臂→2030 双手→2033 家庭通用
- **与 [[embodied-ai|具身智能]] 关系**：VLA 是具身智能的模型实现范式，将视觉/语言/动作统一表征

## My Position

- 与 [[embodied-ai]]、[[robotics-roadmap-2025-2035]] 配合。VLA 是当前机器人基础模型竞赛（美领先）的核心战场。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/global-robotics-roadmap-2025-2035]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Christensen 全球机器人路线图 VLA 章节及代表性系统梳理
