---
type: concept
title: "汽车AI芯片"
date: 2026-04-25
updated: 2026-04-25
tags:
  - automotive
  - chip
  - soc
  - autonomous-driving
  - embodied-ai
source_count: 2
confidence: low
domain_volatility: high
last_reviewed: 2026-04-25
aliases:
  - "汽车AI芯片"
  - "Automotive AI Chip"
  - "automotive-ai-chip"
  - "自动驾驶SoC"
  - "车规AI SoC"
  - "汽车智能计算芯片"
---

# 汽车AI芯片（Automotive AI Chip）

## Definition

汽车 AI 芯片是面向自动驾驶、具身智能、座舱一体化的专用系统级芯片（SoC），核心设计理念在 VLM/World Model 时代已发生根本性转变：传统 AI 算力指标（TOPS）已不是核心竞争力，**标量与矢量计算能力、任务编排调度（Orchestrated Dataflow）和混合精度计算效率**才是关键，因为现代自动驾驶与具身智能算法体系大量依赖多步循环推理、workflow 调度和 Element-wise 算子处理。

## Key Points

- **算力指标颠覆**：VLM/World+Action Expert 时代，核心矩阵乘法（GEMM）的 AI 算力（TOPS）意义甚微；标量/CPU 算力和矢量计算算力比 AI 算力重要得多——理想 M100 论文刻意不披露 TOPS 正是此判断的公开声明
- **理想马赫 M100 架构（2026年）**：
  - CPU：24 核 Cortex-A78AE（ARM CMN-700 互联），中规中矩
  - NPU：14 TPB 簇（每簇 4 TPB）+ CCB（SiFive X280 RISC-V 4核，支持 4 个并发推理）；2D Mesh 总线 + 数据环形总线（DRB）互联；VCIX 接口将矢量 ALU 与 TPB 直接耦合
  - CVU（可配置矢量单元）：解决 Transformer Element-wise 算子（ReLU/GELU/Sigmoid 等）无法被 GPU 加速的问题，与 TCU 集成
  - 存储：LPDDR5X，273GB/s，最高 64GB；HBSM 共享高带宽内存 2MB
  - 外设：11 路摄像头 MIPI CSI，10Gb 双以太网，无 PCIe
- **舱驾融合设计**：14 个 TPB 簇可灵活分配——8 个给自动驾驶，6 个给座舱；与地平线星空 Starry 6P 同类竞品竞争
- **自研编译器**：计算流程图为核心，针对 M100 异构计算单元优化
- **存储带宽短板**：M100 的 273GB/s 对比特斯拉 AI5 的 819GB/s 差距明显，国产芯片在存储带宽上普遍受成本约束

## My Position

## Contradictions

- [[sources/li-auto-mach-m100-deep-dive]] 对比 Thor-U 仅在 UniAD 场景（低算力需求）下测试，不能代表所有工况；实际高算力任务中 Thor-U 可能仍有优势

## Sources

- [[sources/li-auto-mach-m100-deep-dive]]
- [[sources/li-auto-m100-paper-translation]]

## Evolution Log

- 2026-04-25（1 sources）：概念初建，来源为理想M100深度剖析文章；确立"AI TOPS已无关紧要，编排调度和标量/矢量能力才是核心"的新范式认知
- 2026-04-25（2 sources）：强化——论文全文翻译来源与现有定义一致（内容为图片，无增量内容）
