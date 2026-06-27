---
type: concept
title: "氮化镓功率器件"
date: 2026-06-27
updated: 2026-06-27
tags:
  - gan
  - power-electronics
  - wide-bandgap
  - robotics
  - datacenter
source_count: 8
confidence: medium
domain_volatility: medium
last_reviewed: 2026-06-27
aliases:
  - "氮化镓功率器件"
  - "氮化镓"
  - "GaN"
  - "GaN HEMT"
  - "Gallium Nitride"
  - "CoolGaN"
---

# 氮化镓功率器件（GaN Power Devices）

## Definition

氮化镓功率器件（GaN Power Devices）是基于宽禁带半导体氮化镓（GaN）的功率开关器件，通过天然异质结形成的二维电子气（2DEG）实现低导通电阻与高频开关能力。相比硅基 MOSFET，GaN 具备 **Zero Qrr（零反向恢复）**、更低的 RDS(on)×Eoss、更高的工作频率，从而在相同功率下显著缩小体积、提升效率，正成为机器人电机驱动（见 [[concepts/quasi-direct-drive-motor]]）、AI 数据中心供电、汽车 OBC 等高功率密度场景的关键器件，也是英飞凌等厂商在机器人半导体竞争中的差异化护城河之一（见 [[synthesis/robot-semiconductor-competitive-synthesis]]）。

## Key Points

- **材料优势**：禁带宽度 3.4eV（Si 1.1eV）；击穿电场强度 3.3MV/cm（约 Si 的 10 倍）；电子迁移率 2000cm²/V·s；2DEG 无需掺杂即可高导电（见 [[sources/gan-power-devices-tech-applications-outlook-shenzhen-2025]]）。
- **GaN vs Si vs SiC 分工**：GaN 最优高频（>1MHz）；SiC 更适合高压（>650V）中频；Si 成本最低。三者在功率电子中互补而非互替。
- **关键性能（vs Si MOSFET）**：Zero Qrr（无反向恢复损耗）；RDS(on)×Eoss 较 Si 降低约 94%，600V CoolGaN™ 仅为 CoolMOS™ C7 的约 6%；支持 100kHz+ 开关频率使被动元件小型化。
- **机器人电机驱动应用**：CoolGaN™ 100V 系列（如 IGC033S10S1，100V/47A/3.3mΩ）面向 48V 机器人系统；100kHz 开关下驱动器体积缩小约 30%、峰值效率达 99%；覆盖人形机器人 40-50 个关节电机（见 [[concepts/humanoid-robot]]）与灵巧手（见 [[concepts/dexterous-hand]]）微型驱动器（来源：[[sources/infineon-gan-solution-robotics-shenzhen-2025]]、[[sources/infineon-psoc-gan-motor-drive-shenzhen-2025]]）。
- **AI 数据中心供电应用**：随单机架功率破 100kW，600V CoolGaN™ 用于 8kW PSU 的 LLC 级（400kHz 软开关），实现 ~98% 效率、100W/in³ 功率密度；配合 SiC 做 PFC 级，支撑 12V→48V→400/800V HVDC 演进（见 [[sources/infineon-coolgant-ai-datacenter-shenzhen-2025]]、[[sources/infineon-ai-server-power-solution-shenzhen-2025]]、[[sources/ai-datacenter-hvdc-bus-evolution-solutions-shenzhen-2025]]）。
- **市场结构**：消费电子（充电器/适配器）是当前最大市场，预计 2028 年占 GaN 市场约 64%（快充驱动）。
- **产业化拐点**：英飞凌 CoolGaN™ 已迁至 **300mm GaN-on-Si** 晶圆量产，推动与硅器件价格平价；路线图 100V（机器人/消费）→ 600V（数据中心/工业）→ 650V+（汽车 OBC）。
- **集成与创新**：双向 GaN 开关（简化双向 DC-DC，用于储能/V2G）、GaN IC 单片集成（驱动器+HEMT，降寄生降 BOM）、QST 衬底（热膨胀更匹配、支持大直径晶圆）。

## My Position

<!-- 暂无个人立场，待补充 -->

## Contradictions

<!-- 暂未发现来源间分歧。注：本概念来源高度集中于英飞凌视角，存在厂商单一性，竞品（GaN Systems/纳微/Power Integrations）原始口径缺失。 -->

## Sources

- [[sources/gan-power-devices-tech-applications-outlook-shenzhen-2025]]
- [[sources/infineon-gan-solution-robotics-shenzhen-2025]]
- [[sources/infineon-psoc-gan-motor-drive-shenzhen-2025]]
- [[sources/infineon-coolgant-ai-datacenter-shenzhen-2025]]
- [[sources/infineon-ai-server-power-solution-shenzhen-2025]]
- [[sources/ai-datacenter-hvdc-bus-evolution-solutions-shenzhen-2025]]
- [[sources/infineon-complete-solution-robotics-shenzhen-2025]]
- [[sources/infineon-humanoid-robot-feb2026]]

## Evolution Log

- 2026-06-27（8 sources）：概念初建（REFLECT gap 回填，2026-04-25 gap report 已标记）。从英飞凌深圳论坛系列 + 氮化镓专题来源提炼材料优势、GaN/Si/SiC 分工、机器人电机驱动与 AI 数据中心两大应用、300mm 产业化拐点；confidence 设为 medium，已在 Contradictions 标注厂商单一性局限。
