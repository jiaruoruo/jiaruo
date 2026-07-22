---
type: synthesis
title: "ISO 26262 AFSP 复习指南：SGS TÜV Saar 培训课程案例全景"
date: 2026-07-22
tags:
  - automotive-eea
  - functional-safety
  - iso-26262
  - sgs-afsp
  - automotive
  - exam-prep
source_count: 36
confidence: medium
---

# ISO 26262 AFSP 复习指南：SGS TÜV Saar 培训课程案例全景

## Thesis

SGS TÜV Saar 的 ISO 26262 AFSP（Automotive Functional Safety Professional）培训课程案例，本质上是一套围绕 **ISO 26262 安全生命周期 Part 3 → Part 5** 的压缩映射：从 item 定义、HARA、安全目标与 FSC，到系统级 TSC、软硬件分配，再到硬件安全需求、硬件架构度量（SPFM/LFM/PMHF）与 SN 29500 元器件失效率计算。其复习价值不在于背诵单页表格，而在于把 **“功能安全是什么” 转化为 “每一步输出什么、输入什么、算式怎么列”** 的可操作 checklist。对备考者而言，Day 1 概念链、Day 2 需求链、Day 3 计算链是三条必须打通的主线；而重复扫描与多页表格恰恰说明这些基础数据需要被当作“已知条件”反复查用，而非现场推导。

## Evidence

**E1 — Day 1：Item Definition → HARA → ASIL 定级构成概念阶段闭环。** 培训用同一 “Torque Demand / E-car” item 贯穿：FS_71 给出功能目的与框图，0156 给出环境/法规/外部措施；随后 0157–0165 八页 HARA 练习要求从危害事件出发，按 S/E/C 三维度查表定 ASIL。这说明 ISO 26262-3 的核心不是写出 hazard，而是证明 **ASIL 等级有明确的 S/E/C 枚举依据**（见 [[sources/sgs-afsp-day1-item-definition-purpose-function]]、[[sources/sgs-afsp-day1-hara-exercise-p1]] 至 [[sources/sgs-afsp-day1-hara-exercise-p8]]）。

