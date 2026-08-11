---
type: source
title: "SN 29500-3 Page 9 — Temperature Correction Factors (π_T)"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "Siemens / SN 29500-3:2004-12"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, fit-rate, temperature-derating]
raw_file: raw/工作/personal/考试资料/0185_001.pdf
raw_sha256: fdfc0900646e900d0b2f447c9d5ea86b5b83b84135542bf17c4cac4a1a63ee94
last_verified: 2026-07-22
language: en
---

# SN 29500-3 Page 9 — Temperature Correction Factors (π_T)

## Summary

本页为 **SN 29500-3:2004-12** 第 9 页，给出晶体管、二极管、功率半导体的 **温度修正因子 π_T**。表格横轴为参考结温 θ_j,1（°C），纵轴为实际工作结温，用于将参考 FIT 修正到实际工作温度下的 FIT。

## Key Points

- **修正逻辑**：λ_actual = λ_ref × π_T(θ_actual) / π_T(θ_ref)。
- **典型数值**：
  - 当 θ_ref = 55°C、θ_actual = 70°C 时，π_T 约 1.5–2
  - 当 θ_actual = 100°C 时，π_T 可升至 3–10 以上
- **两个子表**：
  - Table 7：晶体管、参考二极管、微波二极管的 π_T
  - Table 8：二极管（不含参考/微波二极管）与功率半导体的 π_T
- **考试关联**：ISO 26262 PMHF 计算必须考虑温度修正；高温会显著增加实际 FIT，是 ASIL 达标的关键设计约束。

## Concepts Extracted

- [[functional-safety]]
- sn29500
- fit-rate
- temperature-correction-factor
- derating

## Entities Extracted

- siemens
