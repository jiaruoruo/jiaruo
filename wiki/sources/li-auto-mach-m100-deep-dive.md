---
type: source
title: "理想自研芯片马赫M100深度剖析，AI算力数字可以忽略不看"
date: 2026-04-23
source_url: "https://mp.weixin.qq.com/s/NEL-J-zNUghpL88pJnGfJg"
domain: "mp.weixin.qq.com"
author: "周彦武"
tags:
  - automotive-chip
  - soc
  - li-auto
  - m100
  - autonomous-driving
  - embodied-ai
processed: true
raw_file: "raw/clippings/2026-04-23理想自研芯片马赫M100深度剖析，AI算力数字可以忽略不看.md"
raw_sha256: "4667f2a02e07d3f9ecf65f07ba822dcb03a4d327b42381d4f5a9f9edc62fef32"
last_verified: 2026-04-25
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 理想自研芯片马赫M100深度剖析，AI算力数字可以忽略不看

## Summary

本文深度剖析理想汽车 2026 年 4 月 20 日发布的自研芯片马赫 M100（论文题目：M100: An Orchestrated Dataflow Architecture Powering General AI Computing）的内部架构。核心观点：在 VLM/World+Action Expert 时代，传统 AI 算力指标（TOPS）已无关紧要，标量与矢量计算能力才是关键。M100 是一个可舱驾融合使用的 SoC。

## Key Points

- **论文核心立场**：M100 刻意不披露 TOPS 算力，因为自动驾驶/具身智能/AI Agent 的算法体系中，核心矩阵乘法算力意义甚微；标量（CPU）和矢量计算算力更重要
- **五大模块**：①24 核 Cortex-A78AE CPU（ARM CMN-700 互联）；②NPU（14 TPB簇 × 4TPB + CCB/RISC-V中央控制）；③分级存储（LPDDR5X，273GB/s，最高 64GB）；④外设（11路摄像头MIPI CSI、10Gb双以太网、无PCIe）；⑤辅助（功能安全岛、安全引擎、ISP/VPU）
- **NPU 关键设计**：CCB 内嵌 SiFive X280 RISC-V 4 核 CPU，支持 4 个并发推理任务；通过 VCIX 接口将 RISC-V 矢量 ALU 与 TPB 直接耦合；专攻 VLA 多轮推理、扩散模型去噪、世界模型生成等标量/矢量混合计算
- **CVU 可配置矢量单元**：解决 Transformer 中 Element-wise 算子（ReLU/GELU/Sigmoid 等）无法被 GPU 加速的问题，与 TCU 集成，提升整体计算效率
- **HBSM 共享高宽带内存**：2MB，减少内存碎片化与数据搬运
- **基准对比**：仅用 8 个 TPB 簇对比英伟达 Thor-U（UniAD 场景），M100 延迟更低；剩余 6 个 TPB 簇留给座舱使用
- **编译器自研**：理想自研编译器和工具链，核心是计算流程图优化

## Concepts Extracted

- [[automotive-ai-chip]]

## Entities Extracted

- [[entities/li-auto]]

## Contradictions

## My Notes

"AI算力数字可以忽略不看"这个论点值得深入思考：VLM/World Model时代，工作负载从纯矩阵乘法（tensor TOPS）转向更多标量/矢量/条件分支/工作流调度，这和 Agent Harness 的"编排层"概念高度一致——M100 的 CCB+RISC-V 设计本质就是把 Harness 调度器烧进了芯片。
