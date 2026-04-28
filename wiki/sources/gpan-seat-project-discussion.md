---
type: source
title: "MCU-Less 座椅项目讨论 V0.5（理想&西威&汇顶）"
date: 2026-04-27
source_type: presentation
source_url: ""
raw_path: "raw/articles/MCU-Less 座椅项目讨论_20260305-V0.5.pptx"
raw_sha256: d2476418
author: "理想汽车 & 西威 & Goodix Technology"
language: zh
tags:
  - gpan
  - mculess
  - automotive
  - seat-controller
  - goodix
  - li-auto
---

# MCU-Less 座椅项目讨论 V0.5（理想&西威&汇顶）

## Summary

三方联合讨论文档（8页，2026-03，V0.5），由理想汽车、西威、汇顶科技共同参与。讨论 GPAN MCULess 方案在理想汽车座椅控制器中的落地拓扑设计、功能需求梳理及软件架构，是 MCULess 方案从 POC 走向量产的关键项目会议记录。

## Key Points

### 网络拓扑方案（4 种候选）

| 方案 | ZCU 主站 PHY | 座椅接入方式 | 优点 | 缺点 |
|---|---|---|---|---|
| A | 通用 PHY | 成环，通过单 GPAN 两端口接 GW（需 4 port） | 兼容性好，ZCU 无需改动 | 不支持分布式音频 |
| B | 通用 PHY | 成环，通过 2 个 GPAN 分别接 GW | 主/备线分离，节点失效可切换；ZCU 失效可接管 | 不支持分布式音频 |
| C | GPAN 专用芯片 | 4 座椅成环接单 ZCU GPAN | 支持分布式音频 | ZCU 资源消耗高；需 GPAN 定制开发 |
| D | GPAN 专用芯片 | 4 座椅分别接 2 个 ZCU GPAN（大环） | 资源均衡，互为备份，功能安全可靠；符合未来趋势 | ZCU 需增加 GPAN 并定制开发 |

**推荐方案 D**：座椅与 ZCU 形成大环，ZCU 互为备份，线路/节点失效可自动切换，最符合功能安全和 SDV 演进趋势。

### 座椅功能需求清单（一/二排）

| 功能类型 | 一排（×2） | 二排（×2） |
|---|---|---|
| 电机 ADC 回采 | 6 路 | ≤6 路 |
| 电机霍尔捕获 | 6 路 | ≤6 路 |
| 加热 | 1 路 | 1 路 |
| 通风 | 2 路 | 2 路 |
| 方向调节 | 12 项 | ≤12 项 |
| 4D 震动 | / | 1 路（预留）|
| 座垫软硬调节 | 通讯（主驾有） | / |
| 按摩 | 通讯 | 通讯 |
| ETH 通道 | ≤3 路 | ≤3 路 |
| CAN | 1 路 | 1 路 |
| LIN | 1 路 | 1 路 |

- 4D 震动功能做预留，需 ZCU 或座舱融合 GPAN 硬件后实现
- 硬件设计最大化，通过空贴适配不同配置

### ZCU 软件架构（5 层）
1. **GPAN 协议栈**：GPAN Protocol SDK 库
2. **RCP 标准接口层**：屏蔽 GPAN/其他 RCP 协议栈细节，提供通用标准接口（实现 MCULess RCP 与具体协议解耦）
3. **座椅设备抽象层**：对 MCULess 座椅边缘节点进行设备抽象（上层功能与 RCP 解耦）
4. **座椅原子服务层**：实现座椅功能的原子服务化
5. **座椅应用层**：实现组合及应用功能

### 待讨论问题（QA）
1. ZCU 主站与座椅节点的网络拓扑形态及 ZCU 主站的 PHY 芯片选择
2. 本期 POC 是否考虑分布式音频及座椅硬件是否提前考虑头枕音频
3. SCU 硬件分工讨论

## Entities Mentioned

- [[entities/goodix-technology]]
- [[entities/li-auto]]

## Concepts

- [[concepts/gpan-communication]]
- [[concepts/mculess-architecture]]
