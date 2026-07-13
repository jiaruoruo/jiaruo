---
type: concept
title: "神经形态计算"
date: 2026-07-13
updated: 2026-07-13
tags:
  - neuromorphic
  - edge-ai
  - spiking-neural-network
  - robotics
  - photonics
source_count: 1
confidence: low
domain_volatility: high
last_reviewed: 2026-07-13
aliases:
  - "神经形态计算"
  - "Neuromorphic Computing"
  - "neuromorphic-computing"
  - "类脑计算"
  - "脉冲神经网络"
---

# 神经形态计算（Neuromorphic Computing）

## Definition

神经形态计算是一类受生物神经系统启发的计算架构，以脉冲编码（Spiking Neural Network, SNN）和事件驱动方式实现感知运动表示，为机器人等边缘场景提供数量级能效提升。路线图（Christensen 2026）将其列为下一代计算趋势与 Layer1 神经形态控制策略方向。

## Key Points

- **代表硬件**：Intel Loihi 2、IBM NorthPole（脉冲编码感觉运动表示，数量级能效提升）
- **机器人应用**：神经形态视觉传感器（DVS 事件相机）产生异步微秒级事件流，适用于快速操作与运动控制；神经形态控制策略路线图里程碑 2029 能效反射控制→2033 全回路脉冲神经网络
- **关联方向**：边缘 AI（机器人本体实时推理）、光子计算（5-10 年展望，为 Transformer 推理提供 teraOPS 吞吐量）、量子优化（多机器人路径规划，2025 TRL 2-3）
- **路线图定位**：下一代计算趋势三大支柱之一（与边缘 AI、光子并列），属 Layer1 算法与 AI 的远期能力

## My Position

- 与 [[edge-ai]]、[[robotics-roadmap-2025-2035]]（Layer1/Layer3）关联。神经形态是机器人本体低功耗实时控制的长期技术储备。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/global-robotics-roadmap-2025-2035]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Christensen 全球机器人路线图计算基础设施与 Layer1 神经形态控制章节
