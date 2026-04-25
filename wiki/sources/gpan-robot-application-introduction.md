---
type: source
title: "GPAN 机器人应用介绍"
date: 2026-04-20
sha256: "77375dd5c630c11d9e640af66483578de6e66c93746e6ecdecf0aa3d8ef911b2"
raw_file: "raw/pdfs/GPAN 机器人应用介绍.pdf"
author: "GPAN 技术团队"
domain:
  - robotics
  - industrial-network
  - real-time-communication
entities: []
concepts:
  - gpan-communication
  - ethercat-realtime-communication
status: processed
---

# GPAN 机器人应用介绍

## Summary

介绍 GPAN（通用精密自动化网络）协议在机器人领域的应用，对比 EtherCAT 与 CAN 总线的技术差异与优势。GPAN 采用 100Base-T1 两线制、环形拓扑、200Mbps 全双工设计，以带宽利用率高（>80%）、控制周期短（最低 20μs）、时间同步精度高（≤40ns）为核心卖点，同时支持 MCULess 远程外设控制方案，可大幅简化机器人节点硬件设计。

## Key Points

- **物理层**：100Base-T1 两线制以太网，环形拓扑，200Mbps 全双工
- **带宽利用率**：>80%，显著优于 EtherCAT 的飞读飞写模式
- **控制周期**：最低 20μs（可满足高性能伺服控制需求）
- **时间同步精度**：≤40ns（硬件级时间戳，优于 IEEE 1588 软件同步）
- **硬件重传机制**：节点级硬件自动重传，保障实时性与可靠性
- **节点间通信**：支持节点到节点直接通信，不必经主控中转
- **MCULess 远程外设控制**：边缘节点无需独立 MCU，通过 GPAN 芯片硬件路由完成数据转发，简化 BOM 和系统架构
- **低功耗**：休眠/唤醒模式下功耗 <100μA，适用于电池供电节点
- **对比 EtherCAT**：GPAN 在带宽利用率和时钟同步精度上更优；EtherCAT 拥有更成熟的生态（CoE/SoE）和更丰富的第三方支持

## Related Concepts

- [[gpan-communication]]
- [[ethercat-realtime-communication]]

## Related Entities
