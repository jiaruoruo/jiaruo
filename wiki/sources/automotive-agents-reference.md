---
type: source
title: "Automotive Claude Code Agents 详细说明书（v1.0.0）"
date: 2026-05-11
source_url: ""
domain: personal
author: "刘万龙"
tags:
  - personal-writing
  - automotive-software
  - claude-code
  - agent-orchestration
  - iso26262
  - autosar
  - functional-safety
processed: true
raw_file: "raw/personal/AUTOMOTIVE_AGENTS_REFERENCE.md"
raw_sha256: "3d680ed34b616b1d9315ff3b51eaff57bb2e5779fb2797ca64f5d76c487caffb"
last_verified: 2026-05-14
possibly_outdated: false
language: "zh"
canonical_source: "https://github.com/sydyg/automotive-claude-code-agents"
personal_writing: true
---

# Automotive Claude Code Agents 详细说明书（v1.0.0）

> ⚠ 个人写作，不参与 source_count 计数。核心立场已写入 [[concepts/agent-harness]] 的 My Position 节。

## Key Points

- **系统架构**：四层结构——Claude Code 用户界面 → 领域 Agents 层 → 工具适配层（Tool Adapter）→ 底层标准知识库
- **资产规模详情**：
  - Agents：40+（覆盖 27 个汽车专业领域）
  - Commands：200+（覆盖 40+ 命令目录）
  - Skills：75+ 专业技能知识单元
  - Knowledge Base：507+ 汽车参考文档
  - Rules：37+ 编码/安全/流程规则
  - Orchestration Patterns：41 多智能体协作模式
- **核心组件设计**：
  - **Agents**：27 个汽车专业领域专属 Agent，每个 Agent 内嵌领域知识和标准约束
  - **Knowledge Base**：507+ 文档，覆盖 ISO 标准原文、OEM 规范、实施指南
  - **Rules**：分层规则（全局安全规则 > 领域规则 > 项目规则）
  - **Hooks**：拦截代码生成，自动注入安全检查（MISRA 违规拦截、ASIL 分配验证）
- **LLM Council 多模型协作框架**：
  - 路由机制：按任务类型分配 LLM（安全分析→Claude，代码生成→较快模型，文档→通用模型）
  - 共识机制：关键决策需多模型表决
  - 冲突处理：定义模型权威层级（领域专家 > 通用 LLM）
- **编排框架（Orchestration）**：41 种模式，包括串行流水线、并行任务分解、反馈循环
- **工具适配层**：支持多种 CI/CD 工具集成（JIRA、GitHub Actions、Jenkins）
- **中国本土化**（Yuxin Zhang 增强）：
  - 机构：吉林大学 / 卓宇科技 / DRIVEResearch
  - 新增 GB/T 标准（GB L2/L3 自动驾驶分级 / CATARC 法规）
  - 支持国产 OEM 工作流

## Concepts Extracted

- [[concepts/agent-harness]]
- [[concepts/autosar-complex-driver]]
- [[concepts/claude-code-workflow]]

## Entities Extracted

- [[entities/automotive-claude-code-agents]]
- [[entities/claude-code]]

## External References

- GitHub: https://github.com/sydyg/automotive-claude-code-agents
- 吉林大学 / 卓宇科技 / DRIVEResearch（Yuxin Zhang 所属机构）

## Contradictions

## My Notes

507+ 知识库文档是这个项目最重要的护城河——它将散布在各标准文档中的汽车领域知识结构化为 AI 可检索的形式。41 个编排模式表明作者对"多 Agent 协作"有系统性思考，而非临时堆砌。
