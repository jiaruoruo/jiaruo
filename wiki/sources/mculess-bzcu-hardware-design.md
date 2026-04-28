---
type: source
title: "基于 GPAN 的 MCULess BZCU 第一阶段硬件设计简要说明（V0.94）"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "内部硬件设计团队"
tags:
  - mculess
  - bzcu
  - hardware-design
  - gpan
  - fpga
  - automotive
processed: true
raw_file: "raw/pdfs/基于GPAN的MCULess BZCU(第一阶段)_硬件设计简要说明V0.94_20250828.pdf"
raw_sha256: "18c2b5247bddc7b8f3e25fdeec3baa886de07f0021d90aaa85539c22706687bb"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 基于 GPAN 的 MCULess BZCU 第一阶段硬件设计简要说明（V0.94）

## Summary

本文档为基于 GPAN 的 MCULess BZCU 硬件原型（第一阶段）的详细设计说明，版本 V0.94（2025年8月28日）。方案采用 4 个 GPAN 节点（1 主 + 3 从）替代原有 3 个 ZCU 域（LZCU/RZCU/BZCU），每个节点配置 2 颗 GE1101 芯片（分别作为 AFE 前端和数字路由），当前原型使用 Xilinx K7 FPGA 作为主控，量产版本将切换为 GE1101 正式流片芯片（BGA144/BGA196）。

## Key Points

- **系统架构**：
  - 4 节点 GPAN 环网：1 个主节点（Master，连接域控制器）+ 3 个从节点（Slave，分别对应 LZCU/RZCU/BZCU 功能域）
  - 主节点通过 100BASE-T1 以太网连接上层域控制器（如理想汽车 BCM）
  - 从节点通过 GPAN 环网接收控制指令，执行本地 IO 操作
- **每节点双芯片配置**：
  - **GE1101 #1（AFE 角色）**：模拟前端处理，负责 ADC 采集（传感器/Hall/温度）和 PWM 生成（驱动控制信号）
  - **GE1101 #2（数字路由角色）**：CAN/LIN 协议路由，以太网帧收发，TDM 音频处理，及节点间 GPAN 帧转发
  - 双芯片通过内部 SPI 互联共享数据
- **FPGA 原型（第一阶段）**：
  - 主控芯片：**Xilinx Kintex-7（K7）FPGA**，替代尚未量产的 GE1101 正式芯片
  - K7 FPGA 运行 GE1101 的行为级仿真 RTL，验证硬件路由逻辑和时序
  - 原型板尺寸：满足实车安装要求，PCB 4 层板，板载 DC-DC 电源（12V→3.3V/1.8V/1.2V）
- **量产封装方案**：
  - **BGA144**：适用于空间受限的从节点（如 LZCU/RZCU），体积小，散热通过铜皮扩散
  - **BGA196**：适用于主节点或功能更复杂的节点，IO 引脚更多，支持更多通信接口
- **替代的 ZCU 域功能**：
  - **LZCU（左区域控制单元）**：控制左侧车门锁/窗/镜/灯/雨刮等负载
  - **RZCU（右区域控制单元）**：控制右侧对应功能
  - **BZCU（后备箱区域控制单元）**：控制后备箱电动开合、充电口、牌照灯、后雷达等
- **关键设计约束**：
  - 全局时钟同步：4 个节点通过 GPAN PTP 协议同步，目标 ≤40ns 时钟偏差
  - 环网冗余：任一节点或链路失效，环网在 ≤2ms 内完成重构（Ring Healing）
  - 工作温度：-40°C ~ +85°C（车规 AEC-Q100 Grade 1 要求）

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/zonal-gateway]]
- [[concepts/eea-architecture]]
- [[concepts/can-eth-protocol-conversion]]
- [[concepts/time-sensitive-networking]]

## Entities Extracted

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Contradictions

<!-- 暂无 -->

## My Notes

第一阶段使用 Xilinx K7 FPGA 而非 GE1101 量产芯片，说明芯片尚处于工程样品/流片阶段（文档日期 2025-08-28）。双 GE1101 配置（AFE + 路由）是当前原型的特殊设计，量产版本可能合并为单芯片（GE1101 集成 AFE 功能）。4节点替代3个ZCU域是以增加一个 Master 节点为代价换取集中控制的灵活性。
