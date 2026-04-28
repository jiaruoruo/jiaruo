---
type: source
title: "MCULess 方案验证——关键技术点与验证范围"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "内部硬件验证团队"
tags:
  - mculess
  - validation
  - latency
  - can-eth
  - automotive
processed: true
raw_file: "raw/pdfs/MCULess方案验证（关键技术点和验证范围）.pdf"
raw_sha256: "895533edef5826b02df3f85839c2f1cf771a34f28507678cdfe7d758cc493473"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCULess 方案验证——关键技术点与验证范围

## Summary

本文档定义了 MCULess 方案的验证技术要点和完整验证范围，包括 CAN-ETH/CAN-CAN/CAN-LIN 三种协议转发的延迟目标（≤100μs）、驱动控制功能验证项、关键技术挑战（触发采样、睡眠/唤醒、故障诊断），并给出了实际测量结果汇总表。

## Key Points

- **通信延迟验证目标**（3 种协议转发路径，均要求 ≤100μs）：
  - **CAN→ETH 路径**：CAN 帧经 GPAN 硬件路由转换为以太网帧发往域控制器，目标 ≤100μs
  - **CAN→CAN 路径**：两 CAN 总线之间经 GPAN 节点透明桥接，目标 ≤100μs
  - **CAN→LIN 路径**：CAN 帧路由到 LIN 子网，目标 ≤100μs
- **驱动控制功能验证项**：
  - HSD 通道开关控制（含过流/短路保护触发与恢复）
  - H-Bridge PWM 调速（0%~100% 占空比连续可调，频率 1kHz~20kHz）
  - EFUSE 可编程限流（I²C 或 SPI 远程设置阈值）
  - 传感器 ADC 采集精度（12-bit，±0.5% FSR 误差要求）
  - Hall 脉冲计数位置检测（±1 步精度要求）
- **关键技术挑战与验证方法**：
  - **触发采样（Trigger Sampling）**：GPAN 收到控制帧后触发本地 ADC 采集，验证从接收 CAN 命令到完成 ADC 采样上报的全链路延迟 ≤500μs
  - **睡眠/唤醒机制**：
    - CAN 唤醒：收到 CAN 总线 wake pattern 后 GPAN 节点唤醒主电源，实测响应 ≤115ms
    - AD 唤醒：模拟量超阈值（如 NTC 温度异常）触发唤醒，实测响应 ≤112.5ms
    - IO 唤醒：GPIO 电平变化（如门锁按键）触发唤醒，实测响应 ≤111ms
  - **故障诊断（Fault Diagnosis）**：驱动芯片故障状态（短路/过温/欠压）须在 ≤2ms 内上报到域控制器
- **实际测量结果汇总**：

  | 验证项 | 目标 | 实测结果 | 结论 |
  |---|---|---|---|
  | CAN→CAN 路由延迟 | ≤100μs | **21~62μs** | ✅ 通过 |
  | CAN→ETH 路由延迟 | ≤100μs | **43~63μs** | ✅ 通过 |
  | CAN→LIN 路由延迟 | ≤100μs | 未单独列出 | 见验证报告 |
  | 音频传输延迟 | <100μs（A2B 规格）| **40μs** | ✅ 通过 |
  | CAN 唤醒响应 | — | 115ms | ✅ |
  | AD 唤醒响应 | — | 112.5ms | ✅ |
  | IO 唤醒响应 | — | 111ms | ✅ |

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/can-eth-protocol-conversion]]
- [[concepts/zonal-gateway]]

## Entities Extracted

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Contradictions

<!-- 暂无 -->

## My Notes

CAN→CAN 路由 21~62μs 和 CAN→ETH 路由 43~63μs 两项数据远低于 ADI 10BaseT1S 的 1.09~1.32ms，实测数据有力支撑了 GPAN 在延迟竞争力上的优势。音频延迟 40μs 满足 A2B（Automotive Audio Bus）<100μs 规格，说明 GPAN 可作为 A2B 替代方案。
