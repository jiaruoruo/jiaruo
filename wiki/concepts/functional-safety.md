---
type: concept
title: "功能安全"
date: 2026-06-27
updated: 2026-07-22
tags:
  - functional-safety
  - automotive
  - iso26262
  - asil
  - robotics
  - automotive-eea
  - embodied-ai
source_count: 72
confidence: medium
domain_volatility: low
last_reviewed: 2026-07-22
aliases:
  - "功能安全"
  - "Functional Safety"
  - "FuSa"
---

# 功能安全（Functional Safety / FuSa）

## Definition

功能安全（Functional Safety，简称 FuSa）是指系统在发生随机硬件失效或系统性失效时，仍能保持或进入安全状态、避免对人身造成不可接受风险的能力。在汽车领域以 **ISO 26262** 标准为核心，用 **ASIL（Automotive Safety Integrity Level，汽车安全完整性等级）** 将安全需求分为 A/B/C/D 四级（D 最严苛），通过失效检测、冗余、降级运行（Limp-Home/Fallback）等机制达成。功能安全是汽车 EEA（见 [[eea-architecture]]）域划分、MCULess（见 [[mculess-architecture]]）适用边界、以及机器人/汽车主控芯片设计的硬性约束，也是英飞凌/瑞萨/ST 等厂商「安全 MCU 护城河」的根基（见 [[synthesis/robot-semiconductor-competitive-synthesis]]）。

## Key Points

- **ASIL 分级（ISO 26262）**：A（最低）→ B → C → D（最高），按严重度（S）、暴露概率（E）、可控性（C）综合评定；不同安全目标对应不同等级的硬件冗余与诊断覆盖率要求。
- **核心机制**：失效检测 → 安全状态切换 → **降级运行（Limp-Home / Fallback）**；要求本地具备在通信或主控失效时独立进入安全态的能力。
- **对 MCULess 的硬约束（关键）**：
  - ✅ 车身域、智能电源域、车灯等：控制逻辑简单，可接受 MCULess（如易冲 CPSQ5355 三通道 LED 驱动，AEC-Q100 Grade 1 + **ASIL-B**，内置 Limp-Home 降级，见 [[sources/mculess-smart-lighting-innovation]]）。
  - ❌ 制动/转向/气囊（**ASIL-D**）：要求本地降级 Fallback，**必须保留 MCU**，禁止 MCULess。
  - ⚠ 底盘气悬域：本地控制算法复杂，MCULess 后域控 CPU +10%，不推荐（见 [[sources/mculess-validation-report]]）。
- **车规 MCU 的功能安全积累**：瑞萨 RH850/U2B（28nm、双 CPU、累计出货 >7 亿颗、失效率 <1ppm、面向 FuSa）是典型安全 MCU；其 FuSa 技术正向机器人安全关键场景迁移（见 [[sources/renesas-rh850-u2b-introduction]]、[[sources/renesas-robot-servo-ethercat-application]]）。
- **AEC-Q 与 ASIL 的区别**：AEC-Q100（车规可靠性等级，按温度 Grade 0/1/2…）是**器件可靠性**认证；ASIL 是**功能安全完整性**等级，二者常并列标注但维度不同。
- **芯片级功能安全设计**：主控 SoC 内置「功能安全岛」+ 安全引擎（如理想马赫 M100，见 [[sources/li-auto-mach-m100-deep-dive]]）；传感器支持 ASIL C/D（如英飞凌 TLE5014 角度传感器，见 [[sources/infineon-sensing-empowers-robotics-shenzhen-2025]]）。
- **向机器人延伸**：人形机器人关节/力矩传感等安全关键链路正引入汽车级 FuSa 方法学（见 [[sources/mckinsey-humanoid-robot-bom-supply-chain]]、[[concepts/humanoid-robot]]）；更系统的机器人物理安全方法学见 [[robot-safety]]（ISO/TS 15066 协作安全、ISO 13849、L1-L4 分层架构）
- **认证备考（内部）**：ISO 26262 考试复习要点与模拟题库（2026-07）覆盖故障链 Fault→Error→Failure、ASIL(HARA 三维度 S×E×E)、安全生命周期(Part3→6)、随机硬件三指标(SPF/LatF/PMHF)、安全机制四类型(冗余/监控/诊断/降级)；域控制器(CCU-ZCU)项目需关注跨域通信安全/共因故障/端到端追溯
- **跨来源综合**：功能安全全景综合见 [[synthesis/functional-safety-landscape-synthesis]]（规范骨架/ASIL 量化/安全生命周期/MCULess 边界/半导体·机器人延伸，74 源）；备考主线另见 [[synthesis/iso26262-afsp-study-guide]]

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂未发现来源间分歧；功能安全是 MCULess「降本叙事」的主要边界约束，详见 [[synthesis/mculess-eea-architecture-synthesis]] -->

## Sources

