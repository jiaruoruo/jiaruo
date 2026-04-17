---
type: source
title: "分布式网关通信TDT"
date: 2026-04-16
source_url: ""
domain: "automotive-eea"
author: ""
tags:
  - automotive
  - eea
  - can-eth
  - gateway
  - zonal-gateway
processed: true
raw_file: "raw/clippings/分布式网关通信TDT.md"
raw_sha256: "05ab1f8d13b9a7c7c51baba1a4aeadb7c1d1aa8e6f3073e225d10a8721cd517a"
last_verified: 2026-04-16
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 分布式网关通信TDT

> ⚠ 来源文件缺少标准 frontmatter，source_url 留空，date 取摄入日期。

## Summary

本文件是一份整车分布式网关通信方向的技术预研立项文档（TDT），面向 EEA 4.0 和 2027 年 OC 量产目标，承接算力平台技术沙盘中"XoverETH 协议转换"与"通信故障监控及处理"两个技术点。文档系统阐述了整车骨干网从 CAN 向以太网迁移的必要性、竞争现状、技术机会点，并定义了五大研究与验证方向的方案框架与关键指标。预研全生命周期预算约 174.9 万元，团队规模约 11 人。

## Key Points

- **架构演进背景**：整车电子电气架构从 EEA 1.0 分布式 CAN 网关 → EEA 2.0 域集中式 → EEA 3.0 中央计算（CCU）+ 区域控制（ZCU）；EEA 4.0 目标在 ETH 上部署底盘/动力等高实时性功能，ETH 取代 CAN 成为整车通信主干网
- **当前痛点（理想汽车 EEA 3.0 现状）**：RZCU 域含 37 个 CANFD + 28 个 LIN 节点；CHCAN2 总线负载 69.88%、ZCAN 66.02%，接近 CAN 总线负载上限；缺乏标准化 CAN-ETH 转换协议；所有 CAN-ETH 数据均上行至 ASW，链路单一
- **三大技术攻关方向**：①CAN(LIN)-ETH 双向转换协议——单帧处理 <30μs，跳过 TCP/IP 栈直接基于以太网底层路由，利用 TSN（802.1Qbv）保障确定性，CAN-ETH 上行复用 MVBS-DDS；②路由转换动态切换策略——路由表初始化 <200ms，故障确认到切换成功 <5ms，支持 ETH-CAN 双通道热备份，非法 ID 拦截成功率 100%；③ZCU 驱动能力原子服务——执行器类 Fire/Forget <1ms，传感器类 Cyclic 抖动 <±20%，CPU/RAM 占用各 <15%
- **两大验证方向**：④ZCU 网关性能验证——3 路 CANFD 50% 总线负载下 CPU <20%，触发式报文 <1ms，零乱序零丢包；⑤ZCU 至 CCU 端到端性能验证——单业务 <1ms，高优先级 <1ms / 低优先级 <2ms，抖动 ±10%
- **竞争洞察**：特斯拉 HW4.0 已实现 ETH 环网主干网；华为 2021 年已完成 CAN-ETH 路由部署；小米下一代 EEA 规划 ETH 主干网；主流新势力整体向 ETH 主干网迁移
- **协议帧结构**：以太网帧含 802.1Q VLAN Tag（TPID 0x8100，含 3bit PRI 优先级字段），上层采用 IP/UDP/SOME/IP 封装，PduHeader ID 作为 CAN 报文映射标识
- **总关键指标**：单帧 <30μs；100 CAN frames/100ms（CPU+内存各 <5%）；触发式端到端 <1ms；故障切换 <5ms；驱动服务 CPU/RAM 各 <15%

## Concepts Extracted

- [[can-eth-protocol-conversion]]
- [[zonal-gateway]]
- [[eea-architecture]]
- [[time-sensitive-networking]]

## Entities Extracted

- [[li-auto]]

## Contradictions

## My Notes
