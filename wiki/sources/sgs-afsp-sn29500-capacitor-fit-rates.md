---
type: source
title: "SGS AFSP Day 3 — SN 29500-4: Capacitor Failure Rates (λref) under Reference Conditions"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, hardware-metrics, capacitor, fit-rate, component-reliability]
raw_file: "raw/personal/考试资料/0186_001.pdf"
raw_sha256: "b94703fb2a57b0ac5f0ccb0ed484b93646684a85995c22fb86adc78139af81d8"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — SN 29500-4: Capacitor Failure Rates (λref) under Reference Conditions

## Summary

本页为 SGS TÜV Saar ISO 26262 AFSP Day 3 硬件分析环节引用的 **SN 29500-4:2004-03** 第 4 页。该表给出各类电容器在参考条件下的基准失效率 λref（FIT），是计算 PMHF、SPFM/LFM 时进行硬件元器件失效率估算的基础数据来源之一。

## Key Points

- **标准**：SN 29500-4:2004-03，Table 1 — *Failure rates for capacitors*。
- **参考条件**：表中所列 λref 为在规定参考工况与整个批次范围内的预期值，温度参考值 θ1 与电压比 Uref/Umax 一并给出。
- **电容器类型与典型 λref（FIT）**：
  - 金属箔（Metal foil）/ 聚苯乙烯、聚丙烯、聚碳酸酯、聚对苯二甲酸乙二醇酯：1–2 FIT
  - 金属化膜（Metallized film）：0.7 FIT
  - 金属化纸（Metallized paper / film）：2 FIT
  - 云母（Mica）、玻璃（Glass）：1–2 FIT
  - 陶瓷（Ceramic）：1–5 FIT（COG/NPO 1 FIT；X7R/X5R 2 FIT；Z5U/Y5V/Y4T 5 FIT）
  - 铝电解（Aluminium electrolytic）：液体电解质 5 FIT，固体电解质 3 FIT
  - 钽电解（Tantalum electrolytic）：液体电解质 10 FIT，固体电解质 1 FIT
  - 可变电容器：10 FIT
- **温度/电压参考**：表中同时给出 θ1（°C）与 Uref/Umax，用于后续 πT、πU 修正。
- **考试关联**：SN 29500-4 的电容 FIT 表常与 Day 3 硬件分析中的 BOM/FIT 计算、故障分布、SPFM/LFM/PMHF 计算题配套使用。

## Concepts Extracted

- [[functional-safety]]
- [[sn29500]]
- [[fit-rate]]
- capacitor
- [[hardware-metrics]]
- [[component-reliability]]
- [[pmhf]]
- SPFM/LFM

## Entities Extracted

- sgs-tuv-saar
