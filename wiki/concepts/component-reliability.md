---
type: concept
title: "元器件可靠性（Component Reliability）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - component-reliability
source_count: 5
confidence: medium
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "Component Reliability"
  - "元器件可靠性"
  - "器件可靠性"
---

# 元器件可靠性（Component Reliability）

## Definition

元器件可靠性是指电子元器件在规定工作条件下、规定时间内完成规定功能的能力。在汽车功能安全（ISO 26262-5）语境下，元器件可靠性通常用失效率（FIT）量化，是 SPFM、LFM、PMHF 计算以及安全机制设计的底层输入。

## Key Points

- **失效率模型**：基准失效率 λref 结合温度、电压、质量等级等应力因子进行修正。
- **常用标准**：SN 29500、IEC 61709、MIL-HDBK-217、元器件厂商数据手册。
- **关键参数**：
  - 工作温度 θ2 与参考温度 θ1
  - 电压/电应力比 U/Umax
  - 质量等级（LL / GP 等）
- **与功能安全的关系**：高可靠性元器件可降低 PMHF；但仅靠降额和选型不能替代安全机制与诊断覆盖。

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
