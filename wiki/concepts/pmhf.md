---
type: concept
title: "PMHF（硬件失效概率度量）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - pmhf
  - hardware-metrics
source_count: 5
confidence: medium
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "PMHF"
  - "Probabilistic Metric for Hardware Failures"
  - "硬件失效概率度量"
---

# PMHF（硬件失效概率度量）

## Definition

PMHF（Probabilistic Metric for Hardware Failures）是 ISO 26262-5 定义的随机硬件失效率概率指标，用于量化 item 中残余硬件失效导致违反安全目标的平均风险。PMHF 通常以 FIT（Failures In Time）表示，不同 ASIL 等级有相应的目标阈值。

## Key Points

- **计算基础**：各元器件 FIT 经故障模式分布、诊断覆盖率（DC）、安全机制、共因失效等修正后的累加。
- **与 SPFM/LFM 的关系**：
  - SPFM 衡量单点故障覆盖。
  - LFM 衡量潜伏故障覆盖。
  - PMHF 是最终的概率化风险指标。
- **目标阈值**：ASIL-D 通常要求 PMHF < 10 FIT；ASIL-B/C 通常 < 100 FIT（具体依项目安全目标）。
- **数据来源**：SN 29500、IEC 61709、元器件手册、实测现场返回数据。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/sgs-afsp-day3-hw-analysis-bom-fault-rates]]
- [[sources/sgs-afsp-day3-hw-analysis-safety-mechanisms-dc]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p6]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p7]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]

## Evolution Log

- 2026-07-22（5 sources）：基于 SGS TÜV Saar AFSP Day 3 PMHF 计算练习建立。
