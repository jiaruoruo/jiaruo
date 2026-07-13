---
type: concept
title: "智能体规划"
date: 2026-07-13
updated: 2026-07-13
tags:
  - agent
  - planning
  - react
  - tree-of-thought
  - hierarchical-planning
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-07-13
aliases:
  - "智能体规划"
  - "Agent Planning"
  - "agent-planning"
  - "Agent 规划层"
  - "任务规划"
---

# 智能体规划（Agent Planning）

## Definition

智能体规划是 Agent 6 层架构中的第 2 层（规划层），是 Agent 的「指挥中心」，职责是把复杂目标拆解为可执行的步骤序列。类比人脑前额叶皮层。

## Key Points

- **4 种规划范式**：
  - ReAct（Reasoning + Acting）：每步「思考→行动→观察」循环，简单可解释但每步重推理效率低
  - Plan-then-Execute：先生成完整计划再执行，全局视野效率高，但计划可能因环境变化失效
  - Tree-of-Thought：探索多条路径选最优（成本/风险打分）
  - Hierarchical Planning：任务分粒度层级，高层 LLM 决策 + 底层专用/小模型执行——2026 多 Agent 系统主流架构
- **核心组件 Plan Manager**：create_plan / replan（失败时重规划）/ adaptive_step（按当前状态动态调步）
- **关键指标**：规划成功率 >80%、重规划次数 <2、步骤效率 <1.5x、上下文利用 >90%
- **常见踩坑**：规划幻觉（生成不存在 API）、过度规划、规划僵化、上下文窗口溢出

## My Position

- 与 [[agent-architecture|Agent 架构]]、[[agent-harness|Agent Harness]]（其 Agentic Loop 即 ReAct 式循环）关联。Hierarchical Planning 是多 Agent 系统的理论基础之一。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/agent-six-layer-architecture]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Knock「Agent 6 层架构」文章规划层章节
