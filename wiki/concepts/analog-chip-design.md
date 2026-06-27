---
type: concept
title: "模拟芯片设计"
date: 2026-06-27
updated: 2026-06-27
tags:
  - analog
  - ic-design
  - chip
source_count: 2
confidence: low
domain_volatility: low
last_reviewed: 2026-06-27
aliases:
  - "模拟芯片设计"
  - "模拟电路设计"
  - "Analog Chip Design"
  - "analog-chip-design"
---

# 模拟芯片设计（Analog Chip Design）

## Definition

模拟芯片设计（Analog Chip Design）处理连续信号，涵盖放大器、稳压器、数据转换器、射频前端等电路设计。相比数字设计更依赖工程师经验与器件级权衡，常用 Cadence Virtuoso（见 [[cadence]]）等工具完成原理图、仿真与版图设计。电源管理 IC（见 [[power-management-ic]]）是其典型应用。

## Key Points

- 处理连续信号，依赖器件级精细权衡
- 典型电路：放大器、稳压器（LDO）、ADC/DAC、射频前端
- 主流工具：Cadence Virtuoso + Spectre 仿真 + Layout Editor
- 电源管理 IC（见 [[power-management-ic]]）为代表应用

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂未发现来源间分歧 -->

## Sources

- [[sources/chip-design-flow-cadence-virtuoso]]
- [[sources/ldo-chip-design-report-uestc-2015]]

## Evolution Log

- 2026-06-27（2 sources）：概念初建，从芯片设计/制造来源批量提取，消除 source 页断链
