---
type: source
title: "我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了"
date: 2026-05-23
source_url: "https://mp.weixin.qq.com/s/JFvYo9RCn9Xm8ilx1Chd6g"
domain: "mp.weixin.qq.com"
author: "欢迎关注的"
tags:
  - agent
  - ai-workflow
  - automation
  - autoresearch
processed: true
raw_file: raw/工作/clippings/AI/2026-05-23我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了.md
raw_sha256: bebe164d7ac4f00d11905ee4e8be9b3df98eead97310373b23ee50c7b87da74a
last_verified: 2026-05-23
possibly_outdated: false
language: "zh"
---

# 我把 Karpathy 的 AutoResearch 搬到了软件开发领域，效果炸了

## Summary

作者把 Karpathy 的 AutoResearch 方法迁移到软件开发，构建全自动开发系统。核心思想：以 program.md 为规则核心，通过多 AI Agent 交叉审核、5 维度量化评分、反馈驱动迭代，实现从 GitHub Issue 识别→代码实现→测试验证→审核合并的闭环。实测约 10 分钟自主完成中等复杂 Issue，代码质量达 9.0/10。

## Key Points

- AutoResearch 精髓三点：① 量化目标（val loss 唯一标准）② 自主循环（无需每轮人工）③ 只保留改进（退化即回滚）
- 迁移映射：把「改 train.py→跑实验→val loss 改善才保留」替换为「实现 Issue→跑测试→多维评分达标才合并」
- 三大改进：多 AI Agent 交叉审核、5 维度量化评分、反馈驱动迭代
- 以 program.md 为规则核心（相当于给 Agent 的「研究/开发章程」，见 [[claude-code-workflow]]）
- 实测：10 分钟完成中等 Issue、零人工干预、评分 9.0/10；通用化可应用任意 GitHub 项目

## Concepts Extracted

- [[claude-code-workflow]]
- [[agent-harness]]

## Entities Extracted

<!-- 无 -->

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
