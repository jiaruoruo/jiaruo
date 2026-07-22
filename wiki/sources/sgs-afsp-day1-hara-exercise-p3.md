---
type: source
title: "SGS AFSP Day 1 — HARA Exercise Page 3: ASIL Evaluation Matrix"
date: 2026-07-22
source_url: ""
domain: automotive-eea
author: "SGS TÜV Saar"
tags: [automotive-eea, functional-safety, iso-26262, sgs-afsp, hara, asil]
raw_file: "raw/personal/考试资料/0160_001.pdf"
raw_sha256: "9392eb9009dfc0077abedff9886aced1981d573a0c0d863ee4f06f0c3a8d4122"
last_verified: 2026-07-22
language: en
---

# SGS AFSP Day 1 — HARA Exercise Page 3: ASIL Evaluation Matrix

## Summary

本页为 SGS AFSP Day 1 HARA 练习 8 页材料中的第 3 页，给出 **ASIL Evaluation Matrix**。矩阵以场景（Scenario / Driving situation）为行、失效模式（Malfunction）为列，要求对每对组合填写 S（Severity）、E（Exposure）、C（Controllability）三个参数，是 ISO 26262 中 ASIL 等级（QM、A、B、C、D）的判定核心。

## Key Points

- **矩阵维度**：
  - 行：4 个场景（停车场无人、停车场有人、路口静止、乡村道路超车）
  - 列：失效模式（Torque demand without driver request、No torque demand at driver request 等）
- **S/E/C**：严重度、暴露度、可控性三参数；每个组合决定一个 ASIL。
- **考试关联**：ASIL 不是先验给定的，而是对每个（失效模式 × 场景）组合评估得出；同一失效模式在不同场景下 ASIL 可能不同。
- **注意**：本页为空白练习模板，未填写具体 S/E/C 数值，用于培训学员练习 ASIL 判定方法。

## Concepts Extracted

- [[functional-safety]]
- automotive-safety-integrity-level
- severity-exposure-controllability
- hara-evaluation-matrix

## Entities Extracted

- sgs-tuv-saar
