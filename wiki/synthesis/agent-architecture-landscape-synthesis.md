---
type: synthesis
title: "Agent 框架三条路线：治理、自进化与安全"
date: 2026-04-25
tags:
  - agent-harness
  - openclaw
  - hermes-agent
  - superagent
  - agent-architecture
source_count: 7
confidence: low
---

# Agent 框架三条路线：治理、自进化与安全

## Thesis

2025-2026 年涌现的 Agent 框架在"技能"的语义上发生了根本分歧，由此形成三条技术路线：**OpenClaw**（入口治理导向——skill = 人定义的 SOP 库）、**Hermes**（自我进化导向——skill = 任务成功后的过程记忆）、**Superagent**（安全治理导向——skill 执行前必须经过策略审批）。三条路线并非零和竞争，而是分别解决 Agent 系统不同层次的问题：秩序/入口层、执行/学习层、合规/安全层。

## Evidence

- **OpenClaw skill 语义（SOP库）**：25+ 聊天渠道入口 + `SOUL.md`/`MEMORY.md`/`USER.md` 记忆文件路线，skill 由人定义、分层加载（global → team → agent），强调"人对 Agent 行为的控制权"。来源：[[sources/openclaw-ai-team-practice]]、[[sources/openclaw-vs-hermes-deep-dive]]

- **Hermes skill 语义（过程记忆）**：每次任务成功后 Agent 自动写入 `SKILL.md`，通过 SQLite+FTS5 全文检索+LLM摘要召回，形成"越用越好"的自我迭代知识库。3层 Memory 架构（会话→持久→技能）是其核心差异化。来源：[[sources/hermes-vs-openclaw-comparison]]、[[sources/openclaw-vs-hermes-deep-dive]]

- **OpenClaw vs Hermes 安全对比**：OpenClaw = 信任模型（单一受信 operator，曾暴露 WebSocket Token 漏洞）；Hermes = 纵深防御（Docker/NixOS 容器 + 凭据过滤 + 注入扫描，截至 2026-04-25 无重大漏洞记录）。来源：[[sources/openclaw-vs-hermes-deep-dive]]

- **Superagent 安全治理路线**：在 OpenClaw/Hermes 的执行层之上增加独立的"策略层"，所有 Agent 动作在执行前经过策略引擎审批，专为企业合规场景设计，是 Agent 安全治理的最严格实现。来源：[[sources/agent-route-comparison-2026]]

- **三条路线选型逻辑**：来源明确给出一句话选型建议——缺入口和秩序→OpenClaw；缺经验沉淀和自我改进→Hermes；需要企业合规/审计→Superagent；更完整的系统两者兼备。来源：[[sources/agent-route-comparison-2026]]、[[sources/openclaw-vs-hermes-deep-dive]]

- **Harness 是 Agent 能力的决定性边界**：模型（LLM）能力是上限，Harness 的工程质量决定 Agent 在现实任务中的实际表现——"同一个 GPT-4，配不同 Harness，结果天壤之别"。来源：[[sources/agent-harness-revolution-2026]]

- **迁移路径存在**：`hermes claw migrate` 命令可导入 OpenClaw 的核心记忆文件，说明两条路线在数据层可互通，降低了从 OpenClaw 迁移到 Hermes 的成本。来源：[[sources/openclaw-vs-hermes-deep-dive]]

## Counter-evidence

- **强推理模型可能压缩 Harness 需求**：o1/o3/Claude 3.5 等具备深度内省推理能力的模型，可能在模型内部完成 Harness 负责的部分任务（如任务分解、记忆检索），使得外部 Harness 复杂度自然萎缩。**知识库中无来源讨论"Agent Harness 将被模型能力取代"这一视角。**

  > ⚠ 回音室风险：知识库来源全部来自 Harness 重要性的支持方（OpenClaw/Hermes 社区），缺乏持"模型能力进化使 Harness 趋于简化"立场的来源，结论可能存在确认偏差。

- **自动 skill 沉淀的质量问题**：Hermes 的自动 skill 生成依赖"任务成功"作为正确性信号，但 LLM 对"成功"的判断本身可能有误，存在错误 skill 被持续累积的风险。知识库无来源量化此风险。

- **OpenClaw 入口广度的可维护性**：25+ 聊天渠道适配维护成本极高，任何渠道 API 变更都可能造成连锁故障。知识库中无来源讨论此维护负担。

## Synthesis

三条路线解决的是 Agent 系统不同层次的工程问题，而非同层次竞争：

```
用户/渠道 → [OpenClaw：入口治理层] → [Hermes：执行+学习层]
                                    ↕
                          [Superagent：安全合规层]
```

**实践选型建议（综合来源）**：
- **个人/小团队自动化**：Hermes（自我进化，无需维护 skill 库）
- **企业/多渠道部署**：OpenClaw（入口统一，行为可控）
- **高合规场景（金融/医疗/政务）**：Superagent 或 OpenClaw+Superagent
- **最完整 Agent 系统**：两者同时使用，OpenClaw 管入口，Hermes 管执行

**深层分歧**：OpenClaw 的核心假设是"人应该持续控制 Agent 的行为边界"；Hermes 的核心假设是"Agent 应该持续自我迭代、减少人的干预"。这一价值观分歧在 Agent 系统成熟后将演变为更根本的 Alignment 问题。

## Confidence Notes

⚠ Confidence Notes：此综合基于 7 个来源，置信度为 low。主要风险：来源均来自 2025-2026 年 Agent 社区，视角高度一致（所有来源均认为 Harness 重要），缺乏学术视角和批评性来源。三条路线的"并列非竞争"判断是笔者的解读，来源本身并未明确支持此框架。

## Limitations

1. **Superagent 来源仅 1 个**（agent-route-comparison-2026），所有 Superagent 相关判断均来自单一来源，可信度低。
2. **缺乏量化数据**：无来源提供 OpenClaw/Hermes 的任务完成率、skill 质量、实际用户规模等指标。
3. **时效性风险高**：Agent 框架迭代极快（domain_volatility: high），本综合在 90 天后需要重新验证。
4. **未覆盖企业级 Agent 平台**：Langchain、AutoGen、CrewAI 等主流企业框架未被知识库摄入，视角不完整。

## Sources

- [[sources/agent-harness-revolution-2026]]
- [[sources/openclaw-ai-team-practice]]
- [[sources/hermes-vs-openclaw-comparison]]
- [[sources/openclaw-vs-hermes-deep-dive]]
- [[sources/openclaw-simulation-rl-agent]]
- [[sources/agent-route-comparison-2026]]
- [[sources/ai-collaboration-practices]]
