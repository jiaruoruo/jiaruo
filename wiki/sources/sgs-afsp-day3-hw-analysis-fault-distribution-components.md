---
type: source
title: "SGS AFSP Day 3 — HW Analysis Exercise Page 3: Fault Distribution by Component Type"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hardware-analysis, failure-modes, fault-distribution]
raw_file: "raw/personal/考试资料/0177_001.pdf"
raw_sha256: "9af8a705680fba15992af838393f1dfa15c831848af720d879d2a782bfe0a1d4"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — HW Analysis Exercise Page 3: Fault Distribution by Component Type

## Summary

本页为 SGS AFSP Day 3 HW Analysis 练习 8 页材料中的第 3 页，给出按 **Birolini** 方法的元器件故障模式分布。表格列出电阻（金属膜/绕线）、MOSFET、功率继电器、二极管等器件的 Open/Short/Drift 等失效模式及其百分比分布。

## Key Points

- **故障模式分布示例**：
  - 电阻 R-M（Metal Film）：Open 40%、Short 0%、Drift 0.5/2.0 等
  - 电阻 R-W（Wire-Wound）：Open 40%、Short 0%、Drift 0.5/2.0
  - T-M（Transistor-MOSFET）：Open/Short/Drift 分布
  - K-P（Power Relays）：Open 20%、Short (welded contacts) 80% 等
  - V-S（Diode Standard）：Open/Short/Change of limiting characteristics 等
- **用途**：将器件总 FIT 分解为具体故障模式 FIT，用于后续故障树/安全机制覆盖率计算。
- **考试关联**：AFSP 考试中需理解故障模式分布对 SPFM/LFM 和 PMHF 的贡献；不同器件类型的主导失效模式不同（如继电器熔焊为 Short，电阻多为 Open/Drift）。

## Concepts Extracted

- [[functional-safety]]
- hardware-analysis
- failure-mode-distribution
- birolini
- open-short-drift

## Entities Extracted

- sgs-tuv-saar
