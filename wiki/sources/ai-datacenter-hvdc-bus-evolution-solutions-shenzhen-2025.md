---
type: source
title: "人工智能数据中心向更高总线电压的演变及可用解决方案"
date: 2026-04-20
sha256: "3b2232ceaae85031292fc65c67aefd111c208a33168babac471c1128ba12867f"
raw_file: "raw/pdfs/深圳We Power AI --人工智能数据中心向更高总线电压的演变及可用解决方案-宋清亮.pdf"
author: "宋清亮（Owen Song），英飞凌科技"
event: "深圳 We Power AI 2025"
domain:
  - ai-infrastructure
  - power-electronics
  - data-center
  - semiconductors
entities:
  - infineon-technologies
concepts: []
status: processed
---

# 人工智能数据中心向更高总线电压的演变及可用解决方案

## Summary

AI 数据中心供电架构正经历从 12V 到 48V 再到 400V/800V 高压直流（HVDC）的演进。驱动因素是 AI GPU/TPU 算力需求的爆炸式增长（CAGR >40%），传统低压架构在高功率密度场景下效率低、损耗大。SiC 和 GaN 作为主流功率器件支撑 HVDC 演进，固态变压器（SST）是下一代数据中心配电架构的核心技术方向。

## Key Points

- **AI GPU/TPU 功率需求**：Training GPU/TPU 单元 CAGR **>40%**（2023-2027），平均 BOM CAGR >10%，半导体 SAM CAGR >50%
- **总线电压演进路线**：12V（传统服务器）→ 48V（ORv3 规范）→ 400V/800V HVDC（下一代 AI 数据中心）
- **48V 优势**：相比 12V，相同功率下电流减小 4×，导线损耗降低 16×，支持更高功率密度机架
- **HVDC 优势**：400V/800V HVDC 直接取消多级 AC-DC 转换，效率显著提升；适合 MW 级超大规模数据中心
- **SiC 在 HVDC 的角色**：SiC MOSFET（650V-1700V）低开关损耗，适合三相 PFC/Vienna 整流及 DC-DC 转换
- **GaN 在 HVDC 的角色**：CoolGaN™ 600V GaN HEMT，RDS(on)×Eoss 仅为 CoolMOS™ C7 的 **6%**，Qrr=0，适合高频开关电源
- **固态变压器（SST）**：取代传统工频变压器，实现 AC/DC 双向隔离转换，是数据中心配电网智能化的关键技术
- **英飞凌产品矩阵**：CoolSiC™ MOSFET + CoolGaN™ HEMT + XDPE 数字电源管理覆盖 HVDC 完整方案

## Related Concepts

## Related Entities

- [[entities/infineon-technologies]]
