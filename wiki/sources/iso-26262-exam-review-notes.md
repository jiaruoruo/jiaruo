---
type: source
title: "ISO 26262 功能安全证书考试—复习要点"
date: 2026-07-13
source_url: ""
domain: "functional-safety"
author: "internal-note"
tags: ["functional-safety", "iso26262", "asil", "exam"]
processed: true
raw_file: "raw/notes/ISO-26262-功能安全证书考试-复习要点.md"
raw_sha256: "4c1d206f89882d18e5fc8ea6e95832d65bcd57265b4dd6c88ce0ae14ffdce579"
last_verified: 2026-07-13
possibly_outdated: false
language: "zh"
canonical_source: ""
---
# ISO 26262 功能安全证书考试—复习要点

## Summary

ISO 26262 功能安全证书考试复习要点（2026-07-08），覆盖标准12部分结构、故障链三要素、ASIL分级(HARA三维度)、安全开发生命周期、安全机制、ASIL分析方法等核心考点。

## Key Points

- 故障链：Fault→Error→Failure→Malfunction→Hazard
- ASIL分级：HARA三维度 S(严重度0-4)×E(可控性1-2)×E(暴露E1-E10)；QM/A/B/C/D(D最严)；ASIL D可分解为C+QM、B+B(需论证独立性)
- 安全生命周期：概念(Part3 HARA+安全目标)→系统(Part4功能安全概念)→硬件(Part5 SPF/LatF/PMHF)→软件(Part6 MISRA/静态分析)→验证→生产(Part7)
- 安全机制：冗余(锁步核/双核/传感器冗余)、监控(看门狗/内存保护/电压)、降级(限扭矩/安全状态)、诊断(BIST/CRC)
- ASIL分析方法(Part9)：FTA、FTA-FMEA、FMEDA、Dependability Tree
- 与实际关联：ACU控制器(ASIL分解/安全机制)、CCU-ZCU(跨域安全通信/故障诊断)、主被动安全融合

## Concepts Extracted

- [[functional-safety]]
- [[vehicle-domain-controller]]

## Entities Extracted


## Contradictions


## My Notes


<!-- source_type: technical-note; raw_sha256 已校验 -->
