---
type: source
title: "SN 29500-3 Page 5 — Failure Rates for Diodes & Power Semiconductors"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "Siemens / SN 29500-3:2004-12"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, fit-rate, diodes, power-semiconductors]
raw_file: raw/工作/personal/考试资料/0184_001.pdf
raw_sha256: faacd28661cd76930ff3e2751687adf413d53cf3327b470fc53f5b8ed5b70785
last_verified: 2026-07-22
language: en
---

# SN 29500-3 Page 5 — Failure Rates for Diodes & Power Semiconductors

## Summary

本页为 **SN 29500-3:2004-12** 第 5 页，给出二极管与功率半导体在参考条件下的期望失效率（λ_ref）。表格为德英双语，涵盖通用二极管、肖特基二极管、稳压/限幅二极管、整流二极管、晶闸管、Triac、专用功率半导体等。

## Key Points

- **Table 2：二极管 FIT 示例**
  - Universal / Schottky diode：1 FIT（θ=55°C）
  - Limiting diode (suppressor)：7 FIT（θ=40°C）
  - Z-diode small signal：1 FIT；power：25 FIT
  - Microwave diode small signal：5–20 FIT；power：50–500 FIT
- **Table 3：功率半导体 FIT 示例**
  - Rectifier diodes：2 FIT（θ=70°C）
  - Rectifier bridges：10 FIT
  - Schottky diodes：10 FIT
  - Thyristors：50 FIT
  - Triacs / Diacs：75 FIT
- **备注**：裸芯片（bare chips）若无足够经验，FIT 需至少乘以 2。
- **考试关联**：ISO 26262 PMHF 计算需正确选用二极管/功率半导体基础 FIT，并考虑温度修正。

## Concepts Extracted

- [[functional-safety]]
- sn29500
- fit-rate
- diode-failure-rate
- power-semiconductor

## Entities Extracted

- siemens
