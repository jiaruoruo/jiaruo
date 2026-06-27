---
type: concept
title: "边缘AI"
date: 2026-06-27
updated: 2026-06-27
tags:
  - edge-ai
  - tinyml
  - mcu
  - npu
  - on-device
source_count: 4
confidence: medium
domain_volatility: high
last_reviewed: 2026-06-27
aliases:
  - "边缘AI"
  - "端侧AI"
  - "Edge AI"
  - "On-device AI"
  - "TinyML"
---

# 边缘AI（Edge AI / On-device AI）

## Definition

边缘AI（Edge AI，又称端侧 AI、On-device AI）是指将神经网络推理直接部署到 MCU、小型 SoC、传感器节点等资源受限设备上本地运行，而非依赖云端。其驱动力是产品已不满足简单阈值判断、需要本地完成识别/异常检测/唤醒等任务；随着 NPU 成为嵌入式芯片标配，MCU 的角色正从「控制器」扩展为「现场判断节点」。边缘AI 的核心约束是「延迟、内存、精度」的不可能三角，主要优化手段为量化、剪枝、推测解码与 KV Cache 管理。

## Key Points

- **不可能三角**：低延迟、小内存、高精度三者不可兼得（保住其二、第三必受损），根源是端侧内存带宽/算力/功耗上限的物理规律。
- **瓶颈是内存带宽而非算力**：自回归推理每步都要把全部权重从内存搬到计算单元，最大吞吐≈内存带宽/权重大小（Memory-Bound）。
- **核心优化**：量化（BF16→INT8 损失 1–3%、→INT4 损失 3–8%；MoE 比 Dense 更抗量化，见 [[mixture-of-experts]]）、推测解码、KV Cache 压缩。
- **硬件趋势**：NPU 进入 MCU/无线/视觉/语音芯片（ST STM32N6 含 Neural-ART、NXP MCX N 含 eIQ Neutron、ESP32-S3 用向量指令）；把矩阵/卷积/激活从主控核搬到 NPU。
- **对 MCU 工程师的影响**：从「控制外设」转向「组织数据流」、从「写业务判断」转向「管理推理结果」（去抖/窗口统计/降级策略），把 NPU 当异步硬件外设设计（见 [[embedded-system]]）。
- **TinyML 基础**：张量/shape、神经元/权重/激活、网络层选型（嵌入式需控参数膨胀）、量化敏感度判断是端侧落地的必备知识。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂未发现来源间分歧 -->

## Sources

- [[sources/npu-embedded-mcu-trend]]
- [[sources/mcu-on-device-ai-inference]]
- [[sources/tinyml-neural-network-basics]]
- [[sources/on-device-ai-impossible-triangle]]

## Evolution Log

- 2026-06-27（4 sources）：概念初建（补全 stub 时从 4 篇边缘AI/MCU 来源提炼）。涵盖不可能三角、Memory-Bound 瓶颈、量化/推测解码、NPU 进 MCU 趋势、MCU 工程师能力迁移；confidence 设为 medium，domain_volatility 设为 high（技术演进快）。
