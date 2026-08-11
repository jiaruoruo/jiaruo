---
type: source
title: everything-claude-code：一套可复用的 Claude Code 工程工作流组件库
date: 2026-05-11
source_url: http://www.uml.org.cn/ai/202602054.asp
domain: uml.org.cn
author: ''
tags:
- claude-code
- llm-engineering
- ai-workflow
- agents
- hooks
- skills
processed: true
raw_file: raw/工作/clippings/AI/2026-05-11everything-claude-code：一套可复用的 Claude Code 工程工作流组件库.md
raw_sha256: 2f45c5296ea624a33ce2c9be4b188d28b9bff9ec7c44ab03fe275628fe18535f
last_verified: 2026-06-27
possibly_outdated: false
language: zh
canonical_source: ''
---
# everything-claude-code：一套可复用的 Claude Code 工程工作流组件库

## Summary

转载自AI贺贺微信公众号的技术文章，介绍 everything-claude-code 开源项目——一个面向 Claude Code（Anthropic官方CLI编程助手）的"全家桶"配置仓库，将 agents/skills/commands/rules/hooks/MCP server 配置集中在一起，把"先计划/先测试/再实现/再验证"的工程纪律固化到工具行为中，而非依赖使用者记忆。

## Key Points

- **项目三大核心价值**：①把高频工程能力产品化；②把工程方法论固化为工具行为；③减少跨项目迁移成本
- **五大组件体系**：
  - **Agents（子代理）**：9个专职角色（planner/architect/tdd-guide/code-reviewer/security-reviewer/build-error-resolver/e2e-runner/refactor-cleaner/doc-updater），独立上下文窗口，适合隔离高输出任务
  - **Skills（技能）**：9类方法论流程（coding-standards/backend-patterns/frontend-patterns/tdd-workflow/security-review/strategic-compact/continuous-learning/verification-loop/eval-harness），支持手动触发（/skill-name）或模型自动触发
  - **Commands（斜杠命令）**：10个预设工作流（/tdd /plan /e2e /code-review /build-fix /refactor-clean /verify /checkpoint /learn /setup-pm）
  - **Rules（规则约束）**：6类常驻约束（security/coding-style/testing/git-workflow/agents/performance）
  - **Hooks（事件钩子）**：10个会话生命周期事件点（SessionStart/UserPromptSubmit/PreToolUse/PermissionRequest/PostToolUse/SubagentStart/SubagentStop/Stop/PreCompact/SessionEnd/Notification）
- **Skills vs Subagents关键区别**：
  - Skills：可复用流程/提示词模板（带参数），既可手动触发也可模型自动调用
  - Subagents：独立上下文窗口+自己的系统提示词，适合隔离"跑测试/分析大量diff"等重型任务
- **Hooks使用注意**：能执行任意命令，存在安全风险，须严格审计；PreToolUse可实现允许/拦截/要求确认三种权限决策
- **安装方式**：作为Claude Code插件安装（/plugin install命令）或手动拷贝agents/rules/commands/skills目录
- **MCP集成**：提供mcp-servers.json配置模板，通过Model Context Protocol将外部服务接入Claude Code工作流

## Concepts Extracted

- [[concepts/claude-code-workflow]]

## Entities Extracted

- [[entities/claude-code]]

## Contradictions

## My Notes
