---
type: source
title: "ECC 应用教程手册与自定义扩展指南（Everything Claude Code）"
date: 2026-05-12
source_url: ""
domain: personal
author: "刘万龙"
tags:
  - personal-writing
  - ecc
  - agent-orchestration
  - claude-code
  - tutorial
processed: true
raw_file: raw/工作/personal/ECC-应用教程手册.md
raw_sha256: 06a2357081c11c552dec979a63388c4310af0ec8a1205b99aa386bd5ab845d0a
companion_files:
  - path: "raw/personal/ECC-自定义模块添加指南.html"
    sha256: "1f25d60b8d57a20be05ec62dc83205806d438be20efe9ee1af8f30b90b601063"
    note: "自定义模块添加指南（中文 HTML 版）"
  - path: "raw/personal/CUSTOM_EXTENSION_GUIDE.html"
    sha256: "c518803582af2b807884c3947ed3e1b189184d7a76ca1ae944385f4d435bcb8f"
    note: "Custom Extension Guide（英文 HTML 版）"
last_verified: 2026-05-14
possibly_outdated: false
language: "zh"
canonical_source: ""
personal_writing: true
---

# ECC 应用教程手册与自定义扩展指南（Everything Claude Code）

> ⚠ 个人写作，不参与 source_count 计数。核心立场已写入 [[concepts/claude-code-workflow]] 的 My Position 节。

## Key Points

- **教程目标**：覆盖从安装到进阶使用的完整学习路径，面向不同角色（个人开发者 / 团队 / 企业集成商）
- **安装方式**：克隆仓库 + install.sh 自动部署，支持全量安装和选择性安装
- **核心使用模式**：
  - 调用 Agent：`@agent-name [任务描述]`
  - 执行 Skill：`/skill [参数]`
  - 运行 Command：`/cmd [参数]`
- **自定义扩展流程（重要）**：
  1. 在 `~/.claude/agents/custom/` 创建 .md 文件，遵循 Agent 标准结构
  2. 在 `~/.claude/skills/custom/` 添加可复用技能单元
  3. 在 `~/.claude/hooks/custom/` 注册自定义 Hooks
  4. 所有自定义内容通过 override 机制加载，不污染框架核心
- **语言适配**：通过 CLAUDE_LANG 环境变量切换，支持 7 种语言（zh-CN / en / ja / ko / de / fr / es）
- **MCP 服务器使用**：14 套配置按用途模块化加载，避免全量引入
- **最佳实践**：
  - 优先复用已有 Agent，再考虑自定义
  - 自定义 Agent 的 Constraints 节必须明确禁止行为
  - Skills 保持单一职责，避免膨胀

## Concepts Extracted

- [[concepts/claude-code-workflow]]
- [[concepts/agent-harness]]

## Entities Extracted

- [[entities/ecc-framework]]
- [[entities/claude-code]]

## External References

## Contradictions

## My Notes

教程手册和扩展指南（中英双语 HTML）合并记录。自定义扩展的 override 模式是 ECC Immutability 原则的用户侧体现——框架升级时自定义内容不受影响。这对企业级部署尤其关键。
