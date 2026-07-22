---
type: concept
title: "HARA（危害分析与风险评估）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - hara
source_count: 1
confidence: low
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "HARA"
  - "Hazard Analysis and Risk Assessment"
  - "危害分析与风险评估"
---

# HARA（危害分析与风险评估）

## Definition

HARA（Hazard Analysis and Risk Assessment）是 ISO 26262-3:2018 概念阶段的核心活动，用于识别 item 在运行过程中可能导致的危害事件，并按严重度（S, Severity）、暴露概率（E, Exposure）、可控性（C, Controllability）三个维度评定汽车安全完整性等级（ASIL）。其输出是 Safety Goal（安全目标）及对应的 ASIL 等级。

## Key Points

- **三维度评估**：
  - S（严重度）：危害对驾乘人员/道路使用者的伤害程度，S0–S3。
  - E（暴露概率）：危害事件发生的运行场景频率，E0–E4。
  - C（可控性）：驾驶员或其他道路使用者避免伤害的能力，C0–C3。
- **ASIL 定级**：由 S/E/C 组合查表得出，分为 QM、A、B、C、D 五级，D 最严苛。
- **输出**：每个危害事件对应一条或多条 Safety Goal，必要时通过 ASIL 分解降低单一要素的等级。
- **外部措施**：在 HARA 中可作为降低 C 或 E 评级的依据，但不属于 ISO 26262 内部安全要求。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/sgs-afsp-day1-item-definition-purpose-function]]

## Evolution Log

- 2026-07-22（1 source）：基于 SGS TÜV Saar AFSP Day 1 HARA 练习建立。
