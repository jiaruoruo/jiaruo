---
type: source
title: "装了最近爆火的 Hermes，和OpenClaw的对比来了！"
date: 2026-04-19
source_url: "https://mp.weixin.qq.com/s/KrZ26wvMvOusJRKtEeFekw"
domain: "ai-agent"
author: "Shubham Saboo"
tags:
  - agent
  - hermes
  - openclaw
  - self-improvement
processed: true
raw_file: "raw/clippings/2026-04-19装了最近爆火的 Hermes，和OpenClaw的对比来了！.md"
raw_sha256: "270abb1cf77d56e350335c46f893b2c5ad08baaa804342eb7d85413d0f40000a"
last_verified: 2026-04-19
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 装了最近爆火的 Hermes，和OpenClaw的对比来了！

## Summary

Shubham Saboo 在运行 OpenClaw 团队数月后发现"Agent 没有变好，是我越来越擅长管理它们"。他在同台机器上加入 Hermes Agent（Nous Research 开源）进行对照实验，发现 Hermes 能自主生成技能文件、自动改进循环，形成"Agent 自己进化"的机制。文章总结了两套系统的核心差异与最优配合策略。

## Key Points

- **OpenClaw 模式（纠正式提示词工程）**：用户发现问题→解释修正方法→更新记忆/指令→等待行为固定；进步依赖用户主动在场，Agent 不会自己进化
- **Hermes 模式（自主进化式）**：复杂任务完成后 Agent 自评估→决定什么值得保留→自动写入 `~/.hermes/skills/` 技能文件；用户可检查/编辑/删除但无需主动发起
- **核心差异**：改进循环所有权不同——OpenClaw 所有权在用户，Hermes 所有权在 Agent 本身
- **Hermes 实例**：Monica 自动写了 `local-writing-canon-analysis/SKILL.md`，包含从已发布文章推断出的具体编辑规则（非笼统声明）；回溯能力可检索数周前的完整排障过程
- **Hermes 安装**：`curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash`；自动检测并导入 OpenClaw 设置；推荐使用前沿模型（学习循环需要强推理能力）
- **agentskills.io 标准**：技能文件可在 OpenClaw、Hermes、Claude Code、Cursor 之间移植，无平台锁定
- **最优分工策略**：需完全控制、可预测的 Agent → OpenClaw；需自主进化、持续改进的协调类 Agent → Hermes；两套同时运行互不干扰（共享同一份 DAILY-INTEL.md 情报文件）

## Concepts Extracted

- [[agent-harness]]

## Entities Extracted

- [[openclaw]]
- [[hermes-agent]]

## Contradictions

## My Notes
