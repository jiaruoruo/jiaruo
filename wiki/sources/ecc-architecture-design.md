---
type: source
title: "ECC 架构设计说明书（Everything Claude Code v2.0.0-rc.1）"
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
raw_file: "raw/personal/ECC-架构设计说明书.md"
raw_sha256: "ee57d0b8ad9670c5043de374f176c79fc86a719b33d65740437ae50b0e975339"
companion_files:
  - path: "raw/personal/ECC-架构图.html"
    sha256: "cd8c78c13146b95cd1663935476f096b26878dcee44309075e68367df9ad635f"
    note: "架构可视化图表（HTML）"
last_verified: 2026-05-14
possibly_outdated: false
language: "zh"
canonical_source: ""
personal_writing: true
---

# ECC 架构设计说明书（Everything Claude Code v2.0.0-rc.1）

> ⚠ 个人写作，不参与 source_count 计数。核心立场已写入 [[concepts/claude-code-workflow]] 和 [[concepts/agent-harness]] 的 My Position 节。

## Key Points

- **项目定位**：ECC（Everything Claude Code）= AI 代理编排框架的"操作系统增强层"，起源于 Anthropic 黑客马拉松获奖项目，经 10+ 个月生产环境验证
- **规模**：53 专用子代理、200+ 工作流技能、69 命令、12+ 语言生态、14 套 MCP 服务器配置、7 种国际化
- **支持框架**：Claude Code / Codex / Cursor / OpenCode / Gemini（Tool Adapter 层解耦）
- **五大设计原则**：
  1. **Agent-First**：每个专业任务均由专属 Agent 承担，避免通用 Agent 稀释专注度
  2. **Skills-First**：可复用知识单元（Skills）独立于 Agent，跨 Agent 共享
  3. **Immutability**：框架核心不可变，用户扩展通过 override 而非修改原文件
  4. **Test-Driven**：每个 Agent / Skill 均有对应测试用例
  5. **Security-First**：权限最小化，Hooks 层拦截危险操作
- **部署场景**：个人开发者 / 团队协作 / 企业级部署 / AI 系统集成商
- **架构分层**：
  - 用户界面层（Claude Code CLI）
  - 编排层（Orchestration：multi-agent 协作、task routing）
  - 核心子系统层（Agents / Skills / Commands / Hooks / Rules / MCP）
  - Tool Adapter 层（跨框架兼容）
  - 基础设施层（CLI 工具 / 安装系统 / i18n）

## Concepts Extracted

- [[concepts/claude-code-workflow]]
- [[concepts/agent-harness]]
- [[concepts/model-context-protocol]]

## Entities Extracted

- [[entities/ecc-framework]]
- [[entities/claude-code]]

## External References

- GitHub 仓库：未公开（私有项目，用户自有）
- Anthropic 黑客马拉松：获奖项目来源

## Contradictions

## My Notes

ECC 是作者将 agent-harness 思想系统化工程化的产物。53 个专用子代理的规模，意味着"专业化 Agent > 通用 Agent"这个判断已经被生产验证。架构图以 HTML 形式提供，可视化了子系统间的编排关系。
