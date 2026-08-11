---
type: source
title: "SN 29500-3 Page 4 — Failure Rates for Transistors (Reference FIT Table)"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "Siemens / SN 29500-3:2004-12"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, fit-rate, transistors]
raw_file: raw/工作/personal/考试资料/0183_001.pdf
raw_sha256: 3f5f323eebe2b7ab73531ed531bad866a533eee8664b7d1252e536902d295864
last_verified: 2026-07-22
language: en
---

# SN 29500-3 Page 4 — Failure Rates for Transistors (Reference FIT Table)

## Summary

本页为 **SN 29500-3:2004-12**（Siemens 标准，用于 ISO 26262 硬件 FIT 计算）第 4 页，给出晶体管在参考条件下的期望失效率（λ_ref，单位 FIT）与参考结温（θ_j,1）。表格为德英双语，涵盖双极型晶体管、晶体管阵列、FET、MOSFET、GaAs FET 等。

## Key Points

- **标准**：SN 29500-3:2004-12，ISO 26262 硬件随机失效计算常用参考数据源。
- **器件类型与参考 FIT 示例**：
  - Bipolar universal：3 FIT（θ=55°C）
  - Bipolar low power：20 FIT（θ=85°C）
  - Bipolar power：60 FIT（θ=100°C）
  - FET / MOS small signal：5 FIT
  - MOS power (SIPMOS)：60 FIT（θ=100°C）
  - MOSFET small signal：10 FIT；power：200 FIT
- **定义**：1 FIT = 10⁻⁹ /h（每 10⁹ 元件小时一次失效）。
- **考试关联**：AFSP 考试中可能要求根据器件类型查表选取基础 FIT，并结合温度、电压、负载等修正因子计算实际 FIT。

## Concepts Extracted

- [[functional-safety]]
- sn29500
- fit-rate
- transistor-failure-rate
- hardware-reliability

## Entities Extracted

- siemens
