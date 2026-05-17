---
type: entity
title: "Claude Code"
date: 2026-05-14
updated: 2026-05-14
tags:
  - llm-tool
  - cli
  - anthropic
  - coding-assistant
  - ai-engineering
entity_type: tool
aliases:
  - "Claude Code"
  - "claude-code"
  - "Anthropic CLI编程助手"
  - "Claude Code CLI"
---

# Claude Code

## Description

Claude Code是Anthropic官方发布的CLI编程助手，以命令行工具形式运行，能够直接读取代码库、执行命令、调用工具，在真实项目中提供代码编写、审查、重构、测试等全流程支持。与普通聊天式AI不同，Claude Code通过agents/skills/commands/rules/hooks机制支持工程化工作流定制，可将软件工程纪律固化到工具行为中。

## Key Contributions

- 提供完整的编程助手能力：代码生成/审查/重构/测试/架构设计/安全扫描
- 支持自定义五大组件：agents（子代理）、skills（技能）、commands（斜杠命令）、rules（规则约束）、hooks（事件钩子）
- 通过MCP（Model Context Protocol）将外部服务接入工作流，实现工具链集成
- 支持插件化安装，everything-claude-code等开源项目为其提供工程化工作流扩展
- 代表了从"聊天式AI"向"具备流程纪律的工程助手"演进的方向

## Related Concepts

- [[concepts/claude-code-workflow]]
- [[concepts/model-context-protocol]]
- [[concepts/agent-harness]]

## Sources

- [[sources/everything-claude-code-workflow-library]]

## Evolution Log

- 2026-05-14（1 sources）：实体页初建，来源为 everything-claude-code 工程工作流组件库介绍文章
