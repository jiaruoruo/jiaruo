---
type: concept
title: "EtherCAT 实时通信"
date: 2026-04-15
updated: 2026-04-15
tags:
  - ethercat
  - real-time-communication
  - robotics
  - fieldbus
source_count: 4
confidence: low
domain_volatility: low
last_reviewed: 2026-04-15
aliases:
  - "EtherCAT 实时通信"
  - "EtherCAT"
  - "ethercat-realtime-communication"
  - "工业实时以太网"
---

# EtherCAT 实时通信（EtherCAT Real-time Communication）

## Definition

EtherCAT（Ethernet for Control Automation Technology）是一种基于以太网的实时工业现场总线协议，由德国倍福（Beckhoff）开发并开放标准化（IEC 61158）。其核心创新是「飞行中读写」（On-the-fly Processing）机制：数据帧在环形拓扑中传递时，每个从站设备直接从帧中提取/插入自己的数据，无需等待，实现极低延迟和极小抖动。在机器人领域，EtherCAT 是连接主控计算机与关节电机驱动器的首选实时通信方案。

## Key Points

- **关键性能指标**：带宽100Mbps，周期时间<100μs（最小0.5ms/2kHz），抖动极小，支持节点数>65000，环型/线型拓扑
- **分布式时钟（DC）**：同步精度 **<100ns**（IEEE 1588增强版，瑞萨官方规格）；各节点时钟偏移补偿算法实现全网络同步
- **对比其他协议**：
  - CAN-FD：5Mbps，周期~1ms，成本低，适合<15关节低成本方案
  - EtherNet/IP：100Mbps，周期1-10ms，抖动0.1-1ms，适合工厂网络
  - 自研协议：性能可定制但开发成本高（特斯拉、小鹏等采用）
- **开源实现**：SOEM（Simple Open EtherCAT Master，C语言，GPLv2）；PySOEM（Python绑定）；IGH EtherCAT（Linux内核模块）
- **人形机器人应用**：Boston Dynamics Atlas 使用 EtherCAT 连接28个液压驱动器；KUKA 工业机械臂标准配置；宇树 H1 推测采用 EtherCAT 或自研协议
- **芯片级实现（瑞萨）**：RZ/T2H/RZ/T2M/RZ/T2L/RA8T2 均内置 EtherCAT 从站控制器（Slave Controller）；RZ/T2H 支持 EtherCAT 主/从，单芯片实现工业机器人驱控一体
- **市场份额**：占全球工业机器人通信协议 35%（2024年，来源：瑞萨）；年增长率12.7%（2023-2025）
- **硬件成本**：主站控制器约¥3500-14000，从站芯片约¥70-210/个；需实时 Linux 内核（PREEMPT_RT）保证确定性
- **选型建议**：追求1kHz力控、多关节协同时选 EtherCAT；成本敏感（<15关节、≤200Hz）时选 CAN-FD

## My Position

## Contradictions

- [[sources/humanoid-robot-research-rapid-prototyping]] vs [[sources/renesas-robot-servo-ethercat-application]]：分布式时钟同步精度表述不同，前者记为「<1μs」，后者（瑞萨官方技术文档）明确为「<100ns（IEEE 1588增强版）」。已采用瑞萨官方数据（一手规格文档），更新 Definition 和 Key Points。

## Sources

- [[sources/renesas-robot-servo-ethercat-application]]
- [[sources/humanoid-robot-research-rapid-prototyping]]
- [[sources/ethercat-gpan-servo-validation]]
- [[sources/robot-sensor-actuator-communication]]

## Evolution Log

- 2026-04-15（1 sources）：概念初建，来源为人形机器人技术研究及快速原型建设报告
- 2026-04-15（2 sources）：修正：分布式时钟精度从「<1μs」更新为「<100ns（IEEE 1588增强版）」，依据瑞萨官方技术文档；补充市场份额数据（35%，2024年）、芯片级实现细节及最小周期（0.5ms/2kHz）
- 2026-04-15（4 sources）：强化——EtherCAT & GPAN 验证方案与传感器沙盘与现有定义一致；新增 GPAN 对比数据（时钟同步目标≤2μs、最小周期31.25μs）及状态估计延迟需求背景