**E2 — Day 2：Safety Goal 特征 → FSC → TSC 是需求逐层细化的标准路径。** 0166 列出安全目标的典型属性（FTTI、safe state、warning/degradation concept、冗余/诊断要求）；0167 要求把 SG 展开为 FSR 并映射到架构；0168–0173 六页从系统需求（SYSR）、系统设计/分配、系统要素需求到组件设计的 HW/SW 分配，完整呈现 ISO 26262-4 的技术安全概念落地（见 [[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]、[[sources/sgs-afsp-day2-fsc-requirements-architecture]]、[[sources/sgs-afsp-day2-tsc-system-level-requirements]] 等）。

**E3 — Day 3：硬件分析是 FIT → 故障分布 → 安全机制 → SPFM/LFM/PMHF 的计算链。** 0174 给出 HW 安全需求与设计示例；0175 电路图、0176 BOM/FIT、0177–0178 故障分布、0179 安全机制与诊断覆盖率、0180–0182 度量计算与结果，组成一个可复现的模板。其中 0182 给出示例结果 SPFM=0.87、LFM=0.74、PMHF≈29.29 FIT，对应典型的 ASIL-B/C 目标区间（见 [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]）。

**E4 — SN 29500 是硬件度量的“查表基础设施”。** 培训引用 SN 29500-2（晶体管/二极管/功率半导体 FIT，0183–0184）、SN 29500-3（温度修正 πT，0185）、SN 29500-4（电容/电阻/电感 FIT 及 πU/πT/πQ，0186–0190）。这些表格不是背景阅读，而是 PMHF 计算题的直接已知条件；πT、πU、πQ 三类修正因子必须按实际工作温度、电压比、质量等级选取（见 [[sources/sgs-afsp-sn29500-transistor-fit-rates]]、[[sources/sgs-afsp-sn29500-temperature-correction-factors]]、[[sources/sgs-afsp-sn29500-capacitor-fit-rates]] 等）。

**E5 — 重复扫描暗示高频复习页。** 0157≈0159、0168≡0169 为重复扫描，说明 HARA 练习页与 TSC system draft 页在课堂中被多次分发/重点讲解，符合“需要反复对照标准表格”的备考规律。

## Counter-evidence

**C1 — 单一培训机构视角。** 全部 36 页均来自 SGS TÜV Saar 单一培训材料，缺少 Exida、TÜV Rheinland、DEKRA 等其他认证机构的并行案例，也缺少 OEM/Tier1 实际项目文档。考试真题可能不会完全沿用 SGS 的表格数字或 item 背景。

**C2 — 扫描件无文本层，数据转录存在人工误差风险。** 部分 FIT 值、πT 值、πU 值从图像 OCR/视觉读取转录，小数点、行/列对应关系可能因表格密集而错配；用于实际项目计算时应核对 SN 29500 标准原文或元器件手册。

**C3 — 案例以单一 “Torque Demand” item 为主。** 该案例覆盖动力域转矩请求，但不涉及制动、转向、BMS、ADAS 感知等更复杂 item；HARA 中 S/E/C 的取值、FTTI 的设定在不同 OEM 项目中可能有显著差异，不能直接把本案例结论外推。

**C4 — 未覆盖软件层面（Part 6）。** AFSP 课程案例集中在 Part 3–5，软件安全需求、软件架构度量、工具链置信度（TCL/Tool Classification）等内容未在 36 页中体现，备考需另行补充。

## Synthesis

复习 ISO 26262 AFSP 时，建议把 36 页案例组织为 **三张工作表**：

1. **Day 1 概念表**：Item Definition（FS_71 + 0156）→ HARA（0157–0165）→ ASIL 定级。重点掌握 S/E/C 查表逻辑、外部措施与内部安全机制的区别、ASIL 分解（ASIL decomposition）的入口条件。
2. **Day 2 需求表**：Safety Goal 特征（0166）→ FSC/FSR（0167）→ TSC/SYSR/SYSELR/HW-SW 分配（0168–0173）。重点掌握需求可追溯性、safe state 与 FTTI 的写法、软硬件边界如何影响后续 SPFM/LFM/PMHF 计算。
3. **Day 3 计算表**：BOM/FIT（0176）→ 故障分布（0177–0178）→ 安全机制/DC（0179）→ SPFM/LFM/PMHF（0180–0182）+ SN 29500 查表（0183–0190）。重点掌握单点故障、残余故障、潜伏故障的区分，诊断覆盖率（DC）如何转化为 λ 的加减，以及 πT/πU/πQ 的修正时机。

AFSP 考试的核心能力不是“知道标准条文”，而是 **能在给定 item、给定故障模式、给定元器件 FIT 的条件下，正确选择安全机制、计算度量指标、判断 ASIL 达标性**。因此本综合页的价值在于把分散的 36 页扫描件还原为一条可跟随的解题链，而非替代标准原文。

## Confidence Notes

置信度为 **medium**。依据：36 个来源数量充足，且为官方培训教材，内容内部自洽；但来源高度集中于 SGS TÜV Saar 单一机构，缺少竞品/OEM 实际项目对照，部分数据来自扫描件转录。按 CLAUDE.md §十，未达 high 所需的“多独立来源交叉验证”，故维持 medium。

## Limitations

- **同源性风险**：全部案例来自同一培训课程，可能存在机构特有的表述习惯和简化假设。
- **扫描转录误差**：表格密集，FIT、πT、πU、πQ 数值在视觉读取中可能产生行/列错位；用于工程计算需以标准原文为准。
- **覆盖盲区**：未涉及 ISO 26262 Part 6 软件安全、Part 8 支持过程、Part 9 ASIL 分解、Part 11 半导体指南等进阶主题。
- **案例单一性**：Torque Demand 案例不足以代表制动、转向、高压电池管理等复杂安全关键系统。

## Sources

- [[sources/sgs-afsp-day1-item-definition-purpose-function]]
- [[sources/sgs-afsp-day1-item-definition-context]]
- [[sources/sgs-afsp-day1-hara-exercise-p1]]
- [[sources/sgs-afsp-day1-hara-exercise-p2]]
- [[sources/sgs-afsp-day1-hara-exercise-p1-duplicate]]
- [[sources/sgs-afsp-day1-hara-exercise-p3]]
- [[sources/sgs-afsp-day1-hara-exercise-p4]]
- [[sources/sgs-afsp-day1-hara-exercise-p5]]
- [[sources/sgs-afsp-day1-hara-exercise-p6]]
- [[sources/sgs-afsp-day1-hara-exercise-p7]]
- [[sources/sgs-afsp-day1-hara-exercise-p8]]
- [[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]
- [[sources/sgs-afsp-day2-fsc-requirements-architecture]]
- [[sources/sgs-afsp-day2-tsc-system-draft]]
- [[sources/sgs-afsp-day2-tsc-system-draft-duplicate]]
- [[sources/sgs-afsp-day2-tsc-system-level-requirements]]
- [[sources/sgs-afsp-day2-tsc-system-design-allocation]]
- [[sources/sgs-afsp-day2-tsc-system-element-requirements]]
- [[sources/sgs-afsp-day2-tsc-component-design-hw-sw-allocation]]
- [[sources/sgs-afsp-day3-hw-safety-requirements-design-example]]
- [[sources/sgs-afsp-day3-hw-analysis-circuit-diagram]]
- [[sources/sgs-afsp-day3-hw-analysis-bom-fault-rates]]
- [[sources/sgs-afsp-day3-hw-analysis-fault-distribution-components]]
- [[sources/sgs-afsp-day3-hw-analysis-fault-distribution-amp-motor]]
- [[sources/sgs-afsp-day3-hw-analysis-safety-mechanisms-dc]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p6]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p7]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]
- [[sources/sgs-afsp-sn29500-transistor-fit-rates]]
- [[sources/sgs-afsp-sn29500-diode-power-semiconductor-fit-rates]]
- [[sources/sgs-afsp-sn29500-temperature-correction-factors]]
- [[sources/sgs-afsp-sn29500-capacitor-fit-rates]]
- [[sources/sgs-afsp-sn29500-resistor-inductor-passive-fit-rates]]
- [[sources/sgs-afsp-sn29500-capacitor-voltage-correction]]
- [[sources/sgs-afsp-sn29500-capacitor-temperature-correction]]
- [[sources/sgs-afsp-sn29500-resistor-temperature-quality-factor]]
