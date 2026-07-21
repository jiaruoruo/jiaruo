---
type: entity
entity_type: tool
title: "Automotive Claude Code Agents"
aliases:
  - automotive-claude-code-agents
  - Automotive Agents
date: 2026-05-14
updated: 2026-05-14
tags:
  - automotive-software
  - claude-code
  - agent-orchestration
  - iso26262
  - autosar
  - functional-safety
  - agent
  - automotive-eea
---

# Automotive Claude Code Agents

## Overview

**Automotive Claude Code Agents** 是一个专为汽车软件工程领域设计的 Claude Code Agent 工具包，将汽车行业标准（ISO 26262、AUTOSAR、MISRA C 等）与 AI 辅助编程能力深度融合。

| 属性 | 值 |
|------|-----|
| 版本 | v1.0.0 |
| GitHub | https://github.com/sydyg/automotive-claude-code-agents |
| 作者 | 刘万龙（增强者：Yuxin Zhang / 吉林大学 / 卓宇科技 / DRIVEResearch） |
| 类型 | 垂直领域 Claude Code Agent 工具包 |
| 状态 | 正式发布（v1.0.0） |

## 覆盖规模

| 资产类型 | 数量 | 说明 |
|----------|------|------|
| Agents | 40+ | 覆盖 27 个汽车专业领域 |
| Commands | 200+ | 40+ 命令目录 |
| Skills | 75+ | 专业技能知识单元 |
| Knowledge Base | 507+ | 汽车参考文档 |
| Rules | 37+ | 编码/安全/流程规则 |
| Orchestration Patterns | 41 | 多智能体协作模式 |

## 支持的行业标准

- **功能安全**：ISO 26262（ASIL 分级、安全目标分解）
- **网络安全**：ISO 21434 / UN R155/R156
- **软件架构**：AUTOSAR Classic / Adaptive
- **编码规范**：MISRA C/C++
- **过程评估**：ASPICE
- **诊断通信**：ISO 14229（UDS）
- **总线通信**：ISO 11898（CAN）
- **预期功能安全**：SOTIF (ISO 21448)
- **中国国标**：GB/T 标准（L2/L3 自动驾驶 / CATARC 法规）

## 核心特色

- **LLM Council**：多模型协作框架，按任务路由不同 LLM（Claude / GPT / Gemini）
- **Hooks 安全拦截**：代码生成时自动检查 MISRA 违规、ASIL 分配
- **41 编排模式**：串行流水线 / 并行任务分解 / 反馈循环
- **HIL/SIL 测试集成**：生成测试脚本，支持台架集成

## 相关来源

- [[sources/automotive-agents-tutorial]]（应用教程 + 架构图）
- [[sources/automotive-agents-reference]]（详细说明书）

## 相关概念

- [[concepts/agent-harness]]
- [[concepts/autosar-complex-driver]]
- [[concepts/claude-code-workflow]]

## 相关实体

- [[entities/ecc-framework]]（父框架，Automotive Agents 是 ECC 的垂直领域衍生）
- [[entities/claude-code]]（宿主工具）

## Evolution Log

- 2026-05-14 个人写作 [[sources/automotive-agents-tutorial]] 建立实体页，确认为作者汽车软件 AI 工程化工具
- 2026-07-21（? sources）：REFLECT 补齐主域标签：agent、automotive-eea
