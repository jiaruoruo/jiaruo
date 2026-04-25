---
type: source
title: "从WiFi无线感知技术到6G展望：AIoT生态系统中的嵌入式系统开发与技术挑战"
date: 2026-04-20
sha256: "aa4cfa7df74f523fc498d09821a7e9bb5c444edf1225c740cffad0f0fc5d58e2"
raw_file: "raw/pdfs/北京主论坛--从WiFi无线感知技术到6G展望：AIoT生态系统中的嵌入式系统开发与技术挑战--佟国香.pdf"
author: "佟国香，英飞凌科技"
event: "北京主论坛 2025"
domain:
  - wireless
  - aiot
  - edge-ai
  - semiconductors
entities:
  - infineon-technologies
concepts: []
status: processed
---

# 从WiFi无线感知技术到6G展望：AIoT生态系统中的嵌入式系统开发与技术挑战

## Summary

覆盖 Wi-Fi 感知技术（WiFi Sensing）、6G 技术展望与 AIoT 生态嵌入式开发挑战的主论坛演讲。Wi-Fi Sensing 利用现有 Wi-Fi 信号的多径传播特性实现无触摸人员检测与环境感知（无需额外传感器）；6G 预计 2030 年商用，将带来 Tbps 级峰值速率、亚毫秒时延和大规模 IoT 连接，进一步拓展 AIoT 边界。

## Key Points

- **Wi-Fi Sensing 原理**：利用 Wi-Fi 信号的 CSI（信道状态信息）变化感知人体运动、存在、手势，无需摄像头或专用传感器
- **Wi-Fi Sensing 应用**：人员存在/计数、跌倒检测、睡眠监测、手势控制；可基于现有 Wi-Fi 基础设施叠加实现
- **英飞凌方案**：AIROC™ Wi-Fi 6/6E（CYW5557x）+ DEEPCRAFT™ 平台支持 Wi-Fi Sensing AI 推理
- **6G 技术展望**：商用目标 2030 年；峰值速率 Tbps 级；时延 <0.1ms；支持海量 IoT 设备（含非地面网络 NTN，卫星 + 无人机）；AI-Native 设计（AI 原生空口）
- **AIoT 嵌入式挑战**：异构计算（MCU + NPU + DSP 协同）；资源受限下的 ML 模型压缩（量化/剪枝）；安全可信执行环境；OTA 固件更新与生命周期管理
- **英飞凌 PSOC™ Edge 方案**：集成 NPU 的低功耗 MCU，支持 TinyML 模型本地推理，配合 AIROC™ 无线实现云边协同
- **标准化与生态**：参与 Wi-Fi Alliance、3GPP、6G 联盟等行业标准组织，推动 AIoT 互操作规范

## Related Concepts

## Related Entities

- [[entities/infineon-technologies]]
