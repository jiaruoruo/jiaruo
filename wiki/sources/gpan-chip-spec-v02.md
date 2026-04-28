---
type: source
title: "GPAN 芯片规格介绍文档 V0.2（2025-08-05）"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "深圳市汇顶科技股份有限公司"
tags:
  - gpan
  - ge1101
  - chip-spec
  - application-scenarios
  - automotive
processed: true
raw_file: "raw/articles/GPAN芯片规格介绍文档_V0.2 2025-08-05.docx"
raw_sha256: "5080ab7389e3b74d0440335f7be68092f57ee4c3e2bd8c43cf09c5c30a883b48"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# GPAN 芯片规格介绍文档 V0.2（2025-08-05）

## Summary

本文档为 Goodix 汇顶科技发布的 GPAN 芯片规格澄清介绍文档（V0.2，2025-08-05），是 GE1101 芯片完整功能规格的权威参考，详细描述了芯片的 MCULess 应用需求、IO 规格全表、主要方案场景列表，以及驱动芯片闭环控制、Hall 采集、ADC、PWM、唤醒、CAN/LIN 路由转发、分布式功放等典型应用场景的系统框图和软件使用说明，同时包含软件与 GPAN 网络解耦设计（逻辑地址→物理地址映射）和数据低时延优化方案。

## Key Points

- **GE1101 功能 IO 完整规格**：

  | 规格项 | 规格 | 说明 |
  |---|---|---|
  | IO 电压 | 2.7V~5.5V | 普通 IO ESD 2kV；MDI IO ESD 8kV |
  | 封装 | BGA144(8×8mm) / BGA196(10×10mm) | 0.65mm ball pitch |
  | MDI（100Base-T1 PHY）| 2 个 | 仅用于 GPAN 组网，不支持直连交换机 |
  | SPI-S/QSPI-S | 3 个 | SPI-S 25MHz，QSPI-S 100MHz |
  | SPI-M | 3 个 | 全双工，支持 CS 选择 |
  | MII/RMII | 2 个 | MII/RMII0：外部数据传输；MII/RMII1：IO 扩展 |
  | DMIC | 1 个 | 数字麦克风，输出 2 路 TDM |
  | I2S/TDM | 2 个 | TDM0：音频输入输出；TDM1：仅主节点音频输出 |
  | CAN/CAN-FD | **5 个** | 支持 CAN/CAN-FD 可配，内置硬件网关 |
  | LIN | **5 个** | 内置硬件网关 |
  | I2C | 1 个 | 支持 8 个 device 中断，最高 1MHz |
  | UART | 1 个 | 最高 115200 波特率 |
  | GPIO | **50 个** | 输入/输出可配，中断/上下拉可配 |
  | PWM-Out | **24 个** | 频率/占空比可配，精度支持 1‰（50kHz）或 1%（500kHz） |
  | PWM-In | **8 个** | 频率/占空比/脉冲计数 |
  | ADC | **16 路** | 12-bit，2M 采样率，支持 PWM/Timer 触发，Emux 4 路选择 |
  | 唤醒规格 | **82 路** | 数字 8 + 模拟 64 + CAN 5 + LIN 5 |

- **7 大典型应用场景**：
  1. **驱动芯片闭环控制**：IO 输出控制（HSD/EFUSE）、PWM+ADC 回采（低边开关）、SPI+PWM 组合（H-Bridge L9945）、PWM 捕获（脉冲统计）、触发 ADC+数字唤醒
  2. **Hall 采集**：单通道脉冲计数或双通道正/反转检测，支持时间戳上报（1ms 任务周期），双路 BLDC 换向检测
  3. **ADC 采集**：软件触发/PWM 触发/Timer 触发并行采样，8 个 PWM 触发源 + 8 个 Timer 触发源，最多 32 通道同一采样包
  4. **PWM 方案**：24 路独立 PWM，频率/占空比可实时更新
  5. **唤醒方案**：数字（8 GPIO 边沿/电平）+ 模拟（64 路 ADC 阈值，轮询 8-bit 精度）+ CAN（PID 范围过滤）+ LIN（Rx GPIO）
  6. **CAN/LIN 路由转发**：最多 1→32 路转发，支持协议互转（不改变 Payload），路由表 256 深度，新包生成时延 **<2μs**，查表为空的包可配丢弃或上报主节点
  7. **分布式功放**：GPAN TDM 替代 A2B 总线，仅需初始化配置音频声道数/采样率/数据精度/I2S-TDM 模式
- **软件与 GPAN 网络解耦设计**：
  - 应用服务映射到逻辑地址（`0xaaaabbbb` 等）→ 不同车型加载不同逻辑地址→物理节点映射表
  - 支持高端车型 6 节点和低端车型 4 节点共用相同软件架构，仅切换映射表
- **数据低时延优化**：
  - 默认采用最低延迟转发方案（GPAN 帧到达即转发）
  - 高优先级数据可替换低优先级数据（优先级抢占）
  - 专用子帧：为子节点设置专用帧保障实时性，但过多专用帧会降低带宽利用率

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/can-eth-protocol-conversion]]
- [[concepts/zonal-gateway]]

## Entities Extracted

- [[entities/goodix-technology]]

## Contradictions

<!-- 暂无 -->

## My Notes

本文档是 GE1101 芯片最完整的功能规格参考，V0.2 版本（2025-08-05），比 V0.1 应用介绍手册更系统。CAN/LIN 路由转发新包生成时延 <2μs 是重要指标——这是芯片硬件路由的内部处理时延，加上网络传播时延后才得到端到端的 21~62μs 测量值。软件/网络解耦设计是 GPAN 跨车型复用的关键架构创新点。
