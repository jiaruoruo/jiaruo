---
type: gap-report
title: "知识库 Gap Analysis（2026-07-21 REFLECT）"
date: 2026-07-21
tags:
  - automotive-eea
  - chip
  - agent
  - embodied-ai
graph-excluded: true
---

# 知识库 Gap Analysis（2026-07-21 REFLECT）

> 产出自 REFLECT 流程 Stage 3。配套综合页：[[synthesis/mculess-eea-architecture-synthesis]]。
> 统计基线：sources=233 / concepts=74 / entities=31 / synthesis=9（本轮 REFLECT 未新增 synthesis 文件；既有 `mculess-eea-architecture-synthesis.md` 补 `automotive-eea` 标签并增补 12 源）。

## 产能平衡信号

- **Sources / Synthesis = 233 / 9 ≈ 25.9**，低于 30 阈值，综合覆盖未严重滞后。
- **孤立概念积压**：source_count=1 且创建 >30 天者 **11 个**（见 Gap 1），低于 10 个的告警线，但已接近。
- **隐性盲区信号**：扫描曾误报 1 处「盲点」，经核查为误报（见 Gap 3），真实盲区不显著。
- **结论**：知识库整体「广而不过浅」，但存在**局部稀薄 hub**（被大量引用却仅 1 个专属来源）与**陈旧孤立概念**两类结构性缺口，应作为后续 INGEST 优先队列。

## Gap 1：孤立概念（source_count=1 且创建 >30 天，共 11 个）

| 概念 | 创建天数 | confidence | volatility | 备注 |
|---|---|---|---|---|
| multimodal-api | 99d | low | high | 多媒体 API，长期单源 |
| text-to-speech | 99d | low | high | 语音合成，长期单源 |
| video-generation | 99d | low | high | 视频生成，长期单源 |
| voice-cloning | 99d | low | high | 声音克隆，长期单源 |
| reinforcement-learning-locomotion | 97d | low | high | 强化学习运动控制 |
| agent-security-governance | 87d | low | high | Agent 安全治理 |
| llm-knowledge-management | 87d | medium | medium | LLM 知识管理 |
| tensor-mathematics | 84d | high | low | 张量数学（高置信但单源）|
| autosar-configuration-toolchain | 68d | low | medium | AUTOSAR 配置工具链 |
| claude-code-workflow | 68d | low | high | Claude Code 工作流 |
| automotive-sensor | 65d | medium | medium | 车载传感器 |

> 建议：优先为 `reinforcement-learning-locomotion`、`claude-code-workflow`、`automotive-sensor`、`agent-security-governance` 补充来源（它们同时是高频被引 hub，见 Gap 2）。

## Gap 2：覆盖稀薄 hub（被多来源引用但 concept.source_count=1，共 9 个）

这些概念处于引用网络中心（被许多 source 页提及/链接），却只有 1 个专属摄入来源——概念页「被引用很多、自有内容很少」。应作为 INGEST 优先队列：回溯那些引用它们但未将其列为「Concepts Extracted」的来源，补建关联。

| 概念 | 被引用次数 | 当前 source_count | 建议 |
|---|---|---|---|
| autonomous-driving | 35 | 1 | 高优先：核心域，需补智驾架构/感知来源 |
| vision-language-action-model | 25 | 1 | 高优先：VLA 是具身智能主线 |
| reinforcement-learning-locomotion | 24 | 1 | 高优先：与 Gap1 重叠 |
| claude-code-workflow | 16 | 1 | 高优先：Agent 主题核心实践 |
| automotive-sensor | 13 | 1 | 中优先：车载传感簇 |
| lidar | 10 | 1 | 中优先：感知硬件 |
| mmwave-radar | 5 | 1 | 中优先：雷达感知 |
| soc-design | 5 | 1 | 中优先：芯片设计 |
| robot-safety | 4 | 1 | 中优先：机器人物理安全 |

## Gap 3：隐性盲区核查（误报已排除）

- 初步扫描标记 `rcp-protocol-mculess-hardware-control-deep-dive` 为「被引 4 次但无页面」盲点。经核查，该 **source 页实际存在**（`wiki/sources/rcp-protocol-mculess-hardware-control-deep-dive.md`），系扫描脚本仅比对 concept/entity slug、漏算 source slug 所致，**非真实缺口**。
- 当前无确证的其他隐性盲区（无「被 ≥8 次提及却无独立页」的概念/实体）。

## Gap 4：主域标签治理（本轮已修复）

- 扫描发现 **84 个概念/实体/synthesis 缺主域标签**，导致集群导航与统计失效（CLAUDE.md §九 line 474）。
- 本轮 REFLECT 已补齐：automotive-eea 0→22、chip 4→32、agent 8→32、embodied-ai 6→38 个文件含对应主域标签；finance 0 属正常（无金融内容摄入）。
- 修复后各域 synthesis 覆盖：automotive-eea 1（既有 mculess-eea 综合，本轮补 `automotive-eea` 标签）、chip 1、agent 1、embodied-ai 2、edge-ai 1，覆盖较均衡。

## 综合候选（下一轮 REFLECT 可选主题）

1. **芯片设计/制造/封装综合**（`chip-design-manufacturing-flow-synthesis` 已存在但较薄，可深化；半导体制造被引 20 次、先进封装/IC 测试/EDA 簇丰富）。
2. **VLA / 具身智能路线综合**（已有 embodied-ai 2 篇，可合并且强化 VLA 与 MCULess/机器人关节网络的交叉）。
3. **Agent Harness 工程全景**（本轮新摄入 yeasy《Harness》，agent-harness 概念扩至 8 源，可独立综合 Claude Code / OpenClaw / Codex / MiniHarness 生产级 Harness 对比）。

## 行动建议（按优先级）

1. **P0**：补 `autonomous-driving` / `vision-language-action-model` / `reinforcement-learning-locomotion` / `claude-code-workflow` 的专属来源（Gap 2 高优先项）。
2. **P1**：为 Gap 1 中高波动（high）孤立概念（multimodal-api / text-to-speech / video-generation / voice-cloning / agent-security-governance）补充来源或合并。
3. **P2**：视需求深化 Gap 4 列出的综合候选。
