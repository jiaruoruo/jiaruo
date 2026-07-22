---
type: concept
title: "硬件架构度量（SPFM / LFM / PMHF）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - hardware-metrics
source_count: 5
confidence: medium
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "Hardware Metrics"
  - "硬件架构度量"
  - "SPFM"
  - "LFM"
  - "Single-Point Fault Metric"
  - "Latent-Fault Metric"
  - "随机硬件指标"
---

# 硬件架构度量（SPFM / LFM / PMHF）

## Definition

硬件架构度量是 ISO 26262-5 用于量化随机硬件失效风险的三个核心指标：

- **SPFM（Single-Point Fault Metric）**：单点故障度量，衡量系统对单点故障的诊断覆盖能力。
- **LFM（Latent-Fault Metric）**：潜伏故障度量，衡量系统对双点故障中第一个故障的诊断覆盖能力。
- **PMHF（Probabilistic Metric for Hardware Failures）**：硬件失效概率度量，量化系统每小时的残余硬件失效率。

不同 ASIL 等级对这些指标有明确的阈值要求。

## Key Points

- **SPFM（单点故障度量）**：关注未被安全机制覆盖的单点故障比例；目标阈值由 [[asil]] 等级驱动，ASIL-D 通常要求 ≥ 99%。
- **LFM（潜伏故障度量）**：关注双点故障中第一个故障未被检测到的比例；ASIL-D 通常要求 ≥ 90%。
- **PMHF（硬件失效概率度量）**：以 FIT 为单位累加残余失效率；ASIL-D 通常要求 < 10 FIT（具体目标值依项目而定）。独立概念页见 [[pmhf]]。
- **计算链路**：BOM/FIT（见 [[fit-rate]]）→ 故障模式分布 → 安全机制与 DC → 单点/残余/潜伏故障分类 → SPFM/LFM/PMHF。
- **与 SN 29500 的关系**：元器件基准 FIT 及 πT/πU/πQ 修正因子（见 [[sn29500]]）是 PMHF 计算的输入；具体查表见 SN 29500 系列源页。
- **SPFM/LFM 合并说明**：二者作为本页的一级小节承载（非独立概念页），以消除「高频提及却无节点」的盲区；相关 wikilink 经本页 aliases 解析。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/sgs-afsp-day3-hw-analysis-bom-fault-rates]]
- [[sources/sgs-afsp-day3-hw-analysis-fault-distribution-components]]
- [[sources/sgs-afsp-day3-hw-analysis-safety-mechanisms-dc]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p6]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]

## Evolution Log

- 2026-07-22（5 sources）：基于 SGS TÜV Saar AFSP Day 3 硬件分析练习建立。
- 2026-07-22（REFLECT 盲区消解）：将 SPFM / LFM 作为本页一级小节正式承载并加入 aliases（Single-Point Fault Metric / Latent-Fault Metric），使二者可解析、消盲区；补强与 [[asil]] / [[pmhf]] / [[sn29500]] / [[fit-rate]] 的交叉链接。source_count 维持 5（结构性合并，未新增来源）。
