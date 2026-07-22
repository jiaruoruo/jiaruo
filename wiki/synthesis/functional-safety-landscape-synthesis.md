---
type: synthesis
title: "功能安全全景综合（Functional Safety Landscape）"
date: 2026-07-22
tags:
  - functional-safety
  - automotive-eea
  - iso-26262
  - gbt-34590
  - automotive
  - mculess
source_count: 72
confidence: medium
---

# 功能安全全景综合（Functional Safety Landscape）

> 本综合为 **[[concepts/functional-safety]]** 主题簇的跨来源横向综合，覆盖 ISO 26262:2018 与 GB/T 34590 标准骨架、SGS AFSP 备考主线、MCULess 适用边界、以及向半导体/机器人延伸。备考细节见子综合 [[synthesis/iso26262-afsp-study-guide]]，本页不重复。

## Thesis

功能安全（FuSa）不是单一技术，而是一套以 **ISO 26262:2018 / GB/T 34590** 为规范骨架、以 **ASIL 分级（S×E×C）** 为量化入口、贯穿「概念→系统→硬件→软件→生产」完整安全生命周期的跨学科约束体系。它的现实约束力体现在三处：**(1)** 作为汽车 EEA 域划分与 MCULess「降本叙事」的硬性边界（ASIL-D 禁用 MCULess）；**(2)** 作为车规 MCU/SoC 安全芯片护城河的根基（安全岛、诊断覆盖率、失效率 <1ppm）；**(3)** 正迁移为机器人安全关键链路的方法学来源（ISO/TS 15066、关节/力矩传感 ASIL C/D）。

## Evidence

**E1 — 规范骨架：ISO 26262:2018 共 12 部分，覆盖完整安全生命周期。**
Part 1 术语、Part 2 功能安全管理、Part 3 概念阶段（Item Definition → HARA → ASIL → Safety Goal）、Part 4 系统层面（FSC/TSC）、Part 5 硬件层面（SPFM/LFM/PMHF）、Part 6 软件层面、Part 7 生产运行、Part 8 支持过程、Part 9 ASIL 导向分析（分解/共存/相关失效）、Part 10 指南、Part 11 半导体应用指南、Part 12 摩托车适用性（见 [[sources/iso-26262-1-2018]] 至 [[sources/iso-26262-12-2018]]）。GB/T 34590 是其中国国标等同/修改采用版，Part 1–12 一一对应，但本批为**征求意见稿**，非正式发布版（见 [[concepts/gbt-34590]]、[[sources/gbt-34590-1-draft]] 至 [[sources/gbt-34590-12-draft]]）。

**E2 — 量化入口：ASIL 由 HARA 的 S（严重度）/E（暴露概率）/C（可控性）三维查表定级 A→D。** 培训案例用同一 "Torque Demand / E-car" item 贯穿 Day 1–3，证明 ASIL 等级必须有明确的 S/E/C 枚举依据，而非主观判断（见 [[sources/sgs-afsp-day1-hara-exercise-p1]]、[[sources/sgs-afsp-day1-hara-exercise-p8]]）。ASIL 分解（Part 9）是降低单要素要求的关键手段。

**E3 — 硬件度量计算链：FIT → 故障分布 → 安全机制/诊断覆盖率(DC) → SPFM/LFM/PMHF。** 示例结果 SPFM=0.87、LFM=0.74、PMHF≈29.29 FIT，对应典型 ASIL-B/C 目标区间；SN 29500 提供晶体管/二极管/功率半导体/电容/电阻的基准 FIT 与 πT/πU/πQ 修正因子，是 PMHF 计算的「查表基础设施」（见 [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]、[[sources/sgs-afsp-sn29500-transistor-fit-rates]]、[[concepts/sn29500]]）。相关指标概念见 [[concepts/hardware-metrics]]、[[concepts/pmhf]]、[[concepts/fit-rate]]。

