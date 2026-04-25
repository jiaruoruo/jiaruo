---
type: source
title: "最新！万字综述Harness革命！"
date: 2026-04-18
source_url: "https://mp.weixin.qq.com/s/0CTwb4aEr5mWwsdRdwzwkw"
domain: "ai-agent"
author: "黄佳"
tags:
  - agent
  - harness
  - context-engineering
  - llm
processed: true
raw_file: "raw/clippings/2026-04-18最新！万字综述Harness革命！.md"
raw_sha256: "720e5c32e45f647ca3e4ed5ec141f9109aead890c02b5a62565f0e1e479c6e9f"
last_verified: 2026-04-19
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 最新！万字综述Harness革命！

## Summary

新加坡科研机构 AI 研究员黄佳在 Datawhale 的分享，以 30 年软件工程演进为视角，系统阐述了 Agent Harness 的历史必然性与核心架构。核心观点：2026 年模型智力已达足够高度，竞争焦点转移至 Harness——即驾驭 Agent 的基础设施层。Agent = Model + Harness，Harness 是让模型大脑进化为 Agent 身体的关键工程。

## Key Points

- **时代判断**：2026 年模型智力已超越普通人类，竞争从"拼模型"转向"拼 Harness"；DeepMind 实验证明同一模型换 Harness 可产生巨大性能差异
- **30年演进主线**：1994 GOF 设计模式（驾驭对象）→ 2002 企业架构（驾驭业务）→ 2010 微服务（驾驭分布式）→ 2017 DDIA（驾驭数据）→ **2026 Harness（驾驭智能体）**；不变的核心是**抽象**和**驾驭复杂性**
- **Agent 核心困境**：Agent 是概率机器，全自动生成代码会导致系统失控；Harness 解决的就是"可控"问题
- **Harness 定义**：Agent = Model + Harness；Harness 是模型外围的运行时与基础设施（上下文管理、权限控制、状态持久化）
- **六大核心组件**：①Agentic Loop（心脏，ReAct 式推理行动循环）；②Tool System（工具调用）；③Memory & Context（记忆与上下文管理）；④Guardrails（权限 Allow/Deny/Ask）；⑤Hooks（守卫，如防止 .env 泄露）；⑥Session（会话连续性）
- **解决五大落地难题**：无限循环、上下文爆炸、权限失控、质量不可控、成本不透明
- **生态格局**：Claude Code（纵深型，#1）> Codex（代码审查力强）> OpenClaw/Hermes（横向扩展型，适合自动化运营）；纵深型与横向型不冲突可配合使用
- **工程师转型**：码农（写代码）→ 工程师（设计并驾驭复杂系统）；护城河是对业务和 IT 系统的深度理解，而非代码能力

## Concepts Extracted

- [[agent-harness]]

## Entities Extracted

- [[openclaw]]

## Contradictions

## My Notes
