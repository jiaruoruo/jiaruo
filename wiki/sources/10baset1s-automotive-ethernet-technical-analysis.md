---
type: source
title: "10BASE-T1S汽车以太网技术深度解析"
source_url: "https://mp.weixin.qq.com/s/e0FwyKwIcOlL7UduVq6hzg"
author: "汽车电子老登"
date: "2026-05-05"
tags: [10baset1s, plca, automotive-ethernet, t30hm1ts3600, ieee-802-3cg, mculess-architecture]
raw_file: "raw/clippings/2026-05-0510BASE-T1S汽车以太网技术深度解析.md"
raw_sha256: b5f581a8b8c7cb567ae708123c2a1d67b47bf02a356b70f8fbd02ac270e047e7
last_verified: 2026-05-05
---

## 核心摘要

IEEE 802.3cg-2019 定义的 10BASE-T1S 标准采用 DME 编码（零直流分量）和 PLCA 冲突避免机制，在单根双绞线上实现 10Mbps 半双工多节点共享总线，总线最长 25m，分支 <0.1m，支持最多 255 个从节点，是汽车 MCU-less 架构的首选物理层。

## IEEE 802.3cg-2019 标准规范

| 参数 | 规范值 |
|------|--------|
| 标准名称 | IEEE 802.3cg-2019 |
| 数据速率 | 10 Mbps |
| 双工模式 | 半双工 |
| 传输介质 | 单根非屏蔽双绞线（UTP） |
| 总线最大长度 | **25m** |
| 分支（Stub）最大长度 | **<0.1m** |
| 终端阻抗 | **100Ω**（总线两端各一个） |
| 最大节点数（IEEE） | 8–16 节点 |
| 编码方式 | 4B/5B + DME（Differential Manchester Encoding） |

## DME 编码原理与 EMC 优势

**DME（差分曼彻斯特编码）特性**：

1. **零直流分量**：每个码元内都有跳变，长期直流平均为 0
2. **EMC 优势**：无直流偏置，减少低频辐射，通过 OEM 整车 EMC 测试更容易
3. **时钟恢复**：接收端可从数据中提取时钟，无需独立时钟线
4. **实现**：4B/5B 编码（每 4 位数据映射为 5 位码字）+ DME 调制

## PLCA（Physical Layer Collision Avoidance）

### 节点角色

| 角色 | PLCA_ID | 数量 | 职责 |
|------|---------|------|------|
| 协调器（Coordinator） | 0 | 1 个 | 发送 BEACON，管理轮询周期 |
| 从节点（Follower） | 1–255 | 最多 255 | 按 ID 顺序轮询，声明发送意图 |

### 一个完整 PLCA 周期

```
协调器发送 BEACON
    ↓
ID=1 的 COMMIT 时隙（有数据→发送，无数据→静默）
    ↓
ID=2 的 COMMIT 时隙
    ↓
...
    ↓
ID=N 的 COMMIT 时隙
    ↓
回到 BEACON（新一轮）
```

### 突发模式（Burst Mode）

- 允许单个节点在一个时隙内连续发送多帧
- `burst_count` 参数控制最大连续帧数
- 适用于需要传输连续数据流的节点（如音频、视频）

### PLCA 故障恢复

- 若协调器故障：经过约 **13ms** 超时后，所有节点自动退化为 **CSMA/CD** 模式
- CSMA/CD 模式下总线利用率约 37%（vs PLCA 的 >90%）
- 支持主冗余（Master Redundancy）：Onsemi 专有特性，双协调器热备份

## Onsemi Master Redundancy（专有特性）

- T30HM1TS3600 支持 Onsemi 专有的主冗余功能
- 两个节点均配置为协调器（PLCA_ID=0）
- 主协调器活跃时备用协调器静默监听
- 主协调器故障后备用协调器自动接管，接管时间 <1ms
- **注意**：此为 Onsemi 专有扩展，非 IEEE 标准，跨厂商互通需确认兼容性

## 多点接入拓扑约束

### 支持的拓扑形式

```
拓扑 1：点对点（P2P）
节点A ────────────────────── 节点B
      100Ω                100Ω

拓扑 2：菊花链（Daisy Chain）
节点A ── 节点B ── 节点C ── 节点D
100Ω                          100Ω

拓扑 3：多分支（Multi-Drop，推荐）
                主干线（≤25m）
100Ω ──┬──────┬──────┬────── 100Ω
       │      │      │
     节点A  节点B  节点C
    （分支<0.1m）
```

### 关键设计约束

| 约束项 | 限制值 | 原因 |
|--------|--------|------|
| 总线总长度 | ≤25m | 信号衰减 + 传播延迟 |
| 分支（Stub）长度 | **<0.1m** | 防止信号反射（阻抗不连续） |
| 终端数量 | 2 个（总线两端） | 100Ω 匹配，消除反射 |
| 最小节点间距 | 无硬性限制 | 建议 >0.1m 减少近端串扰 |

> **Stub <0.1m 是最严格约束**：超过 0.1m 会产生明显信号反射，导致误码率上升，PCB 走线和连接器设计必须严格控制。

## 与 CAN FD 的横向对比

| 特性 | 10BASE-T1S | CAN FD |
|------|-----------|--------|
| 速率 | 10 Mbps | 最高 8 Mbps |
| 节点数 | 最多 255（PLCA） | 最多 64 |
| 总线长度 | 25m | 40m（1Mbps），5m（8Mbps） |
| IP 协议 | 原生支持 | 需适配（AUTOSAR） |
| PoDL 供电 | 支持 | 不支持 |
| gPTP 时间同步 | 支持（±10ns） | 不支持（需 CANFD+时间同步扩展） |
| 汽车成熟度 | 新兴 | 成熟 |
| 芯片成本 | 较高 | 较低 |

## 物理层信号特性

- **差分信号**：正负两根导线，抗共模干扰
- **特征阻抗**：100Ω（单端 50Ω）
- **信号幅度**：差分电压约 ±1V
- **最高频率分量**：约 5MHz（10Mbps/2，奈奎斯特）
- **EMI 屏蔽要求**：非屏蔽双绞线（UTP）通常满足汽车 EMC，特殊场景可用 STP

## 关联概念

- [[concepts/mculess-architecture]] — 10BASE-T1S 是 MCU-less 架构的物理层基础
- [[sources/10baset1s-deep-dive-automotive-architecture-revolution]] — Microchip LAN866x 在此物理层上的应用
- [[sources/podl-automotive-ethernet-power-delivery]] — PoDL 供电叠加在 10BASE-T1S 之上
- [[sources/rcp-protocol-mculess-hardware-control-deep-dive]] — RCP 协议运行在 10BASE-T1S 之上
- [[sources/automotive-ethernet-evolution-10baset1s-to-1gbase]] — TI 完整以太网产品线
