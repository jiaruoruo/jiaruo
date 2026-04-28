---
title: MCU-less架构在汽车电子中的实现路径深度解析
slug: mculess-eea-implementation-deep-dive
source_url: https://mp.weixin.qq.com/s/RFORh-e07XIsKbvZS8_7dg
author: 汽车电子老登
published: 2026-04-28
ingested: 2026-04-28
sha256: dd1ba0a0
tags: [mculess, 10base-t1s, rcp, onsemi, t30hm1ts3600, automotive]
concepts: [mculess-architecture, eea-architecture, can-eth-protocol-conversion, zonal-gateway]
entities: []
---

# MCU-less架构在汽车电子中的实现路径深度解析

## 核心摘要

以安森美 **T30HM1TS3600** 芯片为主线，深度解析 MCU-less 架构的技术实现。该芯片集成 10BASE-T1S MAC-PHY 与 RCP CORE，可在无本地 MCU 的情况下远程控制 PWM/GPIO/SPI/I2C 等物理接口，是 EEA 从分布式 ECU 向区域化软件定义架构演进的关键使能技术。

## 背景：传统分布式 ECU 的局限

- 每个功能模块配备独立 MCU → 硬件冗余、成本高、TTM 长
- 新增功能必须伴随硬件改动
- 分散接口缺乏集中安全防护，攻击面广

区域架构通过将控制逻辑上移至 ZCU，解决上述问题。onsemi 明确将 10BASE-T1S 定位为实现区域架构的关键拐点技术。

## T30HM1TS3600 芯片架构

### 核心模块

| 模块 | 功能 |
|---|---|
| PHY 物理层 | 连接 LINEP/LINEN 差分线，±6 kV ESD（HBM/IEC61000-4-2），ISO7637 瞬态保护 |
| MAC 媒体访问控制层 | TSSI(PtP) 接口桥接，支持 PLCA 诊断、拓扑发现、gPTP 同步 |
| RCP CORE 核心处理器 | 驱动 SPI/UART/I2C/I2S/PDM/GPIO/PWM/CAP/CMP 等外设 |
| MANAGEMENT 管理模块 | POR/UV/TSD，1.2V LDO，独立 VIO（3.3V 或 2.5V） |
| PIN MUX | 20 个可配置引脚，灵活复用 RCP 或 OA MAC-PHY 功能 |

### 外设接口规格

- **SPI**：主从模式，可配 CPOL/CPHA/CS 延迟/MSB-LSB
- **UART**：可配数据位/停止位/奇偶校验/RX 触发模式
- **I2C**：最高 1 Mbps（标准/快速/快速+），不支持多主
- **I2S/TDM**：音频，可配输入/输出方向、FS 模式、同步频率
- **PDM**：MEMS 麦克风，可配采样率和缓冲区长度
- **GPIO**：10 路，独立方向/上下拉/去抖动
- **PWM**：2 路，可配频率和占空比
- **CAP/CMP**：2 路捕捉输入 + 2 路比较器

## 电源管理

| 电源域 | 电压范围 | 说明 |
|---|---|---|
| VBAT | 2.97–52V | 支持 48V 系统，睡眠模式电源 |
| VCC | 3.3V±10% | 主电源 |
| VDD | 1.2V LDO | 内部稳压输出 |
| VIO | 3.3V 或 2.5V | 数字 I/O 电压参考 |
| INH | 0–52V | 控制外部调节器开关 |
| WAKE | 0–52V | 总线唤醒/本地唤醒 |

支持睡眠模式、总线唤醒、本地唤醒、唤醒转发。

## RCP 协议工作原理

- **客户端-服务器模型**：ZCU 作 RCP 客户端，T30HM1TS3600 作 RCP 服务器
- **序列化**：基于 Protocol Buffers（protobuf），语言/平台中立
- **Directive 消息**：seq（序列号）/ cfg（配置）/ act（动作）/ qry（查询）/ acl（取消动作）/ ven（厂商扩展）
- **Report 消息**：seq / cfg 结果 / act 结果 / qry 结果 / ntf（主动通知）
- **同步通信**：非零 seq 指令必须回复相同 seq 的 Report
- **定时执行**：ptime 字段支持 IEEE 802.1AS PTP 格式绝对时间戳调度
- **周期性动作**：repPeriod + repCount，支持无限循环
- **并发命令**：单个 act 内多命令同时执行
- **错误代码体系**：cfgSuccess/cfgNotSupported/actSuccess/actPending/actTooLate 等

## 可靠性与安全设计

- AEC-Q100 Grade 1，-40°C ~ 125°C
- MDI 引脚 ±6 kV ESD；其他引脚 ±2 kV HBM ESD
- ISO7637 Part3：-150V ~ +100V 瞬态保护
- TSD 热关断，结温上限 150°C；峰值焊接 260°C
- ENI/ENI+：增强噪声免疫，支持约 30 节点/25m
- SQI/SQI+：信号质量指示 + 线束缺陷检测（HDD）
- PLCA 主冗余：协调器缺失时自动切换 CSMA/CD

## 应用场景

- **车门控制**：GPIO/CAP 接锁扣传感器，PWM 驱动车窗电机，SPI/I2C 接后视镜调节
- **照明控制**：自适应前照灯（AFS），PWM 控制远近光比例
- **座椅控制**：PWM 驱动加热/通风，CAP 接位置编码器，EEPROM 存多用户配置
- **热管理**：水泵/风扇/PTC 协调控制，优先级调度，故障降级
- **传感器集线器**：SPI/I2C/PDM 多协议异构传感器网络集成

## 后续演进

T30HM1TS3610（更多 IO，20 个 GPIO）为下一代产品，进一步扩展应用场景。
