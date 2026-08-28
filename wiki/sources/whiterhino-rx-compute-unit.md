---
type: source
date: 2026-08-28
title: "白犀牛无人车 RX 车型算力单元硬件方案"
source_url: ""
raw_file: "raw/工作/clippings/机器人/白犀牛无人车（以 RX 车型为主）算力单元硬件方案.md"
raw_sha256: 912436abf69cb41a3fcffd49ea4dfb66db5bce8d25a67a90111e67d6bbdc1547
last_verified: 2026-08-28
domains: [embodied-ai, edge-ai]
entities: [whiterhino]
concepts: [robot-brain-compute-platform, autonomous-driving-compute]
---

# 白犀牛无人车 RX 车型算力单元硬件方案

**来源**：[[whiterhino]]（内部资料，无公开 URL）

## 主要内容

白犀牛（WhiteRhino）RX 车型算力单元方案，采用经纬恒润域控制器，强调制动冗余与供应链多元化。

### 核心算力

- 域控制器：经纬恒润（Jingwei Hengrun）自研域控
- 制动冗余：TwoBox 双冗余制动系统

### 感知硬件

- 激光雷达：3 个 LiDAR
- 摄像头：11 路摄像头

### 供应链

- 供应商数量：65 家
- 策略：多元化供应商降低单点依赖

## 关联资源

- [[jiushi-autonomous-vehicle-brain-hardware]] — 九识智能双 Orin X 方案
- [[neolix-x3-plus-compute-hardware]] — 新石器 X3 Plus 算力方案
