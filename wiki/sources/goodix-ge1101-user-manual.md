---
type: source
title: "GE1101 用户使用手册（硬件寄存器手册 V0.1）"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "Goodix Technology（汇顶科技）"
tags:
  - gpan
  - ge1101
  - hardware
  - register
  - automotive
processed: true
raw_file: "raw/pdfs/GE1101用户使用手册_V0.1.pdf"
raw_sha256: "b63589417d27d9479a2c68f6f95e11dc7f33e0165eaf35d6be37c3587424b084"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# GE1101 用户使用手册（硬件寄存器手册 V0.1）

## Summary

本文件为 Goodix GE1101 GPAN 芯片硬件寄存器级使用手册，详细描述芯片引脚定义、网络拓扑配置寄存器、音频 TDM 帧格式、PTP 时间同步寄存器，以及 MII/SPI/I²C/CAN 等通信接口的底层配置。适合进行驱动开发和 FPGA 原型验证的工程师参考。

## Key Points

- **封装与引脚**：GE1101 采用 QFN48 封装（部分版本支持 BGA144/BGA196 升级包），引脚包含 RGMII/MII 以太网接口、SPI 配置接口、GPIO 扩展口、CAN/LIN 差分对、TDM 音频接口及 PTP 脉冲接口
- **网络拓扑寄存器**：
  - 环网模式（Ring Mode）：通过 `NET_TOPO_REG[1:0]=2'b01` 配置，支持自愈冗余
  - 菊花链模式（Daisy Chain）：`NET_TOPO_REG[1:0]=2'b00`，线性级联
  - 节点地址寄存器：`NODE_ADDR_REG[5:0]`，支持最多 64 个节点地址（0~63）
- **以太网 MII 接口**：标准 MII 信号（TX_CLK/RX_CLK/TXD/RXD/TX_EN/RX_DV），100BASE-TX 速率，通过 `PHY_CTRL_REG` 配置 Auto-Negotiation
- **CAN 接口寄存器**：
  - 波特率配置：`CAN_BRP_REG`（预分频系数）+ `CAN_SEG_REG`（位时间段）
  - 路由规则：`CAN_ROUTE_TABLE[7:0]` 指定 CAN 帧 ID 到目标 GPAN 节点的映射
  - 接收过滤：`CAN_FILTER_REG` 支持掩码过滤和精确 ID 过滤
- **音频 TDM 寄存器**：
  - 帧格式：`TDM_FRAME_REG`（帧长度：16/32/48/64 bit）
  - 时隙数量：`TDM_SLOT_REG[3:0]`，最多 16 个时隙
  - GPAN 音频传输延迟目标：<40μs（硬件路由无软件介入）
- **PTP 时间同步寄存器**：
  - 本地时钟：`PTP_CLK_REG[31:0]`（64-bit 扩展），精度目标 ≤40ns（硬件时间戳）
  - Sync/Follow-Up 消息控制：`PTP_MSG_CTRL_REG`
  - 主从角色配置：`PTP_ROLE_REG[0]`（0=Slave，1=Master）
- **SPI 配置接口**：芯片所有配置寄存器通过 SPI Mode 0 的 16-bit 地址 + 32-bit 数据帧访问，最高 10MHz 时钟

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

寄存器手册是 FPGA 原型阶段（Xilinx K7）验证所必需的参考文档。GE1101 的 PTP 硬件时间戳精度（≤40ns）优于 GPAN 概念页中描述的软件方案目标（≤2μs），后续需更新概念页以反映硬件时间戳的实际精度上限。
