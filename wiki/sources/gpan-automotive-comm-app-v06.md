---
type: source
title: "GPAN 车载通信介绍-应用场景价值分析 V0.6"
date: 2026-04-27
source_type: presentation
source_url: ""
raw_path: "raw/articles/GPAN 车载通信介绍-应用场景价值分析0.6.pptx"
raw_sha256: 9c30787a
author: "Goodix Technology（汇顶科技）"
language: zh
tags:
  - gpan
  - mculess
  - distributed-audio
  - automotive
  - tsn
  - goodix
---

# GPAN 车载通信介绍-应用场景价值分析 V0.6

## Summary

Goodix GPAN 车载通信应用场景价值分析演示文稿（15页，V0.6），为 V0.8 的早期草稿。主体内容与 V0.8 高度重叠，但有以下差异需记录：封装规格标注为 BGA192（V0.8 更新为 BGA196），分布式功放 Jitter 性能数据未包含（V0.8 新增），TSN 内容相同。实质内容请参考更完整的 [[sources/gpan-automotive-comm-app-v08]]。

## Key Points

### 与 V0.8 主要差异

| 项目 | V0.6 | V0.8 |
|---|---|---|
| 最大封装 | BGA192 | BGA196（10×10）|
| Jitter 数据 | 未含 | 新增（Normal:<1.2ns / 性能模式:~50ps）|
| 幻灯片数 | 15 | 20（增加音频方案硬件框图等）|
| 分布式功放时延 | 最低: 100μs 内 | 约 1~5ms (ETH) / ~100μs (GPAN) |

### 核心内容摘要（与 V0.8 一致部分）
- MCULess 方案 6 维综合收益对比（算力/协同/协议/软件/BOM/音频）
- 10Base-T1S vs GPAN MCULess 对比（>290μs vs <50μs）
- 分布式功放 ETH/A2B/GPAN 对比（TSN 复杂度高、A2B 成本高、GPAN 最优）
- TSN 5 大痛点（协议复杂/BOM 成本/系统配置/协议栈适配/改造困难）

## Entities Mentioned

- [[entities/goodix-technology]]

## Concepts

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/time-sensitive-networking]]
