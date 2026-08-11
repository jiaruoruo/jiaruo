---
type: source
title: "EtherCAT IgH 主站搭建方案"
date: 2026-04-01
source_url: ""
domain: "internal"
author: "技术团队"
tags: []
processed: true
raw_file: raw/工作/articles/机器人/ethercat_igh_master_plan.html
raw_sha256: 252e8491c7067d6171b4062534f053909fb70ac1ce2790daf114b2f5bb3d0d10
last_verified: 2026-07-14
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# EtherCAT IgH 主站搭建方案

## Summary

面向 Linux 平台的 IgH EtherCAT Master 部署与开发方案。推荐起步方案：Ubuntu/Debian + Intel 网卡(I210/I211) + IgH Master。覆盖编译安装、配置、验证命令、实时化建议（PREEMPT_RT/SCHED_FIFO/CPU 绑核）和常见问题排查。六阶段实施路径：环境验证→IO 通信→参数访问→周期任务→伺服控制→实时优化。

## Key Points

- 推荐方案：Linux + 专用 Intel 网卡 + IgH EtherCAT Master + 从站
- Native 驱动(Intel I210/I225) 性能最优，Generic 驱动兼容任意 NIC
- 关键验证命令：ethercat master/slaves/pdos/sdos
- 实时化：PREEMPT_RT 内核 + 周期线程绑核 + 关闭 CPU 节能 + SCHED_FIFO 高优先级
- 六阶段路径：环境验证→IO 通信→参数访问→周期任务→伺服控制(CiA402)→实时优化
- EtherCAT 口专口专用，不配置普通 IP

## Concepts Extracted

- [[ethercat-realtime-communication]]
- [[embedded-system]]
- [[robot-software-architecture]]

## Entities Extracted

-

## Contradictions

## My Notes
