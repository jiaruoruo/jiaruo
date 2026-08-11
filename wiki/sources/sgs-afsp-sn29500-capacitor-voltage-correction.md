---
type: source
title: "SGS AFSP Day 3 — SN 29500-4: Capacitor Voltage Derating Factor πU"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, hardware-metrics, capacitor, pi-u, voltage-derating, component-reliability]
raw_file: raw/工作/personal/考试资料/0188_001.pdf
raw_sha256: b04cd4470c97d7e85f4a77defcfe9b77f1e1d9706b73b7e3f3bd5b6dd30e55bf
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — SN 29500-4: Capacitor Voltage Derating Factor πU

## Summary

本页为 SGS TÜV Saar ISO 26262 AFSP Day 3 硬件分析环节引用的 **SN 29500-4:2004-03** 第 7 页（Table 5）。该表给出电容器在不同电压比 U/Umax 下的电压修正因子 πU，以及对应各类电容的模型常数 C2、C3，用于将参考失效率 λref 修正到实际工作电压条件。

## Key Points

- **标准**：SN 29500-4:2004-03，Table 5 — *Constants and factor πU for capacitors*。
- **输入变量**：实际工作电压与最大额定电压之比 U/Umax，范围 0.1–1.0。
- **πU 特性**：
  - 电压比越低（降额越大），πU 越小，失效率越低。
  - U/Umax = 0.5 时多数类型 πU ≈ 1（参考点）。
  - U/Umax = 1.0 时 πU 可达 1.7–154，取决于电容类型（电解类尤其敏感）。
- **典型 πU（U/Umax = 1.0）示例**：
  - 纸/金属化膜/聚苯乙烯类：6.1–11
  - 陶瓷/玻璃/云母：5–7.4
  - 铝电解（液体/固体）：1.7 / 1.5
  - 钽电解（液体/固体）：154 / 56（对过电压极敏感）
- **模型常数 C2、C3**：表中给出每类电容的常数，用于通过公式（通常为指数/幂律形式）计算任意电压比下的 πU。
- **考试关联**：在 PMHF 计算题中，若电容实际工作电压低于额定电压，需用 πU 对 FIT 进行修正；钽电解电容的高 πU 是常见失效率放大来源。

## Concepts Extracted

- [[functional-safety]]
- [[sn29500]]
- [[fit-rate]]
- capacitor
- πU
- voltage derating
- [[hardware-metrics]]
- [[component-reliability]]
- [[pmhf]]

## Entities Extracted

- sgs-tuv-saar
