---
type: entity
title: "特斯拉 Optimus"
date: 2026-04-15
updated: 2026-07-14
tags:
  - company
  - humanoid-robot
  - end-to-end
  - tesla
  - embodied-ai
entity_type: institution
aliases:
  - "特斯拉 Optimus"
  - "Tesla Optimus"
  - "tesla-optimus"
  - "擎天柱"
  - "Tesla Bot"
---

# 特斯拉 Optimus（Tesla Optimus）

## Description

特斯拉人形机器人项目（又名擎天柱/Tesla Bot），由埃隆·马斯克主导，继承 FSD（全自动驾驶）AI 技术和数据飞轮战略。Gen 2（2024年）：173cm，57kg，28 DOF，11 DOF 灵巧手（含触觉传感器阵列），行走速度约1.5m/s。技术成熟度 TRL 6，已在特斯拉工厂内部小规模试用。Gen 3 手部执行器超过 50 个，超过全身其他关节（28 个）之和。

## Key Contributions

- 端到端神经网络控制：借鉴 FSD 多模态 Transformer，直接从视觉输入映射到电机指令，理论上达到最优感知-控制映射
- 数据飞轮战略：百万级车队数据 + 人类远程操控演示数据，构建闭环迭代（部署→采集→训练→再部署）
- 11 DOF 灵巧手：触觉传感器密集分布于指尖/掌心，支持抓鸡蛋、折衣物、装配零件；Gen 2 手速提升30%；Gen 3 手部 50+ 执行器
- 高度集成驱动单元：电机+编码器+驱动器+传感器一体化设计，减少线缆，借鉴电动车电机设计经验
- **BOM 成本标杆**（麦肯锡 2026）：Gen 2 使用中国供应商 BOM ~$46,000，若不使用中国供应商则飙升至 ~$131,000（约 3 倍），印证中国供应链不可替代性
- **永磁体供应约束**：Elon Musk 公开声明磁体供应约束已影响 Optimus 生产；中国控制全球约 69% 稀土开采 + 90% 磁体加工

## Related Concepts

- [[humanoid-robot]]
- [[embodied-ai]]
- [[dexterous-hand]]
- [[humanoid-robot-supply-chain]]

## Sources

- [[sources/humanoid-robot-research-rapid-prototyping]]
- [[sources/tesla-optimus-dexterous-hand-patents-2026]]
- [[sources/honor-robot-china-suppliers-2026]]
- [[sources/mckinsey-humanoid-robot-bom-supply-chain]]
- [[sources/mculess-technology-insight-full-2026-05]]
- [[sources/mcu-less-auto-robot-insight]]
- [[sources/humanoid-robot-oem-supplier-opportunities]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为人形机器人技术研究及快速原型建设报告
- 2026-05-04（3 sources）：更新——专利来源补充 Gen V3 灵巧手 5 项 PCT 专利（WO 2026/080701 等）25 DoF 执行器全前移/腱绳驱动/柔性复合材料无轴承关节；荣耀机器人报告补充中国供应商生态背景
- 2026-05-17（4 sources）：强化——麦肯锡 BOM 报告新增：Gen 3 手部 50+ 执行器（>全身 28 个关节执行器）、BOM $46,000（中国供应商）vs $131,000（无中国供应商）定量成本对比、永磁体供应约束已影响实际生产的公开声明

- 2026-07-14：强化——新来源 [MCU-less 技术洞察（详尽版）：机会分析 · 技术方案 · 执行策略] 补充描述信息
- 2026-07-14：强化——新来源 [MCU-less 技术在汽车和机器人领域的应用洞察] 补充描述信息
- 2026-07-14：强化——新来源 [人形机器人 OEM/供应商机会分析] 补充描述信息
- 2026-07-21（? sources）：REFLECT 补齐主域标签：embodied-ai
