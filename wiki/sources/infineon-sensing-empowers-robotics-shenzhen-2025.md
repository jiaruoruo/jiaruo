---
type: source
title: "传感赋能：半导体创新助力机器人智能进化"
date: 2026-04-20
sha256: "9160f813dbe62ddfe37666ed8b34b506daf61327861b56fd7d4684d4add3943d"
raw_file: "raw/pdfs/深圳We Accelerate Robotics--传感赋能：半导体创新助力机器人智能进化--梁国信.pdf"
author: "梁国信（Liang Guoxin），英飞凌科技"
event: "深圳 We Accelerate Robotics 2025"
domain:
  - robotics
  - sensors
  - semiconductors
entities:
  - infineon-technologies
concepts:
  - humanoid-robot
  - dexterous-hand
status: processed
---

# 传感赋能：半导体创新助力机器人智能进化

## Summary

英飞凌 XENSIV™ 传感器系列全面赋能机器人智能感知，覆盖电流、角度、雷达、麦克风、气压、飞行时间六大感知维度。演讲展示多个具体应用案例：60GHz 雷达实现割草机地表识别（>90% 精度）、高 SNR 麦克风提升语音识别词错率约 10%、气压传感器实现室内楼层定位，以及 hToF 模组实现 SLAM 与避障一体化——无需 LDS 激光雷达。

## Key Points

- **电流传感器 TLI4971/TLE4971**：满量程 ±75A（可选 25/50/75/120A），带宽 240kHz/210kHz，传感电阻 220μΩ，集成 1150V 隔离，电感 <1nH
- **角度传感器**：TLE5009(D) 支持最高 30,000 RPM；TLx5012B(D) 精度 1°（全温全寿命）；TLE5014(D) 精度 <1°，支持 ASIL C(D) 功能安全
- **60GHz 雷达 BGT60TR13C**：配合 PSoC6 MCU（150MHz, 1024KB Flash, 288KB RAM），地表材质分类精度 >90%，识别草地/悬崖/障碍物等 8 类，ML 模型运行于 MCU
- **MEMS 麦克风 IM73D122**：SNR 73dB；在 41dBA/5.6m 低声压环境下，相比 65dB SNR 麦克风，OpenAI Whisper 词错率（WER）降低约 10%
- **气压传感器 DPS368**：分辨率 0.002hPa（≈2cm 高度精度），噪声 ~0.4Pa，IPX8 防水（50m/1h），可实现楼层定位无需 Wi-Fi 或视觉
- **hToF 模组 IRS2875C**：尺寸 31×16×8mm，分辨率 240×180（HQVGA），单模组同时支持 SLAM（点光照）和避障（泛光照），可替代 LDS 激光雷达

## Related Concepts

- [[humanoid-robot]]
- [[dexterous-hand]]

## Related Entities

- [[entities/infineon-technologies]]
