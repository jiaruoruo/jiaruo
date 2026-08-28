---
type: concept
date: 2026-08-28
updated: 2026-08-28
title: "具身大脑算力平台"
aliases:
  - "具身大脑算力平台"
  - "Robot Brain Compute Platform"
  - "robot-brain-compute-platform"
  - "机器人大脑"
tags:
  - embodied-ai
  - edge-ai
source_count: 15
confidence: low
domain_volatility: high
last_reviewed: 2026-08-28
domains: [embodied-ai]
---

# 具身大脑算力平台（Robot Brain Compute Platform）

## Definition

具身大脑算力平台（Robot Brain Compute Platform）是指专为机器人本体或近端部署设计的嵌入式 AI 推理/控制计算模块，承担感知融合、运动控制、任务规划等核心算力任务。区别于数据中心 GPU，具身大脑强调体积紧凑、低功耗、多接口（CAN FD / EtherCAT / GMSL / USB3.0）与实时性（硬实时内核、亚微秒中断响应）。

## Key Points

- **典型算力范围**：50–2070 TFLOPS（覆盖紧凑型到旗舰级）
- **主流芯片平台**：NVIDIA Jetson Thor（T5/N5）、NVIDIA Orin X（双芯 ~500 TOPS ASIL-D）、NVIDIA DRIVE Orin-X（单芯 254 TOPS）
- **形态分类**：
  - 本体嵌入型（N5/T5）：随机器人移动，强调功耗与体积
  - 背包外挂型（B5）：外挂补充算力，灵活部署
  - 高性能域控型（大算力，多 I/O）：工业/L4 自动驾驶
- **关键接口**：EtherCAT（伺服控制）、CAN FD（低速 I/O）、GMSL（摄像头）、Wi-Fi 7（无线）
- **实时性要求**：运动控制 ≥1 kHz（部分 2000 Hz）；亚微秒级中断响应（Xenomai RTOS）
- **代表厂商**：[[mscape-tech]]（N1000 / N201 / N210 / T40）、[[xyz-eai]]（N5 / T5 / B5）、[[jiushi-autonomous]]（双 Orin X）、[[neolix]]（DRIVE Orin-X）、[[whiterhino]]（经纬恒润域控）

## My Position

具身大脑算力是 [[embodied-ai]] 落地的硬件基础，当前市场仍处于早期分化阶段（GPU 通吃 vs 专用 SoC vs 自研芯片路线未定），NVIDIA Orin/Thor 凭借 CUDA 生态占据主流，但功耗和成本压力将驱动专用 SoC 进入。

## Contradictions

<!-- 暂无来源间明确分歧 -->

## Sources

- [[sources/mscape-tech-n1000-wheeled-arm-robot]]
- [[sources/mscape-tech-humanoid-robot-scenarios]]
- [[sources/mscape-tech-dexterous-hand-t40]]
- [[sources/mscape-tech-quadruped-robot-t41]]
- [[sources/mscape-tech-industrial-robot-n100-t40]]
- [[sources/mscape-tech-agv-n210]]
- [[sources/mscape-tech-uav-drone-t40]]
- [[sources/mscape-tech-forklift-n203-t200]]
- [[sources/mscape-tech-mining-truck-n210-n1000]]
- [[sources/mscape-tech-wheeled-arm-robot-multi-scenarios]]
- [[sources/xyz-eai-n5-compact-embodied-brain]]
- [[sources/xyz-eai-t5-domain-controller]]
- [[sources/xyz-eai-b5-brain-backpack]]
- [[sources/xyz-eai-embodied-brain-platform-overview]]
- [[sources/jiushi-autonomous-vehicle-brain-hardware]]

## Evolution Log

- 2026-08-28（15 sources）：概念初建，来源为灵境智源（10 个场景页）与星源智能（4 个产品页）、九识智能大脑方案
