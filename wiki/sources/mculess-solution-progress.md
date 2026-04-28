---
type: source
title: "MCULess 方案进展介绍"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "内部项目进展汇报"
tags:
  - mculess
  - gpan
  - bom-saving
  - ecosystem
  - automotive
processed: true
raw_file: "raw/pdfs/MCULess方案进展介绍.pdf"
raw_sha256: "2854008018fadfe70a54e2df30525b39dd52626e7f15d285dff7fff8d9c7f505"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# MCULess 方案进展介绍

## Summary

本文档为 MCULess 方案阶段性进展汇报，重点呈现方案带来的量化收益（BOM 成本节省、PCB 面积缩减、OTA 简化），以及当前生态合作进展（联电、长安、小鹏、长城+大陆 POC 计划）。

## Key Points

- **量化收益指标**：
  - **BOM 成本节省（ZCU 侧）**：每套 3 个 ZCU 节省约 **141 元 RMB**（主要来自 MCU 芯片及其外围：晶振/LDO/去耦电容/Flash/复位电路）
  - **分布式功放节省**：传统分布式功放方案采用独立 DSP MCU，MCULess 后节省约 **300 元 RMB**（音频路由由 GPAN 芯片 TDM 承担）
  - **PCB 面积缩小**：单节点 PCB 面积减少约 **1000mm²**（约邮票大小），有利于整车线束布局和零件封装
  - **OTA 简化**：边缘节点无 MCU 即无软件，彻底消除边缘节点 OTA 升级需求，减少 OTA 失败风险和售后成本
- **生态合作进展**：
  - **联电（UMC）**：POC 合作确认，验证 GPAN MCULess 在车身域节点的制造可行性
  - **长安汽车**：POC 阶段，聚焦车门控制器（DCM）场景的 MCULess 替代方案
  - **小鹏汽车**：POC 阶段，关注座椅控制器和后备箱节点
  - **长城汽车 + 大陆集团**：联合 POC，大陆集团作为 Tier-1 供应商参与方案集成
- **技术成熟度评估**：
  - 当前处于工程验证阶段（EVT/DVT 过渡期），FPGA 原型（Xilinx K7）已完成基础功能验证
  - GE1101 正式量产芯片（BGA144/BGA196）处于流片后验证阶段
  - 预计量产时间：参考客户 SOP 节点（具体时间未披露）
- **方案推广策略**：
  - 优先从车身域（低安全等级）切入，积累量产经验后向智能电源域扩展
  - 与域控制器厂商（如 Desay SV、Visteon）合作，将 GPAN 作为域内网络标准推广

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/zonal-gateway]]
- [[concepts/eea-architecture]]

## Entities Extracted

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Contradictions

<!-- 暂无 -->

## My Notes

141 元 BOM 节省和 300 元功放节省是针对特定车型的估算，实际收益取决于车型配置和 ZCU 数量。小鹏和长城的 POC 参与说明 MCULess 方案已引起多家主流 OEM 关注，但距离量产仍需完成 ASPICE/ISO 26262 功能安全认证。
