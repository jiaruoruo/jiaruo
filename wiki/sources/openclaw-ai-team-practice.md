---
type: source
title: "用OpenClaw打造一支24小时无休的AI团队，实战来了！"
date: 2026-04-19
source_url: "https://mp.weixin.qq.com/s/xdWnWuwau7lQhR0EQiKTVQ"
domain: "ai-agent"
author: "Shubham Saboo"
tags:
  - agent
  - openclaw
  - multi-agent
  - harness
processed: true
raw_file: "raw/clippings/2026-04-19用OpenClaw打造一支24小时无休的AI团队，实战来了！.md"
raw_sha256: "ae73064194c6760f3f4b8af54cd2f5d46e2b6241a56a6ad68428df65c57aaa9e"
last_verified: 2026-04-19
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 用OpenClaw打造一支24小时无休的AI团队，实战来了！

## Summary

Google Cloud 高级 AI 产品经理 Shubham Saboo 分享了自己用 OpenClaw 搭建 6 人 AI Agent 团队的一个月实战方案。每个 Agent 专注单一职责，通过文件系统（而非 API 或消息队列）协作，实现研究、内容创作、代码审查、邮件通讯的全自动化，每天节省 4-5 小时，月成本低于 400 美元。

## Key Points

- **6 Agent 分工**：Monica（协调官）、Dwight（研究员，每日扫描 X/HN/GitHub/论文）、Kelly（推文）、Rachel（LinkedIn）、Ross（代码审查/修复）、Pam（邮件通讯）；角色以美剧人物命名以固化 personality
- **SOUL.md 核心架构**：每个 Agent 的身份证+岗位描述+行为准则（40-60 行），塞进上下文不溢出；定义 personality、原则、与其他 Agent 关系、决策框架
- **文件系统协作**：Agent 间通信无 API 调用、无消息队列、无编排框架——Dwight 写 `intel/DAILY-INTEL.md`，Kelly/Rachel/Pam 读同一文件；数据双存：JSON（结构化，去重追踪）+ Markdown（人类可读，Agent 读取）
- **双层记忆系统**：每日日志（原始记录，发生了什么）+ MEMORY.md（提炼精华，经验教训、偏好模式）；心跳检查时从日志提炼进长期记忆，Agent 越用越聪明
- **实际成本**：Claude API $200/月 + Gemini $50-70/月 + TinyFish ~$50/月 + ElevenLabs ~$50/月 + OpenClaw 免费 = **<$400/月**；每天节省 4-5 小时，月省 120-150 小时
- **自愈机制**：HEARTBEAT.md 心跳检查，Monica 检测任务是否实际运行；超 26 小时未运行自动强制重跑；网关崩溃用 `openclaw gateway restart`
- **渐进式搭建原则**：第 1 周 1 个 Agent，稳定后再加；单文件"一写多读"避免协调冲突
- **经验总结**：真正的护城河不是模型，而是"学习的系统"——每天都在复利积累的记忆文件和打磨过的 SOUL

## Concepts Extracted

- [[agent-harness]]

## Entities Extracted

- [[openclaw]]

## Contradictions

## My Notes
