---
type: source
title: "GPAN MCULess BOM 成本核算 V0.4"
date: 2026-04-27
source_type: spreadsheet
source_url: ""
raw_path: "raw/articles/成本核算0.4 -- 公共.xlsx"
raw_sha256: "88795209"
author: "Goodix Technology（汇顶科技）"
language: zh
tags:
  - gpan
  - mculess
  - bom-cost
  - automotive
  - goodix
  - distributed-audio
---

# GPAN MCULess BOM 成本核算 V0.4

## Summary

Goodix 内部 Excel 成本核算文档（3 Sheet，V0.4），提供 GPAN MCULess 方案与传统方案的详细 BOM 成本对比。包含：二级网络（3 个 ZCU）、三级网络（ECU 节点）、48V 分布式音频三个维度的量化收益，是 GPAN 方案商业价值论证的核心财务依据。

## Key Points

### Sheet 1：二级网络 3 个 ZCU 收益

**参考价格基准**：
- 8端口IO扩展芯片：2 元/片
- GPAN QFN64(T1)：12 元；QFN64(CAN-FD)：7 元
- GPAN BGA144：14 元；GPAN BGA196：18 元
- 新 MCU（替换后）参考价格：80 元

| ZCU 节点 | 当前方案成本 | GPAN 方案成本 | 节约 |
|---|---|---|---|
| 左前 ZCU | 122 元（TC389×1=80 + IO扩展×20×2=40 + GPAN0） | 108 元（TC4×80 + BGA144×14 + BGA144×14） | **14 元** |
| 右前 ZCU | 105 元（TC389×1=80 + IO扩展×12×2=24） | 94 元（TC4×80 + BGA144×14） | **11 元** |
| 后 ZCU | 162 元（TC399×120 + IO扩展×20×2=40） | 46 元（BGA144×2=28 + BGA196×18） | **116 元** |
| **合计** | **389 元** | **248 元** | **🔑 141 元/套** |

> 注：后 ZCU 去除 TC399（120元）MCU 是最大节约来源。MCU 省掉后 ZCU 面积减少约 1000mm²（18个IO扩展芯片 × PCB 面积）

### Sheet 2：三级网络 ECU 节点收益

| ECU 类型 | 当前方案 | GPAN 方案 | 节约 |
|---|---|---|---|
| 门模块（×4） | S32K144×14×4=56 元 | BGA144×12×4=48 元 | **8 元** |
| 灯模块（×4） | MCU×8×4=32 元 | QFN64×7×4=28 元 | **4 元** |
| 其它 ECU（×8） | MCU×8×8=64 元 | QFN64×7×8=56 元 | **8 元** |
| **三级网络合计** | **152 元** | **132 元** | **🔑 20 元** |

### Sheet 3：48V 分布式音频方案收益

**对比基准：全 A2B 外置集中式音频方案 vs GPAN 分布式音频**

| 收益来源 | 全 A2B 方案 | GPAN 方案 | GPAN 节约 |
|---|---|---|---|
| 芯片成本（transceiver+A2B） | 240 元 | 120 元 | **120 元** |
| 线束成本（喇叭+头枕+RNC收音） | 103.6 元 | 24.4 元 | **79.2 元** |
| 人工装配成本 | 基准 | -50 元 | **50 元** |
| 产线效率提升（机械手自动布线） | 基准 | -30 元 | **30 元** |
| 外置功放+PMIC+控制器 | 36 元 | 0 元 | **36 元** |
| **音频方案合计节约** | 459.6 元 | 144.4 元 | **🔑 315.2 元** |

**线束减重数据**：约 14.88 kg（~15 kg）；每减重 10 kg → 续航延长约 0.5~1 km

**关键参数对比**：
- 喇叭线束平均长度：A2B 4 米 → GPAN 1.2 米（**缩短 70%**）
- 头枕喇叭线束：A2B 4 米 → GPAN 1 米（**缩短 75%**）
- RNC 收音线束：A2B 20 米 → GPAN 12 米（**缩短 40%**）
- 喇叭线束价格：0.7 元/米 → 0.5 元/米（线短则细，成本降低）

### 综合收益汇总

| 收益维度 | 节约金额 |
|---|---|
| 二级网络 ZCU BOM | 141 元/套 |
| 三级网络 ECU BOM | 20 元 |
| 48V 分布式音频 | **315 元** |
| **总计（48V 平台）** | **~476 元/车** |

> 12V 平台音频收益约 60 元，总计约 221 元/车。

## Entities Mentioned

- [[entities/goodix-technology]]

## Concepts

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
