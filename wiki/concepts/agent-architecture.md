---
type: concept
title: "智能体系统架构"
date: 2026-07-13
updated: 2026-07-13
tags:
  - agent
  - agent-architecture
  - system-design
  - planning
  - memory
  - tool-use
  - execution
  - feedback
source_count: 2
confidence: low
domain_volatility: high
last_reviewed: 2026-07-21
aliases:
  - "智能体系统架构"
  - "Agent Architecture"
  - "agent-architecture"
  - "Agent 6层架构"
  - "Agent系统"
---

# 智能体系统架构（Agent Architecture）

## Definition

智能体系统架构指一个真正可用的 AI Agent 不是「大模型 + 工具调用」的简化，而是一个由多层构成的认知-行动系统。Knock（2026-06-28）提出经典的 6 层架构：感知（Perception）→ 规划（Planning）→ 工具（Tool）→ 记忆（Memory）→ 执行（Execution）→ 反馈（Feedback），且这 6 层不是线性流水线，而是循环闭环（感知→规划→执行→反馈→感知……）。

## Key Points

- **6 层职责**：
  - 感知层：把原始输入转为结构化表示（意图识别、实体抽取、多模态对齐、环境状态解析）；低置信度主动澄清、增量感知
  - 规划层：4 种范式——ReAct、Plan-then-Execute、Tree-of-Thought、Hierarchical Planning（多 Agent 主流）
  - 工具层：把 LLM 语言能力转为操作能力；MCP 已成事实标准；最小权限、幂等性、超时熔断
  - 记忆层：工作记忆（上下文窗口）+ 短期记忆（跨轮次）+ 长期记忆（向量库）；含重要性评分与遗忘机制
  - 执行层：计划转工具调用，并发/依赖/重试；沙箱执行 + Human-in-the-Loop 风险分级门控
  - 反馈层：环境/自我/人类三类反馈；Reflexion、Self-Play、Trajectory Optimization 等自我进化方法
- **与 [[agent-harness|Agent Harness]] 的关系**：Harness 概念从"基础设施"视角（Agent = Model + Harness，含 Agentic Loop/Tool System/Memory/Guardrails/Hooks/Session 六组件）描述外围工程层；6 层架构从"认知-行动系统"视角描述单 Agent 内部职能分层。两者互补——Harness 是"身体"，6 层是"身体内部的器官划分"。
- **最小可行 Agent 路线**：感知+执行 → 加工具 → 加规划 → 加记忆 → 加反馈（约 1 个月从 0 到闭环）

## My Position

- 与知识库已有 [[agent-harness|Agent Harness]]、[[agent-security-governance|Agent 安全治理]] 构成 Agent 主题三层：单 Agent 内部分层（本页）、多 Agent/基础设施（Harness）、生产安全（治理）。**已实现统一**：见 [[synthesis/agent-theme-synthesis]]（2026-07-13，将 6 层架构 / Harness / 安全治理归并为三层抽象栈，含 MCP 连接层）。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/agent-six-layer-architecture]]
- [[sources/workbuddy-harness-engineering-case-study]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Knock「Agent 6 层架构」微信公众号文章
- 2026-07-21（2 sources）：强化——WorkBuddy 万字复盘详细描述了 ReAct 循环、工具调用/MCP/Skill/Plugin 概念体系和 Context Engineering 五类动作，验证了 6 层架构中工具层/执行层/反馈层的实践形态
