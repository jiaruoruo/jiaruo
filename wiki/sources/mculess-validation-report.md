---
type: source
title: "MCULess 验证汇报"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "内部硬件验证团队"
tags:
  - mculess
  - validation
  - bzcu
  - recommendation
  - automotive
processed: true
raw_file: "raw/pdfs/MCULess验证汇报.pdf"
raw_sha256: "d7a93866a92c7bf04ed25e486a52196ea5228eba43054b2e09db9de572f91662"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCULess 验证汇报

## Summary

本文档为 MCULess 方案完整验证阶段的总结汇报，给出了各应用域的明确推荐结论：车身域和智能电源域验证通过（推荐采用），底盘气悬域验证不通过（不推荐采用，CPU 负载增加 10%）。文档同时详细记录了通信延迟测试数据和音频传输验证结果。

## Key Points

- **验证总体结论**：
  - ✅ **车身域（Body Domain）**：推荐采用 MCULess 方案。所有 IO 功能（HSD/H-Bridge/EFUSE/传感器）验证通过，通信延迟满足要求
  - ✅ **智能电源域（Smart Power Domain）**：推荐采用 MCULess 方案。电源管理逻辑可由 GPAN 硬件路由完全承担
  - ❌ **底盘气悬域（Chassis Air Suspension Domain）**：**不推荐**采用 MCULess 方案。验证发现域控制器 CPU 负载增加约 **10%**（原因：气悬控制周期短且控制逻辑复杂，原 ZCU MCU 承担了大量本地预处理，MCULess 后所有运算集中到域控，导致负载上升）
- **通信延迟测试数据**：
  - **CAN→CAN 路由**：实测 **21~62μs** ✅（目标 ≤100μs）
  - **CAN→ETH 路由**：实测 **43~63μs** ✅（目标 ≤100μs）
  - 延迟波动区间分析：最小延迟21μs 为轻载场景，最大62μs 为多节点同时传输时的竞争延迟，均在 100μs 约束内
- **音频传输验证**：
  - 实测音频路由延迟：**40μs** ✅
  - 对比基准：A2B（Automotive Audio Bus）行业规格 <100μs
  - 结论：GPAN TDM 音频路由可完整替代 A2B 分布式音频方案，且延迟更低
- **气悬域不推荐原因详析**：
  - 气悬 ECU 的控制算法（车高检测→阀门控制→高度反馈闭环）原在本地 MCU 执行（运算量约占 MCU 30% 负载）
  - MCULess 后，所有传感器数据上传域控处理，再下发控制指令，造成控制回路变长
  - 实测域控 CPU 负载从基线增加 10%，超出预算（目标：增量 ≤5%）
  - 同时底盘安全功能要求本地降级（Fallback）策略，无 MCU 的边缘节点无法独立执行安全降级
- **对整车 MCULess 推广的指导意义**：
  - 优先推广：座椅域、车门域、照明域、后备箱控制域（BZCU）
  - 谨慎评估：底盘域（需要本地计算和安全降级的场景）
  - 禁止推广：制动/转向/气囊等 ASIL-D 功能安全等级场景

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/can-eth-protocol-conversion]]
- [[concepts/zonal-gateway]]
- [[concepts/eea-architecture]]

## Entities Extracted

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Contradictions

<!-- 暂无 -->

## My Notes

底盘气悬域验证失败是 MCULess 方案的重要边界条件，清楚划定了技术适用范围。10% CPU 增量来自于控制逻辑集中化，这与 MCULess 的核心收益（去边缘 MCU）存在本质矛盾：越复杂的本地计算，MCULess 化越难。这一结论对方案推广具有决策价值。
