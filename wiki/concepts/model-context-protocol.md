---
type: concept
title: "模型上下文协议"
date: 2026-04-13
updated: 2026-07-14
tags:
  - mcp
  - protocol
  - llm
  - tooling
source_count: 4
confidence: medium
domain_volatility: medium
last_reviewed: 2026-07-21
aliases:
  - "模型上下文协议"
  - "Model Context Protocol"
  - "model-context-protocol"
  - "MCP"
  - "MCP Server"
---

# 模型上下文协议（Model Context Protocol）

## Definition

模型上下文协议（Model Context Protocol，MCP）是一种开放协议标准，定义了 AI 模型与外部工具/服务之间的标准化通信接口。通过 MCP Server，第三方服务可以将自身能力（如文件操作、API 调用、数据库查询等）以统一格式暴露给 LLM，使模型能够在对话中直接调用这些能力，无需针对每个模型单独适配。

## Key Points

- **设计目标**：标准化 LLM 与外部工具的集成方式，减少重复适配工作
- **MCP Server**：实现 MCP 协议的服务端程序，可将任意能力包装为 LLM 可调用的工具；支持 Python、JavaScript 等多语言实现
- **传输方式**：通常支持 stdio（本地进程间通信）和 HTTP/SSE（远程服务）两种传输模式
- **生态现状**：Anthropic 主导制定，Claude 原生支持；MiniMax 等第三方平台已提供官方 MCP Server 实现，将语音合成、视频生成等能力暴露给 LLM
- **使用场景**：让 AI Agent 在对话中直接调用语音合成、图像生成、数据查询等外部 API，无需人工粘贴结果
- **在 Agent 架构中的位置**（Knock 2026-06-28 补充）：MCP 是 [[tool-use-mcp|Agent 工具层]] 的事实标准，解决 LangChain @tool / AutoGPT JSON Schema 各自为政的碎片化；核心价值含工具发现、类型安全（JSON Schema）、上下文管理、权限控制；传输支持 stdio / HTTP SSE / WebSocket

## My Position

## Contradictions

## Sources

- [[sources/minimax-api-overview]]
- [[sources/agent-six-layer-architecture]]
- [[sources/llm-benchmark-comparison-2026-04]]
- [[sources/workbuddy-harness-engineering-case-study]]

## Evolution Log

- 2026-04-13（1 sources）：概念初建，来源为 MiniMax 开放平台接口概览文档
- 2026-07-13（2 sources）：强化——Knock「Agent 6 层架构」文章明确 MCP 在工具层的标准地位与四项核心价值，补充 stdio/HTTP SSE/WebSocket 传输方式

- 2026-07-14（3 sources）：强化——[顶级大模型 Benchmark 全面对比解析（2026 年 4 月）] 与现有定义一致
- 2026-07-21（4 sources）：强化——WorkBuddy 万字复盘从产品视角详述 MCP 三原语（Resources/Tools/Prompts）、按用户意图组织工具的设计原则、MCP Apps 交互 UI 扩展，以及 MCP/Skill/Plugin 四层概念体系