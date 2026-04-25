---
type: entity
title: "Superagent"
date: 2026-04-25
updated: 2026-04-25
tags:
  - agent
  - security
  - governance
  - enterprise
  - open-source
entity_type: tool
aliases:
  - "Superagent"
  - "superagent"
---

# Superagent

## Description

Superagent 是专注于 AI Agent 安全治理的开源框架，定位不是通用 Agent 助手，而是企业级 Agent 系统的**安全与合规底座**。在 Agent 基础设施三层架构（执行层/学习层/安全层）中，Superagent 占据安全闸门位置，核心能力包括 Guard（输入输出防护）、Redact（敏感数据脱敏）、Scan（数据泄露检测）、Red Team（红队攻击测试），解决企业"Agent做错事怎么办"的核心痛点。

## Key Contributions

- **Guard 防护**：对 Agent 的输入/输出进行实时检测和拦截，防止有害内容通过
- **Redact 脱敏**：自动识别并遮蔽敏感信息，防止数据外泄
- **Scan 检测**：扫描 Agent 工作流中的数据泄露风险
- **Red Team 测试**：提供攻击性测试框架，在上线前发现安全漏洞
- **企业合规支撑**：为 Agent 系统提供审计留证能力，满足安全审查和合规要求

## Related Concepts

- [[agent-security-governance]]
- [[agent-harness]]

## Sources

- [[sources/agent-route-comparison-2026]]

## Evolution Log

- 2026-04-25（1 sources）：实体页初建，来源为 OpenClaw/Hermes/Superagent 三条路线比较文章；定位为 Agent 安全治理层代表性框架
