---
type: source
title: "具身智能上周最值得看的十篇论文：人形机器人从运控基座到视频数据"
date: 2026-06-06
source_url: "https://mp.weixin.qq.com/s/zVMQc0ssRfgyFKSG4b66_Q"
domain: "mp.weixin.qq.com"
author: "yuanxq"
tags:
  - embodied-ai
  - humanoid-robot
  - motion-control
  - research-roundup
processed: true
raw_file: raw/工作/clippings/机器人/2026-06-06具身智能上周最值得看的十篇论文：人形机器人从运控基座到视频数据.md
raw_sha256: 64ab1425ffa9612c36805820f7de17ed34e6c5a5db4d68b69f6d46e5dfe4b49d
last_verified: 2026-06-06
possibly_outdated: false
language: "zh"
---

# 具身智能上周最值得看的十篇论文：人形机器人从运控基座到视频数据

## Summary

具身智能周报，精选 10 篇人形机器人论文，主题覆盖运动基座、视频数据、语言控制、移动操作、状态估计与动态导航。核心判断：人形机器人当前缺的往往是「身体这一层能否稳稳接住上层意图」，运控基座（Behavior Foundation Model，见 [[behavior-foundation-model]]）正被推到台前。

## Key Points

- 核心论点：「会走」不够，难的是走得稳、接得上、摔了还能起来——身体接口层是瓶颈
- HoloMotion-1（地平线）：把野外视频重建动作 + MoCap + 自建数据混合训练，做零样本多动作人形运动基座
- Unified Walking/Running/Recovery（港大）：用状态相关 AMP 把行走/跑步/摔倒恢复放进同一宇树 G1 策略，部署时不显式切模式
- Terrain Consistent RL（Caltech）：让参考轨迹与地形几何一致，暴露 SE(2) 速度接口接入标准导航栈
- 产业背景：智元 BFM-2 已推为「运控基座模型」并预告 BFM-3，论文端与产业端同向推进 foundation model 化

## Concepts Extracted

- [[embodied-ai]]
- [[humanoid-robot]]
- [[behavior-foundation-model]]
- [[reinforcement-learning-locomotion]]

## Entities Extracted

<!-- 无 -->

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
