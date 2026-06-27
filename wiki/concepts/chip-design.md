---
type: concept
title: "芯片设计"
date: 2026-06-27
updated: 2026-06-27
tags:
  - semiconductor
  - ic-design
  - chip
source_count: 10
confidence: medium
domain_volatility: low
last_reviewed: 2026-06-27
aliases:
  - "芯片设计"
  - "集成电路设计"
  - "IC 设计"
  - "Chip Design"
  - "chip-design"
---

# 芯片设计（Chip Design）

## Definition

芯片设计（Chip Design）是指将电路功能需求转化为可制造的集成电路版图的全过程，通常分为前端设计（需求定义、架构设计、RTL 设计、逻辑综合）与后端设计（布局布线、时序收敛、物理验证、流片）两大阶段。设计完成后交由晶圆厂制造，再经封装、测试形成成品芯片。

## Key Points

- 前端流程：需求定义 → 架构设计 → RTL 设计 → 逻辑综合 → 验证
- 后端流程：布局规划 → 布局布线 → 时序收敛 → 物理验证（DRC/LVS）→ 流片（Tape-out）
- 按信号类型分为数字设计、模拟设计（见 [[analog-chip-design]]）、射频设计（见 [[rf-chip-design]]）
- 依赖 EDA 工具链（见 [[eda-tools]]）完成各阶段自动化
- 后期变更通过 ECO（工程变更令）局部修改，避免全流程重做

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂未发现来源间分歧 -->

## Sources

- [[sources/chip-design-flow-cadence-virtuoso]]
- [[sources/chip-design-production-flow]]
- [[sources/chip-rd-process-overview-2014]]
- [[sources/eco-soc-chip-design-application]]
- [[sources/memory-chip-design-guide]]
- [[sources/mems-pressure-sensor-chip-design-2011]]
- [[sources/rf-chip-calibration-design-broadcom-2008]]
- [[sources/semiconductor-defects-glossary]]
- [[sources/vlsi-backend-design-018um]]
- [[sources/vlsi-low-power-design-analysis]]

## Evolution Log

- 2026-06-27（10 sources）：概念初建，从芯片设计/制造来源批量提取，消除 source 页断链
