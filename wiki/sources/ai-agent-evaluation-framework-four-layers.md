---
type: source
title: "AI Agent评测体系：四层质量评估框架"
date: 2026-07-14
source_url: "https://mp.weixin.qq.com/s/2aYxkiWa89pr9lcSwgKbpw"
domain: agent
author: 杨孟莉
tags:
  - agent
  - evaluation
  - quality-assurance
processed: false
raw_file: raw/工作/clippings/AI/2026-07-14-AI Agent评测体系：四层质量评估框架.md
raw_sha256: 72fde0ff5cee109e9a3291773cb4d40f362c3b45e6f848755faf3541bb7e975e
last_verified: 2026-07-21
possibly_outdated: false
language: zh
canonical_source: ""
---

# AI Agent评测体系：四层质量评估框架

## Summary

提出企业级 AI Agent 的系统化评测框架，将 Agent 评测从"单点能力评价"升级为"全流程质量评价"。框架分为四层：评测维度、评测指标、评测标准、评测方法。

## Key Points

- **Agent 执行链路**：理解意图 → 制定计划 → 选择工具 → 调用数据 → 分析结果 → 验证可靠性 → 输出交付
- **四层质量评估框架**：
  1. **评测维度**（评价 Agent 具备哪些能力）：意图理解、任务规划、Skill/工具调用、数据分析、输出质量、稳定性与可靠性、安全合规、用户体验、可观测与调试
  2. **评测指标**（具体测什么）：每维度拆解为可量化指标，如意图识别准确率、任务拆解正确率、Skill 选择准确率
  3. **评测标准**（达到多少算通过）：定义质量门槛（意图识别≥95%、内容准确≥90%、响应≤5s 等），按优秀/良好/合格/不合格分级
  4. **评测方法**（如何自动评测）：自动化测试、规则校验、LLM-as-a-Judge 评分、人工评审、用户反馈与线上监控
- **核心理念**：Agent 评测的核心不是评价"会不会回答"，而是评价"能不能完成任务"
- **持续改进闭环**：测试 → 发现问题 → 分析原因 → 优化 Agent → 再测试

## Concepts Extracted

- [[agent-architecture]]
- [[agent-harness]]

## Entities Extracted

<!-- 无新实体 -->

## Contradictions

<!-- 无 -->

## My Notes

<!-- 与 LangChain 的 Harness Engineering 评测方法论一致——都用评测集驱动优化，但本文更偏企业级质量标准体系，LangChain 更偏工程调优流程。 -->
