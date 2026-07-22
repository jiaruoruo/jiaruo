---
type: concept
title: "FIT / 失效率"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - fit-rate
  - component-reliability
source_count: 5
confidence: medium
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "FIT"
  - "失效率"
  - "Failure In Time"
  - "Failure Rate"
---

# FIT / 失效率

## Definition

FIT（Failure In Time）是元器件失效率的常用单位，定义为每 10⁹ 小时运行时间内发生的失效次数。在汽车功能安全（ISO 26262-5）中，FIT 是计算硬件架构度量 SPFM、LFM、PMHF 的基础输入，通常来自 SN 29500、IEC 61709 或元器件厂商数据手册。

## Key Points

- **单位换算**：1 FIT = 1 次失效 / 10⁹ 小时 ≈ 1.14 × 10⁻⁴ 次失效 / 年（连续运行）。
- **基准失效率 λref**：在标准参考条件下（温度、电压、质量等级）查表得到的 FIT。
- **修正计算**：实际工作条件下需乘以修正因子，如 λ = λref × πT × πU × πQ（电容）。
- **与 PMHF 的关系**：PMHF（Probabilistic Metric for Hardware Failures）是各元器件 FIT 经故障分布、诊断覆盖率、安全机制修正后的累加指标。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/sgs-afsp-sn29500-capacitor-fit-rates]]
- [[sources/sgs-afsp-sn29500-resistor-inductor-passive-fit-rates]]
- [[sources/sgs-afsp-sn29500-capacitor-voltage-correction]]
- [[sources/sgs-afsp-sn29500-capacitor-temperature-correction]]
- [[sources/sgs-afsp-sn29500-resistor-temperature-quality-factor]]

## Evolution Log

- 2026-07-22（5 sources）：基于 SGS TÜV Saar AFSP Day 3 SN 29500 查表练习建立。
