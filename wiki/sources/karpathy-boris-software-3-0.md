---
type: source
title: "Karpathy、Claude Code之父Boris，最新访谈，把整个程序员圈炸了！"
date: 2026-05-23
source_url: "https://mp.weixin.qq.com/s/e1vrUYcGE6RToVkl_HcXZQ"
domain: "mp.weixin.qq.com"
author: "猕猴桃"
tags:
  - agent
  - software-3-0
  - claude-code
  - ai-workflow
processed: true
raw_file: "raw/clippings/2026-05-23Karpathy、Claude Code之父Boris，最新访谈，把整个程序员圈炸了！.md"
raw_sha256: "0d17e97f104e711936be80529389e134d265e524474556220667316441803d1b"
last_verified: 2026-05-23
possibly_outdated: false
language: "zh"
---

# Karpathy、Claude Code之父Boris，最新访谈，把整个程序员圈炸了！

## Summary

红杉 AI Ascent 2026 上 Boris Cherny（Claude Code 之父）与 Karpathy 两场演讲解读。共同结论：编程的执行层已被解决，但方向层反而更难。Boris 称 2026 年彻底没写过一行代码，用手机 Claude App 同时跑 5–10 会话、数百到数千个 Agent，并自创 Sloop 工作流（用 Cron 预约循环任务）。Karpathy 提出 Software 3.0（Prompting 即编程）。

## Key Points

- Boris 工作方式：不再坐电脑前，手机跑数百–数千 Agent；Sloop 工作流用 Cron 做循环（盯 PR/修 CI/抓 Twitter 反馈），一天处理过 150 个 PR
- Anthropic 内部全公司不手写代码，所有 SQL/基础架构由模型生成，Agent 间在 Slack 互相沟通解决问题
- 「为还不存在的模型提前建好 harness」——Claude Code 是违背 PMF 的赌注（见 [[agent-harness]]）
- Karpathy Software 3.0：LLM 是新计算机，代码=1.0、权重=2.0、Prompting=3.0，往上下文窗口塞什么就等于编程
- OpenClaw 安装方式示例：从 shell 脚本变成一段文字说明，Agent 自己读环境、判断、debug、装好

## Concepts Extracted

- [[agent-harness]]
- [[claude-code-workflow]]

## Entities Extracted

- [[entities/claude-code]]

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
