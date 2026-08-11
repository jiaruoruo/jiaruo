---
type: source
title: "Harness（Harness Engineering 指南 / MiniHarness 框架手册）"
date: 2026-07-11
source_url: ""
domain: agent
author: yeasy
tags:
  - agent
  - harness
  - context-engineering
  - mcp
processed: false
raw_file: raw/工作/pdfs/AI/harness_engineering_guide.pdf
raw_sha256: 7e4b69ecedf29af7778af2bb85044d5466fec70fdd6bbeac02a14f380ca7f5eb
last_verified: 2026-07-21
possibly_outdated: false
language: en
canonical_source: ""
---

# Harness（Harness Engineering 指南 / MiniHarness 框架手册）

## Summary

yeasy 所著《Harness》（v1.0.0，2026-07-11）是一部系统讲解 **Harness Engineering（驾驭工程）** 的英文技术书，并提出 **MiniHarness**——一个 Python 实现的 Agent Harness 参考框架。全书以「Agent = Model + Harness」为主线，横向拆解 Claude Code、OpenClaw、OpenAI Codex 等生产级 Harness 的设计，并给出 MiniHarness 的可运行实现。

核心覆盖：Harness 的分层组件（引导/约束/编排/反馈）、MCP 集成（HarnessMCP / MiniHarnessMCP）、沙箱隔离（Linux Bubblewrap/seccomp/Landlock、macOS sandbox-exec、WSL2）、skills / hooks / subagents / memory(compact) 机制、基于 OpenTelemetry 的可观测性，以及 execpolicy 权限模型（allow / prompt / forbidden）。

> ⚠ 文本层质量提示：本 PDF 由 mdPress 生成，文本层字形错乱、正文不可靠抽取。上述 Summary 依据目录结构（约 14 章 + 附录 A/B/C，第 9 章专讲 MCP）与可恢复片段归纳，非逐句精读。若后续获得清晰文本源，建议重新抽取以补全细节。

## Key Points

- **定义式**：Harness = Model + Harness；模型负责推理，Harness 负责把推理组织成可验收、可约束、可观测的工作
- **MiniHarness**：Python 编写的 Agent Harness 参考实现，强调 MCP 原生集成与可组合性
- **生产级 Harness 横向对比**：Claude Code（Rust + Starlark execpolicy + skills/core-skills + MCP + /compact/hooks）、OpenClaw（TypeScript Gateway + Heartbeat/cron + ClawHub skills/plugins + MEMORY.md）、OpenAI Codex（Rust harness + sandbox）
- **沙箱隔离**：Linux Bubblewrap + seccomp / Landlock；macOS sandboxexec；Windows elevated/unelevated sandbox；WSL2 Linux sandbox
- **MCP 接入**：HarnessMCP / MiniHarnessMCP，stdio 与 Streamable HTTP 两种传输
- **权限模型**：execpolicy 三态（allow / prompt / forbidden），Run/Edit 分级
- **可观测性**：OpenTelemetry（otel）埋点，反馈回路可追踪
- **记忆与状态**：memory/compact、MEMORY.md + memory/YYYY-MM-DD.md 的日记式长期记忆模式

## Concepts Extracted

- [[agent-harness]]
- [[model-context-protocol]]
- [[agent-memory]]
- [[agent-architecture]]
- [[tool-use-mcp]]

## Entities Extracted

- [[openclaw]]
- [[claude-code]]

## Contradictions

<!-- 单一来源，暂无与其他来源的分歧 -->

## My Notes

- 与近期摄入的 4 篇 Harness 主题 clippings（LangChain Nemotron 调优、黄仁勋×LangChain 对话、WorkBuddy 万字复盘、AI Agent 四层评测框架）形成「观点 + 实现」互补：后者讲 why/what，本书给 how（可运行框架与对比）。
- 文本层损坏，属 mdPress 渲染通病；建议标记为「待重新抽取」候选，不影响概念挂接。
