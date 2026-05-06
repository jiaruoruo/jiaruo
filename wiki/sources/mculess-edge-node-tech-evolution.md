---
type: source
title: 从分布式ECU到MCU-less边缘节点的技术演进之路
slug: mculess-edge-node-tech-evolution
date: 2026-04-28
source_url: https://mp.weixin.qq.com/s/EmmY1DMTEcXes9tdcH79AA
author: 汽车电子老登
published: 2026-04-28
ingested: 2026-04-28
raw_sha256: e396099781d6268f1de134012c4a8279e9bf333af6430d4e05839293d3396f65
raw_file: "raw/clippings/2026-04-28从分布式ECU到MCU-less边缘节点的技术演进之路.md"
tags: [mculess, 10base-t1s, rcp, gpan, can-fd-light, automotive, eea]
concepts: [mculess-architecture, eea-architecture, can-eth-protocol-conversion, zonal-gateway]
entities: [goodix-technology]
last_verified: 2026-04-28
---

# 从分布式ECU到MCU-less边缘节点的技术演进之路

## 核心摘要

系统梳理分布式 ECU 架构的痛点，分析 ZCU 过渡方案的矛盾，深入解析 MCU-less 核心创新（控制逻辑上移），并对比 10BASE-T1S、CAN FD Light、GPAN 三种主流连接技术路线。

## 传统分布式 ECU 痛点

- 整车 ECU 数量 100–150 个，线束长达 5 km
- 重量、成本、研发复杂度持续攀升
- 软件升级需逐一刷写多个独立 MCU，OTA 困难

## ZCU 过渡方案的矛盾

- ZCU 本身算力提升，但边缘节点 MCU 数量并未显著减少
- 通信协议多样（CAN/LIN/FlexRay/Ethernet 并存），集成复杂
- 真正的"中央计算"需要边缘节点进一步简化

## MCU-less 核心创新：控制逻辑上移

边缘节点去掉 MCU，仅保留：
- IO 扩展芯片（RCP 芯片）负责物理信号采集与输出
- 通过 10BASE-T1S 单对以太网上报/接收指令
- ZCU 运行完整控制逻辑，通过 RCP 协议直接操控边缘 IO

## 三大连接技术对比

| 技术 | 物理层速率 | 拓扑 | 成本 | 时延 | 代表产品 |
|---|---|---|---|---|---|
| 10BASE-T1S | 10 Mbps | 多节点 Multi-drop | 中（约十几元 MAC+PHY）| 确定性（PLCA）| ADI AD3304, Onsemi T30HM1TS3600, Microchip LAN8660 |
| CAN FD Light | 500 Kbps–2 Mbps | 总线 | 低（几毛） | 低 | ST 1991dlh32 |
| GPAN（GE1101）| 100 Mbps | 星型/混合 | 低（~14 RMB） | ~50 μs | 汇顶科技 GE1101 |

## 软件集中化收益

- 整车 OTA 统一推送，无需逐节点刷写
- ZCU 侧软件动态调度，边缘节点功能按需配置
- 安全策略集中部署，减少攻击面

## 产业生态现状

- **ADI AD3304**：量产，宝马采用，$1.3，12 IO，10 Mbps，<1ms 延迟
- **Onsemi T30HM1TS3600/T30HM1TS3610**：样片阶段，10/20 IO，10 Mbps，<1ms
- **Microchip LAN8660**：16 IO，10BASE-T1S
- **汇顶 GPAN GE1101**：100 Mbps，~50 μs，预计 **2026 年 7 月出样品**
- **ST CAN FD Light**：面向简单执行器场景
