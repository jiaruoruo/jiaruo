---
type: concept
title: "MCULess 架构"
date: 2026-04-27
updated: 2026-04-28
tags:
  - mculess
  - automotive
  - eea
  - zonal-gateway
  - bom-cost
source_count: 27
confidence: high
domain_volatility: high
last_reviewed: 2026-04-28
aliases:
  - "MCULess 架构"
  - "MCULess"
  - "mculess-architecture"
  - "无 MCU 边缘节点架构"
  - "去 MCU 方案"
---

# MCULess 架构（MCULess Architecture）

## Definition

MCULess 架构是指在汽车 EEA（电子电气架构）3.0 的区域控制器（ZCU）节点中，**去除独立主机 MCU**，将原先 MCU 承担的信号路由、协议转换、IO 采集职能转移到专用通信芯片（如 Goodix GE1101 GPAN 芯片）的硬件路由层执行，从而降低边缘节点的 BOM 成本、PCB 面积和 OTA 维护复杂度。MCULess 方案的核心是：域控制器（DCU）通过高速网络（GPAN/100BASE-T1）直接控制边缘节点的驱动芯片，无需本地 MCU 参与中间处理。

## Key Points

- **架构演进背景**：
  - 传统 EEA 1.0/2.0：分散 ECU，每功能独立 ECU
  - EEA 3.0（域控架构）：域控制器 + 区域控制器（ZCU）分层，ZCU 仍含独立 MCU
  - MCULess：EEA 3.0 进一步演进，去除 ZCU 中的 MCU，域控直接控制边缘节点
- **技术实现原理**：
  - 边缘节点仅保留：通信芯片（GE1101）+ 驱动芯片（HSD/H-Bridge/EFUSE 等）
  - 通信芯片通过硬件路由表完成：以太网帧↔CAN 帧↔LIN 帧的协议转换
  - IO 采集（ADC/GPIO/Hall）和控制输出（PWM/HSD）由通信芯片硬件直接处理，无软件参与
  - 域控制器承担所有控制逻辑和状态机，对边缘节点执行完全集中式控制
- **量化收益**（基于 Goodix GPAN MCULess 方案实测/估算）：
  - **BOM 成本节省**：每套 3 个 ZCU 节省约 **141 元 RMB**（MCU 本体 + 晶振/Flash/LDO/去耦电路）
  - **分布式功放节省**：约 **300 元 RMB**（音频路由由 TDM 硬件承担）
  - **PCB 面积减少**：约 **1000mm²/节点**
  - **OTA 简化**：边缘节点无软件 → 无需边缘 OTA → 消除 OTA 失败和售后风险
- **通信延迟实测结果**（GPAN MCULess 方案）：
  - CAN→CAN 路由：**21~62μs** ✅（目标 ≤100μs）
  - CAN→ETH 路由：**43~63μs** ✅（目标 ≤100μs）
  - 音频 TDM 路由：**40μs** ✅（A2B 规格 <100μs）
- **适用域与禁用域**：

  | 应用域 | MCULess 适用性 | 原因 |
  |---|---|---|
  | 车身域（门锁/座椅/照明/雨刮） | ✅ 推荐 | 控制逻辑简单，无本地安全计算需求 |
  | 智能电源域 | ✅ 推荐 | 电源路由逻辑可由硬件承担 |
  | 底盘气悬域 | ❌ 不推荐 | 本地控制算法复杂，MCULess 导致域控 CPU +10% |
  | 制动/转向/气囊（ASIL-D） | ❌ 禁止 | 功能安全要求本地降级（Fallback），必须保留 MCU |

- **当前生态进展**（截至 2025 年）：
  - Goodix GPAN MCULess 方案：EVT/DVT 阶段，FPGA（Xilinx K7）原型验证完成
  - 量产芯片 GE1101（BGA144/BGA196）：流片后验证中
  - OEM 合作：理想汽车（BZCU 验证）、长安汽车（POC）、小鹏汽车（POC）、长城+大陆（联合 POC）
  - Tier-1 参与：恒润科技已提交 GPAN 座椅控制器售前方案
- **三大技术流派（2026 年行业视角）**：
  - **10BASE-T1S + RCP**（以太网路线）：ADI E2B（宝马量产）、Onsemi T30HM1TS3600/3610、Microchip LAN8660；10Mbps，<1ms，标准推进中（IEEE TC18 Draft 0.2）
  - **CAN FD Light**（简化 CAN）：ST 1991dlh32；500K–2Mbps，超低成本，适合 LED/简单执行器
  - **UART over CAN**（软硬混合）：TI、Infineon 方案；保留 CAN 物理层，上层协议简化；改造成本低
- **RCP 芯片选型对比**（2026 年数据）：

  | 厂商 | 型号 | IO 数 | 速率 | 延迟 | 价格 | 状态 |
  |---|---|---|---|---|---|---|
  | ADI | AD3304 | 12 | 10 Mbps | <1ms | ~$1.3 | 量产（宝马）|
  | Onsemi | T30HM1TS3600/3610 | 10/20 | 10 Mbps | <1ms | — | 样片 |
  | Microchip | LAN8660 | 16 | 10 Mbps | — | — | — |
  | 汇顶 GE1101 | GPAN | 120/45 | 100 Mbps | ~50 μs | ~14 RMB | 预计 2026Q3 |
  | ST | 1991dlh32 | — | 500K–2M（CAN FD）| 低 | — | — |