**E4 — 对 MCULess 的硬边界：ASIL 决定「能不能去掉 MCU」。**
- ✅ 车身域、智能电源域、车灯（如易冲 CPSQ5355 三通道 LED 驱动，AEC-Q100 Grade 1 + ASIL-B，内置 Limp-Home 降级）：控制简单，可接受 MCULess。
- ❌ 制动/转向/气囊（ASIL-D）：要求本地降级 Fallback，**必须保留 MCU**，禁止 MCULess。
- ⚠ 底盘气悬域：本地算法复杂，MCULess 后域控 CPU +10%，不推荐（见 [[sources/mculess-validation-report]]、[[sources/mculess-smart-lighting-innovation]]、[[concepts/mculess-architecture]]）。功能安全是 MCULess 降本叙事的主要边界约束（与 [[synthesis/mculess-eea-architecture-synthesis]] 交叉）。

**E5 — 车规安全芯片护城河：安全岛 + 诊断覆盖率 + 极低失效率。** 瑞萨 RH850/U2B（28nm、双 CPU、累计出货 >7 亿颗、失效率 <1ppm、面向 FuSa）是典型安全 MCU，其技术正向机器人安全关键场景迁移（见 [[sources/renesas-rh850-u2b-introduction]]、[[sources/renesas-robot-servo-ethercat-application]]）；理想马赫 M100 SoC 内置「功能安全岛」+ 安全引擎（见 [[sources/li-auto-mach-m100-deep-dive]]）；英飞凌 TLE5014 角度传感器支持 ASIL C/D（见 [[sources/infineon-sensing-empowers-robotics-shenzhen-2025]]）。与 [[synthesis/robot-semiconductor-competitive-synthesis]] 共振。

**E6 — 向机器人延伸：汽车级 FuSa 方法学正迁移。** 人形机器人关节/力矩传感等安全关键链路引入汽车级 FuSa；更系统的机器人物理安全方法学见 [[concepts/robot-safety]]（ISO/TS 15066 协作安全、ISO 13849、L1–L4 分层架构），麦肯锡人形机器人 BOM/供应链分析亦指向该趋势（见 [[sources/mckinsey-humanoid-robot-bom-supply-chain]]、[[concepts/humanoid-robot]]）。

## Counter-evidence

> ⚠ **回音室风险（Stage 0 反向检验）**：未找到**反驳** ISO 26262 核心假设（S×E×C 定级模型、随机硬件度量范式、生命周期方法学）的独立来源。具体表现为：
> 1. **单一培训机构视角**：36 份 AFSP 来源全部来自 SGS TÜV Saar，缺少 Exida / TÜV Rheinland / DEKRA 或 OEM/Tier1 实际项目文档对照（见 [[synthesis/iso26262-afsp-study-guide]] Counter-evidence C1）。
> 2. **规范性来源非批判性**：ISO 26262 / GB/T 34590 本身是标准文本（规定「应如何」），不提供对方法学本身的质疑或替代方案。
> 3. **机器人迁移未经验证**：E6 的「汽车 FuSa → 机器人」迁移是趋势性判断，缺乏机器人领域已落地、经认证的反向案例，可能高估方法学直接可移植性。
> 4. **GB/T 34590 版本时效**：本批国标为征求意见稿，与正式版可能存在条文差异，结论若依赖其细节需待正式发布后复核。

## Synthesis

把功能安全主题簇的 72 个来源（去重后）归并为一个可操作的认知框架：

1. **规范层（What is required）**：ISO 26262:2018 第 2 版 12 部分 + GB/T 34590（国标版）构成强制/准强制骨架；Part 10–12 为信息性指南，不增约束力。
2. **方法层（How to do it）**：安全生命周期 = 概念(Part3) → 系统(Part4) → 硬件(Part5) → 软件(Part6) → 生产(Part7)；ASIL 是贯穿各层的统一需求标尺；Part 8/9 是支撑与剪裁手段。
3. **量化层（How to prove it）**：随机硬件层面用 SPFM/LFM/PMHF 三指标 + SN 29500 基准失效率证明达标；系统/软件层面用需求可追溯性与安全机制 DC 证明。
4. **约束层（Where it bites）**：MCULess 降本的合法边界由 ASIL 划定——ASIL-D 安全关键域必须保留 MCU，简单域可 MCULess + Limp-Home。
5. **外延层（Where it spreads）**：车规安全芯片（安全岛/DC/<1ppm）是 FuSa 的商业化落地；同一套方法学正向机器人安全关键链路迁移。

**核心判断**：功能安全的「难」不在单个条款，而在**跨层的可追溯性与端到端责任链**——从 HARA 的 S/E/C 到最终硬件的 PMHF，每一步都必须能正向推导、反向追溯。这也是它成为 MCULess 边界与芯片护城河的根因。

