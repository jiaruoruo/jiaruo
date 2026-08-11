---
type: source
title: "EtherCAT/GPAN 抓包分析"
date: 2026-04-01
source_url: ""
domain: "internal"
author: "技术团队"
tags: []
processed: true
raw_file: raw/工作/articles/机器人/packet_analysis.html
raw_sha256: 57e738369075e6866405a51a36d67f0df60b277b49613873e29d5f46972833b2
last_verified: 2026-07-14
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# EtherCAT/GPAN 抓包分析

## Summary

EtherCAT 和 GPAN 通信协议的抓包分析报告，对比两种协议的帧结构、报文格式和通信时序。

## Key Points

- EtherCAT 帧格式分析（帧头 0x88A4、PDU 类型、从站地址、WKC）
- GPAN 帧格式分析（片段式发送、专用帧/公共帧）
- 两种协议通信时序对比

## Concepts Extracted

- [[ethercat-realtime-communication]]
- [[gpan-communication]]
- [[time-sensitive-networking]]

## Entities Extracted

-

## Contradictions

## My Notes
