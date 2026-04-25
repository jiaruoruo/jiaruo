---
type: concept
title: "Agent Harness"
date: 2026-04-19
updated: 2026-04-25
tags:
  - agent
  - harness
  - llm
  - infrastructure
  - context-engineering
source_count: 5
confidence: low
domain_volatility: high
last_reviewed: 2026-04-25
aliases:
  - "Agent Harness"
  - "agent-harness"
  - "Harness"
  - "Agent基础设施"
  - "Agent运行时"
---

# Agent Harness（Agent 基础设施）

## Definition

Agent Harness 是包裹模型运行的外围基础设施，定义式公式为：**Agent = Model + Harness**。Harness 将无状态的纯推理大模型"大脑"转化为能够持续执行任务的 Agent"身体"，负责上下文管理、工具调用、权限控制、状态持久化、记忆系统等所有非模型本身的工程层。2026 年模型智力进入高原期后，Harness 成为 Agent 系统竞争力的核心战场。

## Key Points

- **时代背景**：2026 年各家模型智力已超越普通人类水平，竞争焦点从"拼模型"转向"拼 Harness"；DeepMind 实验验证——固定同一模型只换 Harness，性能可产生巨大差异
- **历史必然性**：30 年软件工程复杂性中心演进：GOF 设计模式（驾驭对象，1994）→ 企业架构（驾驭业务，2002）→ 微服务（驾驭分布式，2010）→ DDIA（驾驭数据，2017）→ **Harness（驾驭智能体，2026）**；不变核心是"抽象"
- **六大核心组件**：①**Agentic Loop**（心脏，ReAct 式推理→行动→观察循环）；②**Tool System**（工具调用，扩展 LLM 行动范围）；③**Memory & Context**（记忆与上下文压缩管理）；④**Guardrails**（权限控制，Allow/Deny/Ask）；⑤**Hooks**（守卫，防止敏感信息泄露等）；⑥**Session**（会话连续性与状态管理）
- **解决五大落地难题**：无限循环、上下文爆炸、权限失控、质量不可控、成本不透明
- **生态格局**：纵深型（Claude Code #1，深度工程开发）vs 横向型（[[openclaw]] / [[hermes-agent]]，自动化运营）；两类不冲突可配合
- **多 Agent Harness 模式（SOUL.md + 文件系统协作）**：每个 Agent 用 40-60 行 SOUL.md 定义身份/原则/决策框架；Agent 间通过文件系统交接（"一写多读"），无需 API 调用或消息队列；双层记忆（每日日志 + 提炼长期记忆）实现 Agent 随时间增强
- **自主进化 Harness（Hermes 模式）**：复杂任务完成后 Agent 自评估，自动写入 `skills/` 技能文件；agentskills.io 标准使技能文件跨平台移植
- **工程师能力转型**：码农（写代码）→ 工程师（设计并驾驭复杂系统）；Harness 设计能力是 Agent 时代的核心工程竞争力

## My Position

> 个人认知，来源：[[sources/ai-collaboration-practices]]（刘万龙，2026-04-19）

两周 644 个 commit 的实践验证了 Harness 框架的核心命题。我的体感是：**Harness 设计的本质是给 AI 搭舞台**——不是让它更聪明，而是让它在一个清晰的环境里可预测地工作。

**三条最有效的实践**：

1. **Feature Spec 是 Harness 的核心构件**：需求不从对话里传，从文档里传。每个功能对应一个独立 `.md` 文件，是 AI 编码时唯一的需求来源。「正确」的定义是「所有验收标准都打了勾」，而不是「功能上说得过去」。

2. **禁止清单与允许清单同等重要**：AI 会做它被允许做的事，也会做它没有被明确禁止的事。开发任务禁止自己写测试，测试任务禁止修改业务逻辑——职责边界要写死，不能靠 AI 自己判断。

3. **冷启动协议解决持久记忆问题**：AI 没有持久记忆，每次新会话对项目一无所知。解法是把记忆外化成文档（AI-GUIDE.md + CONTEXT.md，合计 ≤ 200 行），每次会话强制读取。这和本知识库的 CLAUDE.md 设计哲学完全一致。

**一句话**：「从 AI 的视角来看，任何在上下文中无法被访问的信息，就等于不存在。」——这是 Harness 设计的底层公理。

**未解决的问题**：多 AI 并行时的上下文隔离（各 Agent 不知道对方在改什么）、文档过期无银弹、「AI 自测自」导致的验收偏差——这些是 Harness 工程的下一个战场。

## Contradictions

## Sources

- [[sources/agent-harness-revolution-2026]]
- [[sources/openclaw-ai-team-practice]]
- [[sources/hermes-vs-openclaw-comparison]]
- [[sources/openclaw-vs-hermes-deep-dive]]
- [[sources/ai-collaboration-practices]]
- [[sources/agent-route-comparison-2026]]

## Evolution Log

- 2026-04-19（3 sources）：概念初建，来源为 Harness革命万字综述、OpenClaw实战方案、Hermes对比实验三篇文章
- 2026-04-19（4 sources）：强化——架构师深度对比文章从系统层拆解 OpenClaw vs Hermes 定位差异，补充 Skill 语义/Memory 架构/安全思路三维度细节
- 2026-04-19 个人写作 [[sources/ai-collaboration-practices]] 确立了对此概念的明确立场
- 2026-04-25（5 sources）：强化——三条路线比较文章从竞争格局视角补充 Agent 基础设施"执行层+学习层+安全层"分层卡位逻辑，丰富 Harness 架构的安全治理维度
