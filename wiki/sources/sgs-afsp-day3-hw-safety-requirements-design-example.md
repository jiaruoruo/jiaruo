---
type: source
title: "SGS AFSP Day 3 — Hardware Safety Requirements and Design Example"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hardware-safety, hardware-design]
raw_file: "raw/personal/考试资料/0174_001.pdf"
raw_sha256: "97d5dc41b00d159a08d1fe18186e3cd722c081f23f783a918e55a9c0cf4b4136"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — Hardware Safety Requirements and Design Example

## Summary

本页为 SGS AFSP Day 3 **Hardware Safety Requirements and Design** 的完整示例页（Seite 1 von 1），系统组件为 "Power Unit and Motor Monitoring"。页面给出将组件安全要求细化到硬件层级的 6 条硬件安全要求（HWSR_01–06，ASIL B），以及对应的硬件电路图（含电机、续流二极管、采样电阻、继电器、MOSFET、运算放大器等）。

## Key Points

- **HWSR_01**：使用分流电阻持续测量电机电流（ASIL B）
- **HWSR_02**：以标准化信号（0.1–10V）持续向电机 ECU 传输测量值（ASIL B）
- **HWSR_03**：通过功率继电器切断电源（ASIL B）
- **HWSR_04**：继电器需在 0.5s 内切断对电机的供电（ASIL B）
- **HWSR_05/HWSR_06**：开关关断=0V、开关导通=5V 的定义（ASIL B）
- **硬件电路图**：+60V 母线、电机 M、续流二极管 D1、采样电阻 R1/R2、晶体管 T1、继电器 K1、运放 IC1（AD8200）、+12V 供电、Motor ECU 控制/开关/模拟输入接口。
- **考试关联**：Day 3 对应 ISO 26262-5 硬件开发；HW 安全要求来自 TSC，经设计验证后还需 HW 架构指标与 PMHF 计算。

## Concepts Extracted

- [[functional-safety]]
- hardware-safety-requirements
- hardware-design
- shunt-resistor
- power-relay
- motor-monitoring

## Entities Extracted

- sgs-tuv-saar
- ad8200
