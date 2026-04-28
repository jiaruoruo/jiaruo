---
type: source
title: "Goodix GPAN 车载通信技术介绍"
date: 2026-04-27
source_url: ""
domain: "automotive-network"
author: "Goodix Technology（汇顶科技）"
tags:
  - gpan
  - automotive
  - mculess
  - adi-10baset1s
  - vehicle-network
processed: true
raw_file: "raw/pdfs/Goodix GPAN Presentation for 车载通信(1).pdf"
raw_sha256: "b13902ffd534ddfb4c502931ba93c23b24c5f979119f01679f834fc88a1fb78d"
last_verified: 2026-04-27
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# Goodix GPAN 车载通信技术介绍

## Summary

本演示文档为 Goodix 面向车载通信客户的 GPAN 技术商务介绍，系统阐述了 GPAN 相对传统 CAN/LIN/以太网的架构优势，重点介绍 MCULess 方案的核心价值，并与 ADI 10BaseT1S 方案进行了详细的竞品对比分析。

## Key Points

- **传统车载通信痛点**：
  - CAN/LIN：带宽低（500kbps~10Mbps），无法支持音频/视频扩展，多总线共存增加线束复杂度
  - 100BASE-TX/1000BASE-T 以太网：成本高，不支持环网，无混合传输能力
  - 现有方案均需边缘节点 MCU 进行协议转换，增加延迟和 BOM 成本
- **GPAN 核心技术优势**：
  - 单芯片混合传输：以太网 + CAN/LIN + 音频（TDM），替代传统多总线架构
  - 环网拓扑：支持冗余自愈，单点故障不中断通信
  - 最多 60 个子节点：满足完整车身域（LZCU + RZCU + BZCU）部署需求
  - 控制回路延迟：**50μs 典型值**（硬件路由，无软件参与）
- **MCULess 方案核心价值**：
  - 边缘节点（ZCU/传感器节点）去除独立 MCU，由 GPAN 芯片硬件路由承担原 MCU 的信号转发功能
  - 每3个 ZCU 节省约 141 元 BOM 成本（MCU + 相关外围器件）
  - 分布式功放节省约 300 元 BOM 成本
  - 边缘节点无需 OTA 升级，降低运营维护复杂度
  - 节点 PCB 面积缩小约 1000mm²
- **与 ADI 10BaseT1S 竞品对比**：

  | 维度 | Goodix GPAN | ADI 10BaseT1S |
  |---|---|---|
  | 控制回路延迟 | **50μs** | 1.09~1.32ms |
  | 网络拓扑 | 环网 + 菊花链 | 仅菊花链（无环网） |
  | 最大节点数 | **60** | 12（受物理层限制） |
  | 混合传输 | 以太网+CAN+LIN+音频 | 仅以太网 |
  | MCULess 支持 | 原生支持 | 需额外 MCU 做协议转换 |
  | GPIO 扩展 IO | 丰富（多路GPIO） | 受限（12个IO） |

- **目标应用场景**：车身域控制器（BCM/ZCU）替换、座椅/车门/照明节点、分布式音频功放网络、汽车后视镜/摄像头节点
- **已验证客户生态**：联电、长安、小鹏汽车、长城汽车（含大陆集团合作）均有 POC 合作计划

## Concepts Extracted

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/zonal-gateway]]
- [[concepts/eea-architecture]]
- [[concepts/can-eth-protocol-conversion]]

## Entities Extracted

- [[entities/goodix-technology]]

## Contradictions

- 与 [[sources/ethercat-gpan-servo-validation]] 关于 GPAN 延迟描述有差异：本演示文档给出 50μs 典型控制回路延迟，ethercat-gpan-servo-validation 中描述节点交换时延为 1.4μs——两者并不矛盾（节点交换时延 vs. 端到端控制回路延迟），但需在概念页中明确区分两种延迟定义

## My Notes

此演示是 Goodix 对外销售材料，用于面向 OEM/Tier-1 客户的商务场景。竞品对比数据（ADI 10BaseT1S 延迟 1.09~1.32ms）来源于 Goodix 内部测试，需注意测试条件可能存在差异。
