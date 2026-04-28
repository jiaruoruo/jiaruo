---
type: concept
title: "大语言模型基准测试评估"
date: 2026-04-27
updated: 2026-04-27
last_reviewed: 2026-04-27
tags:
  - LLM
  - benchmark
  - 模型评测
  - evaluation
domain_volatility: high
source_count: 1
confidence: low
aliases:
  - "大语言模型基准测试评估"
  - "LLM Benchmark Evaluation"
  - "LLM 评测"
  - "模型基准测试"
  - "llm-benchmark-evaluation"
---

# 大语言模型基准测试评估（LLM Benchmark Evaluation）

## Definition

大语言模型基准测试评估是指通过一系列标准化任务和测试集，对不同大语言模型的各项能力进行量化比较的系统方法。评测通常按能力维度分类（如知识推理、数学、代码、长文本、工具使用等），使用统一的评分指标（Pass@1、EM、Acc、Elo 等）实现跨模型横向对比，是研究社区判断模型能力进步和选型的主要依据。

## Key Points

- **三大能力维度**：当前主流评测框架通常涵盖知识与推理（Knowledge & Reasoning）、长文本处理（Long Context）、智能体工具使用（Agentic）三大类
- **主流知识推理基准**：
  - **MMLU-Pro**：12 门学科约 12,000 道题，EM 精确匹配率
  - **SimpleQA / Chinese-SimpleQA**：事实性问答，专测幻觉抑制能力
  - **GPQA Diamond**：博士级专家出题的超难科学问题
  - **HLE（Humanity's Last Exam）**：全球顶尖学者设计的人类最难考试，全部旗舰模型得分均低于 50%
  - **LiveCodeBench / Codeforces**：动态更新的代码竞赛基准，防止数据污染
  - **HMMT / IMOAnswerBench**：哈佛-MIT 数学竞赛 / 国际数学奥林匹克答案验证
  - **Apex / Apex Shortlist**：Anthropic 设计的多步骤逻辑推理基准
- **主流长文本基准**：
  - **MRCR 1M (MMR)**：100 万 Token 超长上下文多轮检索
  - **CorpusQA 1M (ACC)**：企业级 RAG 场景问答准确率
- **主流智能体基准**：
  - **SWE Verified / SWE Pro / SWE Multilingual**：真实 GitHub Issues 自动 bug 修复率
  - **Terminal Bench 2.0**：真实终端命令行操作准确率
  - **BrowseComp**：网页浏览多跳推理
  - **GDPval-AA (Elo)**：人类偏好对话质量 Elo 积分
  - **MCPAtlas Public**：MCP 协议工具使用能力
  - **Toolathlon**：连续多轮工具链规划能力
- **常见评分指标**：Pass@1（单次通过率）、EM（精确匹配）、ACC（准确率）、MMR（平均匹配率）、Elo（动态积分）、Resolved Rate（任务解决率）

## 2026 年 4 月旗舰模型横向快照

| 能力维度 | 当前领先模型 | 备注 |
|---|---|---|
| 知识推理综合 | Gemini 3.1-Pro | 多项知识类测试摘冠 |
| 事实幻觉抑制 | Gemini 3.1-Pro | SimpleQA 75.6，领先 18+ 分 |
| 竞赛数学 | GPT-5.4 | HMMT 97.7，IMO 91.4 |
| 代码竞赛 | DeepSeek V4-Pro | Codeforces 3206，全球第 23 名 |
| 超长文本（1M Token） | Claude Opus 4.6 | MRCR 92.9，CorpusQA 71.7 |
| 软件工程（专业版） | Kimi K2.6 / GLM-5.1 | SWE Pro 58.6 / 58.4，反超西方模型 |
| 人类偏好对话 | GPT-5.4 | GDPval-AA Elo 1674 |
| 工具链规划 | GPT-5.4 | Toolathlon 54.6 |
| MCP 工具协议 | Claude Opus 4.6 | MCPAtlas 73.8 |

## Contradictions

<!-- 暂无 -->

## Sources

- [[sources/llm-benchmark-comparison-2026]]

## Evolution Log

- 2026-04-27（1 sources）：概念页初建，来源为 2026 年 4 月顶级模型 benchmark 横向对比内部整理文章
