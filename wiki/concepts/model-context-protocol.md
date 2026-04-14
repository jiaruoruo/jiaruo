---
type: concept
title: "模型上下文协议"
date: 2026-04-13
updated: 2026-04-13
tags:
  - mcp
  - protocol
  - llm
  - tooling
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-04-13
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

## My Position

## Contradictions

## Sources

- [[sources/minimax-api-overview]]

## Evolution Log

- 2026-04-13（1 sources）：概念初建，来源为 MiniMax 开放平台接口概览文档
