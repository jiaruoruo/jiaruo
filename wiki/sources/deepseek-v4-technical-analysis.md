---
type: source
title: "DeepSeek V4封神了！"
date: 2026-04-25
source_url: "https://mp.weixin.qq.com/s/YFLsNf2QQrIEYF4SwGmcOw"
domain: "mp.weixin.qq.com"
author: "花哥"
tags:
  - deepseek
  - llm
  - moe
  - long-context
  - open-source
processed: true
raw_file: "raw/clippings/2026-04-25DeepSeek V4封神了！.md"
raw_sha256: "9e4f597d1ffeffe1101df82e9a794ca2f284a1c33ea7f7e28cbcfb6d3759edd5"
last_verified: 2026-04-28
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# DeepSeek V4封神了！

## Summary

本文深度解析 DeepSeek-V4 系列（V4-Pro：1.6T 参数/49B 激活，V4-Flash：284B 参数/13B 激活）的技术报告，分析其核心架构创新（mHC 残差连接、混合注意力 CSA+HCA、Muon 优化器、OPD 后训练）及百万 token 上下文的工程实现。DeepSeek 始终追求"同等能力下的成本下限"，V4 将 1M token 上下文的 KV cache 压缩到 V3.2 的 10%，推理 FLOPs 降至 27%。

## Key Points

- **三大架构创新**：①mHC（Manifold-Constrained Hyper-Connections）：把残差流矩阵 B 约束到双随机矩阵流形（Birkhoff polytope），稳定超深层训练；②混合注意力（CSA + HCA 交替）：CSA 温和压缩+稀疏选择（top-k），HCA 大幅压缩+dense；1M token 只需 attend 1024 个压缩块；③Muon 优化器（替代 AdamW）：基于矩阵正交化，Kimi K2 首次大规模验证，DeepSeek 采用 hybrid Newton-Schulz 迭代版本
- **规模参数**：V4-Pro 61层/隐藏维度7168/1+384 MoE experts/每token激活6个；V4-Flash 43层/4096/1+256/激活6个；预训练数据 33T/32T tokens（V3 仅 14.8T）
- **百万上下文实现**：CSA 两层压缩（序列长度 n→n/m→top-k），HCA 压缩率 m'=128；辅助 Sliding Window 分支补偿近距离依赖；Attention Sink 防注意力均摊
- **后训练革新**：用 OPD（On-Policy Distillation）完全替代混合 RL；4 个领域 specialist→OPD 合并到统一 student；三档 reasoning effort mode（Non-think/Think High/Think Max）
- **实验结论**：开源领先（SimpleQA-Verified 57.9 vs K2.6 的 36.9）；匹敌闭源头部代码竞赛（Codeforces 3206 超越 GPT-5.4 的 3168）；但 HLE 仍落后 Gemini-3.1-Pro；落后最前沿闭源约 3-6 个月
- **V4-Flash-Max 被低估**：13B 激活参数，代码数学能打平 GPT-5.2/Gemini-3.0-Pro，是目前效率最极致的推理模型之一
- **DeepSeek 路线一致性**：从 V2 的 MLA 开始，每代都在删 KV cache/激活参数/注意力计算量，V4 是此路线的最新里程碑

## Concepts Extracted

- [[mixture-of-experts]]

## Entities Extracted

- [[entities/deepseek]]

## Contradictions

## My Notes

DeepSeek 的技术路线是"效率第一"而非"能力第一"——这与英伟达/OpenAI 的正面硬刚路线形成鲜明对比。mHC 本质是工程稳定性补丁，Muon 是借用开源社区成果，OPD 是优雅但有工程妥协的后训练方案——这种"诚实的工程主义"风格在大模型领域已经相当稀有。
