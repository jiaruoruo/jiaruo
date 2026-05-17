---
type: source
title: "ECC 详细设计说明书（Everything Claude Code v2.0.0-rc.1）"
date: 2026-05-12
source_url: ""
domain: personal
author: "刘万龙"
tags:
  - personal-writing
  - ecc
  - agent-orchestration
  - claude-code
  - ai-agent-framework
processed: true
raw_file: "raw/personal/ECC-详细设计说明书.md"
raw_sha256: "458d134f0a5844ff54a6a580e4fe8b466c2692eb02c938cb1327910b56b8f61a"
last_verified: 2026-05-14
possibly_outdated: false
language: "zh"
canonical_source: ""
personal_writing: true
---

# ECC 详细设计说明书（Everything Claude Code v2.0.0-rc.1）

> ⚠ 个人写作，不参与 source_count 计数。核心立场已写入 [[concepts/claude-code-workflow]] 的 My Position 节。

## Key Points

- **文档范围**：面向 ECC 开发人员、贡献者、系统集成工程师，1515 行详细设计，覆盖 12 个子系统
- **Agent 文件规范**（标准结构）：
  - `## Role`：核心职责（1-3 句）
  - `## When to Use`：触发场景列表
  - `## Workflow`：分步执行流程
  - `## Output Format`：输出格式标准
  - `## Constraints`：禁止行为清单
- **Agent 分类设计（规划与设计类）**：
  - `planner`：需求→实施计划，识别技术风险和依赖，带优先级子任务分解
  - `architect`：系统级设计决策，高内聚低耦合原则
  - `code-architect`：代码层模块划分与接口设计
- **Skills 子系统**：可复用知识单元，独立于 Agent，跨 Agent 共享，以 Markdown 文件存储
- **Commands 子系统**：slash commands（/cmd），可触发复杂多步骤工作流
- **Hooks 子系统**：拦截 Claude Code 生命周期事件（pre-tool / post-tool / pre-session），安全检查和自动化
- **Rules 子系统**：全局行为约束，优先级高于 Agent 定义，分 project/global 两级
- **MCP 集成层**：14 套 MCP 服务器配置，按用途分类（开发工具 / 数据库 / 服务集成 / 浏览器自动化）
- **国际化设计**：7 种语言，i18n key 替代硬编码文本，支持 locale 动态切换
- **扩展点设计**：用户通过 override 目录自定义，不修改框架原文件（Immutability 原则）

## Concepts Extracted

- [[concepts/claude-code-workflow]]
- [[concepts/agent-harness]]
- [[concepts/model-context-protocol]]

## Entities Extracted

- [[entities/ecc-framework]]

## External References

## Contradictions

## My Notes

详细设计说明书揭示了 ECC 的"层次化扩展"思路：核心不可变 + override 层可扩展。这与传统软件框架设计高度一致，体现了工程成熟度。Hooks 子系统作为安全拦截层的设计尤其重要——它是 Security-First 原则的具体落地。
