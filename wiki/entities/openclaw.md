---
type: entity
title: "OpenClaw"
date: 2026-04-15
updated: 2026-04-15
tags:
  - agent-platform
  - runtime
  - robotics
  - open-source
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

## Sources

- [[sources/openclaw-simulation-rl-agent]]

## Evolution Log

- 2026-04-15（1 sources）：实体页初建，来源为 OpenClaw × Simulation × RL 文章
