---
type: source
title: "GE1101 芯片应用介绍（Goodix SDK/API 手册 V0.1）"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "Goodix Technology（汇顶科技）"
tags:
  - gpan
  - ge1101
  - sdk
  - automotive
processed: true
raw_file: "raw/pdfs/GE1101芯片应用介绍_V0.1.pdf"
raw_sha256: "0197d02ee6c6bf77379d3c5777ddd92cd199a23fe8bc8dda7a386428e6cabf94"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# GE1101 芯片应用介绍（Goodix SDK/API 手册 V0.1）

## Summary

本文件为 Goodix 汇顶科技发布的 GE1101 GPAN 芯片软件应用手册（V0.1 版本），覆盖芯片初始化流程、驱动 API 层设计及各外设接口的编程接口说明。GE1101 是 Goodix GPAN 方案的核心芯片，支持多种车载通信接口混合传输，是 MCULess 架构的关键硬件组件。

## Key Points

- **芯片定位**：GE1101 为 Goodix GPAN 网络的节点芯片，支持以太网数据、CAN/LIN 信号、音频数据的混合路由转发，在 MCULess 方案中替代边缘节点 MCU 的控制职能
- **初始化流程**：上电后依次完成寄存器复位→网络参数配置→通信接口使能→数据路由表加载，配置通过 SPI 主接口写入
- **GPIO API**：支持输入/输出/中断三种模式，每个 GPIO 引脚均可通过 API 独立配置上下拉、驱动强度和中断触发边沿
- **SPI API**：提供 Master/Slave 两种角色，支持 Mode 0/1/2/3，最高时钟可达 20MHz；同时作为芯片本身的配置接口
- **I²C API**：支持 Standard（100kHz）/ Fast（400kHz）/ Fast-Plus（1MHz）三种速率，具备 10-bit 地址扩展能力
- **CAN API**：支持 CAN 2.0A/2.0B，提供发送队列管理和接收过滤器配置；CAN 帧可通过硬件路由在 GPAN 网络中透明转发，实现跨节点 CAN-CAN 桥接
- **LIN API**：支持 LIN 2.1/2.2，Master/Slave 可配，提供帧调度表配置和自动波特率检测
- **UART API**：多路 UART，支持 DMA 模式传输，可配置为调试口或应用数据接口
- **PWM API**：支持多路独立 PWM 输出，周期/占空比可实时更新，适用于电机控制预信号、LED 调光等场景
- **音频 API（AUDIO/TDM）**：支持 TDM（Time-Division Multiplexing）多路音频流，兼容 I²S 接口，可在 GPAN 网络中透明传输音频数据帧

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/can-eth-protocol-conversion]]

## Entities Extracted

- [[entities/goodix-technology]]

## Contradictions

<!-- 暂无 -->

## My Notes

本文档为 V0.1 内部版本，API 接口可能随正式版本变更。GE1101 的 MCULess 价值在于：边缘节点无需独立 MCU 即可完成 IO 采集、信号路由和通信转换，芯片本身承担了原先 MCU 的全部软件逻辑。
