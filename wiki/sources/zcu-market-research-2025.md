---
type: source
title: 车身(区域)研究：ZCU搭载量超200万辆，向"即插即用"模块化平台演进
slug: zcu-market-research-2025
date: 2026-04-28
source_url: https://mp.weixin.qq.com/s/G79bzQzry9pSq2v2iRNiBA
author: 佐思汽研
published: 2026-04-28
ingested: 2026-04-28
sha256: 8bb89b94
tags: [zcu, mculess, 10base-t1s, eea, market-research, automotive, china]
concepts: [mculess-architecture, eea-architecture, zonal-gateway, can-eth-protocol-conversion]
entities: [goodix-technology]
---

# 车身(区域)研究：ZCU搭载量超200万辆，向"即插即用"模块化平台演进

## 核心摘要

佐思汽研 2025 年中国 ZCU 市场研究报告摘要。2024 年中国乘用车 ZCU 渗透率 **8.83%**，搭载量超 200 万辆，市场规模 39.3 亿元（含 BCM/BDC/ZCU 全市场 156.2 亿元）。六大技术趋势：MCU Less / 边缘 AI / SmartFET / 实时性安全冗余 / Plug&Play 模块化 / 10BASE-T1S。

## 市场数据（2024 年）

| 指标 | 数值 |
|---|---|
| 中国乘用车 ZCU 渗透率 | **8.83%** |
| ZCU 搭载量 | **> 200 万辆** |
| ZCU 市场规模 | 39.3 亿元 |
| BCM/BDC/ZCU 全市场规模 | 156.2 亿元 |

## 六大技术趋势

1. **MCU Less**：边缘节点去 MCU，控制逻辑上移至 ZCU
2. **边缘 AI**：ZCU 内集成 NPU，本地推理降低时延
3. **SmartFET**：智能功率 MOSFET，集成驱动和诊断
4. **实时性安全冗余**：TSN + 功能安全 ASIL-B/D 双保障
5. **Plug&Play 模块化**：即插即用，简化整车集成
6. **10BASE-T1S**：单对以太网取代 CAN/LIN 连接边缘节点

## 主要 OEM ZCU 方案

| OEM | 方案亮点 |
|---|---|
| **小米 YU7** | ZCU 减少 75% 控制器，线束减少 40% |
| **小鹏 XEEA3.5** | 减少 50% 硬件，线束减重 30%，300+ 原子化服务（SOA）|
| **Tesla** | 已量产区域架构，Cybertruck/Model S Plaid |
| **宝马** | ADI E2B（10BASE-T1S + RCP）量产用于氛围照明 |
| **大众** | E3 架构，区域控制器逐步推广 |
| **蔚来** | 中央超算 + 区域控制 |
| **岚图** | ZCU 架构量产 |
| **比亚迪** | 自研 ZCU 芯片方案 |
| **理想** | 自研架构 |

## Tier1 方案

- **安波福**：MCU-less 无 MCU 方案，8–40 节点，PoDL 线束成本降低 50%+
- **马瑞利**：区域控制器模块化设计
- **大陆集团**：VCU 区域控制器系列
- **联合电子**：国内合资 Tier1，ZCU 量产

## 10BASE-T1S 生态（关键芯片商）

| 厂商 | 产品 | 特点 |
|---|---|---|
| **NXP** | S32K5（内置 10BASE-T1S PHY + 交换机）| ZCU 主芯片级集成 |
| **ADI** | AD3304（E2B）| 量产，宝马氛围照明 |
| **Microchip** | LAN8660 | 16 IO，10BASE-T1S |
| **TI** | DP83TC812 | 10BASE-T1S PHY |
| **Onsemi** | T30HM1TS3600/3610 | RCP 集成，样片 |
| **汇顶 GPAN** | GE1101 | 100 Mbps，~14 RMB，2026Q3 样品 |

## 安森美无 MCU 方案亮点

- 方案名称：无 MCU 区域节点方案
- 节点规模：8–40 个节点
- 供电方式：PoDL（以太网供电）
- 线束成本降低：**50%+**
- 已应用：宝马 ADI E2B 氛围照明（量产）

## 结论

中国市场 ZCU 渗透率快速提升，MCU Less 和 10BASE-T1S 成为 2025–2027 年核心技术趋势。国产方案（汇顶 GPAN、芯驰等）在成本和生态上有望打破海外垄断。
