---
type: source
title: "GPAN 车载 MCU-less 和分布式音频介绍（V1.8）"
date: 2026-06-01
source_url: ""
domain: "goodix"
author: "汇顶科技"
tags: []
processed: true
raw_file: raw/工作/articles/MCULess/GPAN 车载MCULess和分布式音频介绍(1.8).pptx
raw_sha256: d336b5fcbea35b40cd18b3309869efea667bf30a5fac3f0d935c4516ced79d72
last_verified: 2026-07-14
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# GPAN 车载 MCU-less 和分布式音频介绍（V1.8）

## Summary

汇顶 GPAN（General Purpose Access Network）芯片的车载 MCU-less 和分布式音频完整介绍。GPAN 是高效/可靠/低成本/低时延组网的 IO 扩展芯片，物理层 100Base-T1，全双工 100M 带宽，误码率<10⁻¹⁰，节点交换时延约 1.4µs，环支持 60 个子节点。支持控制数据/音频/视频混合传输，支持环形和菊花链组网。分布式音频方案支持 48K×32bit×48 通道无损传输，同步精度<1µs。芯片交付计划：2026 年 4 月 Tapeout，8 月工程样片，2027 年 3 月量产芯片。

## Key Points

- GPAN：100Base-T1 全双工 100M，误码率<10⁻¹⁰，节点时延 1.4µs，环支持 60 节点
- MCU-less 优势：最多保留 2 个 ZCU MCU，其余用 GPAN 远程 IO 芯片替代，BOM 和维护成本双降
- 分布式音频：48K×32bit×48 通道无损传输，同步精度<1µs，省掉集中式功放
- 对比 10BASE-T1S：时延 <50µs vs >290µs，带宽 200M vs 10M，IO 数量大
- 对比 A2B：Jitter Normal<1.2ns/性能模式~100ps vs A2B S1:1.57ns，线束节约约 65%
- 芯片交付：2026.04 Tapeout → 2026.08 工程样片 → 2027.03 量产(ASIL-B) → 2027.10 AECQ-100
- 三级网络架构：一级 2.5G 骨干 + 二级 100M MCU-less + 三级 CAN-FD/CAN-XL MCU-less
- 成本节省：ZCU MCU-less 约 80¥/车，分布式音频 48V 平台约 300¥/车

## Concepts Extracted

- [[gpan-communication]]
- [[mculess-architecture]]
- [[eea-architecture]]
- [[automotive-ethernet-10base-t1s]]
- [[vehicle-domain-controller]]
- [[zonal-gateway]]
- [[time-sensitive-networking]]
- [[can-eth-protocol-conversion]]

## Entities Extracted

- [[goodix-technology]]

## Contradictions

## My Notes
