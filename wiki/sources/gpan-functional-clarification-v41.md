---
type: source
title: "GPAN 部分功能澄清文档 V4.1"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "深圳市汇顶科技股份有限公司"
tags:
  - gpan
  - frame-format
  - initialization
  - sleep-wakeup
  - watchdog
  - automotive
processed: true
raw_file: "raw/articles/GPAN部分功能澄清文档_V4.1.docx"
raw_sha256: "924131503410fbbe4a70d19567e1f2d6788807cbdf8e2696e78a5c13254b7d53"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# GPAN 部分功能澄清文档 V4.1

## Summary

本文档为 Goodix 内部 GPAN 功能澄清文档（V4.1），深度解析 GPAN 帧格式（72-bit 公共头 + 音频数据 + 数据子块 + HACK）、两种组网初始化方式、完整睡眠/唤醒机制（包括 TC10 支持、Force Sleep 流程）、看门狗、中断系统（192-bit 中断源）、监听模式、两级缓存与流控设计，是理解 GPAN 协议底层实现的最详尽技术文档。

## Key Points

- **GPAN 帧格式**：
  - 公共头：**72 bit**，包含音频长度、热节点指示、大/小包长度与个数、方向等
  - 帧结构：`公共头(72bit) + 音频数据 + 数据子块(多个) + HACK`
  - 子块头：**48 bit**，包含优先级、方向、源/目的节点、是否需要 HACK、Payload 长度、数据类型、组播号
  - MCU→GPAN 通信格式：简化版（节点信息 + 数据类型 + Payload），芯片自动组包为 48-bit 子块头
- **两种组网初始化方式**：
  - **MCU 软件配置**：依次配置主节点→子节点寄存器，5 节点完成约 190μs（SPI 配置）+ 250μs（节点间通信）+ 10ms×n（建链）
  - **硬件自组网**：Strap pin 配置 PHY master/slave，主节点发初始化包流经每节点后自动配置，5 节点总耗时 <15ms（建链并行进行）；比 MCU 软件配置快约 10 倍
- **睡眠机制（Force Sleep + TC10）**：
  - 流程：配置 `rg_wake_det_wait_en=1` + 等待时间 → 由远及近配置 `rg_force_sleep` → 所有节点进入 Sleep 态
  - 睡眠等待期间：不检测网线信号，但其他唤醒源仍工作并记录状态
  - 睡眠时间默认 32ms，唤醒时间默认 8ms（可配）
  - 同时支持 TC10 睡眠唤醒标准
- **4 种唤醒方式**：
  - **网线唤醒**：PHY 能量检测，节点被唤醒后通过 PHY 向相邻节点传递唤醒信号（链式唤醒）
  - **CAN 唤醒**：PID 范围过滤（每路 3 个范围），支持 Standby 快速唤醒→Sleep 防误唤醒
  - **数字 IO 唤醒**：16 路 GPIO，支持上升沿/下降沿/高电平/低电平，支持持续时间配置防抖
  - **模拟 ADC 唤醒**：32 路轮询采样，支持独立门限值（大于/小于/等于/区间），最大 128 次平均处理
- **看门狗**：
  - 基于独立 RC 振荡器（25MHz），与业务时钟独立
  - 支持超时模式（计数归零触发复位）和窗口模式（太早或太晚喂狗均触发复位）
  - 双看门狗互补检测（两个均失效才复位）
  - 最大计数周期约 171 秒
- **中断系统（192-bit 中断源）**：
  - PHY 建链状态（[31:0]）：link_up/down、SQI 告警、ESD 错误、TC10 睡眠/唤醒状态
  - PHY 时钟诊断（[95:80]）：PTP TX/RX 中断
  - 外设异常（[119:239]）：SPI/I2C/UART/CAN/LIN 各外设中断
  - 数据调度（[287:272]）：缓存将满热节点告警
  - 支持高/低电平两种中断输出极性，前后中断间隔时间可配（165μs~10s）
- **监听模式（Monitoring Mode）**：
  - 任意节点可配置为监听节点，复制所有流经该节点的 GPAN 帧
  - 可选择监听 PHY A 或 PHY B 方向数据
  - 不影响正常转发，适用于调试分析和系统监控
- **两级缓存与流控**：
  - 一级缓存：每外设独立存储空间
  - 二级缓存：各外设共用（剩余 <1KB 时触发热节点告警）
  - MCU 写入 GPAN 带宽须 < 所有外设发送带宽之和，否则长期运行会写满缓存

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/can-eth-protocol-conversion]]
- [[concepts/time-sensitive-networking]]

## Entities Extracted

- [[entities/goodix-technology]]

## Contradictions

<!-- 暂无 -->

## My Notes

硬件自组网 <15ms（vs MCU 软件配置数百 ms）是生产部署的重要优势。192-bit 中断系统的设计表明 GPAN 具备完整的系统自诊断能力。双看门狗互补检测体现了功能安全考量（但芯片 ASIL 等级仍为 QM/B，文末问题点"ASIL B 什么时候通过"说明认证尚未完成）。监听模式对于系统调试和售后诊断非常有价值。
