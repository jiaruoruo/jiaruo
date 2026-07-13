---
type: source
title: "机器人安全需求→软/硬件实现方案"
date: 2026-07-13
source_url: ""
domain: "robotics"
author: "internal-note"
tags: ["robot-safety", "functional-safety", "humanoid-robot", "dexterous-hand"]
processed: true
raw_file: "raw/notes/机器人安全需求-软硬件实现方案.md"
raw_sha256: "63b29cb070d5ef8661dc08d45d404a1f91fbe6079fe19cd930c112d4039482cd"
last_verified: 2026-07-13
possibly_outdated: false
language: "zh"
canonical_source: ""
---
# 机器人安全需求→软/硬件实现方案

## Summary

机器人团队安全需求（2026-07-02）的软/硬件实现方案，覆盖灵巧手防夹、基础保护、整机姿态安全、功能安全故障上报、电气安全合规五大类，给出 L1-L4 分层安全架构与逐条硬件/软件实现。

## Key Points

- L1-L4 分层安全架构：硬件层(不可绕过)→驱动层→控制层→应用层；故障上报通道独立于控制通道(CAN FD/Ethernet)
- 灵巧手防夹：关节力矩感知(≤0.01Nm)+指尖力传感(<10ms)+柔性外覆(邵氏20-40A)+阻抗控制降刚度；ISO/TS 15066 手部接触力≤1500N、指尖>10N立即停
- 基础保护 L1-L4 分级响应：警告→降额→停机→锁死；硬件比较器/保险丝/TVS/机械限位不可绕过，软件限位提前5-10°触发
- 整机姿态安全：IMU(1kHz)+ToF+超声；摔倒检测多阈值FSM(倾角>60°且角速度>阈值)；碰撞预测TTC<1s减速、<0.3s停止；急停硬线接安全继电器(ISO 13850)
- 功能安全故障上报：安全MCU双核锁步(STM32H7)/隔离电路/独立电源监测；统一故障码(类别+代码+严重度+时间戳)，CAN FD/ETH上报，心跳10-50ms
- 电气安全合规：IEC 60204-1(整机最适用)、IEC 60335-1、IEC 60034-1:2026、ISO 13849、IEC 61000 EMC；实测验证清单(绝缘/耐压/接地/温升/EMC/ESD/浪涌)

## Concepts Extracted

- [[robot-safety]]
- [[functional-safety]]
- [[humanoid-robot]]
- [[dexterous-hand]]

## Entities Extracted


## Contradictions


## My Notes


<!-- source_type: technical-note; raw_sha256 已校验 -->
