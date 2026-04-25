---
type: gap-report
graph-excluded: true
date: 2026-04-25
---

# Knowledge Gap Report — 2026-04-25

> 通过 REFLECT Stage 3 识别，基于对 24 个 concept 页、16 个 entity 页、55 个 source 页的综合扫描。

---

## 类型 A：孤立概念（source_count = 1，潜在知识孤岛）

以下概念只有单一来源支撑，尚未形成交叉印证：

| 概念 slug | 创建日期 | 唯一来源 | 风险 |
|-----------|---------|---------|------|
| `agent-security-governance` | 2026-04-25 | agent-route-comparison-2026 | 仅一篇博文，无学术/工程实践佐证 |
| `llm-knowledge-management` | 2026-04-25 | karpathy-llm-knowledge-management | Karpathy 个人观点，尚无实践验证来源 |
| `robot-software-architecture` | 2026-04-25 | robot-software-architecture-intro | 单一科普文，无工程规范来源 |
| `automotive-ai-chip` | 2026-04-25 | li-auto-mach-m100-deep-dive + li-auto-m100-paper-translation | 两个来源均来自同一公司（理想汽车），视角单一 |

---

## 类型 B：多处提及但无独立页面的隐性盲区

以下概念/实体在多个来源中重复出现，但 **wiki/concepts/ 或 wiki/entities/ 中没有对应页面**：

### B1. `robot-functional-safety`（机器人功能安全）

**出现频率**：5+ 个来源（infineon-complete-solution、infineon-humanoid-robot-feb2026、renesas-robot-servo-ethercat、renesas-rzt2h-n2h-introduction、renesas-robot-application-guide）

**缺失内容**：
- ISO 13849 / IEC 61508 SIL 2/3 与汽车 ISO 26262 ASIL 的对比
- STO（Safe Torque Off）软件实现方法
- 机器人功能安全认证（TÜV / DEKRA）流程
- 国内机器人功能安全监管空白（2027 年欧盟法规生效前的窗口期）

**建议**：优先创建此概念页，source_count 可直接达到 5，confidence 可设为 medium。

---

### B2. `gan-power-devices`（氮化镓功率器件）

**出现频率**：4+ 个来源（infineon-gan-solution-robotics、infineon-psoc-gan-motor-drive、gan-power-devices-tech-applications-outlook、infineon-humanoid-robot-feb2026）

**缺失内容**：
- GaN vs Si MOSFET 物理特性对比（带隙、电子迁移率）
- CoolGaN HEMT 的工作原理与应用边界
- 机器人场景 GaN 的成本降本曲线（缺数据，需注明）
- 主要厂商：英飞凌 CoolGaN、EPC、GaN Systems、TI

**建议**：创建 `gan-power-devices` 概念页，可直接整合现有 4 个来源。

---

### B3. NVIDIA Jetson 系列（实体缺失）

**出现频率**：3+ 个来源提及 Jetson AGX Orin 是"人形机器人主控标准配置"（humanoid-robot-research-rapid-prototyping、embodied-ai-os-whitepaper-2026、robot-software-architecture-intro），但 wiki/entities/ 中无 `nvidia` 或 `nvidia-jetson` 页面。

**建议**：创建 `nvidia-jetson` 实体页，entity_type: product。

---

### B4. `ros2`（机器人操作系统 2）

**出现频率**：5+ 个来源提及 ROS2 作为机器人软件通信中间件（embodied-ai-os-whitepaper-2026、robot-software-architecture-intro、renesas-rzt2h-n2h-introduction、renesas-robot-servo-ethercat-application），但 wiki/concepts/ 中无 `ros2` 概念页。

**建议**：创建 `ros2` 概念页，此概念是机器人软件架构的核心骨干，缺失将导致多个 wikilink 悬空风险。

---

## 类型 C：覆盖稀薄的主题域

### C1. **MoE → Agent 使能关系（未被综合）**

- `mixture-of-experts` 概念（2 个来源）和 `agent-harness` 概念（5 个来源）之间存在**未被显式建立的使能关系**：MoE 架构使得运行大参数量模型的边际成本大幅下降，这正是 Agent Harness 可以在生产环境中长时间运行的技术基础。
- **缺失综合**：没有任何来源或综合页面将"MoE 降本"与"Agent Harness 可行性"建立因果链接。

### C2. **汽车→机器人技术迁移路径（覆盖碎片化）**

- 知识库有大量汽车半导体内容（英飞凌 AURIX、瑞萨 RH850、EEA 架构、GPAN）和大量机器人内容，但**没有一个综合视角**讨论"哪些汽车技术可以直接迁移到机器人，哪些需要重新设计"。
- 已摄入的 2026-04-23-new-business-cocreation-workshop output 文件系统梳理了此问题，但尚未从 wiki/synthesis 层正式提炼。

### C3. **Agent 框架与 LLM 知识管理的交汇（未被综合）**

- `llm-knowledge-management`（Karpathy 方法论）和 `agent-harness`（Harness Memory 层）描述的是同一类问题的不同视角：如何让 AI 系统高效管理长期知识。
- **建议**：两个概念页添加交叉 wikilink，或写综合页。

---

## 类型 D：Synthesis 层完全空白

在本次 REFLECT 之前，`wiki/synthesis/` 目录为空（0 个 synthesis 页）。这意味着：
- 所有跨来源的综合判断只存在于 `wiki/outputs/`（带 graph-excluded）中，无法被 Obsidian 知识图谱关联
- 高价值的竞争分析、架构对比等结论无法被 wiki 内其他页面 wikilink 引用

**本次 REFLECT 已创建 2 个 synthesis 页**：
- [[synthesis/robot-semiconductor-competitive-synthesis]]
- [[synthesis/agent-architecture-landscape-synthesis]]

---

## 优先级推荐（按价值/创建成本比）

| 优先级 | 行动 | 预期价值 |
|--------|------|---------|
| 🔴 P1 | 创建 `robot-functional-safety` 概念页 | 5 个已有来源可直接整合，confidence 可达 medium |
| 🔴 P1 | 创建 `gan-power-devices` 概念页 | 4 个已有来源，是机器人功率器件的核心技术 |
| 🟠 P2 | 创建 `ros2` 概念页 | 补全机器人软件架构的骨干节点，防止断链 |
| 🟠 P2 | 创建 `nvidia-jetson` 实体页 | 修复机器人主控方案中的实体缺失 |
| 🟡 P3 | 在 `mixture-of-experts` 页添加 agent-harness 交叉链接 | 低成本建立隐性关联 |
| 🟡 P3 | 摄入更多 ST/TI/NXP 机器人材料 | 修正现有综合的来源偏差 |
