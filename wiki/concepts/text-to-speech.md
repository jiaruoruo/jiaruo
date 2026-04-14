---
type: concept
title: "文字转语音"
date: 2026-04-13
updated: 2026-04-13
tags:
  - tts
  - speech
  - audio
  - ai
source_count: 1
confidence: low
domain_volatility: high
last_reviewed: 2026-04-13
aliases:
  - "文字转语音"
  - "语音合成"
  - "TTS"
  - "text-to-speech"
  - "T2A"
  - "文本转语音"
---

# 文字转语音（Text-to-Speech）

## Definition

文字转语音（Text-to-Speech，TTS），又称语音合成，是将输入的文本内容转换为自然人声音频的 AI 技术。现代 TTS 系统通常基于深度学习模型，可控制音色、语速、语调、输出格式等参数，并支持多语言和流式输出。

## Key Points

- **同步 vs 异步**：短文本（≤10,000 字符）适合同步接口（实时返回音频）；长文本（最长 100 万字符）使用异步接口，通过 task_id 轮询结果
- **模型分级**：通常分 hd（高质量）和 turbo（低延迟）两档，按场景选择；MiniMax 当前最新为 speech-2.8 系列
- **音色选择**：平台预置 300+ 系统音色，亦支持用户自定义复刻音色（Voice Cloning）
- **多语言支持**：MiniMax TTS 支持 40 种语言，包括中文（含粤语）、英语、日语、韩语等主流语种
- **输出格式**：通常支持 mp3、pcm、flac、wav（wav 一般仅限非流式）
- **字幕时间戳**：异步长文本接口支持返回句级时间戳，可用于字幕生成场景
- **临时 URL 注意**：异步任务结果 URL 有效期有限（MiniMax 为 9 小时），需及时下载

## My Position

## Contradictions

## Sources

- [[sources/minimax-api-overview]]

## Evolution Log

- 2026-04-13（1 sources）：概念初建，来源为 MiniMax 开放平台接口概览文档
