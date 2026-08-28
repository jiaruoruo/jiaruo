---
type: source
date: 2026-08-28
title: "九识智能 自动驾驶车辆大脑硬件方案"
source_url: ""
raw_file: "raw/工作/clippings/机器人/九识智能-大脑硬件方案.md"
raw_sha256: 7185256b9ed2a8eb13e2cf7fa602f9d6ccc96dc6defb79dd524a823223b335d6
last_verified: 2026-08-28
domains: [embodied-ai, edge-ai]
entities: [jiushi-autonomous]
concepts: [robot-brain-compute-platform, autonomous-driving-compute]
---

# 九识智能 自动驾驶车辆大脑硬件方案

**来源**：[[jiushi-autonomous]]（内部资料，无公开 URL）

## 主要内容

九识智能（Jiushi Intelligent）面向 L4 无人配送车的 [[robot-brain-compute-platform]] 硬件方案，采用双 NVIDIA Orin X 域控架构。

### 核心算力

- 主控：双 NVIDIA Orin X 域控制器
- 算力：~500 TOPS INT8
- 品牌认证：Zelos Inside

### 感知硬件

- 激光雷达：4 个 LiDAR
- 摄像头：10+ 路摄像头

### AI 能力

- 视觉语言模型（VLM）
- 视觉语言动作模型（VLA）
- L4 全栈自动驾驶

## 关联资源

- [[neolix-x3-plus-compute-hardware]] — 新石器 X3 Plus 算力方案
- [[whiterhino-rx-compute-unit]] — 白犀牛 RX 算力单元
