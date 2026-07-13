---
type: concept
title: "智能体反馈循环"
date: 2026-07-13
updated: 2026-07-13
tags:
  - agent
  - feedback
  - self-reflection
  - reflexion
  - learning
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-07-13
aliases:
  - "智能体反馈循环"
  - "Agent Feedback Loop"
  - "agent-feedback-loop"
  - "Agent 反馈层"
  - "自我反思"
---

# 智能体反馈循环（Agent Feedback Loop）

## Definition

智能体反馈循环是 Agent 6 层架构中的第 6 层（反馈层），是 Agent 进化的关键。没有反馈 Agent 永远同一水平；有了反馈才能从每次执行中学习。反馈层把反思→经验记忆→在线学习→下一步行动串成闭环。

## Key Points

- **3 类反馈来源**：环境反馈（工具返回值，如 API 200 vs 500）、自我反馈（Agent 自身评估）、人类反馈（用户评价）
- **自我反思 SelfReflection**：结果验证 + 目标检查 + 一致性检查 + 异常检测 → 决定 retry / investigate / replan / continue
- **两类学习**：
  - 在线学习 In-Context Learning：同任务内把反馈加入工作记忆（高优先级）
  - 离线学习 Experience Replay：跨任务从历史经验聚类失败模式（频率≥3 才算模式），提取可复用规则更新行为策略
- **自我进化方法**：Reflexion（失败生成自然语言反思笔记）、Self-Play（两实例互评对抗）、Trajectory Optimization（记录完整轨迹用 RL 优化，成功增强/失败抑制）
- **FeedbackLoop 工程实现**：反思→记录经验（成功/失败）→在线学习→决定下一步（CONTINUE/RETRY/REPLAN/DEBUG/ABORT/HUMAN_ESCALATION）

## My Position

- 与 [[agent-memory|Agent 记忆]]（经验记忆是反馈的产物）、[[agent-architecture|Agent 架构]] 配合。反馈层是 Agent 从 Demo 变产品的关键一层。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/agent-six-layer-architecture]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Knock「Agent 6 层架构」文章反馈层章节
