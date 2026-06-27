---
type: source
title: "Anthropic终于公开了他们内部Skill方法论。"
date: 2026-06-21
source_url: ""
domain: ""
author: ""
tags:
  - agent
  - skill
  - context-engineering
  - claude-code
processed: true
raw_file: "raw/clippings/Anthropic终于公开了他们内部Skill方法论。.md"
raw_sha256: b637e5baefbeae66185aa87fbc4f770abd9ccc4f8065987083c38065540f3a49
last_verified: 2026-06-27
possibly_outdated: false
language: "zh"
---

# Anthropic终于公开了他们内部Skill方法论。

## Summary

解读 Anthropic 博客《Lessons from building Claude Code: How we use skills》。核心论点：Skill 的本质是 Context Engineering（上下文工程）而非提示词——它解决的是上下文、经验沉淀与能力复用问题。Skill = 把老师傅经验写下来，重点写 Gotchas（常踩的坑），而非常识；重复执行的工作应沉淀为 Script 而非长 Instructions。

## Key Points

- Skill 本质是 Context Engineering：何时放进 Skill、何时拆成 References、何时写成 Script、何时用 Gotchas 约束模型
- 不要写废话：Skill 沉淀组织「隐性知识」，重点写模型不知道的 Gotchas（如「这个表不能按 created_at 排序」）
- Skill 是文件夹而非单个 md：SKILL.md + references/ + scripts/ + examples/ + assets/
- 反例教训：文风 Skill 塞上万字会占满上下文、反而让模型思考变浅；长 Instructions 执行不稳定，应改为 Script
- 优秀 Skill 解决的从来不是提示词问题，而是上下文/经验沉淀/能力复用（见 [[claude-code-workflow]]、[[agent-harness]]）

## Concepts Extracted

- [[claude-code-workflow]]
- [[agent-harness]]

## Entities Extracted

<!-- 无 -->

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
