---
type: source
title: "英飞凌为AI服务器提供高效率高功率密度供电方案"
date: 2026-04-20
sha256: "bced59e8a50026d8e06b321c056350a6fc0eca8553ca2afe4cd0f5002cb0bd55"
raw_file: "raw/pdfs/深圳We Power AI --英飞凌为AI服务器提供高效率高功率密度供电方案--卢柱强.pdf"
author: "卢柱强，英飞凌科技"
event: "深圳 We Power AI 2025"
domain:
  - ai-infrastructure
  - power-electronics
  - data-center
  - semiconductors
entities:
  - infineon-technologies
concepts: []
status: processed
---

# 英飞凌为AI服务器提供高效率高功率密度供电方案

## Summary

基于 Si/SiC/GaN 混合方案的 AI 服务器 8kW PSU 设计详解。面向 1MW/机架目标加速的数据中心演进，英飞凌提供覆盖 PFC 前端到 LLC DC-DC 输出的完整高效率供电方案，结合 SiC MOSFET（PFC 级）和 CoolGaN™（LLC 级）实现高功率密度与高效率协同，满足 OCP 等行业规范要求。

## Key Points

- **数据中心功率趋势**：1MW/机架目标加速了 ±400V 直流配电总线的采用
- **±400V HVDC 优势**：减少配电损耗，提高配电效率，支持更高功率密度机架（>100kW/rack）
- **8kW PSU 方案**：基于 Si/SiC（PFC 级）+ GaN（LLC 级）混合架构，输出 50V DC，效率 >97%
- **CoolSiC™ MOSFET**：在 PFC 整流级提供低导通损耗和低开关损耗，支持 Vienna PFC 三相高效整流
- **CoolGaN™ HEMT**：在 LLC 谐振转换级实现 400kHz 高频软开关，大幅缩小变压器和输出滤波器体积
- **XDPE 数字电源管理 IC**：配合英飞凌 PSU 方案提供数字控制、PRM Bus 通信（PMBus/I2C）和电源时序管理
- **OCP 规范支持**：符合 OCP（Open Compute Project）DC-SCM / CRPS 等开放电源规范，支持云服务器厂商认证
- **液冷支持**：采用顶部散热封装设计，支持新型冷板（Cold Plate）液冷 SMPS，适配未来高密度数据中心

## Related Concepts

## Related Entities

- [[entities/infineon-technologies]]
