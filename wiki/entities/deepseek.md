---
type: entity
title: "DeepSeek"
date: 2026-04-25
updated: 2026-04-25
tags:
  - llm
  - open-source
  - chinese-ai
  - efficiency
  - moe
entity_type: institution
aliases:
  - "DeepSeek"
  - "deepseek"
  - "DeepSeek AI"
  - "幻方量化"
---

# DeepSeek

## Description

DeepSeek 是幻方量化（High-Flyer）旗下的 AI 研究机构，以开源大语言模型研究著称。DeepSeek 始终坚持"同等能力下的成本下限"技术路线，从 V2 的 MLA（Multi-head Latent Attention）开始，每代模型都在持续压缩 KV cache、激活参数和注意力计算量。2026 年 4 月发布的 DeepSeek-V4 系列（V4-Pro 1.6T 参数、V4-Flash 284B 参数）是这一路线的最新里程碑，实现百万 token 上下文下 KV cache 压缩至 V3.2 的 10%。

## Key Contributions

- **效率优先路线**：不追求能力上限（HLE 排名），而是追求"同等能力下的成本下限"——这是区别于 OpenAI/Google 的核心竞争策略
- **MoE 架构持续演进**：DeepSeekMoE（1 shared + N routed experts），V4 使用 1+384/1+256 专家，每 token 激活 6 个
- **V4 三大架构创新**：①mHC 残差连接（约束到双随机矩阵流形，稳定超深层训练）；②混合注意力（CSA + HCA 交替，1M token 只需 attend 1024 个压缩块）；③Muon 优化器（替代 AdamW）
- **开源承诺**：在 2026 年持续坚持全模型权重开源，反压闭源商业大厂
- **V4-Flash-Max 效率极致**：13B 激活参数打平 GPT-5.2/Gemini-3.0-Pro，是当前效率最高的推理模型之一

## Related Concepts

- [[mixture-of-experts]]

## Sources

- [[sources/deepseek-v4-technical-analysis]]
- [[sources/llm-benchmark-comparison-2026]]

## Evolution Log

- 2026-04-25（1 sources）：实体页初建，来源为 DeepSeek V4 技术分析文章；记录 V4 系列的架构创新与 DeepSeek 一贯的效率优先路线
- 2026-04-27（2 sources）：强化——benchmark 横向对比数据补充 DeepSeek V4 竞争力量化数据：Codeforces 3206（全球第 23 名）、LiveCodeBench 93.5 第一、Apex Shortlist 90.2 第一；同时标注 HLE（37.7）和 SimpleQA（57.9）相对弱项
