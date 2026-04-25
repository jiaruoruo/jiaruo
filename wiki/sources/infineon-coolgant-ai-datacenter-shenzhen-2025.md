---
type: source
title: "英飞凌CoolGaN™赋能AI数据中心"
date: 2026-04-20
sha256: "be45ce2239729c3be1e6c2047a65cb55bd32808926632e569c305a22476ebe6b"
raw_file: "raw/pdfs/深圳We Power AI --英飞凌CoolGaN™赋能AI数据中心--程文涛.pdf"
author: "程文涛，英飞凌科技消费、计算与通讯业务部门"
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

# 英飞凌CoolGaN™赋能AI数据中心

## Summary

CoolGaN™ 氮化镓功率器件赋能下一代 AI 服务器开关电源（SMPS）。随着 AI 数据中心单机架功率突破 100kW，PSU 面临 EDPP 规范下的 190% 峰值负载、更高开关频率和更高功率密度要求；CoolGaN™ 600V GaN HEMT 凭借 Zero Qrr 和极低 RDS(on)×Eoss 成为最优选择，英飞凌 8kW PSU 参考设计实现了 ~98% 效率和 100W/in³ 功率密度。

## Key Points

- **AI 市场增长**：AI Training GPU/TPU 单元 CAGR **>40%**；半导体 SAM CAGR **>50%**（2023-2027）
- **EDPP 规范**：PSU 需支持 190% 峰值负载（500μs），160% 负载（5ms），130% 负载（50ms），电流斜率 2.5A/μs
- **GaN vs Si 性能对比**：CoolGaN™ 600V 的 RDS(on)×Eoss 仅为 CoolMOS™ C7 的 **6%**；RDS(on)×Qg 仅 **13%**；Qrr = **0%**（完美软开关特性）
- **三代 AI PSU 架构**：第一代 277/347Vac 单相 5.5kW → 第二代 8kW → 第三代 3相 480Vac + 380V 直流配电 22kW（Vienna PFC + FB LLC）
- **8kW PSU 参考设计（REF_8KW_HFHD_PSU）**：输出 50V DC/8kW；效率 ~98%；功率密度 100W/in³（比 ORv3 规格体积减小 38%）；LLC 开关频率 400kHz；Hold-up 20ms @100% 负载；输入 180-275Vac
- **300mm GaN 晶圆**：提升供应稳定性、性能与成本效益，推动与硅基器件价格平价
- **未来方向**：三相拓扑（Vienna PFC）+ 更高直流分配电压（400V）+ 顶部散热封装支持液冷冷板

## Related Concepts

## Related Entities

- [[entities/infineon-technologies]]
