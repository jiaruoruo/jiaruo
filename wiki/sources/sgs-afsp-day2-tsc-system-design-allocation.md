---
type: source
title: "SGS AFSP Day 2 — TSC Exercise Page 3: System Design & Allocation of SYSR"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, technical-safety-concept, safety-architecture]
raw_file: "raw/personal/考试资料/0171_001.pdf"
raw_sha256: "22ea4ff6f28eb1b440bcbb4b9c43d03500cba92efb10fbf7d2524c9625060d28"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 2 — TSC Exercise Page 3: System Design & Allocation of SYSR

## Summary

本页为 SGS AFSP Day 2 TSC 练习 5 页材料中的第 3 页，给出 **System Design and Allocation of System Safety Requirements**。框图中 Pedal Sensor、Motor-ECU、Power Unit with Motor Monitoring、E-Motor、400V Battery、Display 等系统元素上标注了各自承担的 SYSR 编号（如 SYSR1–SYSR8 分配至 Motor-ECU，SYSR1/SYSR6 分配至 Power Unit），并标注硬线 Torque off 路径与 ABS 速度信号反馈。

## Key Points

- **分配原则**：系统安全要求需分配到系统元素；必要时增加额外信号路径。
- **框图标注**：
  - Pedal Sensor：SYSR5
  - Motor-ECU：SYSR1–SYSR8
  - Power Unit with Motor Monitoring：SYSR1、SYSR6
  - E-Motor：QM
  - 400V Battery：QM
  - Speed signal SYSR7 from ABS
  - Torque off SYSR6
- **考试关联**：ASIL 可随分配分解或继承；QM 元素不执行安全功能但可能提供输入。

## Concepts Extracted

- [[functional-safety]]
- technical-safety-concept
- system-safety-requirements
- safety-architecture
- asil-allocation

## Entities Extracted

- sgs-tuv-saar
