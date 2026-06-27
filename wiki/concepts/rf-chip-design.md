---
type: concept
title: "射频芯片设计"
date: 2026-06-27
updated: 2026-06-27
tags:
  - rf
  - analog
  - ic-design
source_count: 1
confidence: low
domain_volatility: low
last_reviewed: 2026-06-27
aliases:
  - "射频芯片设计"
  - "RF 设计"
  - "射频集成电路"
  - "RF Chip Design"
  - "rf-chip-design"
---

# 射频芯片设计（RF Chip Design）

## Definition

射频芯片设计（RF Chip Design）面向高频信号处理，涵盖收发器、功率放大器、低噪声放大器等电路。由于工艺偏差与温度漂移，射频芯片普遍需要校准（如 IQ 不平衡校准、DC 偏置校准、频率校准）以保证性能一致性。属于模拟芯片设计（见 [[analog-chip-design]]）的高频分支。

## Key Points

- 处理高频信号，含收发器/PA/LNA 等电路
- 关键技术：IQ 不平衡校准、DC 偏置校准、频率校准
- 校准用于补偿工艺偏差与温漂
- 属于模拟芯片设计（见 [[analog-chip-design]]）的高频分支

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂未发现来源间分歧 -->

## Sources

- [[sources/rf-chip-calibration-design-broadcom-2008]]

## Evolution Log

- 2026-06-27（1 sources）：概念初建，从芯片设计/制造来源批量提取，消除 source 页断链
