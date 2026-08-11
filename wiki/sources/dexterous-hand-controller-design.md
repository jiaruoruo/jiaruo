---
type: source
title: "灵巧手控制器详细设计"
date: 2026-07-13
source_url: ""
domain: "robotics"
author: "internal-note"
tags: ["dexterous-hand", "motor-control", "ethercat", "freertos"]
processed: true
raw_file: raw/工作/notes/dexterous-hand-design.md
raw_sha256: c8c06bec1e1da5db39f521e1fa0fed5f4fd9fc8f4a4cdcf92c34649fe19352b4
last_verified: 2026-07-13
possibly_outdated: false
language: "zh"
canonical_source: ""
---
# 灵巧手控制器详细设计

## Summary

理想汽车机器人平台灵巧手控制器详细设计（2026-07-01），定义 14-20 DOF、1kHz位置环/10kHz电流环FOC、EtherCAT通信的控制器架构，给出处理器选型与FreeRTOS任务设计。

## Key Points

- 指标：14-20 DOF；位置环1kHz/电流环10kHz FOC；端到端延迟<2ms；EtherCAT/CAN-FD通信；24V供电
- 推荐方案B：主控 STM32H743(M7 480MHz)+分布式协处理器 STM32G474×N(每片2-3关节FOC)；14 DOF 约 ¥140(主控¥45+协处理器×6×¥22)
- FreeRTOS(主控)+裸机状态机(协处理器)：FOC 100μs太紧不能用RTOS；9任务优先级 PRI9 EtherCAT从站→PRI1系统监控
- 算法层：逆运动学(Jacobian伪逆/CCD)、轨迹五次多项式/S曲线、阻抗控制 Z=M s²+D s+K、力位混合、触觉滑移检测
- 与大脑节点数据流：EtherCAT PDO 1ms下发(gesture_command/joint_target/impedance_param)+上发(joint_state/force_torque/touch_data/health_status/fault_code)
- 风险：FOC算力→分布式协处理器；主协同步<50μs(SPI DMA)；EtherCAT实时性 SOEM+ETH DMA实测1ms稳定

## Concepts Extracted

- [[dexterous-hand]]
- [[robot-software-architecture]]
- [[ethercat-realtime-communication]]

## Entities Extracted


## Contradictions


## My Notes


<!-- source_type: technical-note; raw_sha256 已校验 -->
