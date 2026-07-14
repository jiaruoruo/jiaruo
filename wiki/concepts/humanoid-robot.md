---
type: concept
title: "人形机器人"
date: 2026-04-15
updated: 2026-07-14
tags:
  - humanoid-robot
  - robotics
  - embodied-ai
source_count: 18
confidence: low
domain_volatility: high
last_reviewed: 2026-07-14
aliases:
  - "人形机器人"
  - "Humanoid Robot"
  - "humanoid-robot"
  - "仿人机器人"
---

# 人形机器人（Humanoid Robot）

## Definition

人形机器人（Humanoid Robot）是具有接近人类形态（双足、双臂、头部）的机器人，能够在为人类设计的环境中工作并执行多样化任务。当前主流人形机器人身高173-180cm，重量47-70kg，21-28个关节自由度（DOF），续航1-2小时，集成大脑模型（高层决策）和小脑模型（运动控制）的分层架构。

## Key Points

- **技术架构**：大脑（多模态大模型/具身智能框架，10Hz）+ 小脑（强化学习/MPC，1kHz）+ 混合架构为当前最佳实践
- **主流厂商技术路线**：
  - 宇树 H1（TRL 7）：RL + 准直驱电机 + 开源生态，行走速度3.3m/s
  - 特斯拉 Optimus Gen2（TRL 6）：端到端神经网络 + 数据飞轮 + 11 DOF 灵巧手，57kg
  - 小米 CyberOne（TRL 5-6）：Cybergear 电机（0.29 Nm/g）+ IoT 生态，21 DOF
  - 小鹏 PX5（TRL 4-5）：汽车工程跨界 + 制造优势，约70kg
  - 智元 Agibot（TRL 5-6）：清华学术工程化 + 灵巧操作见长
- **硬件关键指标**（2025年数据）：重量47-70kg，身高173-180cm，DOF 21-28，灵巧手11-24 DOF，续航1-2小时，准直驱力矩密度0.29 Nm/g（最高）
- **市场规模**：2025年约53亿美元，预计2030年380亿美元（IDC）；2023-2025年机器人领域风投增长3倍，2025年达 $407亿/年
- **快速原型方案**：Isaac Gym + Octo + ROS 2 + EtherCAT，约53万元、2.5人团队、12-18周可完成功能原型
- **技术发展阶段**：2000-2010机械本体阶段 → 2015-2020控制算法突破 → 2021-2023 AI 赋能爆发 → 2024-2025产业化加速 → 2026+通用化与规模量产
- **核心挑战**：端到端黑盒安全性、长尾场景泛化、电池续航（1-2小时）、灵巧操作精度（精细任务成功率<70%）
- **BOM 成本现状**（麦肯锡 2026）：典型 BOM $30,000-$150,000/台，目标 <$20,000 为大众市场门槛；执行器占 40-60%，是最大单项成本
- **整机执行器数量**（特斯拉 Optimus Gen 3）：身体约 28 个关节执行器 + 手部 50+ 执行器（手部超过全身其他部分）
- **中国供应链优势**：永磁体加工占全球 90%，不用中国供应商制造 Optimus Gen 2，BOM 从 ~$46,000 飙升至 ~$131,000（约 3 倍）
- **宇树 G1**：公开列表起售价约 $13,500（≈ ¥97,500），中国产业集群成本优势的具体体现

## My Position

## Contradictions

## Sources

- [[sources/embodied-ai-os-whitepaper-2026]]
- [[sources/infineon-gc-humanoid-robot-jun2025]]
- [[sources/infineon-humanoid-robot-feb2026]]
- [[sources/st-smart-industry-robotics-v9]]
- [[sources/renesas-robotic-platform-2025]]
- [[sources/renesas-robot-application-guide-2025]]
- [[sources/robot-sensor-actuator-communication]]
- [[sources/renesas-robot-servo-ethercat-application]]
- [[sources/humanoid-robot-research-rapid-prototyping]]
- [[sources/mckinsey-humanoid-robot-bom-supply-chain]]
- [[sources/global-robotics-roadmap-2025-2035]]
- [[sources/robot-safety-implementation]]
- [[sources/mculess-technology-insight-full-2026-05]]
- [[sources/ethercat-industry-report-2025]]
- [[sources/mcu-less-technology-insight-core]]
- [[sources/mcu-less-application-opportunities]]
- [[sources/mcu-less-auto-robot-insight]]
- [[sources/humanoid-robot-oem-supplier-opportunities]]

## Evolution Log

- 2026-04-15（1 sources）：概念初建，来源为人形机器人技术研究及快速原型建设报告
- 2026-04-15（2 sources）：强化——瑞萨官方文档与现有定义一致；补充芯片级方案视角：RA8T2/RZ/T2L 关节驱动（FOC+EtherCAT），RZ/V2H 作为 AI 控制器实现大脑+小脑架构
- 2026-04-15（3 sources）：强化——传感器沙盘补充状态感知融合需求（状态估计延迟<5ms、频率>500Hz）与现有定义一致
- 2026-04-15（9 sources）：强化——英飞凌/ST/瑞萨多份文档一致印证市场规模、整机结构（44轴/BOM构成）、半导体方案架构，与现有定义高度一致；英飞凌更新中国市场预测至2025年15K台、全球70%份额
- 2026-05-17（10 sources）：强化——麦肯锡 BOM 报告新增供应链视角：执行器占比 40-60%、当前 BOM $30,000-$150,000/台、整机执行器拓扑（Optimus 身体 28 个 + 手部 50+ 个）、宇树 G1 $13,500 定价、供应链规模化困境量化数据
- 2026-07-13（11 sources）：强化——全球机器人路线图补充人形硬件路线图里程碑：双足人形（工厂）2027 试产 10 台→2031 年产万台；双足人形（家庭）2030 辅助生活试用→2035 有限部署；灵巧手 2027 20DoF+触觉→2031 类人灵巧度；区域格局（美软件优先/中规模优先/欧信任优先）
- 2026-07-13（12 sources）：强化——内部机器人安全需求软/硬件实现方案补充安全维度：L1-L4 分层架构、灵巧手防夹(ISO/TS 15066)、整机姿态安全(摔倒/碰撞)、功能安全故障上报，与人形机器人物理交互安全直接相关（详见 [[robot-safety]]）

- 2026-07-14（18 sources）：强化——[MCU-less 技术洞察（详尽版）：机会分析 · 技术方案 · 执行策略] 与现有定义一致
- 2026-07-14（18 sources）：强化——[EtherCAT 行业应用与实现方案调研报告 2025] 与现有定义一致
- 2026-07-14（18 sources）：强化——[MCU-less 技术应用洞察-核心观点解读] 与现有定义一致
- 2026-07-14（18 sources）：强化——[MCU-less 应用机会点汇总] 与现有定义一致
- 2026-07-14（18 sources）：强化——[MCU-less 技术在汽车和机器人领域的应用洞察] 与现有定义一致
- 2026-07-14（18 sources）：强化——[人形机器人 OEM/供应商机会分析] 与现有定义一致