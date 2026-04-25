---
type: entity
title: "OpenClaw"
date: 2026-04-15
updated: 2026-04-25
tags:
  - agent-platform
  - runtime
  - robotics
  - open-source
  - harness
  - multi-agent
entity_type: tool
aliases:
  - "OpenClaw"
  - "openclaw"
  - "OpenClaw Agent 平台"
---

# OpenClaw

## Description

面向具身智能和 AI Agent 的控制平面平台，强调 Agent Runtime 能力（任务可执行、可回放、可治理、可持续训练）。核心组件：Gateway/Runtime（会话、事件、工具调用、权限策略、审计日志）、Skills 体系（能力封装与版本管理）、Nodes（仿真/机器人/浏览器等执行节点）。ClawHub 类似"npm for agents"的 Skills 注册与分发中心。

## Key Contributions

- Agent Runtime 架构：将仿真平台、机器人执行节点统一为可调用的 Node，标准化 `sim.reset/step/get_state/render` 接口
- Skills 体系：Perception/Control/Policy/Training Skills 同一套接口在仿真和真机复用，工程化 Sim-to-Real
- 分层控制集成：低频层（0.2-1Hz）负责任务拆解/工具编排/异常处理，配合高频 RL 控制器（10-50Hz）
- 安全治理：权限最小化、审计溯源、私有 registry + 白名单为内置架构层能力

## Related Concepts

- [[robot-simulation-framework]]
- [[embodied-ai]]
- [[sim-to-real-transfer]]
- [[agent-harness]]

## Sources

- [[sources/openclaw-simulation-rl-agent]]
- [[sources/agent-harness-revolution-2026]]
- [[sources/openclaw-ai-team-practice]]
- [[sources/hermes-vs-openclaw-comparison]]
- [[sources/openclaw-vs-hermes-deep-dive]]
- [[sources/agent-route-comparison-2026]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为 OpenClaw × Simulation × RL 文章
- 2026-04-19（4 sources）：强化——OpenClaw 在 Agent Harness 生态中的定位得到多篇实战文章印证；补充横向扩展型/手动纠正式/文件系统协作等新特性
- 2026-04-19（5 sources）：强化——架构师深度对比文章补充：OpenClaw 核心资产是 25+ 渠道 + Gateway 控制面（入口和秩序）；Skill = SOP 库；Memory = 文件路线；安全 = 信任模型 + 配置审计
- 2026-04-25（6 sources）：强化——三条路线比较文章印证 OpenClaw「生态优先」定位；明确其弱点（重、成本失控风险）和最适用场景（快速搭建、需成熟生态托底）
