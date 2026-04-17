---
type: concept
title: "CAN-ETH 协议转换"
date: 2026-04-16
updated: 2026-04-16
tags:
  - automotive
  - can-bus
  - ethernet
  - protocol
  - gateway
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-04-16
aliases:
  - "CAN-ETH 协议转换"
  - "CAN to Ethernet Protocol Conversion"
  - "can-eth-protocol-conversion"
  - "XoverETH"
  - "CAN-ETH互转"
  - "CAN以太网协议转换"
---

# CAN-ETH 协议转换（CAN-to-Ethernet Protocol Conversion）

## Definition

CAN-ETH 协议转换是指在整车骨干网由 CAN 总线向以太网（Ethernet）迁移过程中，实现 CAN 帧与以太网数据包之间高效、低延迟双向转换的标准化技术。随着 EEA 架构向中央计算+区域控制演进，区域网关（ZCU）需要在 CAN/LIN 节点与 ETH 骨干网之间充当协议转换桥梁，支撑车身/底盘/动力等功能集中部署于中央算力单元（CCU）。

## Key Points

- **核心场景**：整车 EEA 3.0/4.0 架构中，ZCU 负责将域内 CAN/CANFD/LIN 报文转换为以太网帧，通过 100M ETH 上行至 CCU；反向亦然（ETH→CAN 直接路由）
- **轻量协议路线**：跳过完整 TCP/IP 协议栈，直接基于以太网底层协议路由，减少封装/解封装时间；CAN-ETH-CAN 场景使用精简协议定义；CAN-ETH 上行复用 MVBS-DDS（SOME/IP）协议
- **帧结构设计**：以太网帧含 IEEE 802.1Q VLAN Tag（TPID 0x8100），3bit PRI 字段承载 CAN 报文优先级；上层采用 IP/UDP/SOME/IP 封装；PduHeader ID 承载 CAN Bus ID + CAN ID 映射
- **触发策略**：触发式/周期<10ms 报文设置 TRIGGER_ALWAYS（立即发送）；周期≥10ms 报文设置 TRIGGER_NEVER + 1ms 超时或缓存>640字节时发送，兼顾实时性与带宽效率
- **优先级调度**：支持多业务并发的优先级调度策略；配合 TSN（IEEE 802.1Qbv）时间感知整形，保障高优先级 CAN 报文（刹车/转向等）确定性传输
- **关键性能指标**：单帧（≤512字节以太网帧）处理时间 <30μs；100 CAN frames/100ms 容量（CPU <5%，内存 <5%）；触发式报文端到端 <1ms；周期<20ms 报文抖动 <±20%；周期≥20ms 报文抖动 <±10%
- **冗余支持**：支持报文一对多协议转换冗余，配合动态路由策略实现链路故障切换

## My Position

## Contradictions

## Sources

- [[sources/distributed-gateway-communication-tdt]]

## Evolution Log

- 2026-04-16（1 sources）：概念初建，来源为分布式网关通信TDT内部预研立项文档
