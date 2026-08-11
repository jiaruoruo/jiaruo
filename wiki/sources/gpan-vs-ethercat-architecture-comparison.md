---
type: source
title: "GPAN vs EtherCAT 全维度架构对比"
date: 2026-06-01
source_url: ""
domain: "goodix"
author: "汇顶科技"
tags: []
processed: true
raw_file: raw/工作/articles/MCULess/GPAN-ETHCAT对比架构图.html
raw_sha256: f2d5891ae5b07b9dc13c2bad1f826802f18eefaeda974776334b2c3a883885ab
last_verified: 2026-07-14
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# GPAN vs EtherCAT 全维度架构对比

## Summary

从十大技术维度和成本维度全面对比 GPAN 与 EtherCAT。技术维度：带宽利用率(GPAN≥80% vs EC~40%)、控制周期(GP≥20µs vs EC≥100µs)、转发时延(GP固定1.4µs vs EC 0.5-5µs)、同步性能(GP 40ns ps级 vs EC 27.2ns有抖动)、错误重传(GP硬件子报文 vs EC软件全帧)、子节点互传(GP直接 vs EC主站中转)、远程外设控制(GP CAN/LIN/SPI/I2C/UART/PWM/ADC vs EC仅GPIO)、睡眠唤醒(GP支持 vs EC不支持)、软件复杂度(GP 3层 vs EC 4层)、主站设计(GP CPU解耦 vs EC需加速卡)。成本维度：GPAN 节省 80-90%+ TCO。

## Key Points

- 带宽利用率：GPAN≥80% vs EtherCAT~40%（持续循环模式 vs RTT 等待模式）
- 控制周期：GPAN≥20µs vs EtherCAT≥100µs，30关节 200M 环网仅需 10.28µs
- 转发时延：GPAN 固定 1.4µs vs EtherCAT 0.5-5µs 波动
- 同步精度：GPAN 40ns ps 级（频率同步+GPAN-1588v2，4节点误差仅 13.8ns）vs EtherCAT 27.2ns 有抖动
- 错误重传：GPAN 硬件子报文级重传 vs EtherCAT 软件整帧丢弃重传
- 子节点互传：GPAN 节点直接互传（如左腿失衡→右腿自动补偿）vs EtherCAT 必须主站中转
- EtherCAT 3年 TCO 约 15-100万+，GPAN 节省 80-90%+（无软件许可/CPU溢价/加速卡/认证费）
- 迁移三阶段：单关节验证→3-5关节子系统→整机替换

## Concepts Extracted

- [[gpan-communication]]
- [[ethercat-realtime-communication]]
- [[mculess-architecture]]
- [[robot-software-architecture]]

## Entities Extracted

- [[goodix-technology]]

## Contradictions

## My Notes
