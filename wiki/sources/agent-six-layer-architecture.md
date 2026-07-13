---
type: source
title: "Agent的6层架构：感知、规划、工具、记忆、执行、反馈"
date: 2026-06-28
source_url: "https://mp.weixin.qq.com/s/Ve1E7L4qOQPapiRpDQcYYw"
domain: "mp.weixin.qq.com"
author: "Knock"
tags: [agent-architecture, agent-system, planning, memory, tool-use, feedback-loop, mcp]
processed: true
raw_file: "raw/clippings/2026-06-28-Agent的6层架构：感知、规划、工具、记忆、执行、反馈.md"
raw_sha256: e3afdca810446fe1052b0e9621364de11d9dc6ffb889b2a9411da7ced0e46240
last_verified: 2026-07-13
possibly_outdated: false
language: "zh"
canonical_source: "https://mp.weixin.qq.com/s/Ve1E7L4qOQPapiRpDQcYYw"
---

# Agent的6层架构：感知、规划、工具、记忆、执行、反馈

## Summary

微信公众号 Knock 的文章，主张一个真正可用的 AI Agent 不是「大模型 + 工具调用」的简化，而是一个由 6 层架构构成的认知-行动循环闭环系统：感知（Perception）→ 规划（Planning）→ 工具（Tool）→ 记忆（Memory）→ 执行（Execution）→ 反馈（Feedback）。文章按工程视角逐层拆解每层的职责、核心技术、设计原则与踩坑，并给出最小可行 Agent 的搭建路线（感知+执行→加工具→加规划→加记忆→加反馈）和 2026 年技术栈推荐（感知 GPT-5.5/Claude Opus 4、规划 LangGraph/CrewAI、工具 MCP、记忆 ChromaDB+Redis、执行 Temporal/Celery、反馈 W&B+自定义）。

## Key Points

- Agent 6 层不是线性流水线，而是循环闭环：感知→规划→执行→反馈→感知……
- **感知层**：把原始输入转为结构化表示（意图识别、实体抽取、多模态对齐、环境状态解析）；关键设计含输入归一化管道、置信度门控（低置信度主动澄清）、增量感知。
- **规划层**：4 种范式——ReAct（思考-行动-观察循环）、Plan-then-Execute、Tree-of-Thought（搜索最优路径）、Hierarchical Planning（多 Agent 主流，高层 LLM 决策+底层专用模型执行）。
- **工具层**：工具本质是「把 LLM 语言能力转化为操作能力」；MCP（Model Context Protocol，Anthropic 2025 提出）已成为事实上的工具接入标准，解决工具接入碎片化；设计原则含最小权限、幂等性、超时与熔断。
- **记忆层**：工作记忆（受上下文窗口限制）+ 短期记忆（跨轮次）+ 长期记忆（向量数据库，理论无限）；实践含重要性评分、遗忘机制（时间衰减/冲突覆盖/主动清理）。
- **执行层**：把计划转为工具调用，管理并发与依赖、异常重试；安全机制含沙箱执行（Docker，默认禁网）与 Human-in-the-Loop 风险分级门控（read/create/modify/delete/financial/irreversible）。
- **反馈层**：3 类反馈（环境/自我/人类）；自我进化方法含 Reflexion（反思笔记）、Self-Play（自我对弈）、Trajectory Optimization（轨迹优化）；工程上用 FeedbackLoop 把反思→经验记忆→在线学习→下一步行动串起来。

## Concepts Extracted

- [[agent-architecture]]
- [[agent-memory]]
- [[tool-use-mcp]]
- [[agent-planning]]
- [[agent-feedback-loop]]
- [[human-in-the-loop]]

## Entities Extracted

- [[model-context-protocol]]
- [[langgraph]]
- [[claude-opus-4]]

## Contradictions

<!-- 暂无 -->

## My Notes

- 与知识库已有 [[sources/agent-route-comparison-2026]]（OpenClaw/Hermes/Superagent 三条路线）、[[sources/agent-harness-revolution-2026]]（Harness 革命）互补：那边讲"选哪条路线/用什么 harness"，这边讲"单 Agent 内部怎么分层"。可作为 Agent 架构概念页的核心中文来源。
- 文中模型年份/代际（GPT-5.5、Claude Opus 4、Gemini 2.5 Ultra 2M context）属 2026 年视角表述， intake 时按原文记录，不修正。
