---
type: source
title: "灵巧手系统需求规格说明书 v1.0"
date: 2026-07-13
source_url: ""
domain: "robotics"
author: "internal-note"
tags: ["dexterous-hand", "requirements"]
processed: true
raw_file: raw/工作/notes/机器人/灵巧手需求规格说明书-v1.md
raw_sha256: 37f54ab47c25fe1d9407eaed0a8c2c9f98abba7e3a2819ac321886a828127004
last_verified: 2026-07-13
possibly_outdated: false
language: "zh"
canonical_source: ""
---
# 灵巧手系统需求规格说明书 v1.0

## Summary

灵巧手系统需求规格说明书 v1.0（2026-07-01，草稿），覆盖运动控制、状态指示、智能化、通信软件、安全、电气六大类需求，定义闭环<2ms、操控>1kHz、48V/250W等关键指标。

## Key Points

- 运动控制：闭环周期<2ms(MC-14)、操控频率>1kHz(MC-09)、传感器采样≥1kHz(MC-11)、指令延迟<5ms(MC-12)、感知延迟<5ms(MC-13)、力控带宽>100Hz
- 反射库(MC-06)：接触反射/防滑反射/柔顺抓握反射，定义触发条件与力/位置响应策略
- 智能化(AI)：手势动作库、小脑智能(滑移检测/肌肉记忆/条件反射)、仿真环境、算法工具包(模仿/强化学习)、ROS集成、多模态融合
- 通信软件：EtherCAT(SW-01)、OTA及现场升级(SW-02)
- 安全(SAF)：防夹(SAF-01)、基础保护(SAF-02)、整机安全(SAF-03)、功能安全故障上报(SAF-04)、电气安全IEC 60335-1:2020+IEC 60034-1:2026(SAF-05)
- 电气：额定48V/<3.5A/<170W(EL-01)，最大5A/<250W(EL-02)

## Concepts Extracted

- [[dexterous-hand]]
- [[robot-safety]]
- [[functional-safety]]

## Entities Extracted


## Contradictions


## My Notes


<!-- source_type: technical-note; raw_sha256 已校验 -->
