---
type: concept
title: "TSC（技术安全概念）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - tsc
source_count: 1
confidence: low
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "TSC"
  - "Technical Safety Concept"
  - "技术安全概念"
---

# TSC（技术安全概念）

## Definition

TSC（Technical Safety Concept）是 ISO 26262-4:2018 中的核心活动，把 FSC 输出的功能安全需求（FSR）转化为技术安全需求（TSR），并分配到系统架构、硬件要素和软件要素。TSC 是功能安全从“做什么”到“怎么做”的桥梁。

## Key Points

- **输入**：FSC 的功能安全需求（FSR）与系统架构草案。
- **输出**：技术安全需求（TSR），包括系统级需求（SYSR）、系统要素级需求（SYSELR）、硬件/软件分配。
- **系统级设计**：定义系统架构、接口、安全机制、故障检测与响应策略。
- **HW/SW 分配**：将 TSR 分配到硬件和软件，并确保硬件度量（SPFM/LFM/PMHF）与软件架构度量可达标。
- **与 FSC 的关系**：FSC 回答“功能上如何安全”，TSC 回答“技术上如何实现并验证安全”。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/sgs-afsp-day1-item-definition-purpose-function]]

## Evolution Log

- 2026-07-22（1 source）：基于 SGS TÜV Saar AFSP Day 2 TSC 练习建立。
