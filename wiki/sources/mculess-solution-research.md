---
type: source
title: "MCULess 方案调研报告"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "内部技术调研"
tags:
  - mculess
  - gpan
  - eea
  - bzcu
  - adi-10baset1s
processed: true
raw_file: "raw/pdfs/MCULess方案调研.pdf"
raw_sha256: "33ed28fb0cb48c19e91427e94b8d3ab4eb0e92febc27ed8d5ebe3b32fb2e6a69"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCULess 方案调研报告

## Summary

本调研报告系统梳理了传统 EEA 3.0 ZCU 架构与 MCULess 架构的对比分析，重点研究 Goodix GPAN MCULess 方案与 ADI 10BaseT1S 方案的技术差异，并制定了 BZCU（Body Zone Control Unit）验证计划。报告为 MCULess 方案的技术选型提供了决策依据。

## Key Points

- **传统 ZCU 架构痛点**：
  - 每个 ZCU 节点配置独立 MCU（如 RH850/TC3xx 系列），负责本地 IO 采集和信号路由
  - 多 MCU 带来 BOM 成本高、OTA 维护复杂、PCB 面积大等问题
  - MCU 软件开发周期长，增加系统集成难度
- **MCULess 架构原理**：
  - 在 EEA 3.0 架构中，将 ZCU 节点的 MCU 职能转移到 GPAN 芯片的硬件路由层
  - 域控制器（DCU）通过 GPAN 网络直接下发控制指令到边缘节点，边缘节点仅含 GPAN 芯片 + 驱动芯片，无独立 MCU
  - 适用场景：车身域（门控/座椅/照明/雨刮）、智能电源域；**不适用**：底盘域（安全关键，MCU 不可省略）
- **Goodix GPAN vs ADI 10BaseT1S 详细对比**：

  | 参数 | Goodix GPAN（GE1101）| ADI 10BaseT1S |
  |---|---|---|
  | 控制回路延迟 | 50μs | 1.09~1.32ms |
  | 环网支持 | ✅（自愈冗余） | ❌ |
  | 最大节点 | 60 | 12 |
  | CAN/LIN 集成 | 原生支持（硬件路由） | 需外置转换芯片 |
  | 音频传输 | ✅（TDM）| ❌ |
  | MCULess 方案 | 完整支持 | 不支持 |
  | 生态成熟度 | 较新（POC 阶段） | 已有量产案例 |

- **BZCU 验证目标**：针对理想汽车 EEA 3.0 的 BZCU 节点（替代后备箱/车身控制相关 ZCU），验证 MCULess 方案在实际车身 IO 场景下的可行性
- **验证范围划定**：
  - 功能验证：HSD（High Side Driver）输出控制、桥式驱动（H-Bridge）、EFUSE 保护、传感器信号采集
  - 通信验证：CAN-ETH、CAN-CAN、CAN-LIN 协议转发延迟测试
  - 睡眠/唤醒验证：CAN 唤醒、AD 唤醒、IO 唤醒响应时间

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

<!-- 暂无 -->

## My Notes

本调研报告明确指出 MCULess 方案对底盘域（气悬、制动、转向）不适用，这与 mculess-validation-report 中的验证结论一致（气悬域 CPU 负载增加 10%，不推荐）。ADI 10BaseT1S 生态更成熟，但 GPAN 在延迟和功能集成度上有显著优势。
