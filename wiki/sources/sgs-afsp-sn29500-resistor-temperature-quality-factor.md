---
type: source
title: "SGS AFSP Day 3 — SN 29500-4: Resistor/Inductor πT and Capacitor Quality Factor πQ"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, hardware-metrics, resistor, inductor, capacitor, pi-t, pi-q, quality-factor, component-reliability]
raw_file: raw/工作/personal/考试资料/0190_001.pdf
raw_sha256: 5f856e3dbbf46003e715fe49c45df0a9ec34dae77dc4ee647a3df865cb2e0b4c
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — SN 29500-4: Resistor/Inductor πT and Capacitor Quality Factor πQ

## Summary

本页为 SGS TÜV Saar ISO 26262 AFSP Day 3 硬件分析环节引用的 **SN 29500-4:2004-03** 第 10 页。包含电阻器/电感器温度修正因子 πT（Table 7、Table 8）以及电容器质量等级修正因子 πQ（Table 9），是 FIT 修正与可靠性降额计算的最后一组关键参数。

## Key Points

- **4.2 Resistors / Inductors, Transformers**
  - **Table 7 — 温度依赖常数**：
    - 电阻器：A = 0.873，EA1 = 0.16 eV，EA2 = 0.44 eV，θU,ref = 40 °C
    - 电感器/变压器：A = 0.996，EA1 = 0.06 eV，EA2 = 1.13 eV，θU,ref = 40 °C
  - **Table 8 — Factor πT**：
    - 电阻器：θ1 = 55 °C 或 85 °C；θ2 从 25 °C 到 125 °C
      - θ1 = 55 °C 时，πT 在 25 °C 为 0.49，125 °C 为 5.1
      - θ1 = 85 °C 时，πT 在 25 °C 为 0.25，125 °C 为 2.6
    - 电感器/变压器：θ1 = 55/60/85 °C；高温下 πT 可达 29（θ1=55, θ2=125）
- **4.3 Quality factor for capacitors, factor πQ**
  - **Table 9 — 电容器质量等级 πQ**：
    - 等级 LL（Long Life / 封装/长寿命型）：πQ = 1
    - 等级 GP（General Purpose / 通用型/非封装型）：πQ = 2
    - 覆盖金属化膜、聚苯乙烯、聚丙烯、铝电解等类型
    - 脚注说明：LL 对铝电解指 Long Life Grade；对薄膜电容指 encapsulated components；GP 指 General Purpose Grade 或非封装型。
- **考试关联**：
  - 电阻/电感在高温工作环境下需查 Table 8 修正 πT。
  - 电容的 πQ 在 1–2 之间，直接影响 PMHF 结果；选择 LL 等级器件可使失效率减半。
  - 与 πT、πU 共同构成 SN 29500 的完整修正链：λ = λref × πT × πU × πQ（电容）或 λ = λref × πT（电阻/电感）。

## Concepts Extracted

- [[functional-safety]]
- [[sn29500]]
- [[fit-rate]]
- resistor
- inductor
- capacitor
- πT
- πQ
- quality factor
- [[hardware-metrics]]
- [[component-reliability]]
- [[pmhf]]

## Entities Extracted

- sgs-tuv-saar
