---
type: entity
entity_type: tool
title: "Everything Claude Code (ECC)"
aliases:
  - ECC
  - Everything Claude Code
date: 2026-05-14
updated: 2026-05-14
tags:
  - ai-agent-framework
  - claude-code
  - agent-orchestration
  - open-source
---

# Everything Claude Code (ECC)

## Overview

**ECC（Everything Claude Code）** 是一个 AI 代理编排框架的"操作系统增强层"，专为 Claude Code 及其他主流 AI 编程工具设计。起源于 Anthropic 黑客马拉松获奖项目，经 10+ 个月生产环境验证。

| 属性 | 值 |
|------|-----|
| 版本 | v2.0.0-rc.1 |
| 类型 | AI Agent 编排框架 |
| 支持框架 | Claude Code / Codex / Cursor / OpenCode / Gemini |
| 规模 | 53 专用 Agent / 200+ Skills / 69 Commands |
| MCP 配置 | 14 套 |
| 国际化 | 7 种语言 |
| 状态 | 生产就绪（Release Candidate） |

## 核心能力

- **53 个专用子代理**：每个 Agent 对应一个专业任务领域（planner / architect / code-architect / reviewer / tester 等）
- **200+ 工作流技能（Skills）**：可跨 Agent 共享的可复用知识单元
- **69 命令（Commands）**：slash commands，触发复杂多步骤工作流
- **Hooks 层**：拦截 Claude Code 生命周期事件（pre-tool / post-tool / pre-session），实现安全检查和自动化
- **Tool Adapter 层**：屏蔽底层 AI 工具差异，实现跨框架兼容
- **14 套 MCP 服务器配置**：按用途模块化加载（开发工具 / 数据库 / 服务集成 / 浏览器自动化）

## 设计原则

1. **Agent-First**：专业任务 → 专属 Agent，避免通用 Agent 稀释专注度
2. **Skills-First**：知识单元独立于 Agent，可复用
3. **Immutability**：框架核心不可变，用户通过 override 扩展
4. **Test-Driven**：每个 Agent / Skill 均有测试用例
5. **Security-First**：权限最小化，Hooks 拦截危险操作

## 相关来源

- [[sources/ecc-architecture-design]]（架构设计说明书 + 架构图）
- [[sources/ecc-detailed-design]]（详细设计说明书）
- [[sources/ecc-tutorial-and-extension]]（应用教程 + 扩展指南）

## 相关概念

- [[concepts/claude-code-workflow]]
- [[concepts/agent-harness]]
- [[concepts/model-context-protocol]]

## 相关实体

- [[entities/claude-code]]（ECC 的主要宿主框架）
- [[entities/automotive-claude-code-agents]]（ECC 的垂直领域衍生项目）

## Evolution Log

- 2026-05-14 个人写作 [[sources/ecc-architecture-design]] 建立实体页，确认 ECC 为作者核心 AI 工程化工具
