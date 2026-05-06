---
type: source
title: "汽车以太网技术深度解析：从10BASE-T1S到1000BASE-T1的全面演进"
source_url: "https://mp.weixin.qq.com/s/GXSwjBnidNetwX6TkwjYlQ"
author: "汽车电子老登"
date: "2026-05-05"
tags: [automotive-ethernet, 10baset1s, 100baset1, 1000baset1, ti, rce, plca, tsn]
raw_file: "raw/clippings/2026-05-05汽车以太网技术深度解析：从10BASE-T1S到1000BASE-T1的全面演进.md"
raw_sha256: d4ae84be41a9d71a37e7ad70c205e83da20219f89c3457186cf97543f31cb3d4
last_verified: 2026-05-05
---

## 核心摘要

汽车以太网从 10BASE-T1S（10Mbps 多节点）到 100BASE-T1（100Mbps 点对点）再到 1000BASE-T1（1Gbps PAM-3），TI 提供覆盖全速率的 DP83 系列产品线，并推出 RCE 边缘节点芯片实现 MCU-less 架构。

## TI 汽车以太网完整产品线

| 标准 | TI 芯片型号 | 速率 | 关键特性 |
|------|-----------|------|---------|
| 10BASE-T1S | DP83TD530-Q1 | 10 Mbps | PLCA，多节点，低成本 |
| 10BASE-T1S | DP83TD535-Q1 | 10 Mbps | PLCA + PoDL 支持 |
| 100BASE-T1 | DP83TC814-Q1 | 100 Mbps | 点对点，汽车 EMC |
| 100BASE-T1 | DP83TC815-Q1 | 100 Mbps | MACsec 安全加密 |
| 1000BASE-T1 | DP83TG720-Q1 | 1 Gbps | PAM-3，MACsec，低延迟 |
| 1000BASE-T1 | DP83TG721-Q1 | 1 Gbps | ASIL-B 功能安全 |
| RCE 边缘节点 | DP83ED565-Q1 | 10 Mbps | 18 GPIO，2 SPI，RCE |
| RCE 边缘节点 | DP83ED567-Q1 | 10 Mbps | 34 GPIO，5 SPI，RCE |

## 三标准横向对比

| 特性 | 10BASE-T1S | 100BASE-T1 | 1000BASE-T1 |
|------|-----------|-----------|------------|
| 速率 | 10 Mbps | 100 Mbps | 1 Gbps |
| 拓扑 | 多节点共享 | 点对点 | 点对点 |
| 最大节点数 | 16（IEEE）/50（实测） | 2 | 2 |
| 最大距离 | 25m（总线）| 15m | 15m |
| 供电（PoDL） | 支持 | 不支持 | 不支持 |
| PLCA | 支持 | 不适用 | 不适用 |
| 典型应用 | 区域边缘节点 | 域控-传感器 | 骨干网/摄像头 |
| 编码 | DME（4B/5B） | PAM-2 | PAM-3 |

## RCE 芯片详细规格

### DP83ED565-Q1（小型号）

| 参数 | 数值 |
|------|------|
| GPIO | 18 路 |
| SPI | 2 路 |
| UART | 3 路 |
| ADC | 10 路 |
| PWM | 5 路 |
| 跨触发管理器 | 16 通道，响应时间 **1μs** |
| 接口速率 | 10 Mbps（10BASE-T1S） |

### DP83ED567-Q1（大型号）

| 参数 | 数值 |
|------|------|
| GPIO | 34 路 |
| SPI | 5 路 |
| UART | 3 路 |
| ADC | 10 路 |
| PWM | 5 路 |
| 跨触发管理器 | 16 通道，响应时间 **1μs** |

## TSN（时间敏感网络）机制

- **IEEE 802.1AS（gPTP）**：全局时间同步，精度 ±10ns
- **IEEE 802.1Qbv（TAS）**：时间感知整形器，确定性调度
- **IEEE 802.1Qbu（帧抢占）**：高优先级帧可中断低优先级帧
- **IEEE 802.1Qcr（异步整形）**：无需时钟同步的流量整形

## 车窗防夹案例分析

| 方案 | 响应延迟 | 实现方式 |
|------|---------|---------|
| 传统 MCU 方案 | 10–20ms | 本地 MCU 采样 + CAN 上报 |
| RCE 网络控制 | 30–50ms | RCP 指令往返（网络延迟） |
| RCE + 本地跨触发 | **1μs** | DP83ED 内置 16 通道交叉触发器，本地硬件直接响应 |

> **关键洞察**：虽然 RCE 网络控制延迟较高，但通过芯片内置的 16 通道跨触发管理器（1μs 本地响应），可在不需要 MCU 的情况下实现比传统方案更快的安全响应。

## 前照灯 RCE 方案效益

| 指标 | 传统方案 | RCE 方案 |
|------|---------|---------|
| 开发周期 | 基准 | **缩短 40%** |
| BOM 成本 | 基准 | **降低 15%** |
| PCB 面积 | 基准 | 减少（去掉 MCU） |
| OTA 复杂度 | 高（多节点） | 低（集中更新） |

## TC-10 低功耗

- 睡眠电流：35μA
- 唤醒时间：<100μs
- 支持本地 WAKE 引脚唤醒 + 网络远程唤醒

## 关联概念

- [[concepts/mculess-architecture]] — RCE 芯片是 MCU-less 的核心硬件
- [[concepts/zonal-gateway]] — ZCU 通过 1000BASE-T1 骨干网连接
- [[sources/rcp-protocol-mculess-hardware-control-deep-dive]] — RCP 在 10BASE-T1S 上运行
- [[sources/10baset1s-automotive-ethernet-technical-analysis]] — 10BASE-T1S 详细技术规范