- **硬件极简化量化数据**（2026 行业综合）：
  - 传统 ECU BOM：$15–25 → MCU-less 方案：$8–12（节省约 40%）
  - PCB 面积：25×35mm → 15×20mm（节省约 51%）
  - 线束减重：50–60%
  - ZCU 控制器数量减少 75–80%（小米 YU7：减少 75%；小鹏 XEEA3.5：减少 50% 硬件）
- **中国市场（2024 年，佐思汽研）**：ZCU 渗透率 8.83%，搭载量 >200 万辆，市场规模 39.3 亿元

## My Position

MCULess 架构是 EEA 3.0 向 EEA 4.0（软件定义汽车）演进的重要过渡方案，其核心价值在于通过硬件路由替代软件路由来降低系统复杂度。但这也意味着边缘节点的灵活性大幅降低——任何路由逻辑变更都需重新配置硬件路由表而非升级软件。这与"软件定义汽车"的长期方向存在一定矛盾，MCULess 更适合功能稳定、变更需求少的车身舒适域，而非需要频繁功能迭代的智能驾驶域。

## Contradictions

- [[sources/mculess-validation-report]] 指出底盘气悬域 MCULess 不推荐（CPU +10%），而 [[sources/mculess-solution-research]] 也明确标注底盘域为禁用场景，两者结论一致
- [[sources/goodix-gpan-automotive-presentation]] 宣传 MCULess 的 OTA 简化优势，但实际上，将控制逻辑集中到域控后，域控的 OTA 复杂度会相应增加，这一权衡关系在销售材料中未充分披露

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
- [[sources/mculess-eea-implementation-deep-dive]]
- [[sources/zcu-mculess-next-gen-architecture]]
- [[sources/mculess-edge-node-tech-evolution]]
- [[sources/mculess-ecu-central-computing-path]]
- [[sources/mculess-hardware-simplification-revolution]]
- [[sources/mculess-10baset1s-rcp-discussion]]
- [[sources/mculess-smart-lighting-innovation]]
- [[sources/zcu-market-research-2025]]
- [[sources/sdv-architecture-revolution]]

## Evolution Log

- 2026-04-27（10 sources）：概念初建，来源为 Goodix GPAN MCULess 方案完整资料集（芯片手册 + 调研报告 + 验证报告 + 硬件设计 + 售前方案）
- 2026-04-27（12 sources）：raw/articles 批次新增 5 个来源，补充 RCP（ADI/NXP 10Base-T1S）vs GPAN 详细对比表（10M 半双工 vs 100M 全双工、控制延迟 1.09ms vs 50μs、节点数 12 vs 60）、座椅项目 ZCU BOM 成本明细（总节省 161 RMB/套）、IO 支持矩阵（CAN×5 / LIN×5 / GPIO×50 / PWM×24 / ADC×16 / 82 唤醒源）
- 2026-04-27（17 sources）：raw/articles 二进制文件解析批次新增 5 个来源，补充 SDV 演进 4 阶段路线（现有→ZCU含音频→逐步去MCU→全车集中）、座椅项目 4 种拓扑候选方案（推荐大环方案 D）、ZCU 5 层软件架构（GPAN SDK→RCP抽象层→设备抽象层→原子服务→应用）、BOM 三级网络节约 20 元/车、48V 音频节约 315 元/车、ASIL-B 安全支持
- 2026-04-28（18 sources）：raw/clippings 批次新增 1 个来源，补充全行业 MCU-less 竞品对比表（ADI/TI/NXP/ST/Infineon/汇顶科技 GE1101）；GE1101 以 64 路 IO + 100BaseT1 + ~14 RMB 价格在规格上最全；确认 2026 Q2 量产计划
- 2026-04-28（27 sources）：raw/clippings 批次新增 9 个来源（多篇深度技术文章），重大知识更新：①三大技术流派（10BASE-T1S+RCP / CAN FD Light / UART over CAN）完整对比；②RCP 协议标准化历史（宝马 2023 TC14 提案→2024 TC18 Draft 0.2）；③RCP 芯片选型对比表（ADI AD3301/AD3304/AD3305、Onsemi T30HM1TS3600/T30HM1TS3610、Microchip LAN8660、汇顶 GE1101、ST 1991dlh32）；④量化成本数据（传统 ECU BOM $15–25 → MCU-less $8–12，PCB 25×35mm→15×20mm，线束减重 50–60%）；⑤中国市场 ZCU 2024 渗透率 8.83%、搭载量>200 万辆；⑥Onsemi T30HM1TS3600 芯片完整架构（PHY/MAC/RCP CORE/管理模块/PIN MUX、全接口规格、多级电源管理）；⑦易冲半导体 CPSQ5355 车灯 MCU-less 案例（ASIL-B，65V，2A/ch，UART 2Mbps，OTP）；⑧双重解耦概念（软硬解耦+软软解耦）
