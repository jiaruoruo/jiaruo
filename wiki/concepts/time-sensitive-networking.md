---
type: concept
title: "时间敏感网络"
date: 2026-04-16
updated: 2026-04-16
tags:
  - networking
  - tsn
  - real-time
  - automotive
  - ethernet
source_count: 1
confidence: low
domain_volatility: low
last_reviewed: 2026-04-16
aliases:
  - "时间敏感网络"
  - "Time-Sensitive Networking"
  - "time-sensitive-networking"
  - "TSN"
  - "IEEE 802.1 TSN"
  - "确定性以太网"
---

# 时间敏感网络（Time-Sensitive Networking，TSN）

## Definition

时间敏感网络（Time-Sensitive Networking，TSN）是 IEEE 802.1 工作组制定的一套以太网扩展标准集，通过时间感知整形（TAS，IEEE 802.1Qbv）、帧抢占（802.1Qbu）、信用整形（802.3br）等机制，在标准以太网基础上实现有界延迟、极低抖动的确定性数据传输。TSN 是车载网络和工业网络中高实时性通信的核心使能技术，为 CAN-ETH 协议转换场景中高优先级报文的确定性传输提供保障。

## Key Points

- **核心标准**：IEEE 802.1Qbv（时间感知整形，TAS）——通过门控列表（GCL）将时间划分为时间槽，为不同优先级流量预调度专用传输窗口；IEEE 802.1Qbu（帧抢占）——允许高优先级帧中断低优先级帧传输；802.1AS（精确时间协议，gPTP）——全网时间同步基础
- **在 CAN-ETH 转换中的作用**：为高优先级 CAN 报文（刹车、驾驶控制、底盘稳定等）预留专用传输时间槽，避免被低优先级流量（OTA、日志上传等）阻塞，确保端到端延时满足 <1ms 目标
- **与 VLAN 优先级配合**：配合 IEEE 802.1Q 的 3bit PRI 字段（0-7 共 8 个优先级级别），TSN 调度器按优先级实施差异化转发；车载场景中底盘/驾控类报文通常占用最高优先级（7）
- **与 SOME/IP 集成**：TSN 负责传输层确定性保障，SOME/IP 提供服务发现、序列化和发布订阅层；两者共同构成车载 SOA 架构的通信基础
- **应用场景**：车载底盘控制（制动/转向，<1ms 要求）；L4 自动驾驶传感器数据（确定性实时传输）；工业机器人运动控制；音视频传输（802.1Qat 流预留）
- **与 EtherCAT 对比**：EtherCAT 通过专有「飞读飞写」机制实现确定性，TSN 是在标准以太网上的开放标准扩展，两者目标类似但技术路线不同；TSN 更适合整车多业务混合承载场景

## My Position

## Contradictions

## Sources

- [[sources/distributed-gateway-communication-tdt]]

## Evolution Log

- 2026-04-16（1 sources）：概念初建，来源为分布式网关通信TDT内部预研立项文档
