---
type: source
title: "SGS AFSP Day 3 — HW Analysis Exercise Page 6: Metrics Calculation Table for SG1"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hardware-analysis, spfm, lfm, pmhf]
raw_file: raw/工作/personal/考试资料/0180_001.pdf
raw_sha256: 4c177da6d345083ea88a7bfb79727868e58e786c722fdfe97b6bb3e7ac5dd5a6
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — HW Analysis Exercise Page 6: Metrics Calculation Table for SG1

## Summary

本页为 SGS AFSP Day 3 HW Analysis 练习 8 页材料中的第 6 页，给出针对 **Safety Goal 1 "Unintended acceleration shall be avoided"** 的完整硬件架构度量计算大表。表格按元器件（R1、R2、T1、K1、D1、IC1、M 等）列出故障模式、FIT、安全机制、DC、单点/残余/潜伏故障贡献等，用于后续 SPFM、LFM、PMHF 计算。

## Key Points

- **分析对象**：Safety Goal 1（非预期加速需避免）。
- **表格维度**：Component / Failure mode distribution / Failure rate (FIT) / DC / Safety mechanism / Residual fault rate / Latent fault rate / Comments。
- **关键结果预告**：经本页与第 7 页汇总后，第 8 页给出 SPFM ≈ 0.87、LFM ≈ 0.74、PMHF ≈ 29.29 FIT（见 [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]）。
- **考试关联**：这是 ISO 26262-5 硬件架构度量的实操练习；AFSP 考试会要求理解 SPFM/LFM/PMHF 的计算逻辑与目标值（ASIL B：SPFM≥90% 或 80%，LFM≥60% 或 40%，PMHF≤100 FIT 等，依表 4/5/6）。
- **注意**：本页数据密集，为训练用计算表，部分数值可能为示例假设。

## Concepts Extracted

- [[functional-safety]]
- hardware-analysis
- spfm
- lfm
- pmhf
- residual-fault
- latent-fault

## Entities Extracted

- sgs-tuv-saar
