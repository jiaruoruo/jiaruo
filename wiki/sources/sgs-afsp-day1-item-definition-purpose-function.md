---
type: source
title: "SGS AFSP Day 1 — Training Example: Item Definition, Purpose and Function (Torque Demand)"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, item-definition, torque-demand, e-mobility, functional-block-diagram, training-example]
raw_file: "raw/personal/考试资料/FS_71_220_26_2336.pdf"
raw_sha256: "e02a37b88bde586c2ef25746ee4455c241d00c2de297be510899c886ab1d8943"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 1 — Training Example: Item Definition, Purpose and Function (Torque Demand)

## Summary

本页为 SGS TÜV Saar ISO 26262 AFSP Day 1 培训示例的 **Item Definition 第 1 页**（Seite 1 von 2）。文档定义了用于电动汽车的 “Torque Demand” 功能项，给出文档目的、功能描述与功能框图，是后续 HARA 与 FSC 分析的起点。与 [[sgs-afsp-day1-item-definition-context]]（第 2 页，环境条件/法规/外部措施）成对使用。

## Key Points

- **文档目的**：为安全生命周期后续活动建立正确假设，确保危害分析与风险评估在一致理解下展开。
- **功能项（Item）**：电动汽车中实现 **Torque Demand（转矩需求）** 功能。
- **功能描述**：
  - 驾驶员踩下加速踏板后，系统按请求由 E-motor 输出对应转矩。
  - 用于全球范围内的量产乘用车（serial passenger cars）。
  - 能量来源为 400 V 电池；系统需向驾驶员提示运行状态与故障信息。
- **功能框图**：
  - 输入：Driver torque request
  - 处理：Logic → Power Unit
  - 输出：E-motor
  - 辅助/交互：
    - Indication（to other item）— 来自 Logic 的指示信号
    - 400 V Battery → Power Unit
- **考试关联**：
  - Item Definition 是 ISO 26262-3:2018 概念阶段第一步，是 HARA 的输入。
  - 框图中的每个功能块在后续 FSC/TSC 中会被分解为技术安全需求与安全机制。
  - “Torque Demand” 是 SGS AFSP 培训中的经典案例背景，贯穿于 Day 1–Day 3 的练习题。

## Concepts Extracted

- [[functional-safety]]
- [[item-definition]]
- [[hara]]
- [[fsc]]
- [[tsc]]
- torque-demand
- e-mobility
- functional-block-diagram
- training-example

## Entities Extracted

- sgs-tuv-saar
