---
type: concept
title: "张量数学基础"
date: 2026-04-28
updated: 2026-04-28
tags:
  - mathematics
  - tensor
  - vector
  - scalar
  - ai-fundamentals
source_count: 1
confidence: high
domain_volatility: low
last_reviewed: 2026-04-28
aliases:
  - "张量"
  - "tensor"
  - "tensor-mathematics"
  - "标量向量张量"
  - "Scalar Vector Tensor"
---

# 张量数学基础（Tensor Mathematics）

## Definition

张量（Tensor）是标量和矢量概念的推广，是一种可以用来表示矢量、标量和其他张量之间线性关系的多线性函数。直观上，张量是一个 n 维数值阵列，其维度等级用"阶（rank）"描述。标量、向量、矩阵等都是特殊类型的张量，是深度学习框架（如 TensorFlow、PyTorch）中数据表示的核心抽象。

## Key Points

- **标量（Scalar）= 零阶张量**：
  - 只有大小，没有方向
  - 无论选取何种坐标系，数值恒保持不变
  - 例：质量（5 kg）、温度（37°C）、能量（100 J）
- **向量 / 矢量（Vector）= 一阶张量**：
  - 同时具有大小（magnitude）和方向
  - 可用一维数组表示，如 `[x, y, z]`
  - 例：位移、速度、力、电场强度
- **矩阵（Matrix）= 二阶张量**：
  - 二维数值阵列 `[[a, b], [c, d]]`
  - 常用于线性变换、图像表示
- **高阶张量（Higher-order Tensor）= 三阶及以上**：
  - 三阶张量：如 RGB 图像（宽×高×通道数）
  - 四阶张量：如一批图像（批次×宽×高×通道数）
  - 深度学习中的激活值、权重矩阵等均以高阶张量表示

- **阶（Rank）的定义**：

  | 阶数 | 名称 | 形状示例 | 例子 |
  |---|---|---|---|
  | 0 | 标量 | `()` | 温度、损失值 |
  | 1 | 向量 | `(n,)` | 词嵌入、特征向量 |
  | 2 | 矩阵 | `(m, n)` | 权重矩阵、图像灰度 |
  | 3 | 3D 张量 | `(m, n, p)` | 彩色图像、序列 batch |
  | 4 | 4D 张量 | `(b, h, w, c)` | 图像 mini-batch |
  | N | N 阶张量 | `(d₁, ..., dₙ)` | 任意多维数据 |

- **在 AI / 深度学习中的重要性**：
  - TensorFlow 命名即来自"Tensor"（张量在计算图中的流动）
  - 神经网络的所有参数（权重、偏置）和中间激活值均以张量形式存储和计算
  - GPU 并行计算的高效性本质上是对高维张量进行批量矩阵乘法

## My Position

张量是理解深度学习和 AI 系统的基础数学工具。其核心价值在于统一了标量、向量、矩阵等不同维度数据的抽象表示，使得神经网络的前向传播、反向传播和梯度更新都可以用统一的张量运算框架描述。理解张量阶数与数据维度的对应关系，是读懂 AI 论文中形状标注（如 `[B, T, D]`）的前提。

## Contradictions

暂无

## Sources

- [[sources/scalar-vector-tensor-concepts]]

## Evolution Log

- 2026-04-28（1 source）：概念初建，来源为博客园基础解释文章；覆盖标量/向量/张量定义与阶数层级关系
