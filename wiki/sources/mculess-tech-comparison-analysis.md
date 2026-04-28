---
type: source
title: "MCU-LESS 技术行业现状分析与应用场景设想"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "内部技术分析（理想汽车项目相关）"
tags:
  - mculess
  - gpan
  - adi-10baset1s
  - zcu
  - cost-analysis
  - automotive
processed: true
raw_file: "raw/articles/MCU-LESS.md"
raw_sha256: "f9d8b35f9a3d6a6d5684e39b8d3a10e87007a8a22547ed1088a321406d3b0c65"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCU-LESS 技术行业现状分析与应用场景设想

## Summary

本文档为内部 MCU-LESS 技术分析笔记，系统对比了 RCP（ADI/NXP 10Base-T1S）与 Goodix GPAN 两种 MCULess 实现方案，提出了三层 MCULess 架构设想（SoC 层/区域层/边缘层），并给出了基于理想汽车 ZCU 体系的详细 BOM 成本核算（总二级网络节省 161 元），以及整车控制器清单和 OC 项目量产验证规划。

## Key Points

- **RCP（10Base-T1S）vs GPAN 对比**：

  | 维度 | ADI/NXP RCP（10BaseT1S）| Goodix GPAN |
  |---|---|---|
  | 带宽 | 10M（半双工） | 100M（全双工） |
  | 时钟同步精度 | IEEE 802.1AS | **PTP ≈80ns** |
  | 转发时延 | — | **约 1.4μs** |
  | 休眠唤醒协议 | OPEN Alliance TC10/TC14 | 自定义 + 支持 TC10 |
  | 典型芯片 | ADI AD3301/4/5，NXP TJA1415 | GE1101 |
  | 芯片 Pin 数 | 20~40 Pin（IO 较少） | 48/144/196 Pin |
  | RCP 总结 | 最小调度周期 1ms，带宽有限；国外公司下代未明确规划 | 通信协议为私有协议，国内仅汇顶一家 |

- **MCULess 三层架构设想**：
  - **顶层（High-End）**：超强算力 SoC 集成虚拟 MCU + 高性能多核 MCU
  - **中间层（Zonal）**：高性能多核 MCU（Zone Controller）或 MCU-LESS；全车仅剩 2~4 颗大 MCU
  - **底层（Edge）**：完全 MCU-LESS，执行器变"哑巴硬件"或"智能驱动"，消灭门控/座椅/灯控/水泵等数十个分布式 MCU
- **详细 BOM 成本核算**（基于理想汽车 ZCU + 4851 IO 扩展芯片替代方案）：

  | ZCU 节点 | 当前方案成本 | GPAN 方案成本 | 节省 |
  |---|---|---|---|
  | 左前 ZCU（TC389 + 16×4851）| **125 元** | 104 元（2×BGA144） | **21 元** |
  | 右前 ZCU（TC389 + 8×4851）| **103 元** | 92 元（1×BGA144） | **11 元** |
  | 后 ZCU（TC399 + 18×4851）| **171 元** | 42 元（BGA144×2+BGA196） | **129 元** |
  | **二级网络总计** | — | — | **161 元** |

  - GPAN 芯片价格参考：QFN64 9 元（T1），BGA144 12 元，BGA196 18 元
  - 4851（8选1 IO 扩展）价格参考：2.5 元/颗，硬件面积 64mm²/颗
- **BZCU IO 支持性验证**（汇顶 MCU-LESS 芯片资源 vs BZCU 需求 MAP）：
  - 支持：IA/IDL/ID/HALL/PWM 输入，PWM/OD 输出，SPI/I2C/RMII/CAN-FD/LIN 总线
  - **不支持**：SENT 信号（硬件不支持），PSI5（需 SPI 转 PSI5 外接芯片）
- **关键验证项**（截止 11.15 进展）：已完成 31 项，调试中 8 项，已解决 22 个问题，未解决 8 个
- **待验证难点**：车窗/座椅防夹、底盘高度传感器 1ms 采集、SENT/PSI5 专用信号、休眠功耗与唤醒时间、高功能安全处理（EPB ASIL-D、主动悬架 ASIL-C）、主节点资源（RAM/Flash/CPU）
- **OC 项目量产验证规划**：
  - MCU-LESS Master：PZCU（电源域控）
  - MCU-LESS Slave：SCU 或 CTM（当前 MCU：S32K144）

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/zonal-gateway]]
- [[concepts/eea-architecture]]
- [[concepts/can-eth-protocol-conversion]]

## Entities Extracted

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Contradictions

- 本文给出的二级网络总节省为 **161 元**，而 [[sources/mculess-solution-progress]] 提到每套 3 个 ZCU 节省约 **141 元**——差异来自计算范围：本文含右前 ZCU（实际只用 1 颗 BGA144 做 IO 扩展，无独立 GPAN）；两文档对"GPAN 节点配置"的假设不同，并不矛盾，需结合具体车型硬件规格确认

## My Notes

本文档揭示了 GPAN 相对传统 4851 IO 扩展芯片方案的真实成本对比——后 ZCU 节省 129 元的核心来自用 BGA196（150 IO）完全替换 18 颗 4851。SENT 和 PSI5 不支持是重要边界条件：底盘传感器大量使用 PSI5，这进一步限制了 MCULess 在底盘域的可行性。
