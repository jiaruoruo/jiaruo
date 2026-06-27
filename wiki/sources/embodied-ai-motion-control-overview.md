---
type: source
title: "具身智能运动控制技术介绍"
date: 2026-06-07
source_url: "https://mp.weixin.qq.com/s/XUYFeBxiucz1eBjDJ2LPUA"
domain: "mp.weixin.qq.com"
author: "去哪儿拿offer"
tags:
  - embodied-ai
  - humanoid-robot
  - motion-control
  - wbc-mpc
processed: true
raw_file: "raw/clippings/2026-06-07具身智能运动控制技术介绍.md"
raw_sha256: "4dc98d1d95019fabcdd0a372806bb5064b2d7e123dada50f3df9c4f1f835b6ac"
last_verified: 2026-06-07
possibly_outdated: false
language: "zh"
---

# 具身智能运动控制技术介绍

## Summary

系统介绍人形机器人具身智能运动控制，定位为连接「大脑认知」与「物理执行」的核心枢纽。采用「大脑-小脑-肢体」三层分层架构，涵盖运动学/动力学、全身控制（WBC）、模型预测控制（MPC）、强化学习与模仿学习、视觉-语言-动作（VLA）模型等核心技术栈。

## Key Points

- 与传统工业机器人「预编程+精确建模」不同，具身智能强调泛化性、自主性、交互性，应对非结构化动态环境
- 三层架构：大脑层（LLM/VLM/VLA 认知决策）→ 小脑层（WBC/MPC/RL 毫秒级运动控制）→ 肢体层（骨架/关节/执行器/传感器）
- 特殊挑战：双足动态平衡、28–55 自由度全身协调、环境适应、人机交互安全（见 [[functional-safety]]）
- 小脑层核心 WBC 把运动与力目标表示为带优先级的优化问题；MPC 做滚动预测；RL 学习鲁棒策略（见 [[reinforcement-learning-locomotion]]）
- VLA 模型代表多模态 AI 与机器人控制深度融合，直接从视觉+语言生成动作指令

## Concepts Extracted

- [[embodied-ai]]
- [[humanoid-robot]]
- [[reinforcement-learning-locomotion]]
- [[functional-safety]]

## Entities Extracted

<!-- 无 -->

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
