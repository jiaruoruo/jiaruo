---
type: entity
title: "Hermes Agent"
date: 2026-04-19
updated: 2026-04-25
tags:
  - agent
  - harness
  - self-improvement
  - open-source
entity_type: tool
aliases:
  - "Hermes Agent"
  - "hermes-agent"
  - "Hermes"
  - "NousResearch Hermes"
---

# Hermes Agent

## Description

Hermes Agent 是 Nous Research 开发的开源 AI Agent 框架，以"自主进化"为核心差异化特性。与 OpenClaw 的"人工纠正式"模式不同，Hermes 在复杂任务完成后能自动评估执行过程、生成可复用技能文件（`~/.hermes/skills/`），实现 Agent 自主学习与能力积累，无需用户主动触发改进循环。

## Key Contributions

- **自主技能生成**：任务完成后自动将经验写入 `~/.hermes/skills/<task>/SKILL.md`，形成具体可操作的规则（非笼统描述），工作留下可复用痕迹
- **回溯能力**：可检索数周前对话的完整排障过程，工作历史自然形成知识库
- **agentskills.io 标准支持**：技能文件与 OpenClaw、Claude Code、Cursor 互通，无平台锁定
- **与 OpenClaw 互补**：OpenClaw 主导需完全控制的定时任务（可预测），Hermes 主导需自主进化的协调类 Agent；两套可共享同一份情报文件（如 DAILY-INTEL.md）并行运行

## Related Concepts

- [[agent-harness]]

## Sources

- [[sources/hermes-vs-openclaw-comparison]]
- [[sources/openclaw-vs-hermes-deep-dive]]
- [[sources/agent-route-comparison-2026]]

## Evolution Log

- 2026-04-19（1 sources）：实体页初建，来源为 Hermes vs OpenClaw 对比实战文章
- 2026-04-19（2 sources）：强化——架构师深度对比文章补充：Hermes 核心资产是学习型执行循环；Skill = 过程记忆（`skill_manager_tool.py`）；Memory 三层架构（SQLite+FTS5）；安全 = 纵深防御；六种 terminal backend；迁移路径 `hermes claw migrate`
- 2026-04-25（3 sources）：强化——三条路线比较文章印证 Hermes「学习效率优先」定位；确认其「越用越顺」叙事和「反内耗」情绪共鸣；适合成本敏感+愿折腾的开发者
