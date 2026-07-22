---
type: concept
title: "Item Definition（项目定义）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - item-definition
source_count: 1
confidence: low
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "Item Definition"
  - "项目定义"
  - "Item Definition 项目定义"
---

# Item Definition（项目定义）

## Definition

Item Definition 是 ISO 26262-3:2018 概念阶段的起点，指对待开发系统（item）的功能、边界、运行环境、法规约束及外部风险降低措施进行完整描述。其输出是后续 HARA（危害分析与风险评估）的前置输入，也是安全生命周期中所有后续活动（FSC、TSC、HW/SW 安全需求）的参照基线。

## Key Points

- **核心内容**：功能描述、功能框图、与非安全相关元素的交互、环境条件、法规与标准、外部措施。
- **与 HARA 的关系**：Item Definition 提供 item 的边界与运行场景，HARA 在此基础上识别危害事件并评定 ASIL。
- **与 FSC/TSC 的关系**：FSC 把安全目标（Safety Goal）展开为功能安全需求；TSC 进一步把 FSC 细化为技术安全需求并分配到系统/硬件/软件。
- **外部措施**：不属于 ISO 26262 内部安全机制，但会影响 S/E/C 评估（如驾驶员可控性、被动安全系统）。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/sgs-afsp-day1-item-definition-purpose-function]]

## Evolution Log

- 2026-07-22（1 source）：基于 SGS TÜV Saar AFSP Day 1 培训案例建立，与 functional-safety 概念页互补。
