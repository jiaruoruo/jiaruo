---
type: source
title: "麦肯锡拆解人形机器人 BOM：最贵的是执行器，最缺的是供应链"
date: 2026-05-14
source_url: "https://mp.weixin.qq.com/s/i6o53bpMDTp7S_sm99odiw"
canonical_source: "https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins"
domain: "mp.weixin.qq.com"
author: "Ani Kelkar, Christian Jansen, Erik Sparre, Mark Patel, Mikael Robertson（麦肯锡工业实践）"
tags:
  - humanoid-robot
  - supply-chain
  - bom
  - actuator
  - mckinsey
processed: true
raw_file: raw/工作/clippings/机器人/2026-05-20麦肯锡拆解人形机器人 BOM：最贵的是执行器，最缺的是供应链.md
raw_sha256: 33ad064c1d92faad1d99284b18f320ff7fc24dc081164f8a0cd782d52a1da7ea
last_verified: 2026-06-27
possibly_outdated: false
language: "zh"
---

# 麦肯锡拆解人形机器人 BOM：最贵的是执行器，最缺的是供应链

## Summary

麦肯锡工业实践团队系统拆解人形机器人的硬件 BOM 结构与供应链成熟度，提出了"价值集中点与供应商准备度错配"的核心判断。文章量化了五大硬件领域的成本占比，绘制了从低到高的供应瓶颈风险图，分析了中国供应链的结构性优势，并对 OEM 垂直整合向供应商平台生态系统演进的路径提出了战略建议。

## Key Points

- **BOM 五大硬件领域**（合计占整机成本 85-90%）：
  - 执行器：40-60%（最大成本驱动 + 最主要性能差异化因素）
  - 传感与感知：10-20%
  - 计算与控制：10-15%
  - 结构件：5-10%
  - 电池：5-10%
- **当前 BOM 成本**：典型人形机器人约 $30,000-$150,000/台；目标 <$20,000 被广泛视为大众市场门槛
- **不用中国供应商的成本测算**：特斯拉 Optimus Gen 2 使用中国供应商 BOM ~$46,000，若不使用则飙升至 ~$131,000（约 3 倍）
- **供应瓶颈风险分级**：
  - 低风险：BLDC/PMSM 电机、电池电芯、摄像头、LiDAR/雷达（相邻行业规模化）
  - 中等风险：编码器/IMU（需认证适配）、视觉硬件（重新封装）
  - 高风险：谐波/应变波减速器、行星滚柱丝杠、六轴力/力矩传感器、触觉传感器
- **执行器内部成本拆解**：齿轮箱 30-50%、驱动器 15-20%、电机 10-20%、机械部件 10-20%、传感器 5-10%
- **特斯拉 Optimus**：Gen 3 手部 50+ 执行器，身体约 28 个关节执行器；永磁体供应约束已影响 Optimus 生产（Elon Musk 公开声明）
- **宇树 G1**：公开列表起售价约 $13,500
- **中国供应链结构性优势**：永磁体加工占全球 90%、精密轴承 40%、电机 35%、功率电子 30%；工业机器人 2024 年新增装机 29.5 万台（全球 54%）
- **触觉传感器**：无主导架构，高度碎片化，多数方案来自初创公司或研究机构
- **电池动态**：Samsung SDI 在 InterBattery 2026 发布人形机器人专用固态电池，目标 2027H2 量产；LG Energy Solution 确认为 Boston Dynamics Atlas 供应 46 系列圆柱形电芯（2028 年起）
- **供应链分化预判**：中国更早实现硬件规模化与早期成本压缩；美欧通过前沿 AI 成熟度、系统架构、高保障认证部署差异化
- **规模化困境**：低产量阻碍供应商投资专用生产线 → 无成本下降 → 终端用户需求受限（正反馈锁死）
- **五大供应商战略**：早期共同开发、投资安全与认证（SIL/ASIL）、标准化+模块化设计、可规模化制造能力证明、全生命周期收入流

## Concepts Extracted

- [[humanoid-robot]]
- [[dexterous-hand]]
- [[humanoid-robot-supply-chain]]

## Entities Extracted

- [[entities/tesla-optimus]]
- [[entities/unitree-robotics]]
- [[entities/mckinsey]]

## Contradictions

<!-- 与其他来源的分歧，格式：
- 与 [[sources/other-source]] 在「xxx」问题上存在分歧：[具体描述] -->

## My Notes

<!-- 个人批注、延伸思考，主观内容放此处 -->
