---
type: source
title: "Automotive Claude Code Agents 应用教程（v1.0.0）"
date: 2026-05-11
source_url: ""
domain: personal
author: "刘万龙"
tags:
  - personal-writing
  - automotive-software
  - claude-code
  - agent-orchestration
  - iso26262
  - autosar
  - functional-safety
processed: true
raw_file: "raw/personal/AUTOMOTIVE_AGENTS_TUTORIAL.md"
raw_sha256: "820196f108306cd185edc6d9ce45a2dce23f439b0155cdf712cb25f94eb7f4a3"
companion_files:
  - path: "raw/personal/AUTOMOTIVE_AGENTS_ARCHITECTURE.html"
    sha256: "218bed0a7fc58764272e1c143f94d53a09afa022c88240e32a8e76a658d21dc9"
    note: "系统架构可视化图（HTML）"
last_verified: 2026-05-14
possibly_outdated: false
language: "zh"
canonical_source: "https://github.com/sydyg/automotive-claude-code-agents"
personal_writing: true
---

# Automotive Claude Code Agents 应用教程（v1.0.0）

> ⚠ 个人写作，不参与 source_count 计数。核心立场已写入 [[concepts/autosar-complex-driver]] 和 [[concepts/agent-harness]] 的 My Position 节。

## Key Points

- **项目定位**：automotive-claude-code-agents，专为汽车软件工程师设计的 Claude Code Agent 工具包，GitHub: sydyg/automotive-claude-code-agents
- **目标用户**：汽车软件工程师、ECU 开发人员、功能安全专家、自动驾驶工程师、车载网络工程师
- **核心价值**：将 AI 能力与汽车行业标准深度融合，工程效率提升 10 倍以上（量化声明）
- **覆盖规模**：40+ Agents、200+ Commands、75+ Skills、507+ 知识库文档、37+ Rules、41 编排模式
- **支持行业标准**：ISO 26262（功能安全）、ISO 21434（网络安全）、AUTOSAR Classic/Adaptive、ASPICE、MISRA C/C++、ISO 14229（UDS）、ISO 11898（CAN）、SOTIF (ISO 21448)、UN R155/R156、GB/T 标准
- **安装方式**：`git clone` + `./install.sh`，部署到 `~/.claude/`，命令以 `automotive-` 前缀命名
- **核心命令示例**：
  - `/automotive-review`：汽车软件代码审查（MISRA C/C++ 合规检查）
  - `/automotive-safety-audit`：功能安全审计（ISO 26262 ASIL 等级验证）
  - `/automotive-security-scan`：网络安全扫描（ISO 21434）
  - `/automotive-autosar-generate`：AUTOSAR 配置代码生成
- **LLM Council 机制**：多模型协作框架，不同任务分配不同 LLM（Claude/GPT/Gemini），发挥各模型长处
- **HIL/SIL 测试支持**：生成测试脚本，与测试台架集成
- **中国标准增强**（Yuxin Zhang 新增）：GB L2/L3/泊车功能/CATARC 法规合规支持

## Concepts Extracted

- [[concepts/agent-harness]]
- [[concepts/autosar-complex-driver]]
- [[concepts/claude-code-workflow]]

## Entities Extracted

- [[entities/automotive-claude-code-agents]]
- [[entities/claude-code]]

## External References

- GitHub: https://github.com/sydyg/automotive-claude-code-agents
- ISO 26262: 道路车辆功能安全标准（E/E系统）
- ISO 21434: 道路车辆网络安全工程标准

## Contradictions

## My Notes

这是将 ECC 框架垂直化到汽车领域的产物。507+ 知识库文档意味着大量行业标准被编码为 AI 可理解的知识。LLM Council 多模型协作是个关键设计——不同标准域（安全 vs 性能）可能需要不同 LLM 的优势。
