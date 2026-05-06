---
type: source
title: "RCP协议深度解析：MCU-less架构下如何实现远程硬件控制"
source_url: "https://mp.weixin.qq.com/s/p87JOK_zLOuvtVnhXPzusQ"
author: "汽车电子老登"
date: "2026-05-05"
tags: [rcp, mculess-architecture, 10baset1s, plca, gptp, automotive-ethernet]
raw_file: "raw/clippings/2026-05-05RCP协议深度解析：MCU-less架构下如何实现远程硬件控制.md"
raw_sha256: b796da158e61eec6783769c12209a56cad3fb2c7c723c8a0fae486fc2c0f3737
last_verified: 2026-05-05
---

## 核心摘要

RCP（Remote Control Protocol）是运行在 10BASE-T1S 以太网之上的应用层协议，采用 UDP/IP + Protocol Buffers 封装，实现区域控制器（ZCU）对 MCU-less 边缘节点硬件 IO 的远程控制，延迟 <1ms。

## RCP 协议帧格式

```
┌──────────────────────────────────────────────────────────┐
│ 4B Header │ 2B CmdType │ 2B NodeAddr │ 1B HWParam │      │
│ (0x524350 │ (0x0001–   │ (0–65535)   │ 1B DataLen │ N B  │
│ ="RCP"+   │ 0x0006)    │             │            │ Data │
│ Version+  │            │             │            │      │
│ Type)     │            │             │            │      │
├──────────────────────────────────────────────────────────┤
│ 2B CRC16-CCITT                                           │
└──────────────────────────────────────────────────────────┘
```

- **帧头**：4 字节，Magic = 0x524350（ASCII "RCP"）+ 版本号 + 帧类型
- **指令类型**：2 字节，0x0001–0x0006（GPIO读/写/配置，SPI/I2C/UART/PWM 等）
- **节点地址**：2 字节，支持最多 65535 个节点地址
- **硬件参数**：1 字节（引脚编号、接口索引等）
- **数据长度**：1 字节
- **数据载荷**：N 字节
- **校验**：CRC16-CCITT

## 实时性保障：PLCA + gPTP

- **PLCA**（Physical Layer Collision Avoidance）：TDMA 轮询调度，消除冲突，总线利用率 >90%
- **gPTP**（IEEE 802.1AS）：全网时间同步精度 **±10ns**
- **端到端延迟**：<1ms（基于 10BASE-T1S），典型值 <150μs

## 主流芯片对比

| 厂商 | 芯片型号 | IO 数量 | 速率 | 状态 |
|------|---------|--------|------|------|
| Onsemi | T30HM1TS3600 | 20 PIN MUX | 10 Mbps | 量产 |
| ADI | AD3301/3304/3305 | 12 IO | 10 Mbps | 量产 |
| Microchip | LAN8660 | 16 IO | 10 Mbps | 样片 |
| 汇顶 GE1101 | GE1101 | 120 IO | 100 Mbps | 2026Q7 样片 |
| ST | 1991dlh32 | — | CAN FD Light 500K–2Mbps | 开发中 |

> **GE1101 关键参数**：120 路 IO，100Mbps 速率，预计 2026Q3 量产，延迟 50μs

## RCP 支持的硬件接口

| 接口类型 | 说明 |
|---------|------|
| GPIO | 数字输入/输出，支持中断上报 |
| SPI | 最高 25MHz，支持 Master/Slave |
| I2C | 100/400 kHz，多从设备 |
| UART | 标准串口通信 |
| PWM | 频率/占空比可编程 |
| I2S | 音频接口 |
| PDM | 数字麦克风接口 |

## TC18 标准化进展

- RCP 协议正在 IEEE TC18 工作组推进标准化
- 目标：形成车规级行业标准，统一各厂商实现
- 当前状态：草案阶段，多家 Tier1/OEM 参与

## 协议栈层次

```
应用层：msgDirective (ZCU→节点) / msgReport (节点→ZCU)
传输层：UDP/IP
网络层：IPv4
数据链路层：MAC (Ethernet II)
物理层：10BASE-T1S (IEEE 802.3cg)
        + PLCA (冲突避免)
        + gPTP (时间同步)
        + TC-10 (低功耗唤醒)
```

## 性能对比

| 指标 | CAN FD | RCP/10BASE-T1S |
|------|--------|----------------|
| 带宽 | 8 Mbps | 10 Mbps |
| 节点数 | 64 | 65535 |
| 延迟 | ~1ms | <150μs |
| 供电（PoDL） | 不支持 | 支持 |
| IP 协议兼容 | 否 | 是 |

## 关联概念

- [[concepts/rcp-remote-control-protocol]] — RCP 协议核心概念
- [[concepts/mculess-architecture]] — RCP 是 MCU-less 的控制通道
- [[sources/podl-automotive-ethernet-power-delivery]] — PoDL 为 RCP 节点供电
