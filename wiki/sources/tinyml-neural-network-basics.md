---
type: source
title: "玩转边缘AI（TInyML）：需要掌握的神经网络基础知识汇总！"
date: 2026-06-14
source_url: "https://mp.weixin.qq.com/s/mgiKHZVlB4xQ1-LOXKcQoQ"
domain: "mp.weixin.qq.com"
author: "子衡"
tags:
  - edge-ai
  - tinyml
  - neural-network
  - mcu
processed: true
raw_file: "raw/clippings/2026-06-14玩转边缘AI（TInyML）：需要掌握的神经网络基础知识汇总！.md"
raw_sha256: "6a94c1faf034f7b4a4901843a0d840ff8b0d667372a7d4ccde7838db2a7c2daf"
last_verified: 2026-06-14
possibly_outdated: false
language: "zh"
---

# 玩转边缘AI（TInyML）：需要掌握的神经网络基础知识汇总！

## Summary

面向嵌入式工程师的 TinyML 神经网络基础知识汇总（作者贺老师）。核心论点：做嵌入式 AI 不需深奥数学，但必须真正掌握张量/形状、神经元/权重/激活、网络层类型、训练知识（损失/反向传播/过拟合/量化）等基础，否则看不懂模型结构、判断不了模型是否适合 MCU、定位不了部署问题。

## Key Points

- 先搞清输入/输出/张量/shape：模型学的是输入与输出的映射，shape 一错模型即失效
- 神经元三要素：权重、偏置、激活函数（激活决定网络非线性能力）
- 网络层选型需考虑嵌入式部署：全连接易参数膨胀、卷积适合局部特征、池化/展平/归一化各司其职
- 训练知识：损失函数、反向传播、过拟合、评估指标
- 量化是端侧落地关键，需理解量化后精度下降的来源（见 [[edge-ai]]、[[on-device-ai-impossible-triangle]]）

## Concepts Extracted

- [[edge-ai]]

## Entities Extracted

<!-- 无 -->

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
