---
type: source
title: "SGS AFSP Day 3 — HW Analysis Exercise Page 2: BOM & Fault Rates (FIT)"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hardware-analysis, fit-rate, bom]
raw_file: raw/工作/personal/考试资料/0176_001.pdf
raw_sha256: 539eed3097882f904fd104b7f88bd4b041576ffa2c965c97ec16d00990b1d874
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — HW Analysis Exercise Page 2: BOM & Fault Rates (FIT)

## Summary

本页为 SGS AFSP Day 3 HW Analysis 练习 8 页材料中的第 2 页，给出示例电路的 **Bill of Materials（BOM）与故障率（FIT）表**。表格列出 7 个关键器件（R1/R2 分流电阻、T1 晶体管、K1 继电器、D1 二极管、IC1 运放、M 电机）的供应商、基础故障率、温度/电压/负载/环境等修正因子，以及最终使用故障率 FIT。

## Key Points

- **器件与基础 FIT 示例**：
  - R1 Shunt Resistor：SN29500，0.2 FIT
  - T1 Transistor：SN29500，60 FIT
  - K1 Relay：SN29500，30 FIT
  - IC1 AD8200：SN29500，3 FIT
  - M Motor：Supplier，50 FIT
- **修正因子**：温度（参考温度、工作温度）、电压、负载、环境、失效判据等；本例中多数修正因子取 1。
- **温度假设**：功率元件平均工作温度 70°C；环境温度每升高 10°C 有特定修正。
- **考试关联**：ISO 26262-5 硬件度量计算需从元器件 FIT 出发；FIT（Failures In Time，10⁹ 小时失效数）是 PMHF 与 SPFM/LFM 计算基础。

## Concepts Extracted

- [[functional-safety]]
- hardware-analysis
- fit-rate
- bom
- sn29500
- component-derating

## Entities Extracted

- sgs-tuv-saar
