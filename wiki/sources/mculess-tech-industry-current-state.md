---
type: source
title: "MCU-LESS技术行业现状与应用设想"
date: 2026-06-28
source_url: ""
domain: "internal-note"
author: "未知"
tags: [mculess, gpan, rcp, automotive-ethernet, goodix, adi, nxp, zcu]
processed: true
raw_file: "raw/clippings/MCU-LESS.md"
raw_sha256: f9d8b35f9a3d6a6d5684e39b8d3a10e87007a8a22547ed1088a321406d3b0c65
last_verified: 2026-07-13
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCU-LESS技术行业现状与应用设想

## Summary

一份内部技术笔记（疑似车企 EEA 团队），梳理 MCU-LESS 两条技术路线的行业现状与上车设想。路线一为 **RCP + 10Base-T1S**（ADI AD330x MACPHY、NXP TJA1415，基于 IEEE 802.3cg，10Mbps 半双工多点拓扑，PLCA 确定性调度，最小周期 1ms）；路线二为 **GPAN**（汇顶 GE1101，100M 全双工，类 EtherCAT 私有协议，PTP 精度约 80ns，转发时延约 1.4us）。笔记给出三层应用架构设想（顶层高算力 SoC 虚拟 MCU / 中间层 Zone Controller 或 MCU-LESS / 底层无 MCU 哑硬件），并附汇顶 GPAN 芯片资源 MAP 表、ZCU 二级网络成本评估（左前/右前/后 ZCU 合计节约约 161 元/车）、整车控制器通信类型梳理、OC 项目量产验证（Master PZCU + Slaver SCU/CTM，当前 MCU S32K144）。

> ⚠ 此来源缺少标准 frontmatter，来源未知（推断为内部技术笔记），部分数据为内部验证进展（截止 11.15），可能已过时。

## Key Points

- **RCP/10Base-T1S 路线**：底层通信基于 10M Base-T1S，调度型通信，最小调度周期 1ms，可用带宽有限，适用于实时性与数据量同 CAN/CANFD 场景；已有芯片 Pin 少（20~40 Pin），IO 有限；ADI/NXP/TI/ON 下一代产品暂未规划
- **GPAN 路线**：底层基于 100M 以太，类 EtherCAT 全双工，时延小，适用较大数据量高实时性；缺点为私有协议、现有软件工具链基本不支持；已有 48Pin 原型芯片，27 年规划 48/144/196 Pin，外设丰富；国内仅汇顶一家，注意供应风险
- **三层应用架构**：顶层 SoC 集成虚拟 MCU（+高性能多核 MCU）；中间层 Zone Controller 或 MCU-LESS（全车仅剩 2-4 颗大 MCU）；底层无 MCU（执行器变哑硬件/智能驱动，传感器变原始数据发送者），消灭数十个分布式 MCU
- **应用目标**：降 BOM、减软件/OAT 节点数、提软件迭代效率、PCB 小型化
- **成本评估**：左前 ZCU 125→104 元、右前 103→92 元、后 ZCU 171→42 元，二级网络合计节约约 161 元/车
- **验证进展（截止 11.15）**：底层功能调试已完成 31 项、解决 22 问题；调试中 8 项、未解决 8
- **汇顶量产计划**：2025-12-24（具体节点空缺，疑为内部占位）

## Concepts Extracted

- [[mculess-architecture]]
- [[gpan-communication]]
- [[rcp-remote-control-protocol]]
- [[automotive-ethernet-10base-t1s]]
- [[zonal-gateway]]

## Entities Extracted

<!-- 以下实体页暂未创建（汇顶 GE1101、ADI AD330x、NXP TJA1415 为芯片型号，可后续单独摄入建立实体页）；以纯文本标注
- Goodix GE1101 — 汇顶 GPAN MCULess 芯片
- ADI AD330x — ADI 10Base-T1S MACPHY 系列
- NXP TJA1415 — NXP 10Base-T1S 收发器
-->

## Contradictions

- 与 [[sources/mculess-tech-comparison-analysis]]（引用 raw/articles/MCU-LESS.md）可能为同一主题的另一种整理版本，但本文件位于 raw/clippings/ 且内容侧重行业现状对比与内部验证，二者角度不同，暂按独立来源处理；建议后续 REFLECT 时核对是否为同一原始资料的重复摄入。

## My Notes

- 来源文件无 frontmatter、无作者、无 URL，按 CLAUDE.md「缺少 frontmatter」规则处理：date 取文件系统推断（2026-06-28，与同期其他 clippings 一致），标注「来源未知」。
- 内容含大量内部数据（成本表、验证进展、整车控制器清单），敏感度高，仅作技术现状记录，不对外传播。
