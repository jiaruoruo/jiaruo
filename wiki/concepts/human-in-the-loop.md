---
type: concept
title: "人在回路"
date: 2026-07-13
updated: 2026-07-13
tags:
  - agent
  - safety
  - human-in-the-loop
  - risk-control
  - governance
source_count: 1
confidence: low
domain_volatility: medium
last_reviewed: 2026-07-13
aliases:
  - "人在回路"
  - "Human-in-the-Loop"
  - "HITL"
  - "人类确认门控"
  - "Human Gate"
---

# 人在回路（Human-in-the-Loop）

## Definition

人在回路（HITL）是 Agent 系统中对高风险操作引入人类确认的安全机制。在 Agent 6 层架构的执行层中，Human Gate 按风险等级决定是否需人类确认后再执行。

## Key Points

- **风险分级**（Knock 2026 提案）：read=0（自动）/ create=1（自动）/ modify=2（日志记录）/ delete=3（需确认）/ financial=4（强制确认）/ irreversible=5（双重确认）
- **门控逻辑**：should_confirm 判断风险等级 ≥3 则需确认；request_confirmation 通知人类并设超时（如 5 分钟）
- **与 [[agent-security-governance|Agent 安全治理]] 的关系**：HITL 是安全治理层在生产中的具体落地机制之一（权限收口/Ask 动作）；治理层侧重 Guard/Redact/Scan/Red Team 四模块，HITL 侧重执行时的风险门控
- **渐进自治原则**：从「人类审批所有操作」逐步过渡到「只审批高风险操作」

## My Position

- 本概念从"执行层风险门控"视角切入，与 [[agent-security-governance|Agent 安全治理]]（企业级安全基础设施）、[[agent-harness|Agent Harness]] 的 Guardrails 组件（Allow/Deny/Ask）共同构成 Agent 安全主题。

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/agent-six-layer-architecture]]

## Evolution Log

- 2026-07-13（1 sources）：概念初建，来源为 Knock「Agent 6 层架构」文章执行层安全机制章节
