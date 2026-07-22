---
type: concept
title: "ASIL（汽车安全完整性等级）"
date: 2026-07-22
updated: 2026-07-22
tags:
  - functional-safety
  - iso-26262
  - automotive-eea
  - asil
  - automotive
source_count: 13
confidence: medium
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "ASIL"
  - "Automotive Safety Integrity Level"
  - "汽车安全完整性等级"
---

# ASIL（汽车安全完整性等级，Automotive Safety Integrity Level）

## Definition

ASIL 是 ISO 26262 中基于**危险分析与风险评估（HARA）**为安全目标分配的风险等级，由**严重度 S、暴露概率 E、可控性 C** 三个维度组合确定，分为 **A（最低）→ B → C → D（最高）** 四级，并含 **QM（质量管理，无功能安全要求）**。ASIL 是贯穿功能安全生命周期的统一需求标尺：从概念阶段的 HARA 定级，到系统/硬件/软件各阶段的架构、流程与随机硬件度量目标，均由 ASIL 等级驱动。

## Key Points

- **S/E/C 三维定级（ISO 26262-3）**：S（危害后果严重度，S0–S3）、E（运行场景暴露概率，E0–E4）、C（驾驶员或其他措施对危害的控制能力，C0–C3）；三者组合经标准查表得到 ASIL A/B/C/D 或 QM。定级必须有明确的 S/E/C 枚举依据，而非主观判断（见 [[sources/sgs-afsp-day1-hara-exercise-p1]]）。
- **安全目标 → 需求链**：HARA 导出带 ASIL 的**安全目标（Safety Goal）**，再经 FSC 分解为 FSR、经 TSC 分配为系统/软硬件安全需求（见 [[fsc]]、[[tsc]]、[[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]）。
- **ASIL 分解（ISO 26262-9）**：将高 ASIL 需求分解为两个低 ASIL 冗余要素（如 ASIL-D = ASIL-B(D) + ASIL-B(D)），前提是要素间满足**独立性**、无相关失效（DFA）。
- **与随机硬件指标挂钩（ISO 26262-5）**：不同 ASIL 对 SPFM/LFM/PMHF 有显式阈值（典型：ASIL-D 要求 SPFM ≥ 99%、LFM ≥ 90%、PMHF < 10 FIT）。详见 [[hardware-metrics]]、[[pmhf]]。
- **对 MCULess 的硬约束**：ASIL-D 安全关键域（制动/转向/气囊）要求本地降级 Fallback，**必须保留 MCU**，禁止 MCULess；ASIL-B 简单域（车身/车灯/智能电源）可接受 MCULess + Limp-Home（见 [[mculess-architecture]]、[[functional-safety]]）。
- **ASIL vs AEC-Q**：ASIL 是**功能安全完整性**等级（方法学/流程），AEC-Q100 是**器件可靠性**认证（温度 Grade），维度不同、常并列标注。
- **GB/T 34590 对应**：与 ISO 26262 同套 ASIL 定级方法；本库国标文件为征求意见稿，引用时需注意版本时效（见 [[gbt-34590]]）。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂无来源间分歧；ASIL 定级方法在 ISO 26262 与 GB/T 34590 中同源一致，差异仅可能在征求意见稿条文层面 -->

## Sources

- [[sources/iso-26262-1-2018]]
- [[sources/iso-26262-2-2018]]
- [[sources/iso-26262-3-2018]]
- [[sources/iso-26262-4-2018]]
- [[sources/iso-26262-5-2018]]
- [[sources/iso-26262-9-2018]]
- [[sources/gbt-34590-1-draft]]
- [[sources/gbt-34590-3-draft]]
- [[sources/gbt-34590-4-draft]]
- [[sources/gbt-34590-5-draft]]
- [[sources/gbt-34590-9-draft]]
- [[sources/sgs-afsp-day1-hara-exercise-p1]]
- [[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]

## Evolution Log

- 2026-07-22（13 sources）：从 `functional-safety` 析出为独立概念页（原 ASIL 仅作父概念子项，盲区扫描显示其在 62 个文件中被提及却无专属节点）。涵盖 S/E/C 三维定级、安全目标→需求链、ASIL 分解、与随机硬件指标/MCULess 边界的挂钩；置信度 medium（标准 + 培训交叉，但培训为单一机构）。
