---
type: source
title: "GPAN 芯片规格介绍文档（V0.2）"
date: 2025-08-05
source_url: ""
domain: "goodix"
author: "汇顶科技"
tags: []
processed: true
raw_file: raw/工作/articles/MCULess/GPAN芯片规格介绍文档_V0.2 2025-08-05.docx
raw_sha256: 5080ab7389e3b74d0440335f7be68092f57ee4c3e2bd8c43cf09c5c30a883b48
last_verified: 2026-07-14
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# GPAN 芯片规格介绍文档（V0.2）

## Summary

GPAN 芯片（GE1101）规格介绍文档 V0.2。覆盖物理层通信标准（100Base-T1 全双工 100M）、IO 类型（SPI/QSPI/PWM/I2C/UART/CAN/LIN/ADC/GPIO）、音频接口（I2S/TDM/PDM）、封装（BGA196/BGA144/QFN64/QFN32）、孤岛保护（GPIO 输出电平锁定/看门狗）等芯片级规格。

## Key Points

- 物理层：100Base-T1 全双工 100M，误码率<10⁻¹⁰
- IO 类型丰富：SPIs/QSPIs/PWM In/Out/I2C/UART/xMII/LIN/CAN/CAN-FD/ADC/GPIO
- 音频接口：I2S/TDM/PDM，采样率 12K-192K，精度 16-32bit
- 封装：BGA196(10×10)/BGA144(8×8)/QFN64(9×9)/QFN32(5×5)
- 安全特性：ASIL-B、GPIO 输出电平锁定、内置看门狗、网络异常检测<100µs
- 芯片交付：2026.04 Tapeout → 2026.08 工程样片 → 2027.03 量产

## Concepts Extracted

- [[gpan-communication]]
- [[mculess-architecture]]
- [[automotive-ethernet-10base-t1s]]
- [[can-eth-protocol-conversion]]

## Entities Extracted

- [[goodix-technology]]

## Contradictions

## My Notes
