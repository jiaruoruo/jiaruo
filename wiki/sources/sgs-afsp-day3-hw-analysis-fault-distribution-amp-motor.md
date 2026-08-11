---
type: source
title: "SGS AFSP Day 3 — HW Analysis Exercise Page 4: Fault Distribution for Amplifier & Motor"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hardware-analysis, failure-modes, fault-distribution]
raw_file: raw/工作/personal/考试资料/0178_001.pdf
raw_sha256: 1d156ea9ddd6d48fea5d803d3acc0c6dbfbf51abae9adc98ce2f57c72c9136ba
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — HW Analysis Exercise Page 4: Fault Distribution for Amplifier & Motor

## Summary

本页为 SGS AFSP Day 3 HW Analysis 练习 8 页材料中的第 4 页，继续按 Birolini 方法给出 **双差分放大器（AMP）与电机（Motor）** 的故障模式分布。放大器列出各引脚间短路（short circuits）的分布；电机列出 Break、Short circuit of coil、High transition resistance、Intermittent operation 等失效模式分布。

## Key Points

- **AMP（Dual Differential Amplifier）故障模式**：
  - 各引脚对（NC-XXX、IN-GND、IN-IN、IN-Out、OUT-GND 等）short 分布，多数 2%
  - Functional faults（wrong amplifying、internal stuck at oscillation、offset）占 9% 等
- **Motor 故障模式**：
  - Break（线圈开路）：25%
  - Short circuit of the coil：25%
  - High transition resistance on the commutator：25%
  - Intermittent operation：25%
- **假设**：Birolini 假设 75% 为短路、25% 为功能性故障（functional faults）。
- **考试关联**：复杂 IC 与执行器（电机）的故障模式分布是 PMHF 计算难点；需结合安全机制确定诊断覆盖率。

## Concepts Extracted

- [[functional-safety]]
- hardware-analysis
- failure-mode-distribution
- operational-amplifier-faults
- motor-faults

## Entities Extracted

- sgs-tuv-saar
