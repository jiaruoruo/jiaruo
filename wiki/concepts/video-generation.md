---
type: concept
title: "AI 视频生成"
date: 2026-04-13
updated: 2026-04-13
tags:
  - video
  - generative-ai
  - multimodal
source_count: 1
confidence: low
domain_volatility: high
last_reviewed: 2026-04-13
aliases:
  - "AI 视频生成"
  - "视频生成"
  - "video generation"
  - "video-generation"
  - "文生视频"
  - "图生视频"
---

# AI 视频生成（Video Generation）

## Definition

AI 视频生成（Video Generation）是指利用深度学习模型，根据文本描述（文生视频）或参考图像（图生视频）自动合成动态视频内容的技术。当前主流方案基于扩散模型或自回归模型，可生成数秒至数十秒的视频片段。

## Key Points

- **输入模式**：文生视频（text-to-video）和图生视频（image-to-video），部分模型支持首帧/尾帧/主体参考图控制
- **异步任务模式**：视频生成耗时较长，通常为异步接口：提交任务获取 task_id → 轮询状态 → 状态成功后获取 file_id → 下载文件
- **分辨率与时长**：MiniMax Hailuo-02 支持最高 1080P、最长 10 秒；Hailuo-2.3 在动作和物理表现上进一步升级
- **模板化 Agent**：平台提供预置视频 Agent 模板（如服装试穿、换脸等），降低使用门槛，输入图片或文字即可生成特定风格视频
- **性价比分级**：通常提供标准版（更高质量）和快速版（Fast/Turbo，更高性价比）两档

## My Position

## Contradictions

## Sources

- [[sources/minimax-api-overview]]

## Evolution Log

- 2026-04-13（1 sources）：概念初建，来源为 MiniMax 开放平台接口概览文档
