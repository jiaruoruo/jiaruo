---
type: source
title: "OpenClaw vs Hermes：一文深入理解两大通用 Agent"
date: 2026-04-19
source_url: "https://mp.weixin.qq.com/s/oKuSgz5CP4aPOjt_o2Vi8g"
domain: "mp.weixin.qq.com"
author: "架构师（JiaGouX）"
tags:
  - agent-harness
  - openclaw
  - hermes-agent
  - comparison
  - agent-architecture
processed: true
raw_file: "raw/clippings/2026-04-19OpenClaw vs Hermes：一文深入理解两大通用 Agent.md"
raw_sha256: "9f3f255949835429f17ac97c5529208cc9802bb08b8aff26f11c4c7849770d51"
last_verified: 2026-04-19
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# OpenClaw vs Hermes：一文深入理解两大通用 Agent

## Summary

架构师（JiaGouX）公众号深度对比文章，把 OpenClaw 和 Hermes Agent 放在同一框架下分析：两者都是通用 Agent 系统，但工程重心截然不同。OpenClaw 的厚度在入口和控制面；Hermes 的厚度在执行循环和经验沉淀。文章从系统定位、Skill 语义、Memory 架构、安全思路、迁移路径、选型建议六个维度完成对比。

## Key Points

- **定位分野**：OpenClaw = 本地优先 Agent Gateway（管入口和秩序）；Hermes = 学习型 Agent Runtime（管执行和经验）；两者都属通用 Agent 系统，但厚度长在不同层
- **入口能力差距**：OpenClaw 覆盖 25+ 聊天渠道（WhatsApp/Telegram/Slack/Discord/WeChat/Feishu 等）+ macOS/iOS/Android 节点 + Live Canvas；Hermes 支持 CLI 和主流聊天平台，但入口能力相对轻量
- **Skill 语义差异**：OpenClaw skill = SOP 库（人定义、系统治理、50+ 内置、加载优先级分层）；Hermes skill = 过程记忆（Agent 从成功任务自动沉淀、`skill_manager_tool.py` 实现 create/update/delete）
- **Memory 三层架构（Hermes）**：会话记忆（单次上下文）→ 持久记忆（MEMORY.md + USER.md，跨会话）→ 技能记忆（SQLite + FTS5 全文检索，LLM 摘要召回，自我迭代）
- **Memory 文件路线（OpenClaw）**：SOUL.md（Agent 性格）+ USER.md（用户偏好）+ memory/*.md（日常日志）+ MEMORY.md（精选长期记忆）；上下文压缩前静默写入防丢失
- **安全思路对立**：OpenClaw = 信任模型 + 配置审计（personal assistant，单一受信 operator；曾暴露 WebSocket Token 漏洞）；Hermes = 纵深防御（审批 + Docker/NixOS 容器隔离 + 凭据过滤 + 注入扫描；截至目前无重大漏洞）
- **迁移支持**：`hermes claw migrate` 可导入 OpenClaw 的 SOUL.md/MEMORY.md/USER.md/skills/allowlist/部分 messaging settings/API keys；建议先 `--dry-run`，把迁移作为试用入口而非架构替换
- **选型一句话**：缺入口和秩序 → OpenClaw；缺经验沉淀和自我改进 → Hermes；更完整的 Agent 系统两者兼备

## Concepts Extracted

- [[agent-harness]]

## Entities Extracted

- [[entities/openclaw]]
- [[entities/hermes-agent]]

## Contradictions

## My Notes
