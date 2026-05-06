---
type: source
title: "PoDL技术在汽车以太网供电的创新应用"
source_url: "https://mp.weixin.qq.com/s/QCWzcz2BOFLHa7XSzSUCJA"
author: "汽车电子老登"
date: "2026-05-05"
tags: [podl, 10baset1s, automotive-ethernet, mculess-architecture, t30hm1ts3600, wire-harness]
raw_file: "raw/clippings/2026-05-05PoDL技术在汽车以太网供电的创新应用.md"
raw_sha256: 315c51247b54159c466ffc011ef95d497992c24d9019bc4f5c1bc5de7b854893
last_verified: 2026-05-05
---

## 核心摘要

PoDL（Power over Data Line）基于 IEEE 802.3cg 标准，在单根双绞线上同时传输 10Mbps 数据与 48V 直流电，为 MCU-less 边缘节点提供一线供电能力，大幅减少线束。

## PoDL 基本原理

- **标准**：IEEE 802.3cg，10BASE-T1S 物理层
- **传输介质**：单根非屏蔽双绞线（UTP）
- **数据速率**：10 Mbps
- **供电电压**：48V DC（叠加在数据信号上）
- **耦合设计**：耦合电容 CP/CM 100nF + 共模扼流圈（CMC）240μH，实现数据与电源隔离

## 核心芯片：T30HM1TS3600（Onsemi）

- **VBAT 范围**：2.97V – 52V（支持 12V/24V/48V 汽车总线）
- **工作温度**：-40°C 至 150°C（AEC-Q100 Grade 1）
- **保护机制**：POR 2.0V、欠压保护（UV）、过温保护（TSD 150°C）
- **引脚复用**：GPIO / SPI / I2C / UART / PWM / I2S / PDM（20 个物理引脚）

## AWG 线规选型对比

| 规格 | 电阻（Ω/km） | 适用功率 |
|------|------------|---------|
| 24 AWG | 85 Ω/km | 低功率节点 |
| 22 AWG | 54 Ω/km | 中等功率 |
| 20 AWG | 34 Ω/km | 中高功率 |
| 18 AWG | 21 Ω/km | 高功率节点 |

## PoDL vs CAN vs PoE 对比

| 特性 | PoDL (10BASE-T1S) | CAN FD | PoE (IEEE 802.3af) |
|------|------------------|---------|--------------------|
| 数据速率 | 10 Mbps | 8 Mbps | 100 Mbps+ |
| 供电 | 支持（48V） | 不支持 | 支持（48V） |
| 线束数量 | 1 对 | 1 对 | 2 对 |
| 多节点 | 支持（多点接入） | 支持 | 不支持多点 |
| 汽车认证 | AEC-Q100 | AEC-Q100 | 非汽车标准 |

## 区域架构应用案例

### 车门模块
- 传统方案：每个执行器独立 ECU + CAN 线
- PoDL 方案：单根双绞线连接多个 MCU-less 节点（车窗、门锁、后视镜）
- 效果：线束减少 30–50%，连接器减少 40%

### 照明系统
- 前照灯/尾灯控制节点通过 PoDL 获取电源和控制指令
- 无需独立电源线和信号线

### 传感器网络
- 摄像头、超声波传感器通过 PoDL 组成多点总线

## 成本效益分析（年产 10 万辆）

| 项目 | 节省 |
|------|------|
| 线束成本 | $120/车 |
| 装配成本 | $80/车 |
| 整车重量 | -4.5 kg/车 |
| 保修成本 | $50/车 |
| **投资回报期** | **2.5 年** |
| **NPV（10年）** | **$1800 万** |

- MCU-less 节点节省：$3–5/节点（去掉独立 MCU）
- 故障率下降：30%（减少连接点数量）

## EMI 抑制设计

- CMC（共模扼流圈）240μH 抑制共模噪声
- 差分信号传输，抗干扰能力强
- DME 编码（零直流分量）改善 EMC 性能
- 100Ω 终端匹配，防止信号反射

## 关联概念

- [[concepts/mculess-architecture]] — MCU-less 节点依赖 PoDL 供电
- [[concepts/zonal-gateway]] — 区域网关作为 PoDL 供电端
- [[concepts/rcp-remote-control-protocol]] — RCP 协议运行在 10BASE-T1S 之上
