---
type: source
title: "RZ/T2H & N2H Series Introduction"
date: 2026-04-15
source_url: ""
domain: "local"
author: "Renesas Electronics Corporation"
tags:
  - renesas
  - rzt2h
  - n2h
  - industrial-network
  - motor-control
processed: true
raw_file: "raw/pdfs/RZT2H_N2H_Introduction.pdf"
raw_sha256: "e63182311af47cd8e17cb086896a2f9465c2d1edf6e7e77bdaefe6f08ba97d2a"
last_verified: 2026-04-15
possibly_outdated: false
language: "en"
canonical_source: ""
---

# RZ/T2H & N2H Series Introduction

## Summary

瑞萨 RZ/T2H 和 RZ/N2H 产品详细介绍（Dec 2024，49页）。RZ/T2H 是异构 SoC，4× Cortex-A55（1.2GHz）+ 2× Cortex-R52（1.0GHz），支持9轴电机控制和多协议工业以太网，是驱控一体的旗舰工业机器人控制芯片。

## Key Points

- **RZ/T2H 规格**：4×Cortex-A55（1.2GHz）+ 2×Cortex-R52（1.0GHz）异构；2MB系统RAM；9轴电机控制（MTU3 + GPT 56ch）；多协议工业以太网（EtherCAT/PROFINET/EtherNet-IP/CC-Link IE/TSN/OPC UA over TSN）；Delta-Sigma IF 30ch；16ch/14ch 编码器接口；LCD 控制器；安全加密引擎
- **RZ/N2H 规格**：同 CPU 配置；侧重网络主站功能；与 RZ/T2L 配合实现协作机器人（主站+各轴从站）
- **应用方案**：RZ/T2H 单芯片实现工业机器人（驱控一体）；RZ/N2H+RZ/T2L 双芯片实现协作机器人（主站+各轴独立控制）
- **RZ 系列定位**：RZ/T 系列专注工业网络实时控制；RZ/V 系列专注视觉AI；RZ/G 专注 HMI；RZ/A 专注2D图形

## Concepts Extracted

- [[ethercat-realtime-communication]]
- [[humanoid-robot]]

## Entities Extracted

- [[renesas-electronics]]

## Contradictions

## My Notes
