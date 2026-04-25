---
type: concept
title: "音色克隆"
date: 2026-04-13
updated: 2026-04-13
tags:
  - tts
  - voice
  - cloning
  - ai
source_count: 1
confidence: low
domain_volatility: high
last_reviewed: 2026-04-13
aliases:
  - "音色克隆"
  - "音色复刻"
  - "声音克隆"
  - "Voice Cloning"
---

# 音色克隆（Voice Cloning）

## Definition

音色克隆（Voice Cloning）是通过上传目标说话人的参考音频，让 AI 模型学习并复刻其音色特征，从而在后续语音合成中使用该定制音色生成语音的技术。区别于使用预置系统音色，克隆音色能够还原特定人物的语音风格。

## Key Points

- **使用流程**：上传待克隆音频获取 file_id → 可选上传示例音频增强效果 → 调用克隆接口生成 voice_id → 在 TTS 接口中使用该 voice_id
- **临时音色机制**：克隆生成的音色为临时音色，须在 **7 天（168小时）内** 在任意语音合成接口中调用一次，否则自动删除
- **计费时机**：克隆接口本身不立即计费，费用在**首次用于语音合成时**收取（试听行为不计）
- **使用限制**：通常需要完成平台实名认证（个人或企业）方可调用
- **应用场景**：IP 音色复刻、有声书特定配音、虚拟人定制声线等

## My Position

## Contradictions

## Sources

- [[sources/minimax-api-overview]]

## Evolution Log

- 2026-04-13（1 sources）：概念初建，来源为 MiniMax 开放平台接口概览文档
