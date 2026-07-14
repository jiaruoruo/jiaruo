---
type: source
title: "Windows SOEM EtherCAT 主站搭建"
date: 2026-04-01
source_url: ""
domain: "internal"
author: "技术团队"
tags: []
processed: true
raw_file: "raw/articles/Windows SOEM EtherCAT 主站.html"
raw_sha256: "cbc6784d1943be5e25f955f2a24747d71621a706817bbab6a0362273946cf5d1"
last_verified: 2026-07-14
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# Windows SOEM EtherCAT 主站搭建

## Summary

Windows 平台下使用 SOEM（Simple Open EtherCAT Master）搭建 EtherCAT 主站的方案。覆盖 Npcap 网络抓包库配置、SOEM 编译、从站扫描和 PDO 周期收发示例。

## Key Points

- Windows 平台需 Npcap 库支持 Layer 2 原始以太网帧收发
- SOEM 纯用户空间 C 库，静态内存分配，适合嵌入式和快速原型
- SOEM 2.0 重大更新：CMake 迁移、ecx_ API、ENI 解析器、GPLv3+商业双授权

## Concepts Extracted

- [[ethercat-realtime-communication]]
- [[embedded-system]]

## Entities Extracted

-

## Contradictions

## My Notes
