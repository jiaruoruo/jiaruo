---
type: concept
title: "区域网关"
date: 2026-04-16
updated: 2026-04-16
tags:
  - automotive
  - eea
  - gateway
  - zcu
  - distributed-control
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-04-16
aliases:
  - "区域网关"
  - "分布式网关"
  - "Zonal Gateway"
  - "zonal-gateway"
  - "ZCU"
  - "Zone Control Unit"
  - "区域控制器"
---

# 区域网关（Zonal Gateway）

## Definition

区域网关（Zonal Gateway，ZCU，Zone Control Unit）是"中央计算+区域控制"EEA 架构中按物理区域部署的分布式网关控制器，负责汇聚该区域内所有 CAN/LIN/CANFD 节点，并通过以太网与中央计算单元（CCU）连接。ZCU 是域网关（Domain Gateway）的演进形态——从按功能域划分变为按车身物理区域划分，执行协议转换、路由转发、驱动抽象和服务化封装等功能。

## Key Points

- **典型部署（理想汽车 EEA 3.0）**：LZCU（左区域）管理 8 路 CANFD + 6 路 LIN；RZCU（右区域）管理 4 路 CANFD + 6 路 LIN（含动力驱动、底盘、高压管理）；BZCU（后区域）管理 7 路 CANFD + 1 路 CAN + 6 路 LIN（含底盘制动、悬架）
- **从域网关演进**：EEA 1.0/2.0 中央式/域集中式网关（CGW/XCU）→ EEA 3.0/4.0 分布式区域网关（ZCU），架构从「功能域」转向「物理区域」
- **四大核心功能**：①协议转换（CAN/LIN ↔ ETH，见 [[can-eth-protocol-conversion]]）；②动态路由（优先级调度、冗余切换）；③驱动能力原子服务化（向 CCU 提供远程调用接口）；④安全防护（非法 ID 拦截、异常流量冻结）
- **驱动原子服务**：ZCU 将硬件驱动功能封装为独立的最小服务单元（Server 端），CCU 部署 Client 端，通过 ETH（MVBS-DDS）实现跨平台无感调用；支撑业务上移和整车功能灵活部署，降低 ZCU 硬件成本
- **性能要求**：路由表初始化 <200ms（早于 CCU 启动完成）；故障确认到路由切换 <5ms；非法 ID 拦截成功率 100%；触发式报文路由延时 <1ms；CPU 占用：3 路 CANFD 50% 总线负载下 <20%
- **冗余策略**：ETH-CAN 双通道热备份；主路故障时自动修改路由表切换备用路径（例：BMS→RZCU→ETH→CCU 切换为 BMS→RZCU→CAN→CCU）；支持负载均衡（ETH 负载 >70% 时触发分流）
- **趋势**：网关从「通信路由」向「通信+计算」融合演进；ZCU 偏向执行驱动，CCU 承载上层算法，形成分层解耦架构

## My Position

## Contradictions

## Sources

- [[sources/distributed-gateway-communication-tdt]]

## Evolution Log

- 2026-04-16（1 sources）：概念初建，来源为分布式网关通信TDT内部预研立项文档
