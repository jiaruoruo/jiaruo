---
type: source
title: "SGS AFSP Day 2 — TSC Exercise Page 5: Component Design & HW-SW Allocation"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, technical-safety-concept, component-design, hw-sw-allocation]
raw_file: "raw/personal/考试资料/0173_001.pdf"
raw_sha256: "113385ea5c3cb8f8c096b0ef00f06aacd7b4f81be8ca4e15a607ea0d2e3bd8dd"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 2 — TSC Exercise Page 5: Component Design & HW-SW Allocation

## Summary

本页为 SGS AFSP Day 2 TSC 练习 5 页材料中的第 5 页（末页），给出 **Component Design and Allocation of Component Safety Requirements**。展示 "Power Unit with Motor Monitoring" 内部框图：Analog Input → Power Electronics → Output to motor；同时有 Motor Current (SYSELR1)、Analog Output (SYSELR2)、Power Switch (SYSELR3)、Switch Input (SYSELR4)、400V Input 等安全相关元素。

## Key Points

- **组件内部设计**：模拟输入、功率电子、电机电流监测、模拟输出、功率开关、开关输入、400V 输入。
- **HW-SW 分配说明**：系统元素安全要求可分配到硬件、软件或二者组合；本培训示例中所有元素均分配到硬件实现。
- **考试关联**：HW/SW 分配决策需记录；不同实现方式（纯硬件 vs 软硬件结合）影响后续 HW 安全要求规格与 SW 安全要求规格。
- **注意**：页面注明下一步将系统安全要求在硬件层级进一步细化（Hardware Safety Requirements Specification）。

## Concepts Extracted

- [[functional-safety]]
- technical-safety-concept
- component-design
- hw-sw-allocation
- hardware-safety-requirements

## Entities Extracted

- sgs-tuv-saar