- [[sources/mculess-validation-report]]
- [[sources/mculess-smart-lighting-innovation]]
- [[sources/mculess-tech-comparison-analysis]]
- [[sources/renesas-rh850-u2b-introduction]]
- [[sources/renesas-robot-servo-ethercat-application]]
- [[sources/li-auto-mach-m100-deep-dive]]
- [[sources/infineon-sensing-empowers-robotics-shenzhen-2025]]
- [[sources/mckinsey-humanoid-robot-bom-supply-chain]]
- [[sources/iso-26262-exam-review-notes]]
- [[sources/iso-26262-exam-practice-questions]]
- [[sources/mculess-technology-insight-full-2026-05]]
- [[sources/ethercat-team-planning-report-2026]]
- [[sources/mcu-less-seats-project-2026-03]]
- [[sources/mcu-less-application-opportunities]]
- [[sources/sgs-afsp-day1-item-definition-purpose-function]]
- [[sources/sgs-afsp-day1-item-definition-context]]
- [[sources/sgs-afsp-day1-hara-exercise-p1]]
- [[sources/sgs-afsp-day1-hara-exercise-p2]]
- [[sources/sgs-afsp-day1-hara-exercise-p3]]
- [[sources/sgs-afsp-day1-hara-exercise-p4]]
- [[sources/sgs-afsp-day1-hara-exercise-p5]]
- [[sources/sgs-afsp-day1-hara-exercise-p6]]
- [[sources/sgs-afsp-day1-hara-exercise-p7]]
- [[sources/sgs-afsp-day1-hara-exercise-p8]]
- [[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]
- [[sources/sgs-afsp-day2-fsc-requirements-architecture]]
- [[sources/sgs-afsp-day2-tsc-system-draft]]
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
- [[sources/iso-26262-1-2018]]
- [[sources/iso-26262-2-2018]]
- [[sources/iso-26262-3-2018]]
- [[sources/iso-26262-4-2018]]
- [[sources/iso-26262-5-2018]]
- [[sources/iso-26262-6-2018]]
- [[sources/iso-26262-7-2018]]
- [[sources/iso-26262-8-2018]]
- [[sources/iso-26262-9-2018]]
- [[sources/iso-26262-10-2018]]
- [[sources/iso-26262-11-2018]]
- [[sources/iso-26262-12-2018]]
- [[sources/gbt-34590-1-draft]]
- [[sources/gbt-34590-2-draft]]
- [[sources/gbt-34590-3-draft]]
- [[sources/gbt-34590-4-draft]]
- [[sources/gbt-34590-5-draft]]
- [[sources/gbt-34590-6-draft]]
- [[sources/gbt-34590-7-draft]]
- [[sources/gbt-34590-8-draft]]
- [[sources/gbt-34590-9-draft]]
- [[sources/gbt-34590-10-draft]]
- [[sources/gbt-34590-11-draft]]
- [[sources/gbt-34590-12-draft]]

## Evolution Log

- 2026-06-27（8 sources）：概念初建（REFLECT gap 回填）。横跨汽车 EEA、MCULess、机器人半导体三大簇，从已有 8 个来源提炼 ASIL 分级、Limp-Home 降级机制、MCULess 域适用边界（ASIL-D 禁用）、安全 MCU 积累等核心内容；confidence 设为 medium。
- 2026-07-13（10 sources）：强化——内部 ISO 26262 考试复习要点与模拟题库补充认证备考视角：故障链、ASIL(HARA 三维度)、安全生命周期、随机硬件三指标(SPF/LatF/PMHF)、安全机制四类型；并链接 [[robot-safety]] 概念（机器人物理安全方法学，ISO/TS 15066 协作安全）

- 2026-07-14（14 sources）：强化——[MCU-less 技术洞察（详尽版）：机会分析 · 技术方案 · 执行策略] 与现有定义一致
- 2026-07-14（14 sources）：强化——[机器人行业 EtherCAT 总线通信开发团队规划报告] 与现有定义一致
- 2026-07-14（14 sources）：强化——[MCU-Less 座椅项目讨论（V0.5）] 与现有定义一致
- 2026-07-14（14 sources）：强化——[MCU-less 应用机会点汇总] 与现有定义一致
- 2026-07-21（14 sources）：REFLECT 补齐主域标签：automotive-eea、embodied-ai
- 2026-07-22（50 sources）：强化——全量摄入 SGS TÜV Saar ISO 26262 AFSP 培训案例 36 页扫描件，覆盖 Day 1 Item Definition/HARA、Day 2 FSC/TSC、Day 3 硬件分析/SPFM/LFM/PMHF 与 SN 29500 元器件 FIT/πT/πU/πQ 查表；新建综合页 [[synthesis/iso26262-afsp-study-guide]]；functional-safety source_count 14→50，confidence 维持 medium（单一培训机构来源+扫描转录风险）
- 2026-07-22（74 sources）：强化——全量摄入 raw/pdfs/功能安全/ 下 ISO 26262:2018 第 1–12 部分正式标准（12 源）+ GB/T 34590 征求意见稿第 1–12 部分（12 源）；新建枢纽概念 [[iso-26262]]、[[gbt-34590]]；functional-safety source_count 50→74，confidence 维持 medium
- 2026-07-22（REFLECT）：新建跨来源综合 [[synthesis/functional-safety-landscape-synthesis]]（74 源，medium），消解功能安全簇「广而不深」；反向检验标注回音室风险（AFSP 单机构、规范来源非批判性、机器人迁移未验证、国标草稿时效）
- 2026-07-22（MERGE）：去重——两份 SGS AFSP 重复扫描源页（day1-hara-exercise-p1-duplicate、day2-tsc-system-draft-duplicate）改为重定向至各自主键；Sources 列表移除重复条目，source_count 74→72（唯一来源）
