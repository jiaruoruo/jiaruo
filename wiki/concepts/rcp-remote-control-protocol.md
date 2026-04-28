---
type: concept
title: "RCP 远程控制协议"
date: 2026-04-28
updated: 2026-04-28
tags:
  - rcp
  - mculess
  - 10base-t1s
  - automotive
  - eea
  - ieee
source_count: 5
confidence: medium
domain_volatility: high
last_reviewed: 2026-04-28
aliases:
  - "RCP"
  - "Remote Control Protocol"
  - "远程控制协议"
  - "rcp-remote-control-protocol"
---

# RCP 远程控制协议（Remote Control Protocol）

## Definition

RCP（Remote Control Protocol，远程控制协议）是一种专为汽车 MCU-less 架构设计的轻量级通信协议，允许区域控制器（ZCU）通过 **10BASE-T1S 单对以太网**直接远程控制边缘节点的物理接口（GPIO/PWM/SPI/I2C/UART 等），而无需在边缘节点部署本地 MCU。由**宝马**于 2023 年在 IEEE TC14 工作组提出，目前由 IEEE TC18 工作组推进标准化（Draft 0.2 阶段）。

## Key Points

### 标准化历史

| 时间 | 事件 |
|---|---|
| 2023 年 5 月 | 宝马在 IEEE TC14 工作组提出 RCP 概念 |
| 2024 年 7 月 | IEEE TC18 工作组成立，专项推进 RCP 标准化 |
| 2026 年 4 月 | Draft 0.2，标准仍在制定中 |

### 工作原理

- **客户端-服务器模型**：ZCU 运行 RCP 客户端，边缘节点 RCP 芯片作 RCP 服务器
- **指令传递**：ZCU 生成原生总线指令（SPI 命令/I2C 读写/GPIO 设置/PWM 配置）→ 封装为 RCP 消息 → 通过 10BASE-T1S 传输 → 边缘节点 RCP CORE（硬件状态机）直接执行
- **无软件介入**：边缘节点不需要操作系统，不需要应用程序，全部由硬件状态机完成

### 消息结构（protobuf 序列化）

**Directive 指令消息**（ZCU → 边缘节点）：
- `seq`：序列号，非零时服务器必须回复同 seq 的 Report
- `cfg`：配置列表（外设参数配置）
- `act`：动作列表（执行命令）
- `qry`：查询列表
- `acl`：取消周期性动作
- `ven`：厂商自定义扩展

**Report 报告消息**（边缘节点 → ZCU）：
- `seq`：对应 Directive 的序列号
- `cfg`/`act`/`qry` 结果
- `ntf`：主动通知（异步事件）

### 高级特性

- **定时执行**：`ptime` 字段支持 IEEE 802.1AS PTP 格式绝对时间戳调度
- **周期性动作**：`repPeriod` + `repCount`，支持单次/有限次/无限循环
- **并发执行**：单个 act 内多命令同时执行，无需多次交互
- **gPTP 时间同步**：通过 TSSI 接口支持微秒级时间同步，配合 TSN 应用

### 封装协议选项

| 封装方式 | 特点 | 推荐度 |
|---|---|---|
| SOME/IP | 成熟，AUTOSAR 广泛使用，开销较大 | 可用 |
| **IEEE 1722（AVTP）** | 低延迟，时间敏感，帧头开销小，原生支持 TSN | **推荐** |
| Protocol Buffers | 紧凑序列化，语言中立（Onsemi 方案采用）| 实现层选项 |

### 与 10BASE-T1S 的关系

- RCP 依赖 **10BASE-T1S（IEEE 802.3cg）** 作为物理和链路层
- PLCA 机制保障确定性传输延迟（时分复用）
- 配合 PoDL（以太网供电）可实现单对线数据+供电

### MCU-less 三种部署模式

1. **端节点部署**：仅边缘节点使用 RCP 芯片，ZCU 保持传统形态
2. **ZCU 部署**：ZCU 运行 RCP 客户端软件，统一管理下挂 RCP 节点
3. **全链路部署**：中央平台到边缘节点全链路 RCP 化

### 主要 RCP 芯片

| 厂商 | 型号 | IO 数 | 速率 | 延迟 | 状态 |
|---|---|---|---|---|---|
| ADI | AD3304（E2B）| 12 | 10 Mbps | <1ms | 量产（宝马采用）|
| Onsemi | T30HM1TS3600 | 10 | 10 Mbps | <1ms | 样片 |
| Onsemi | T30HM1TS3610 | 20 | 10 Mbps | <1ms | 样片 |
| Microchip | LAN8660 | 16 | 10 Mbps | — | — |
| 汇顶 GPAN | GE1101 | 120/45 | 100 Mbps | ~50 μs | 预计 2026Q3 |

## My Position

RCP 是 MCU-less 架构的核心使能协议，其标准化进程（Draft 0.2）显示汽车行业对该技术路线有强烈共识。主要挑战在于：①10BASE-T1S MAC+PHY 成本约十几元 RMB 远高于 CAN 收发器（几毛钱），成本差距短期难以弥补；②RCP 标准尚未最终确定，各厂商实现存在差异（Onsemi 用 protobuf，ADI 用自定义格式）；③CAN 生态极其成熟，工具链迁移成本高。预计 2026–2028 年随宝马等头部量产项目扩大规模，生态会逐步成熟。

## Contradictions

- AlvinY 分析认为 IEEE 1722 更适合 RCP 封装（低延迟），但 Onsemi T30HM1TS3600 实际采用了 Protocol Buffers，两种路线并存，标准未最终确定前难以判断优劣

## Sources

- [[sources/mculess-10baset1s-rcp-discussion]]
- [[sources/mculess-eea-implementation-deep-dive]]
- [[sources/mculess-edge-node-tech-evolution]]
- [[sources/mculess-hardware-simplification-revolution]]
- [[sources/zcu-market-research-2025]]

## Evolution Log

- 2026-04-28（5 sources）：概念初建，来源为 2026-04-28 批次 raw/clippings 多篇深度技术文章，覆盖 RCP 起源（宝马 2023）、标准化进程（TC18 Draft 0.2）、Onsemi T30HM1TS3600 完整实现、封装协议对比（SOME/IP vs IEEE 1722）、三种部署模式
