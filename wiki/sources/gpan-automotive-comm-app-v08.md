---
type: source
title: "GPAN 车载通信介绍-应用场景价值分析 V0.8"
date: 2026-04-27
source_type: presentation
source_url: ""
raw_path: "raw/articles/GPAN 车载通信介绍-应用场景价值分析(0.8).pptx"
raw_sha256: "32288345"
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

# GPAN 车载通信介绍-应用场景价值分析 V0.8

## Summary

Goodix GPAN 车载通信应用场景价值分析演示文稿（20页，V0.8），重点呈现 MCULess 与分布式功放的方案对比，并附有 TSN 现状与痛点分析。为 V0.6 的升级版，数据略有更新（特别是分布式功放性能数据）。

## Key Points

### GPAN 核心定位
- MCULess IO 扩展芯片：ZCU/ECU 节点去除 MCU，通过 GPAN 远程控制外设
- 总线融合：同一网络承载以太网包 + CAN/LIN 控制数据 + 音频 + 视频
- 可扩展性：100M/1G/2.5G/5G/10G 协议兼容，保护投资

### MCULess 方案对比

| 对比项 | 10Base-T1S MCULess | 100Base-T1 GPAN |
|---|---|---|
| 内部处理时延 | >290μs | **<50μs** |
| 带宽 | 半双工 10M | **环模式全双工 200M** |
| IO 数量 | 少 | **大** |
| 音频播放 | 困难 | **容易** |

| 对比项 | 10Base-T1S | CAN-FD GPAN |
|---|---|---|
| 生态 | 差，国内未商用 | **好，CAN 生态成熟** |
| 网络改造成本 | 高 | **无** |
| 软件开销 | 大 | **极小，直接远程控制** |

### 分布式功放方案对比（V0.8 更新数据）

| 对比项 | 以太网音频 | A2B | GPAN |
|---|---|---|---|
| 时延 | 约 1~5ms | μs 级（半双工） | **~100μs（全双工+大带宽）** |
| Jitter | 未公布 | S1:1.57ns/S10:5.5ns | **Normal:<1.2ns / 性能模式:~50ps** |
| RNC（≤2-3ms） | 有风险 | 支持 | **支持** |
| ANC（≤0.5-1ms） | 不支持 | 支持 | **支持** |
| 综合成本 | 高 | 高 | **低** |

> 注：本版 Jitter 性能模式值为 ~50ps，V1.8 更新为 ~100ps，以 V1.8 为准

### 车载以太网 TSN 痛点分析
TSN 在国内车载领域的商用化挑战：

| 难点 | 简述 |
|---|---|
| 协议复杂 | IEEE 802.1 子标准族，多协议组合配置极复杂 |
| BOM 成本高 | 交换机/PHY/MCU 均需 TSN 支持，直接增加成本 |
| 系统配置复杂 | 资源预留和调度时隙管理困难 |
| 协议栈适配 | 与现有平台适配难度大，验证困难 |
| 改造困难 | CAN/LIN 网络适配改造困难 |
| 投入产出比 | 国内无商业成功案例 |

**GPAN 的优势**：通过简化架构（低时延/低抖动满足 TSN 需求，出口归一化），无需 TSN 即可满足车载实时音视频需求。

## Entities Mentioned

- [[entities/goodix-technology]]

## Concepts

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/time-sensitive-networking]]
