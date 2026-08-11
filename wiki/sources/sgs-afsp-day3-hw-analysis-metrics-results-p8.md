---
type: source
title: "SGS AFSP Day 3 — HW Analysis Exercise Page 8: Architectural Metrics & PMHF Results"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hardware-analysis, spfm, lfm, pmhf]
raw_file: raw/工作/personal/考试资料/0182_001.pdf
raw_sha256: a8c504efb2624e2aaaad61d124bc465f4a7f741e7682ad1159997da04d7e89d2
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — HW Analysis Exercise Page 8: Architectural Metrics & PMHF Results

## Summary

本页为 SGS AFSP Day 3 HW Analysis 练习 8 页材料中的第 8 页（末页），汇总给出 **SPFM、LFM、PMHF 的计算公式与结果**，并提及 Failure Rate Classes（FRC）检查。

## Key Points

- **SPFM（Single-Point Fault Metric）**：
  - 公式：SPFM = 1 − Σ(λ_SP + λ_RF) / Σλ
  - 结果：**SPFM = 0.87**（即 87%）
- **LFM（Latent-Fault Metric）**：
  - 公式：LFM = 1 − Σλ_LF / (Σλ_LF + Σλ_MP)
  - 结果：**LFM = 0.74**（即 74%）
- **PMHF（Probabilistic Metric for random Hardware Failures）**：
  - 公式：PMHF = Σλ_SP + Σλ_RF + Σλ_MP × λ_LF × T_lifetime
  - 结果：**PMHF ≈ 29.29**（单位：FIT）
  - 分解：PMHF_est = 0.74 + 0.13 + 29.01 × T_lifetime
- **Failure Rate Classes（FRC）**：作为替代方法，按 ISO 26262-5 Table 8/9/10 检查要求。
- **考试关联**：AFSP 必考指标——需熟记 ASIL 对应目标值与公式；注意本例为训练示例，实际项目需用真实 FIT 与 DC。

## Concepts Extracted

- [[functional-safety]]
- hardware-analysis
- spfm
- lfm
- pmhf
- failure-rate-classes

## Entities Extracted

- sgs-tuv-saar
