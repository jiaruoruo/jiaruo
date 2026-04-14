---
type: source
title: "接口概览 - MiniMax 开放平台文档中心"
date: 2026-04-13
source_url: "https://platform.minimaxi.com/docs/api-reference/api-overview"
domain: "platform.minimaxi.com"
author: ""
tags:
  - minimax
  - api
  - multimodal
  - llm
  - tts
  - video-generation
processed: true
raw_file: "raw/clippings/2026-04-13-接口概览 - MiniMax 开放平台文档中心.md"
raw_sha256: "c28ba018d66f29725c8cca00d06ffa3683ad6e9da599fbb7bce39ecfc606effa"
last_verified: 2026-04-13
possibly_outdated: false
language: "zh"
canonical_source: "https://platform.minimaxi.com/docs/api-reference/api-overview"
---

# 接口概览 - MiniMax 开放平台文档中心

## Summary

MiniMax 开放平台的全模态 API 接口概览文档，涵盖文本生成、语音合成（同步/异步）、音色克隆、音色设计、视频生成、视频 Agent、图像生成、音乐生成、文件管理及官方 MCP 服务器等能力。文本模型可通过 Anthropic SDK（推荐）或 OpenAI SDK 兼容接入，所有生成类接口均支持按量付费或 Token Plan 两种计费方式。

## Key Points

- **文本生成**：M2.7 / M2.5 / M2.1 / M2 系列，均支持最大 204,800 token；推荐通过 Anthropic SDK 接入，亦兼容 OpenAI SDK
- **同步语音合成（T2A）**：单次最长 10,000 字符，支持 300+ 音色、流式输出、40 种语言；模型分 hd / turbo 两档（speech-2.8 为最新）
- **异步长文本语音合成（T2A Async）**：单次最长 100 万字符，支持字幕时间戳（精确到句），结果 URL 有效期仅 9 小时
- **音色克隆（Voice Cloning）**：上传参考音频快速复刻；临时音色，7 天内需调用才能永久保留；费用在首次语音合成时收取
- **音色设计（Voice Design）**：基于文字描述 prompt 生成定制音色；同为临时音色，7 天有效
- **视频生成**：Hailuo-2.3（最新）/ Hailuo-02（1080P/10s）；支持文生视频和图生视频；异步任务模式（task_id → file_id → 下载）
- **视频 Agent**：11 个预设模板（换脸、跳水、服装试穿等），基于模板+用户图片/文字生成视频
- **图像生成**：image-01 / image-01-live（支持画风设置），支持文生图和图生图
- **音乐生成**：music-2.6，输入歌词+描述生成人声歌曲
- **文件管理**：上传/列出/检索/下载/删除；总容量 100GB，单文件上限 512MB；支持 pdf/docx/txt/jsonl/mp3/m4a/wav
- **官方 MCP**：提供 Python 版（MiniMax-MCP）和 JS 版（MiniMax-MCP-JS）MCP Server 实现

## Concepts Extracted

- [[multimodal-api]]
- [[text-to-speech]]
- [[voice-cloning]]
- [[video-generation]]
- [[model-context-protocol]]

## Entities Extracted

- [[minimax]]

## Contradictions

## My Notes
