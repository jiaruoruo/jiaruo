---
type: concept
title: "FSC（功能安全概念）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - fsc
source_count: 1
confidence: low
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "FSC"
  - "Functional Safety Concept"
  - "功能安全概念"
---

# FSC（功能安全概念）

## Definition

FSC（Functional Safety Concept）是 ISO 26262-3:2018 中把 Safety Goal 细化为功能安全需求（FSR, Functional Safety Requirement）并分配到系统架构要素的过程。它在概念阶段完成，关注“功能层面需要做什么来保证安全”，而不涉及具体的技术实现。

## Key Points

- **输入**：Safety Goal 及其 ASIL 等级，来自 HARA。
- **输出**：功能安全需求（FSR），通常包含 safe state、FTTI（故障容错时间间隔）、warning/degradation concept、冗余与诊断要求等属性。
- **与 TSC 的关系**：FSC 是功能层抽象，TSC（Technical Safety Concept）在 ISO 26262-4 中把 FSR 进一步细化为技术安全需求并分配到硬件/软件。
- **安全机制类型**：FSC 阶段初步确定需要的安全机制类型，如监控、冗余、诊断、降级等。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/sgs-afsp-day1-item-definition-purpose-function]]

## Evolution Log

- 2026-07-22（1 source）：基于 SGS TÜV Saar AFSP Day 2 FSC 练习建立。
