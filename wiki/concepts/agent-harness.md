---
type: concept
title: "Agent Harness"
date: 2026-04-19
updated: 2026-07-21
tags:
  - agent
  - harness
  - llm
  - infrastructure
  - context-engineering
source_count: 8
confidence: low
domain_volatility: high
last_reviewed: 2026-07-21
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

**ECC 给出了新答案（2026-05-14 补充）**：[[entities/ecc-framework]] 以 53 专用 Agent + Hooks 安全层 + Immutability 原则的组合，实质上是对上述三个问题的工程回应：
- 上下文隔离 → 专用 Agent 独立上下文窗口，职责边界清晰
- 文档过期 → Immutability 原则，框架核心不可变，自定义通过 override 隔离
- 验收偏差 → Rules 层常驻约束 + Test-Driven 设计原则内嵌测试要求

**垂直化 Harness 的价值**：[[entities/automotive-claude-code-agents]] 将 Harness 工程能力垂直化到汽车软件领域——507+ 行业知识库 + 40+ 专业 Agent + 合规检查 Hooks，证明了"通用 Harness + 领域知识库 + 行业规则层"是可复制的垂直化模式。
- **参考实现与工程全景（yeasy《Harness》, 2026-07）**：MiniHarness 给出 Python 版 Agent Harness 参考框架；横向对比 Claude Code（Rust+Starlark execpolicy+sandbox）/ OpenClaw（TypeScript Gateway+ClawHub）/ OpenAI Codex（Rust harness）的生产级 Harness；落地要素含 MCP 集成、Bubblewrap/seccomp/Landlock 沙箱、skills/hooks/subagents/memory(compact)、OpenTelemetry 可观测、execpolicy 三态权限

## Contradictions

## Sources

- [[sources/agent-harness-revolution-2026]]
- [[sources/openclaw-ai-team-practice]]
- [[sources/hermes-vs-openclaw-comparison]]
- [[sources/openclaw-vs-hermes-deep-dive]]
- [[sources/ai-collaboration-practices]]
- [[sources/agent-route-comparison-2026]]
- [[sources/ecc-architecture-design]]（个人写作）
- [[sources/automotive-agents-reference]]（个人写作）
- [[sources/harness-engineering-guide]]

## Evolution Log

- 2026-04-19（3 sources）：概念初建，来源为 Harness革命万字综述、OpenClaw实战方案、Hermes对比实验三篇文章
- 2026-04-19（4 sources）：强化——架构师深度对比文章从系统层拆解 OpenClaw vs Hermes 定位差异，补充 Skill 语义/Memory 架构/安全思路三维度细节
- 2026-04-19 个人写作 [[sources/ai-collaboration-practices]] 确立了对此概念的明确立场
- 2026-04-25（5 sources）：强化——三条路线比较文章从竞争格局视角补充 Agent 基础设施"执行层+学习层+安全层"分层卡位逻辑，丰富 Harness 架构的安全治理维度
- 2026-05-14 个人写作 [[sources/ecc-architecture-design]] / [[sources/automotive-agents-reference]] 补充：ECC 对多 Agent 隔离/文档过期/验收偏差三大难题的工程回应；垂直化 Harness 可复制模式
- 2026-07-21（6 sources）：强化——LangChain Harness 调优 Playbook（只改 Harness 不改模型，Nemotron 3 Ultra 以 1/10 成本逼近 Opus）、黄仁勋×LangChain 对话（Harness 取代 Workflow 成为企业核心架构）、WorkBuddy Harness 工程万字复盘（Context Engineering 五类动作 + MCP/Skill/Plugin 完整体系），补充 Harness Engineering 的量化方法论和企业架构视角
- 2026-07-21（7 sources）：强化——AI Agent 四层质量评估框架（评测维度/指标/标准/方法），补充 Agent 评测体系视角
- 2026-07-21（8 sources）：强化——yeasy《Harness》技术书（MiniHarness Python 参考框架 + Claude Code/OpenClaw/OpenAI Codex 生产级 Harness 横向对比 + MCP 集成 + Bubblewrap/seccomp/Landlock 沙箱 + OpenTelemetry 可观测 + execpolicy 权限），补充 Harness 的工程实现与全景视角
