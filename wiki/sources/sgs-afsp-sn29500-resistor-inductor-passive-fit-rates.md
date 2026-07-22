---
type: source
title: "SGS AFSP Day 3 — SN 29500-4: Resistor, Inductor and Other Passive Component Failure Rates"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, hardware-metrics, resistor, inductor, passive-component, fit-rate, component-reliability]
raw_file: "raw/personal/考试资料/0187_001.pdf"
raw_sha256: "f737b98fee7c8c09699c27850995e92a56072170c41339d71b77520705ce5a24"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — SN 29500-4: Resistor, Inductor and Other Passive Component Failure Rates

## Summary

本页为 SGS TÜV Saar ISO 26262 AFSP Day 3 硬件分析环节引用的 **SN 29500-4:2004-03** 第 5 页。该页给出电阻器、电感器/变压器以及其他无源元器件的基准失效率 λref（FIT），并给出对应的温度参考值 θ1，用于后续 πT 修正与硬件度量计算。

## Key Points

- **标准**：SN 29500-4:2004-03，包含 Table 2（Resistors）、Table 3（Inductors）、Table 4（Other passive components）。
- **Table 2 — 电阻器 λref（FIT）**：
  - 碳膜（Carbon film）≤100 kΩ：0.3 FIT；>100 kΩ：1 FIT
  - 金属膜（Metal film）：0.2 FIT
  - 电阻网络/薄膜电路（Networks / film circuits）：标准 0.1 FIT，定制 0.5 FIT
  - 金属氧化物（Metal-oxide）：5 FIT
  - 线绕（Wire-wound）：5 FIT
  - 可变电阻（Variable）：30 FIT
  - θ1 取值：55 °C（多数）、85 °C（金属氧化物/线绕）
- **Table 3 — 电感器/变压器 λref（FIT）**：
  - EMC 用电感器 ≤3 A：1.5 FIT；>3 A：3 FIT
  - 低频电感器/变压器 ≤25 kHz：3 FIT
  - 高频电感器/变压器 >25 kHz：5 FIT
  - 开关电源主变压器/电感器：10 FIT
  - θ1 取值：55–85 °C
- **Table 4 — 其他无源元器件 λref（FIT）**：
  - 压敏电阻（Varistors）：1
  - PTC 热敏电阻（测量/加热启动）：5
  - NTC 热敏电阻：3
  - 浪涌保护器（Surge arresters）：1
  - 陶瓷谐振器：5
  - 滤波器（Filters）：10
  - 声表面波滤波器（SAW）：20
  - 声表面波振荡器：30
  - 压控振荡器（VCO）：40
  - 压电元件/传感器：30
  - 晶体（Crystals）：15
  - 晶体振荡器：30–200 FIT（随补偿方式升高）
  - 穿心电容/滤波器：5
  - 熔断器（Fuses）：25 FIT
- **考试关联**：BOM 元器件 FIT 累加、单点/潜伏故障覆盖计算均以这些基准值为输入。

## Concepts Extracted

- [[functional-safety]]
- [[sn29500]]
- [[fit-rate]]
- resistor
- inductor
- passive component
- [[hardware-metrics]]
- [[component-reliability]]
- [[pmhf]]
- SPFM/LFM

## Entities Extracted

- sgs-tuv-saar
