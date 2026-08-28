---
type: source
date: 2026-08-28
title: "新石器无人车 X3 Plus 算力硬件方案"
source_url: ""
raw_file: "raw/工作/clippings/机器人/新石器无人车（以第四代主力车型 X3 Plus 为代表）算力硬件方案.md"
raw_sha256: 1aa72f924a3a23514ad4840232f4dc171860319b4b4faefeef47e297d722376b
last_verified: 2026-08-28
domains: [embodied-ai, edge-ai]
entities: [neolix]
concepts: [robot-brain-compute-platform, autonomous-driving-compute]
---

# 新石器无人车 X3 Plus 算力硬件方案

**来源**：[[neolix]]（内部资料，无公开 URL）

## 主要内容

新石器第四代主力车型 X3 Plus 的算力硬件方案，采用单 NVIDIA DRIVE Orin-X 实现 ASIL-D 级别安全算力。

### 核心算力

- 主控：NVIDIA DRIVE Orin-X（单颗）
- 算力：254 TOPS
- 功能安全：ASIL-D 认证

### 感知硬件

- 摄像头：12 路高清摄像头
- 激光雷达：2× RSLiDAR Fairy 96 线

### AI 模型

- 端到端模型：Neolix-VA

### 通信

- 双 5G + C-V2X

## 关联资源

- [[jiushi-autonomous-vehicle-brain-hardware]] — 九识智能双 Orin X 方案
- [[whiterhino-rx-compute-unit]] — 白犀牛 RX 算力单元