## Confidence Notes

⚠ Confidence Notes：此综合基于 **72** 个来源（去重后：ISO 26262 标准 12 + GB/T 34590 征求意见稿 12 + SGS AFSP 培训 34 + MCULess/半导体/机器人延伸 14），置信度为 **medium**。

- **支撑 medium 的因素**：来源数量远超 5+ 阈值；标准文本与培训案例在 ASIL 定级、硬件度量计算链上内部自洽；MCULess 边界、车规芯片案例有独立行业报道交叉印证。
- **维持 medium、未升 high 的原因（按 CLAUDE.md §十需用户确认）**：AFSP 子簇高度同源（单一培训机构），且核心规范来源为「规定性」而非「批判性」，反向检验未找到独立反驳来源——存在确认偏差风险。若将本综合置信度升至 high，须经老贾明确确认。

## Limitations

- **同源性偏差**：AFSP 子簇 36 源来自单一机构；标准子簇为规范性文本。结论的「正确性」建立在 ISO 26262 体系本身有效的前提上，本库未收录其学术/产业质疑。
- **扫描转录误差**：AFSP 部分 FIT/πT/πU/πQ 数值来自扫描件视觉读取，密集表格可能行/列错位；工程计算须以标准原文或元器件手册为准。
- **覆盖盲区（已消解）**：ASIL 原仅在 `functional-safety` 子项承载、SPFM/LFM 原仅间接提及；经 2026-07-22 后续处理，已新建独立概念页 [[concepts/asil]]（13 源），并将 SPFM/LFM 作为一级小节并入 [[concepts/hardware-metrics]] 并加入 aliases，三者均可解析、盲区消除（详见 `wiki/outputs/gap-report-2026-07-22.md` 行动清单第 1–4 项）。
- **版本时效**：GB/T 34590 为征求意见稿，正式发布后需复核差异。
- **机器人迁移待验证**：E6 为趋势判断，非已认证落地事实。

## Sources

- [[concepts/functional-safety]]
- [[concepts/iso-26262]]
- [[concepts/gbt-34590]]
- [[sources/iso-26262-1-2018]]、[[sources/iso-26262-2-2018]]、[[sources/iso-26262-3-2018]]、[[sources/iso-26262-4-2018]]、[[sources/iso-26262-5-2018]]、[[sources/iso-26262-6-2018]]、[[sources/iso-26262-7-2018]]、[[sources/iso-26262-8-2018]]、[[sources/iso-26262-9-2018]]、[[sources/iso-26262-10-2018]]、[[sources/iso-26262-11-2018]]、[[sources/iso-26262-12-2018]]
- [[sources/gbt-34590-1-draft]]、[[sources/gbt-34590-2-draft]]、[[sources/gbt-34590-3-draft]]、[[sources/gbt-34590-4-draft]]、[[sources/gbt-34590-5-draft]]、[[sources/gbt-34590-6-draft]]、[[sources/gbt-34590-7-draft]]、[[sources/gbt-34590-8-draft]]、[[sources/gbt-34590-9-draft]]、[[sources/gbt-34590-10-draft]]、[[sources/gbt-34590-11-draft]]、[[sources/gbt-34590-12-draft]]
- [[synthesis/iso26262-afsp-study-guide]]
- [[sources/sgs-afsp-day1-hara-exercise-p1]]、[[sources/sgs-afsp-day1-hara-exercise-p8]]、[[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]、[[sources/sgs-afsp-sn29500-transistor-fit-rates]]
- [[sources/mculess-validation-report]]、[[sources/mculess-smart-lighting-innovation]]、[[concepts/mculess-architecture]]、[[synthesis/mculess-eea-architecture-synthesis]]
- [[sources/renesas-rh850-u2b-introduction]]、[[sources/renesas-robot-servo-ethercat-application]]、[[sources/li-auto-mach-m100-deep-dive]]、[[sources/infineon-sensing-empowers-robotics-shenzhen-2025]]、[[synthesis/robot-semiconductor-competitive-synthesis]]
- [[sources/mckinsey-humanoid-robot-bom-supply-chain]]、[[concepts/robot-safety]]、[[concepts/humanoid-robot]]
