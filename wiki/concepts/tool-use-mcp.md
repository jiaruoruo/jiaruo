---
type: concept
title: "智能体工具调用"
date: 2026-07-13
updated: 2026-07-13
tags:
  - agent
  - tool-use
  - mcp
  - function-calling
source_count: 2
confidence: low
domain_volatility: high
last_reviewed: 2026-07-21
aliases:
  - "智能体工具调用"
  - "Agent Tool Use"
  - "tool-use-mcp"
  - "Agent 工具层"
  - "工具调用"
---

# 智能体工具调用（Agent Tool Use）

## Definition

智能体工具调用是 Agent 6 层架构中的第 3 层（工具层），是 Agent 与外部世界交互的接口。工具的本质是「把 LLM 的语言能力转化为操作能力」——没有工具 LLM 只能说话，有了工具才能做事。

## Key Points

- **工具分类**：数据获取（搜索/API/DB/文件）、操作执行（代码/浏览器/文件/系统）、生成（文本/图像/可视化）、通信（消息/通知/协作）
- **工具注册与发现**：现代框架中工具热插拔，ToolRegistry 支持语义搜索返回相关工具（embedding + 余弦相似度，取 top-5）
- **MCP 成为标准**：Anthropic 2025 年底提出的 [[model-context-protocol|MCP（Model Context Protocol）]] 已成事实工具接入标准，解决 LangChain @tool / AutoGPT JSON Schema 各自为政的碎片化；核心价值含工具发现、类型安全（JSON Schema）、上下文管理、权限控制
- **设计原则**：最小权限（只给完成任务所需最小权限）、幂等性（重试无副作用）、超时与熔断（每个调用有 timeout + circuit breaker）
- **2026 技术栈**：工具层推荐 MCP Protocol 标准化接入

## My Position

- 本概念侧重"工具层工程实现"（注册/发现/安全），与 [[model-context-protocol|MCP]]（协议标准本身）、[[agent-harness|Agent Harness]] 的 Tool System 组件三者互补。MCP 是标准，工具层是架构位置，Harness 是承载容器。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/agent-six-layer-architecture]]
- [[sources/workbuddy-harness-engineering-case-study]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Knock「Agent 6 层架构」文章工具层章节
- 2026-07-21（2 sources）：强化——WorkBuddy 万字复盘从产品视角详述工具调用/Function Call 流程、外接能力形态选择矩阵（内置 Tool vs Skill/MCP/Plugin），以及 Tool/Skill/MCP/Plugin 四层概念体系
