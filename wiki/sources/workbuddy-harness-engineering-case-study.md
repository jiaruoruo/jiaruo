---
type: source
title: "万字复盘：从模型到可用Agent，WorkBuddy的Harness工程是怎么做的？"
date: 2026-07-16
source_url: "https://mp.weixin.qq.com/s/GkhemHUAhKWV-3Uxaa1Mqg"
domain: agent
author: Anne（WorkBuddy 腾讯）
tags:
  - agent
  - harness
  - context-engineering
  - mcp
  - skill
  - plugin
  - evaluation
processed: false
raw_file: raw/工作/clippings/AI/2026-07-16-万字复盘：从模型到可用Agent，WorkBuddy的Harness工程是怎么做的？.md
raw_sha256: caa6735e2f9b0be6ef4072d34269979e5df428829cbd3d792bda3516f9b58c7e
last_verified: 2026-07-21
possibly_outdated: false
language: zh
canonical_source: ""
---

# 万字复盘：从模型到可用Agent，WorkBuddy的Harness工程是怎么做的？

## Summary

腾讯 WorkBuddy 团队从产品视角全面拆解 Agent 运行机制和 Harness 工程实践。从模型基础（预训练/后训练/RLHF）→ 工具调用（Function Call）→ MCP/Skill/Plugin 概念体系 → Context Engineering → Harness Engineering（前馈/反馈/权限/验证/编排/可观测性）→ Loop Engineering，提供了一份完整的 Agent 产品化路线图。

## Key Points

- **模型抽象**：模型是无状态的函数，输出 = 模型(系统提示词 + 工具 + 会话历史 + 上下文 + 用户指令)；产品需要在模型外维护状态、接入工具和执行环境
- **四大概念体系**：
  - **工具调用（Function Call）**：模型请求执行动作的基础协议
  - **MCP（Model Context Protocol）**：外部系统标准化接入协议（Resources/Tools/Prompts 三原语；MCP Apps 扩展支持交互式 UI）
  - **Skill**：一类任务的标准执行流程（步骤+脚本+验收标准）
  - **Plugin**：一组能力（MCP+Skill+Rules+Hooks）的可安装分发单位
- **外接能力形态选择**：稳定底层操作→内置 Tool；外部系统→Skill/MCP/Plugin；团队高频流程→Skill；组合能力→Plugin
- **ReAct 循环**：推理→行动→观察的多轮循环，是 Agent 执行任务的基础模式
- **Context Engineering 五类动作**：写入（Write）、选择（Select）、检索（Retrieve）、压缩（Compress）、隔离（Isolate）
- **Prompt Cache**：利用前缀复用降低多轮对话的计算成本
- **Harness Engineering**：前馈（行动前指导）/反馈（执行后验证）/权限控制（Approval Gate）/结果验证/任务编排（Sub-agent）/可观测性（trace）
- **Karpathy 观点**：Agent 是新的数字信息消费者，软件设计需考虑"Agent 怎么理解、怎么操作、怎么验证"

## Concepts Extracted

- [[agent-harness]]
- [[model-context-protocol]]
- [[tool-use-mcp]]
- [[agent-architecture]]
- [[agent-planning]]
- [[agent-memory]]

## Entities Extracted

- [[openclaw]]
- [[langgraph]]

## Contradictions

<!-- 无 -->

## My Notes

<!-- 本文是目前知识库中关于 Agent 产品化最完整的工程实践文档。与 LangChain Harness 调优文互补：本文讲"建什么"（Harness 架构设计），LangChain 文讲"怎么调"（Harness 调优方法论）。 -->
