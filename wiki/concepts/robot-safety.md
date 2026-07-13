---
type: concept
title: "机器人安全"
date: 2026-07-13
updated: 2026-07-13
tags:
  - robot-safety
  - functional-safety
  - humanoid-robot
  - safety
source_count: 1
confidence: medium
domain_volatility: high
last_reviewed: 2026-07-13
aliases:
  - "机器人安全"
  - "Robot Safety"
  - "物理安全"
  - "Physical Safety"
---

# 机器人安全（Robot Safety）

## Definition

机器人安全（Robot Safety）指机器人在与人/环境共存时，通过硬件不可绕过保护 + 软件监控降级的多层机制，避免夹伤、碰撞、摔倒、电气危险等造成人身或设备不可接受风险的综合能力。与汽车 [[functional-safety]]（ISO 26262）方法论同源，但场景扩展到协作机器人/人形机器人的物理交互安全，核心标准包括 ISO/TS 15066（协作机器人）、ISO 13849（安全控制系统）、IEC 61508（通用功能安全）、ISO 13850（急停）、ISO 12100（机械安全）。

## Key Points

- **L1-L4 分层安全架构**：硬件层（不可绕过）→ 驱动层（过流/过压/过温/看门狗）→ 控制层（阻抗控制/力矩限制/软件限位）→ 应用层（姿态估计/摔倒检测/碰撞预测/故障诊断）；故障上报通道独立于控制通道（CAN FD / Ethernet）
- **灵巧手防夹**（与 [[dexterous-hand]] 强相关）：每自由度关节力矩传感（≤0.01Nm）+ 指尖力传感（<10ms）+ 柔性外覆（邵氏 20-40A）+ 阻抗控制降刚度；ISO/TS 15066 规定协作手部接触力 ≤1500N、指尖 >10N 立即停
- **基础保护分级响应**：L1 警告（降速+日志）→ L2 降额 → L3 停机（切输出+故障码）→ L4 锁死（硬件关断+人工干预）；硬件比较器/保险丝/TVS/机械限位不可绕过，软件限位提前 5-10° 触发
- **整机姿态安全**：IMU(1kHz)+ToF+超声；摔倒检测多阈值 FSM（倾角>60° 且角速度>阈值）；碰撞预测 TTC<1s 减速、<0.3s 停止；急停硬线接安全继电器（ISO 13850），安全回路达 ISO 13849 PLd 以上
- **功能安全故障上报**：安全 MCU 双核锁步（STM32H7）+ 隔离电路 + 独立电源监测；统一故障码（类别+代码+严重度+时间戳），CAN FD/ETH 上报，心跳 10-50ms，环形缓冲掉电保存
- **电气安全合规**：IEC 60204-1（整机最适用）、IEC 60335-1:2020、IEC 60034-1:2026、ISO 13849、IEC 61000 EMC；实测验证清单（绝缘≥2MΩ/耐压 1000-1500V AC/接地≤0.1Ω/温升/EMC/ESD±6kV/浪涌）

## My Position

机器人安全的工程原则应是「硬件兜底、软件递进」：任何安全关键功能必须有硬件级最终保护（不可绕过），软件只做更精细的降级与预测。这与汽车功能安全的 Limp-Home/Fallback 哲学一致，也解释了为何 [[humanoid-robot]] 的关节/力矩链路正引入汽车级 FuSa 方法学。

## Contradictions

<!-- 暂无来源间分歧 -->

## Sources

- [[sources/robot-safety-implementation]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为机器人团队安全需求软/硬件实现方案（内部工程文档 v1.0，2026-07-02），提炼 L1-L4 分层架构、灵巧手防夹、基础保护分级、整机姿态安全、功能安全故障上报、电气安全合规六大块
