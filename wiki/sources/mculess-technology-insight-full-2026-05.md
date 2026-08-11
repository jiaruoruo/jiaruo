---
type: source
title: "MCU-less 技术洞察（详尽版）：机会分析 · 技术方案 · 执行策略"
date: 2026-05-02
source_url: ""
domain: "internal"
author: "内部整理"
tags: []
processed: true
raw_file: raw/工作/articles/MCULess/2026-05-02-mculess-technology-insight-full.md
raw_sha256: 1e992ed539a83f5b9f324fc846e2bd03f350c754adc4696b34ad5e9f97b0985e
last_verified: 2026-07-14
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCU-less 技术洞察（详尽版）：机会分析 · 技术方案 · 执行策略

## Summary

按 Why→What→How 三段式深度分析 MCU-less 技术趋势。覆盖汽车 ZCU 市场（2024 年 39.3 亿元，渗透率 8.83%）和机器人量产爬坡期。汽车与机器人架构同构映射（CCU→主控/ZCU→肢体控制器/ECU→关节模组）。MCU-less 适用范围为车身舒适域 ASIL-B 以下，ASIL-D 必须保留本地 MCU。四大技术路线对比（10BASE-T1S+RCP / 100BASE-T1+RCP / CAN FD Light / UART over CAN）。

## Key Points

- 中国 ZCU 市场 2024 年 39.3 亿元，渗透率 8.83%，2026-2028 翻倍至 20%+
- 三代 EEA 演进：分布式(50-100 ECU) → ZCU(30-50) → MCU-less(50-80 RCP 节点，零边缘固件)
- MCU-less 线束减 60%、新功能 TTM 从 12-24 月降至 3-6 月、整车 BOM 节省 30%
- 汽车与机器人架构同构：CCU=主控计算机、ZCU=肢体控制器、ECU=关节模组+外设节点
- ASIL-D 功能安全（制动/转向/气囊）必须保留本地 MCU，MCU-less 仅适用 ASIL-B 以下
- 竞品全景：ADI AD3304(E2B) 宝马量产最成熟、汇顶 GE1101 100Mbps/120路IO 2026Q3 样品、ST CAN FD Light 低成本
- 特斯拉 Optimus Gen2 已验证 ASIC 化关节模组 MCU-less 可行性，全球首例量产

## Concepts Extracted

- [[mculess-architecture]]
- [[gpan-communication]]
- [[eea-architecture]]
- [[automotive-ethernet-10base-t1s]]
- [[rcp-remote-control-protocol]]
- [[vehicle-domain-controller]]
- [[zonal-gateway]]
- [[functional-safety]]
- [[humanoid-robot]]
- [[time-sensitive-networking]]

## Entities Extracted

- [[goodix-technology]]
- [[tesla-optimus]]
- [[unitree-robotics]]
- [[li-auto]]

## Contradictions

## My Notes
