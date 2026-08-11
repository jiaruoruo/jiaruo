---
type: source
title: "不用改模型，只调Harness！让Agent便宜又好用"
date: 2026-07-14
source_url: "https://mp.weixin.qq.com/s/3YDRaWZ4_qhhNNj66cprhQ"
domain: agent
author: 小北
tags:
  - agent
  - harness
  - context-engineering
  - open-source-models
processed: false
raw_file: raw/工作/clippings/AI/2026-07-14-不用改模型，只调Harness！让Agent便宜又好用.md
raw_sha256: 41c3706ed85fdb998f20ef15f11a4a2b53bae7aeb3ce8a672b5d85ed00e3fcb7
last_verified: 2026-07-21
possibly_outdated: false
language: zh
canonical_source: "https://www.langchain.com/blog/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook"
---

# 不用改模型，只调Harness！让Agent便宜又好用

## Summary

LangChain 分享了 Nemotron 3 Ultra 的 Harness 调优案例：不修改模型权重、不调整生成参数，只优化 Agent 运行环境（提示词、工具描述、中间件、上下文注入时机），使开放模型表现逼近 Opus 4.8，单次成本从 ~43 美元降至 ~4.5 美元（约 1/10）。

## Key Points

- **核心论点**：Agent 能力不只取决于模型，更取决于模型被放进了什么样的 Harness
- **Harness 调优效果**：Nemotron 3 Ultra 得分从 0.80 → 0.84（最佳 0.86），Opus 4.8 最佳 0.87；成本 4.48 美元 vs 43.48 美元
- **调优方法论**：评测 → 观察 trace → 诊断失败模式 → 小步工程改动 → 再次评测（类似 ML 的训练/验证/测试集流程）
- **关键原则**：
  - 一次跑得好 ≠ 真的变好（需要多次重复验证）
  - 不要每次都跑全量评测集（先用小样本筛选）
  - 泛化提示词效果有限，针对性提示更有效
- **Context Engineering 核心案例**：文件读取规则从工具描述移到工具返回结果中，效果立竿见影——"文字没有变，位置变了，行为就变了"
- **Prompt 管"建议"，中间件管"保证"**：确定性行为应��用代码中间件（循环保护、重试、强制终止），而非依赖 Prompt
- **区分真实优化 vs benchmark trick**：能迁移到不同任务/模型/数据的改进才值得保留
- **Harness 的边界**：长程多轮对话中的状态维护等���模型能力范畴，不应无限贴补丁

## Concepts Extracted

- [[agent-harness]]
- [[model-context-protocol]]

## Entities Extracted

- [[langgraph]]
- [[claude-opus-4]]

## Contradictions

<!-- 无 -->

## My Notes

<!-- 这篇文章提供了 Harness Engineering 的可量化方法论。与知识库已有 agent-harness 概念互补——已有概念讲"什么是 Harness"，本文讲"怎么调优 Harness"。 -->
