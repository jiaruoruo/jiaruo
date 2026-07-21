---
type: concept
title: "智能体记忆系统"
date: 2026-07-13
updated: 2026-07-13
tags:
  - agent
  - memory
  - vector-db
  - context-management
  - long-term-memory
source_count: 3
confidence: low
domain_volatility: medium
last_reviewed: 2026-07-21
aliases:
  - "智能体记忆系统"
  - "Agent Memory"
  - "agent-memory"
  - "Agent 记忆层"
  - "AI 记忆"
---

# 智能体记忆系统（Agent Memory）

## Definition

智能体记忆系统是 Agent 6 层架构中的第 4 层（记忆层），让 Agent 能够记住当前任务上下文（短期）、回忆过去经验与知识（长期）、并从成败中学习（经验记忆）。没有记忆的 Agent 像每次从零开始的实习生。

## Key Points

- **三层记忆架构**：
  - 工作记忆（Working Memory）：当前任务上下文 + 近期对话 + 中间结果，受上下文窗口限制，生命周期单次任务
  - 短期记忆（Short-term）：近期交互历史 + 会话级知识，跨轮次不跨会话
  - 长期记忆（Long-term）：用户偏好 + 世界知识 + 经验教训，向量数据库理论无限，永久
- **工作记忆管理**：滑动窗口 + 摘要压缩（保留系统提示与最近 N 轮，旧对话压缩为摘要）
- **长期记忆实现**：向量检索（ChromaDB/Pinecone/Milvus）+ 知识图谱；含重要性评分（用户提及 0.4 / 任务相关 0.3 / 新颖性 0.2 / 时效性 0.1）
- **经验记忆**：记录成功/失败案例，检索时优先返回失败案例（从错误学习更有价值）
- **遗忘机制**：时间衰减（6 个月前对话权重减半）、冲突覆盖（用户改地址则更新）、主动清理（用户可要求遗忘）

## My Position

- 与 [[model-context-protocol|MCP]]、[[agent-architecture|Agent 架构]] 配合理解：记忆层是 Agent 状态持久化的核心，[[agent-harness|Agent Harness]] 概念中 "Memory & Context" 组件即对应此层。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/agent-six-layer-architecture]]
- [[sources/workbuddy-harness-engineering-case-study]]
- [[sources/harness-engineering-guide]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Knock「Agent 6 层架构」文章记忆层章节
- 2026-07-21（2 sources）：强化——WorkBuddy 万字复盘从产品视角描述了记忆在产品侧的实现（对话连续性、Memory 和用户偏好由产品侧维护状态再注入），以及 Memory 在完整任务流中的角色（读取用户偏好、表达方式、文章结构等）
- 2026-07-21（3 sources）：强化——yeasy《Harness》归纳 memory/compact 与 MEMORY.md + memory/YYYY-MM-DD.md 日记式长期记忆模式，为"记忆由产品侧维护再注入"提供框架级参照
