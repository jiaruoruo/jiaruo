---
type: source
title: "SGS AFSP Day 3 — HW Analysis Exercise Page 1: Circuit Diagram"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hardware-analysis, circuit-diagram]
raw_file: "raw/personal/考试资料/0175_001.pdf"
raw_sha256: "062bc6f44145f2dd224d0b2eaa7329c29b28da019b2757b56722c7fb52740857"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — HW Analysis Exercise Page 1: Circuit Diagram

## Summary

本页为 SGS AFSP Day 3 **HW Analysis** 练习 8 页材料中的第 1 页，给出示例组件 "Power Unit and Motor Monitoring" 的完整电路原理图。图中包含 +60V 供电、电机 M、续流二极管 D1、采样电阻 R1、限流/下拉电阻 R2、MOSFET T1、继电器 K1、双运放 IC1（AD8200）、+12V 供电，以及到 Motor ECU 的 analogue input、control output、switch output 接口。

## Key Points

- **电路功能**：电机驱动 + 电流监测 + 可关断路径。
- **关键器件**：
  - 电机 M（+60V）
  - 续流二极管 D1
  - 电流采样：R1（shunt）、R2
  - 开关执行：T1（MOSFET）、K1（relay）
  - 信号调理：IC1（AD8200 双差分运放）
  - 供电：+60V、+12V
- **考试关联**：HW 分析的第一步是理解电路功能和各器件在功能安全中的作用；后续需对每器件进行 FIT、失效模式、故障分布、DC 分析。

## Concepts Extracted

- [[functional-safety]]
- hardware-analysis
- circuit-diagram
- motor-driver
- current-sensing
- ad8200

## Entities Extracted

- sgs-tuv-saar
- ad8200
