---
type: source
title: "SGS AFSP Day 3 — SN 29500-4: Capacitor Temperature Correction Factor πT"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, sn29500, hardware-metrics, capacitor, pi-t, temperature-derating, component-reliability]
raw_file: "raw/personal/考试资料/0189_001.pdf"
raw_sha256: "f89ce34f103c62731f5131fb953323c4b67999e2aaea3bddc436026e91b739db"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 3 — SN 29500-4: Capacitor Temperature Correction Factor πT

## Summary

本页为 SGS TÜV Saar ISO 26262 AFSP Day 3 硬件分析环节引用的 **SN 29500-4:2004-03** 第 9 页（Table 6）。该表给出电容器在不同工作温度下的温度修正因子 πT，以及每类电容的温度模型常数（EA1、EA2、A、θU,ref），用于将基准 FIT 修正到实际工作温度。

## Key Points

- **标准**：SN 29500-4:2004-03，Table 6 — *Constants and factor πT for capacitors*。
- **输入变量**：电容器工作温度 θ2（°C），范围 20–125 °C；参考温度 θ1 通常为 40 °C。
- **πT 特性**：
  - 温度越低，πT 越小；温度越高，πT 显著增大。
  - θ2 = 40 °C 时多数类型 πT ≈ 1（与 θ1 对齐）。
  - θ2 = 125 °C 时 πT 可达 1.81–346，取决于类型与活化能。
- **典型 πT（θ2 = 125 °C）示例**：
  - 纸/金属化膜类：约 206–346
  - 陶瓷/玻璃/云母：约 16–286
  - 铝电解（液体/固体）：约 245 / 3.3
  - 钽电解（液体/固体）：较高（液体电解质尤其显著）
- **模型常数**：每类电容给出活化能 EA1、EA2（eV）与常数 A，用于 Arrhenius 类公式计算 πT。
- **考试关联**：PMHF 计算中必须按电容实际壳温/环境温选取 πT；高温场景下 πT 是失效率修正的主导项，常与 πU、πQ 叠加使用。

## Concepts Extracted

- [[functional-safety]]
- [[sn29500]]
- [[fit-rate]]
- capacitor
- πT
- temperature derating
- [[hardware-metrics]]
- [[component-reliability]]
- [[pmhf]]

## Entities Extracted

- sgs-tuv-saar
