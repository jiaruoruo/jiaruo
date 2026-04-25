---
type: source
title: "和 AI 协作的一些实践与思考"
date: 2026-04-19
source_url: ""
domain: personal
author: "刘万龙"
tags:
  - personal-writing
  - ai-collaboration
  - agent-harness
  - feature-spec
  - context-engineering
processed: true
raw_file: "raw/personal/和 AI 协作的一些实践与思考.md"
raw_sha256: "91a4f308c55c45c3d446efdeb5f6f3417030e2d010b9b05b07452d5b64aa6bfe"
last_verified: 2026-04-19
possibly_outdated: false
language: "zh"
canonical_source: ""
personal_writing: true
---

# 和 AI 协作的一些实践与思考

> ⚠ 个人写作，不参与 source_count 计数。核心立场已写入 [[agent-harness]] 的 My Position 节。

## Key Points

- **触发点**：OpenAI Harness Engineering 实验——3 名工程师 + Codex，五个月，100 万行代码，交付速度估计为手写代码的 10 倍；工程师角色转变为「设计环境、定义意图、构建反馈回路」
- **核心洞见**：「从 AI 的视角来看，任何在上下文中无法被访问的信息，就等于不存在。」—— 放进代码库的才算数
- **AI 协作三支柱**：
  - **Workflow（流程）**：正向工作流（README→AI-GUIDE.md）+ Feature Spec（每功能独立 .md，唯一需求来源）+ 禁止清单（与允许清单同等重要）
  - **Long-term Memory（记忆）**：冷启动协议（AI-GUIDE.md + CONTEXT.md，合计 ≤ 200 行）+ Reusable 文档索引（防止重复造轮子）+ 状态由人维护（AI 只读 todo/done）
  - **Cost（成本）**：强弱模型分工——写 Spec/验收/代码审查用强模型，开发/测试执行用弱模型；价格差约 10 倍（Claude Sonnet 4.5 vs MiniMax 2.5）
- **实践成果**：两周，一人，644 个 commit，完整 SaaS（多通知渠道 + 团队权限 + 支付订阅 + 测试覆盖）
- **未解决的问题**：并行 AI 上下文隔离（多 Agent 冲突）、文档过期无银弹、「AI 自测自」验收偏差

## Concepts Extracted

- [[agent-harness]]

## Entities Extracted

- [[minimax]]

## External References

- OpenAI Harness Engineering: https://openai.com/zh-Hans-CN/index/harness-engineering/（未 ingest，作者引用的核心触发来源）

## Contradictions

## My Notes

两周 644 commit 的数据印证了 agent-harness 框架的实际有效性。Feature Spec → 弱模型执行的流水线，本质上是把「Harness 设计」从抽象概念落地为具体工程约定。
