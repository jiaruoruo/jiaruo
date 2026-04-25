---
type: source
title: "基于英飞凌PSOC™ C3与GaN的电机驱动方案"
date: 2026-04-20
sha256: "6eae6cdaa914e7aecb1be683219631976f43d2eca2c5ac7e61c3b46d0a3451f3"
raw_file: "raw/pdfs/深圳We Accelerate Robotics--基于英飞凌PSOC C3与GaN的电机驱动方案--韩兴涛.pdf"
author: "韩兴涛，贝能国际应用设计中心（睿能科技全资子公司）"
event: "深圳 We Accelerate Robotics 2025"
domain:
  - robotics
  - motor-control
  - power-electronics
  - semiconductors
entities:
  - infineon-technologies
concepts:
  - humanoid-robot
  - quasi-direct-drive-motor
status: processed
---

# 基于英飞凌PSOC™ C3与GaN的电机驱动方案

## Summary

基于英飞凌 PSC3M5EDLGQ1 MCU 与 CoolGaN™ IGC033S10S1 功率器件，设计了紧凑型高性能伺服电机驱动器（48V/1.5kW）。GaN 器件使 PCB 体积相比传统 Si 方案缩小 30%，100kHz 开关频率支持三环高速控制（电流环 100kHz），效率最高达 99%。驱动器尺寸仅 50×82×8mm，适合机器人关节驱动应用。

## Key Points

- **核心 MCU PSC3M5EDLGQ1**（PSOC C3 M 系列，专为电机驱动设计）：180MHz 主频，128KB Flash，VQFN-48 封装
- **GaN 功率器件 IGC033S10S1**：100V/47A（@Tc 100°C），RDS(on) 3.3mΩ，3×5mm PQFN 封装；栅极驱动 1EDN7126U（1.5A）
- **核心性能**：额定 48V DC（最高 60V），1.5kW 功率，最大扭矩 28.65Nm，额定电流 38A，调制频率 100kHz，效率最高 99%
- **三环控制**：电流环 100kHz，速度环 10kHz，位置环 5kHz；总运算耗时 4.1μs（@180MHz/100kHz）
- **编码器**：23 位绝对值，RS485，2.5Mbps，多摩川协议
- **电流传感器 TLI4971-A075**：±75A 满量程，16mV/A，220μΩ（系列含 25/50/75/120A）
- **PCB 尺寸**：50×82×8mm，4 层板，体积比 Si 方案缩小 30%，无大电解电容
- **接口**：CAN（1Mbps）/ UART（115.2kbps）；保护：过流/欠压/过压/堵转/过热/缺相

## Related Concepts

- [[humanoid-robot]]
- [[quasi-direct-drive-motor]]

## Related Entities

- [[entities/infineon-technologies]]
