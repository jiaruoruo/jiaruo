---
type: entity
title: "理想汽车"
date: 2026-04-16
updated: 2026-04-16
tags:
  - automotive
  - chinese-oem
  - eea
  - new-energy-vehicle
entity_type: institution
aliases:
  - "理想汽车"
  - "Li Auto"
  - "li-auto"
  - "理想"
  - "LIXIANG"
---

# 理想汽车（Li Auto）

## Description

理想汽车（Li Auto，LIXIANG）是中国头部新能源汽车制造商，主打增程式电动车（EREV）产品，代表车型包括 L9、L8、L7、L6 及 MEGA 系列。理想汽车以技术主导的产品策略著称，其 EEA 架构演进路径（EEA 1.0→3.0，目标 4.0）是中国新势力中较为典型的"中央计算+区域控制"架构落地案例。

## Key Contributions

- **EEA 3.0 架构实践**：落地 CCU（中央算力单元）+ HU（人机交互主机）+ LZCU/RZCU/BZCU（三区域网关）架构，通过百兆以太网骨干网连接区域控制器
- **区域网关规模参考**：RZCU 域管理 37 个 CANFD + 28 个 LIN 节点；CHCAN2 总线负载已达 69.88%，是推动 CAN-ETH 迁移的真实压力案例
- **整车网络数据基准**：提供了完整的 EEA 3.0 整车网络通信拓扑（5 大 ZCU、各网段节点数/总线负载/报文周期）及以太网服务 ID 规模（2919 个 ETH Service ID），是 CAN-ETH 协议转换研究的重要真实数据来源

## Related Concepts

- [[eea-architecture]]
- [[zonal-gateway]]
- [[can-eth-protocol-conversion]]

## Sources

- [[sources/distributed-gateway-communication-tdt]]

## Evolution Log

- 2026-04-16（1 sources）：实体页初建，来源为分布式网关通信TDT内部预研立项文档；记录理想汽车 EEA 3.0 架构详细数据
