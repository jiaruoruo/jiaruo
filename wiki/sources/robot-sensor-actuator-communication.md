---
type: source
title: "机器人传感器执行器通信技术沙盘"
date: 2026-04-15
source_url: "https://li.feishu.cn/docx/QHz3d2euvokknNxn4kicgERcncg"
domain: "li.feishu.cn"
author: ""
tags:
  - sensor-fusion
  - actuator
  - servo-drive
  - state-estimation
  - robotics
processed: true
raw_file: "raw/clippings/2026-04-15‌﻿⁡​﻿​⁤‬⁣​⁣‍​‍‌​​​⁡​﻿⁣‍⁣‌‌‌⁣‬​‌​‍‍​⁢﻿‌‬⁢⁣‬​⁤⁤‌‍⁡‍机器人传感器执行器通信技术沙盘.md"
raw_sha256: "b80f8064e9098a60e700e6aae7d00d8373a13ee20fb19e833fcb75d7c87f68b9"
last_verified: 2026-04-15
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 机器人传感器执行器通信技术沙盘

## Summary

飞书云文档，以结构化沙盘（必要性/可行性/领先性三维度）梳理机器人传感器与执行器通信技术体系。覆盖状态感知融合（IMU/编码器/力/位传感器）、足端接触力估计（六维力传感器/关节力矩传感器）、全身状态估计器（EKF/UKF多传感器融合）、高带宽电机伺服驱动等核心技术方向，为机器人系统设计提供技术地图。

## Key Points

- **状态感知融合**：IMU/编码器/力/位传感器融合是动态平衡和运动控制的绝对基础；EKF/UKF 框架成熟；主要挑战在参数标定和极限运动下的鲁棒性调优
- **足端接触力估计**：六维力传感器直接测量，或通过关节力矩传感器+动力学模型估计；领先指标：精度<5%、带宽>1kHz；结合机器学习自适应补偿模型误差
- **全身状态估计器**：EKF/UKF 融合 IMU、编码器、足端力；需运动学/动力学模型 + 传感器外参标定；领先指标：延迟<5ms、频率>500Hz；传感器故障时通过模型预测保持连续性
- **高带宽电机伺服驱动**：FOC + PID 闭环为标准技术；领先性体现在控制频率（数十kHz）、相位延迟极低；自适应控制、前馈补偿、非线性补偿推向物理极限
- **技术领先判断框架**：不在于是否拥有该技术，而在于精度、速度、鲁棒性的极致优化——高速跑跳时微小延迟/估计偏差即导致失控

## Concepts Extracted

- [[quasi-direct-drive-motor]]
- [[ethercat-realtime-communication]]
- [[humanoid-robot]]

## Entities Extracted

## Contradictions

## My Notes
