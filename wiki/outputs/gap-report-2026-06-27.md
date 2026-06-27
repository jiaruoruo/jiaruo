---
type: gap-report
date: 2026-06-27
graph-excluded: true
---

# Gap Report — 2026-06-27

_REFLECT Stage 3 知识空白分析。配套 synthesis：`wiki/synthesis/mculess-eea-architecture-synthesis.md`。_

## 一、隐性盲区（多来源提及 × 无独立页）— P0 优先

| 主题 | 提及来源数 | 概念页 | 优先级 | 说明 |
|---|---|---|---|---|
| **功能安全 / ISO 26262 / ASIL** | 23 | ✅ 已建（2026-06-27） | ~~P0~~ 已解决 | 已新建 [[concepts/functional-safety]]（8 源，medium）：ASIL 分级、Limp-Home 降级、MCULess 域边界（ASIL-D 禁用）、安全 MCU 积累。 |
| **GaN 功率器件 / 氮化镓** | 11 | ✅ 已建（2026-06-27） | ~~P0~~ 已解决 | 已新建 [[concepts/gan-power-devices]]（8 源，medium）：材料优势、GaN/Si/SiC 分工、机器人电机驱动与 AI 数据中心、300mm 产业化拐点。 |
| **SmartFET / 智能高边开关** | 多篇 ZCU 来源 | ❌ 无 | P1 | ZCU 六大趋势之一，与 MCULess 边缘驱动芯片直接相关。 |

## 二、孤立概念（source_count=1 且创建 >30 天）— P1

以下概念长期单来源，未被新摄入强化，存在定义偏狭或过时风险：

- **被低估的核心概念**（重要性 >> 来源数，应优先补源）：
  - `eea-architecture`（source_count=1）：是整个汽车簇的顶层框架，却仅 1 源支撑，与 mculess(27)/gpan(23)/zonal-gateway(3) 严重不匹配。建议从既有 MCULess/ZCU 来源回填多源。
  - `can-eth-protocol-conversion`、`time-sensitive-networking`：汽车骨干网关键技术，均仅 1 源。
- **AI/多模态簇孤儿**（2026-04-13 批，至今未强化）：`model-context-protocol`、`multimodal-api`、`text-to-speech`、`video-generation`、`voice-cloning`——成簇出现但彼此无链接、无综合，疑似一次性摄入后搁置。
- **其他**：`reinforcement-learning-locomotion`、`robot-software-architecture`、`llm-knowledge-management`、`llm-benchmark-evaluation`、`tensor-mathematics`、`agent-security-governance`、`autosar-configuration-toolchain`、`claude-code-workflow`、`automotive-sensor`、`humanoid-robot-supply-chain`。

> 注：2026-06-27 新建的 12 个芯片概念（advanced-packaging/autonomous-driving/eda-tools/flexible-electronics/lidar/low-power-design/memory-design/mems/mmwave-radar/power-management-ic/rf-chip-design/sensor-design/soc-design/wire-bonding）创建未满 30 天，暂不计入孤儿，但多为单源，需后续摄入强化。

## 三、覆盖稀薄的主题领域 — P2

- **独立第三方/竞品原始口径缺失**：MCULess 簇高度依赖汇顶（Goodix）视角，缺 ADI/NXP/Onsemi 原厂资料与独立实测，构成系统性回音室风险（见 synthesis Limitations）。
- **集中化的隐性成本未覆盖**：MCULess「降本」核算只算边缘节点，域控制器侧增加的算力/功能安全/OTA 成本无来源量化。
- **AI/多模态簇**：仅有零散 API 介绍，缺模型能力对比、落地案例与综合。

## 四、矛盾对（已显式记录，持续跟踪）

- MCULess OTA「简化」vs 域控复杂度上升（见 [[concepts/mculess-architecture]] Contradictions）。
- GPAN 私有技术领先 vs RCP 标准化生态优势（见 synthesis E4/C4）。

## 建议下一步动作（按优先级）

1. **新建 `functional-safety` 概念页**（P0，从已有 23 源回填，立即提升三大簇连通性）。
2. **新建 `gan-power-devices` 概念页**（P0，从英飞凌 11 源回填）。
3. **回填 `eea-architecture` 多来源**（P1，消除「顶层框架单源」失衡）。
4. 处理 AI/多模态孤儿簇：择机 REFLECT 或合并，避免长期搁置。
