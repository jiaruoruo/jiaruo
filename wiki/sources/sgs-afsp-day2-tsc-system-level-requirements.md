---
type: source
title: "SGS AFSP Day 2 — TSC Exercise Page 2: Safety Requirements at System Level"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, technical-safety-concept, system-safety-requirements]
raw_file: raw/工作/personal/考试资料/0170_001.pdf
raw_sha256: 70f34c503dec2ca3dce1ec7258f601004ef590a1a9fd4bebb95251c24eb5b58c
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 2 — TSC Exercise Page 2: Safety Requirements at System Level

## Summary

本页为 SGS AFSP Day 2 TSC 练习 5 页材料中的第 2 页，给出 **Technical Safety Concept „System“ (Item)**。将 FSC 中的 FSR 细化为系统级安全要求 SYSR1–SYSR8，并分别映射到 HW 架构指标（SYSR10–SYSR11）与随机硬件故障概率指标 PMHF（SYSR20）。页面为表格模板，含已填示例（如电机状态监测周期 <0.25s、电机电流比较周期 <0.25s，ASIL B）。

## Key Points

- **系统级要求编号**：SYSR1–SYSR8（由 FSR1–FSR6 导出）。
- **已填示例**：
  - SYSR1：电机状态需以 <0.25s 周期持续监测（对应 FSR1/FSR4，ASIL B）
  - SYSR2：电机电流需与期望值以 <0.25s 周期比较（ASIL B）
- **HW 架构指标**：SYSR10–SYSR11（单点/潜伏故障度量）。
- **PMHF**：SYSR20（随机硬件故障概率指标）。
- **考试关联**：系统级安全要求是 FSC→TSC 的细化；后续会再分配到 HW/SW 与系统元素。

## Concepts Extracted

- [[functional-safety]]
- technical-safety-concept
- system-safety-requirements
- hw-architectural-metrics
- pmhf

## Entities Extracted

- sgs-tuv-saar
