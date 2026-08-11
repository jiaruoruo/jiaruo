---
type: source
title: "端侧 AI 的不可能三角：延迟、内存、精度"
date: 2026-06-14
source_url: "https://mp.weixin.qq.com/s/SB_HVQdcNre4w-xoCV9pPQ"
domain: "mp.weixin.qq.com"
author: "AIPlayer"
tags:
  - edge-ai
  - on-device
  - llm-inference
  - quantization
processed: true
raw_file: raw/工作/clippings/AI/2026-06-14端侧 AI 的不可能三角：延迟、内存、精度.md
raw_sha256: 301b2b2f9b8605a60f4ee7ae009f060eff44bf1d72c0067e659cd4e488743c78
last_verified: 2026-06-14
possibly_outdated: false
language: "zh"
---

# 端侧 AI 的不可能三角：延迟、内存、精度

## Summary

拆解端侧 AI 部署的「不可能三角」：低延迟、小内存、高精度三者不可兼得，保住任意两个第三个必受损。这是物理规律（内存带宽/算力/功耗上限）而非某模型局限。系统讲解量化、推测解码、KV Cache 管理三类优化的本质与代价。

## Key Points

- 不可能三角：低延迟（首 token<100ms、>20 tok/s）/ 小内存（手机 2–4GB）/ 高精度，三选二
- 瓶颈是内存带宽而非 FLOPS：自回归每步都要把全部权重从内存搬到计算单元，最大吞吐≈内存带宽/权重大小（Memory-Bound）
- 量化：BF16→INT8（损失 1–3%）→INT4（损失 3–8%）；MoE 架构比 Dense 更抗量化（见 [[mixture-of-experts]]）
- 推测解码：小 draft 模型预猜 N token，大 target 模型一次性验证，用额外内存换延迟
- KV Cache 管理是第三类优化；方案选择取决于任务对精度的容忍度（见 [[edge-ai]]）

## Concepts Extracted

- [[edge-ai]]
- [[mixture-of-experts]]

## Entities Extracted

<!-- 无 -->

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
