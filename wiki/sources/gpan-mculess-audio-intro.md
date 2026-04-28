---
type: source
title: "GPAN 车载MCULess和分布式音频介绍 V1.8"
date: 2026-04-27
source_type: presentation
source_url: ""
raw_path: "raw/articles/GPAN 车载MCULess和分布式音频介绍(1.8).pptx"
raw_sha256: d336b5fc
author: "Goodix Technology（汇顶科技）"
language: zh
tags:
  - gpan
  - mculess
  - distributed-audio
  - automotive
  - a2b
  - goodix
---

# GPAN 车载MCULess和分布式音频介绍 V1.8

## Summary

Goodix 官方 PPTX 演示文稿（33页，V1.8），系统介绍 GPAN 芯片在车载 MCULess 和分布式音频两大核心应用场景的技术方案、与竞品对比及量产路线图。为目前最完整的 GPAN 市场推广资料。

## Key Points

### GPAN 整体定位
- General Purpose Access Network：高效/可靠/低成本/低时延组网的 IO 扩展芯片
- 支持**控制数据 + 音频数据 + 视频数据**混合传输（单总线替代多总线）
- 全双工 100M（100Base-T1），误码率 <10⁻¹⁰，节点交换时延 ~1.4μs
- 环网最多 60 个子节点，节点间传输距离 100 米

### MCULess 方案
- **核心主张**：约 90% IO 可通过 IO 扩展芯片进行本地/远程扩展，MCU 选型只需关心算力
- **适用场景**：除霜、座椅按摩通风、坐垫加热、氛围灯、雷达配电、遮阳帘、雾灯、悬架开关等
- **传统方案 vs GPAN MCULess 6 维对比**：

  | 对比维度 | 传统方案 | GPAN MCULess | 核心收益 |
  |---|---|---|---|
  | 算力成本 | 高，无法共享 | 低，算力共享 | 减少综合 MCU 算力需求 |
  | 协同控制 | 高，需网关协同 | 低，天然协同 | 算力共享 |
  | 协议互转 | 高，CAN 网段多 | 低，GPAN 硬件互转 | 减少 CAN 端口 |
  | 软件开发/维护 | 高，众多 MCU | 低，MCU 大幅减少 | 减少开发维护成本 |
  | 硬件 BOM | 高，MCU+IO扩展 | 低，无需 IO 扩展芯片 | 减少 BOM 数量 |
  | 音频支持 | 高，A2B 贵+走线多 | 低，控制+音频天然融合 | 分布式功放最佳方案 |

- **量化收益估算**（见 [[sources/gpan-bom-cost-analysis]]）：
  - 替换 ZCU MCU 节省约 **50 元/节点**
  - 去掉外围扩展芯片，减少 PCB 面积
  - 48V 分布式功放方案综合节约约 **300 元**（*待细化）
  - 12V 平台约 **60 元**

### 与竞品 10Base-T1S MCULess 对比

| 对比项 | 10Base-T1S MCULess | GPAN MCULess |
|---|---|---|
| 内部处理时延 | 大，>290μs | **短，<50μs** |
| 带宽 | 小，半双工 10M | **大，环模式全双工 200M** |
| IO 数量 | 少，受限于带宽/时延 | **大，带宽时延优** |
| 音频播放 | 困难 | **容易** |
| 适用网络层级 | 三级网络（带宽/时延不敏感） | 二级+部分三级（时延敏感/防夹/音频） |

### 分布式音频方案（ANC/RNC）

| 对比项 | 以太网音频 | A2B | **GPAN** |
|---|---|---|---|
| 线束长度节约 | 无 | 无 | **约 65%** |
| 芯片成本 | 高（TSN 升级） | 高（独家垄断） | **低（自研无专利风险）** |
| 单向时延 | >200μs | ~62μs | **<50μs（性能提升 20%）** |
| Jitter（Slave SYNC） | 未公布 | S1:1.57ns / S10:5.5ns | **Normal:<1.2ns / 性能模式:~100ps** |
| RNC（≤1ms）支持 | 差/无法实现 | 支持 | **最优** |
| ANC（≤0.5ms）支持 | 不支持 | 支持 | 支持 |
| 单线故障 | 环模式支持 | ❌ | **环模式支持** |
| 综合成本 | 高 | 高 | **低** |

- GPAN 音频参数：采样率 12K/24K/48K/96K，精度 16/20/24/32bit，单向最多 48 通道
- 同步精度：各节点 Sync 同步 <1μs；传输时延抖动 <1μs

### 芯片选型路线图（截至 V1.8）

| 重要节点 | 预计时间 | 备注 |
|---|---|---|
| 芯片 Tapeout | 2026-04-15 | 客户第一阶段需求验证完毕 |
| 工程样片送样 | 2026-08-01 | 第一版工程样片 |
| 量产芯片（BGA196/144/QFN64/32） | 2027-03 | 支持 ASIL-B |
| 第三方 AECQ-100 报告 | 2027-10 | 含 EMC/EMI/ESD |

### 封装矩阵（完整版）
- **BGA196（10×10）**：车规量产主力，150 IO
- **BGA144（8×8）**：车规量产，64 模拟 IO
- **QFN64（9×9）** / **QFN32（5×5）**：低成本版
- 支持 5G/2.5G/1G（开发中）+ 100M + CAN/CAN-FD + CAN-XL（开发中）

### SDV 演进路线（4 阶段）
1. 现有方案：音频和 ZCU 分离，组网复杂，A2B 芯片+线束成本高
2. 第一步：ZCU 包含音频系统（省约 50 元+300 元）
3. 第二步：逐步去除 MCU（替换 ZCU 中 MCU → 节约约 80 元）
4. 最终趋势：仅 HPC 保留处理器，全车软件集中，一/二/三级分级网络冗余

### 安全特性
- 支持 ASIL B（GPAN 芯片）+ ASIL D（VCP MCU）
- 单侧线路故障后，1ms 内切换为双菊花链
- 备份控制器通过交换机接管网络

## Entities Mentioned

- [[entities/goodix-technology]]
- [[entities/li-auto]]（理想汽车）

## Concepts

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
- [[concepts/time-sensitive-networking]]（TSN 对比）
