---
type: concept
title: "多模态 API"
date: 2026-04-13
updated: 2026-04-15
tags:
  - api
  - multimodal
  - llm
source_count: 1
confidence: low
domain_volatility: high
last_reviewed: 2026-04-15
aliases:
  - "多模态 API"
  - "multimodal API"
  - "multimodal-api"
  - "多模态接口"
---

# 多模态 API（Multimodal API）

## Definition

多模态 API（Multimodal API）是指通过统一的 HTTP/SDK 接口，同时提供文本、语音、图像、视频、音乐等多种模态内容生成与处理能力的 AI 平台接口体系。开发者可以用同一套认证体系（API Key）调用不同模态的模型，而无需为每种能力单独集成不同厂商的服务。

## Key Points

- 核心特征：统一认证（单一 API Key）、多模态覆盖、兼容主流 SDK（如 OpenAI/Anthropic SDK 格式）
- MiniMax 平台涵盖模态：文本生成、语音合成（TTS）、音色克隆、视频生成、图像生成、音乐生成
- 文本模型：M2.7 / M2.7-highspeed / M2.5 / M2.5-highspeed / M2.1 / M2.1-highspeed / M2，均支持最大 204,800 token；M2.7 为当前旗舰
- 接入方式通常分为：HTTP 直接请求、官方 SDK、兼容第三方 SDK（OpenAI/Anthropic 格式）
- 生成类任务分同步（实时返回）和异步（task_id 轮询）两种模式，长内容生成通常为异步

## My Position

## Contradictions

## Sources

- [[sources/minimax-api-overview]]

## Evolution Log

- 2026-04-13（1 sources）：概念初建，来源为 MiniMax 开放平台接口概览文档
- 2026-04-15（1 sources）：修正：来源文件更新（SHA-256 变更），补充 M2.7 / M2.7-highspeed 为当前旗舰文本模型
