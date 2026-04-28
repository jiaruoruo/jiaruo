---
type: entity
entity_type: institution
title: "Goodix Technology（汇顶科技）"
date: 2026-04-27
updated: 2026-04-27
tags:
  - semiconductor
  - automotive
  - gpan
  - china
source_count: 21
aliases:
  - "汇顶科技"
  - "Goodix"
  - "goodix-technology"
  - "Goodix Technology"
  - "汇顶"
---

# Goodix Technology（汇顶科技）

## Overview

Goodix Technology（汇顶科技，股票代码：603160.SH）是中国领先的半导体公司，总部位于深圳，以指纹识别芯片起家，现已扩展至车载通信芯片领域。在汽车 EEA 架构演进方向上，Goodix 推出了 GPAN（General Precision Automation Network）车载网络芯片系列，主打产品为 GE1101，支持 MCULess 架构，面向汽车 EEA 3.0 区域控制器（ZCU）节点的降本增效需求。

## Key Facts

- **成立时间**：2002 年
- **总部**：中国深圳
- **上市**：A 股上市（603160.SH，上交所科创板）
- **核心产品线**：
  - 指纹识别芯片（消费电子主营）
  - GPAN 车载通信芯片（GE1101）
  - 触控芯片（手机/汽车 HMI）
- **GE1101 芯片规格**：
  - 封装：QFN48（初版）/ BGA144 / BGA196（车规量产版）
  - 接口：100BASE-T1 以太网 MAC + MII、CAN 2.0A/2.0B、LIN 2.1/2.2、多路 GPIO/SPI/I²C/UART/PWM、TDM 音频
  - 拓扑：环网（Ring）/ 菊花链（Daisy Chain），最多 60 个子节点
  - 控制延迟：50μs 典型（端到端控制回路），21~62μs（CAN→CAN 实测）
  - PTP 时钟同步：≤40ns（硬件时间戳）
- **MCULess 方案生态**：
  - OEM 合作：理想汽车、长安汽车、小鹏汽车、长城汽车
  - Tier-1 合作：恒润科技（Hirain）、大陆集团（联合 POC）
  - 晶圆制造伙伴：联电（UMC）
- **技术成熟度**（截至 2025 年 8 月）：
  - FPGA 原型（Xilinx K7）验证完成，GE1101 量产芯片流片后验证中
  - BZCU（理想汽车）第一阶段硬件设计完成（V0.94）

## Relationships

- 主导产品：[[concepts/gpan-communication]]
- 核心方案：[[concepts/mculess-architecture]]
- 客户：[[entities/li-auto]]
- 竞品：ADI（Analog Devices）10BaseT1S 方案

## Sources

- [[sources/goodix-ge1101-app-intro]]
- [[sources/goodix-ge1101-user-manual]]
- [[sources/goodix-gpan-automotive-presentation]]
- [[sources/mculess-solution-research]]
- [[sources/mculess-solution-progress]]
- [[sources/mculess-based-zcu-validation]]
- [[sources/mculess-validation-scope]]
- [[sources/mculess-validation-report]]
- [[sources/gpan-seat-controller-presales]]
- [[sources/mculess-bzcu-hardware-design]]
- [[sources/mculess-tech-comparison-analysis]]
- [[sources/ethercat-gpan-servo-validation-design]]
- [[sources/gpan-mculess-validation-full-report]]
- [[sources/gpan-chip-spec-v02]]
- [[sources/gpan-functional-clarification-v41]]
- [[sources/gpan-mculess-audio-intro]]
- [[sources/gpan-automotive-comm-app-v08]]
- [[sources/gpan-automotive-comm-app-v06]]
- [[sources/gpan-seat-project-discussion]]
- [[sources/gpan-bom-cost-analysis]]
- [[sources/mculess-vendor-research-report]]

## Evolution Log

- 2026-04-27（10 sources）：实体初建，来源为 GPAN MCULess 方案完整资料集，覆盖芯片规格/方案调研/验证结果/售前应用
- 2026-04-27（15 sources）：raw/articles 批次新增 5 个来源（MCU-LESS 技术对比分析、EtherCAT-GPAN 伺服验证设计、GPAN MCULess 完整验证报告、GPAN 芯片规格 V0.2、GPAN 功能澄清 V4.1），补充 GE1101 完整 IO 规格表、7 大应用场景、72-bit 帧头格式、两种初始化模式及 Force Sleep 机制等底层技术细节
- 2026-04-27（20 sources）：raw/articles 二进制文件解析批次新增 5 个来源（PPTX V1.8/V0.8/V0.6 市场推广文件、座椅项目三方讨论 PPTX、BOM 成本核算 XLSX），补充芯片路线图（Tapeout 2026-04-15 / 工程样片 2026-08-01 / 量产 2027-03 / AECQ-100 2027-10）、完整封装矩阵（BGA196/BGA144/QFN64/QFN32 及 5G/2.5G/1G 路线图）、48V 平台综合节约约 476 元/车
- 2026-04-28（21 sources）：raw/clippings 批次新增 1 个来源，提供行业竞品视角（ADI $1.3/12路IO/10BaseT1S；TI $0.487/13路IO；ST/Infineon LED 驱动为主）；外部调研确认 GE1101 在 IO 数量（64路）和速率（100BaseT1 vs 10BaseT1S）上具备显著竞争优势；2026 Q2 量产计划与内部 Roadmap 文件一致
