---
type: source
title: "嵌入式系统如何支撑具身智能？"
date: 2026-06-07
source_url: "https://mp.weixin.qq.com/s/QPywqTq1UmkV1ymyC6nBhA"
domain: "mp.weixin.qq.com"
author: "做个无知者"
tags:
  - embodied-ai
  - embedded-system
  - real-time
  - functional-safety
processed: true
raw_file: raw/工作/clippings/机器人/2026-06-07嵌入式系统如何支撑具身智能？.md
raw_sha256: 1423ea27fb42909aa5eeb37df377f816c6ef278505241cc67aa480ccfbf812ed
last_verified: 2026-06-07
possibly_outdated: false
language: "zh"
---

# 嵌入式系统如何支撑具身智能？

## Summary

从嵌入式工程视角论述具身智能的物理闭环本质。核心论点：具身智能是一套闭环系统而非单一 AI 模型——模型负责理解/规划/策略，嵌入式系统负责把能力落到传感、计算、控制、执行与安全边界。很多具身智能原型失败不是模型不可用，而是工程闭环太脆（时间戳不统一、传感漂移、控制线程被推理抢占、缺降级与回滚）。

## Key Points

- 核心论点：嵌入式系统不是底层配角，而是整个系统的硬约束来源，要兜住感知/推理/控制/执行/安全/运维六件事
- 感知闭环：传感器抽象从「读数值」升级为「读带状态的数据」（时间戳+质量分+校准版本+异常标志）
- 实时控制：AI 给目标，嵌入式系统保证确定性周期执行；硬实时控制/安全停机/功耗保护必须由嵌入式可靠承接
- 可靠落地：可控失效比单次智能表现更重要——安全监控应独立于高层智能模块
- 需补齐能力：统一时间基准、确定性调度、异常诊断与降级、OTA 与回滚（见 [[embedded-system]]）

## Concepts Extracted

- [[embodied-ai]]
- [[embedded-system]]
- [[functional-safety]]

## Entities Extracted

<!-- 无 -->

## Contradictions

<!-- 暂未发现与其他来源的分歧 -->

## My Notes

<!-- 个人批注、延伸思考 -->
