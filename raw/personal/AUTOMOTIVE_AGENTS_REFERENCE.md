# Automotive Claude Code Agents — 详细说明书

> **版本**: v1.0.0 | **语言**: 中文 | **更新**: 2026-05-11  
> **项目**: [automotive-claude-code-agents](https://github.com/sydyg/automotive-claude-code-agents)

---

## 目录

1. [项目概述](#1-项目概述)
2. [系统架构](#2-系统架构)
3. [核心组件：Agents（智能体）](#3-核心组件agentsintelligent-agents)
4. [核心组件：Commands（命令）](#4-核心组件commands命令)
5. [核心组件：Skills（技能）](#5-核心组件skills技能)
6. [核心组件：Knowledge Base（知识库）](#6-核心组件knowledge-base知识库)
7. [核心组件：Rules（规则）](#7-核心组件rules规则)
8. [核心组件：Hooks（钩子）](#8-核心组件hooks钩子)
9. [LLM Council 多模型协作框架](#9-llm-council-多模型协作框架)
10. [编排框架（Orchestration）](#10-编排框架orchestration)
11. [工具适配层（Tool Adapter）](#11-工具适配层tool-adapter)
12. [各领域Agent详解](#12-各领域agent详解)
13. [配置参考](#13-配置参考)
14. [项目目录结构参考](#14-项目目录结构参考)
15. [标准符合性矩阵](#15-标准符合性矩阵)

---

## 1. 项目概述

### 1.1 简介

**Automotive Claude Code Agents** 是一个专为汽车软件工程量身打造的专业级 Claude Code Agent 工具包。它将汽车行业深厚的领域知识、行业标准规范与 AI 辅助编程能力深度融合，赋能汽车软件工程师在 Claude Code 环境中高效完成复杂的工程任务。

本工具包由 Yuxin Zhang（吉林大学 / 卓宇科技 / DRIVEResearch）在原始版本基础上增强，新增了**中国汽车标准合规性**（GB L2/L3/泊车功能/CATARC 法规）支持。

### 1.2 定位与价值

| 维度 | 描述 |
|------|------|
| **目标用户** | 汽车软件工程师、ECU 开发人员、功能安全专家、自动驾驶工程师、车载网络工程师 |
| **核心价值** | 将 AI 能力与汽车行业标准深度融合，提升工程效率 10 倍以上 |
| **适用场景** | 代码生成、标准合规审查、架构设计、安全分析、诊断调试、测试自动化 |
| **技术基础** | Claude Code + 专业 Agents + 标准 Rules + 领域 Skills |

### 1.3 覆盖规模

| 资产类型 | 数量 | 说明 |
|----------|------|------|
| **Agents** | 40+ | 涵盖 27 个汽车专业领域 |
| **Commands** | 200+ | 覆盖 40+ 命令目录 |
| **Skills** | 75+ | 专业技能知识单元 |
| **Knowledge Base** | 507+ | 汽车参考文档 |
| **Rules** | 37+ | 编码/安全/流程规则 |
| **Orchestration Patterns** | 41 | 多智能体协作模式 |

### 1.4 支持的行业标准

| 标准 | 领域 |
|------|------|
| ISO 26262 | 功能安全 |
| ISO/SAE 21434 | 网络安全 |
| AUTOSAR Classic/Adaptive | 软件架构 |
| ASPICE | 软件过程评估 |
| UN R155/R156 | 法规合规 |
| SOTIF (ISO 21448) | 预期功能安全 |
| MISRA C/C++ | 编码规范 |
| ISO 14229 (UDS) | 诊断通信 |
| ISO 11898 (CAN) | 总线通信 |
| GB/T 标准 | 中国国标 |

---

## 2. 系统架构

### 2.1 整体架构图

```
┌─────────────────────────────────────────────────────────────────┐
│                    Claude Code 用户界面                          │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                     核心调度层 (Core Layer)                      │
│  ┌─────────────────┐  ┌──────────────────┐  ┌────────────────┐  │
│  │  LLM Council    │  │  Skill Router    │  │ Tool Adapter   │  │
│  │ (多模型协作)    │  │  (任务路由)      │  │ (工具抽象)     │  │
│  └─────────────────┘  └──────────────────┘  └────────────────┘  │
└────────────────────────────┬────────────────────────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                    编排层 (Orchestration Layer)                  │
│   41种编排模式：自适应调试、任务竞标、变更传播、合规审计...     │
└────────────────────────────┬────────────────────────────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
┌────────────────┐ ┌─────────────────┐ ┌──────────────────┐
│   Agents 层    │ │  Commands 层    │ │   Skills 层      │
│  (领域专家)    │ │  (执行命令)     │ │  (技能知识)      │
│  40+ agents    │ │  200+ commands  │ │  75+ skills      │
└────────────────┘ └─────────────────┘ └──────────────────┘
         │                   │                   │
         └───────────────────┼───────────────────┘
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                   知识与规则层                                   │
│  ┌─────────────────────────────┐  ┌───────────────────────────┐ │
│  │   Knowledge Base (507+ 文档)│  │   Rules (37+ 规则文件)    │ │
│  └─────────────────────────────┘  └───────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 数据流向

```
用户请求 → Claude Code
    ↓
Skill Router 识别任务类型
    ↓
匹配领域 Agent（功能安全/网络安全/ADAS/电池等）
    ↓
Agent 激活对应 Skills + Rules
    ↓
Commands 执行具体操作
    ↓
调用 Tool Adapter（CANoe/MATLAB/ECU 工具等）
    ↓
返回带标准合规标注的结果
```

### 2.3 安装架构

工具包采用**追加安装**（Append-Only）策略，绝不覆盖用户现有配置：

- 所有资产安装到 `~/.claude/` 目录
- 全部使用 `automotive-` 命名空间前缀，避免冲突
- 支持 `--dry-run` 预览、`--status` 检查、`--uninstall` 卸载

---

## 3. 核心组件：Agents（智能体）

### 3.1 概念说明

Agent 是具备特定领域专业知识的智能体。每个 Agent：
- 定义了角色与职责
- 声明了所使用的 Skills 集合
- 包含领域特定的工作流程
- 遵循对应的行业标准

### 3.2 Agent 配置文件格式

```yaml
name: <agent-name>
version: "1.0.0"
description: |
  <功能描述>

role: <角色名称>
expertise:
  - <专业领域1>
  - <专业领域2>

skills_used:
  - <skill-namespace>/<skill-name>

standards:
  - ISO 26262
  - AUTOSAR

workflows:
  - name: <工作流名称>
    steps:
      - <步骤1>
      - <步骤2>
```

### 3.3 Agent 领域目录（40+ Agents）

#### 3.3.1 核心基础 Agents（agents/core/）

| Agent 文件 | 名称 | 功能 |
|-----------|------|------|
| `llm-council.yaml` | LLM Council 编排器 | 多模型辩论框架，Claude Opus 4.6 + GPT-5.4 协同 |
| `skill-router.yaml` | 技能路由器 | 11个汽车领域智能任务路由 |
| `tool-adapter.yaml` | 工具适配器 | 商业/开源工具统一抽象层 |

#### 3.3.2 功能安全 Agents（agents/functional-safety/）

专注于 ISO 26262 全生命周期安全工程：
- 危害分析与风险评估（HARA）
- 功能安全概念（FSC）制定
- 安全目标与 ASIL 分配
- 安全案例构建（Safety Case）
- 功能安全审核（Audit）

#### 3.3.3 网络安全 Agents（agents/cybersecurity/）

覆盖 ISO/SAE 21434 和 UN R155/R156：

| Agent | 职责 |
|-------|------|
| `automotive-security-architect.md` | 安全架构设计，TARA 分析 |
| `can-ids-developer.md` | CAN 总线入侵检测系统开发 |
| `secure-boot-specialist.md` | 安全启动链，信任根（Root of Trust） |
| `penetration-tester.md` | 渗透测试，模糊测试（Fuzzing） |
| `pki-specialist.md` | PKI 基础设施，HSM 集成 |
| `incident-response.md` | 安全事件响应 |
| `compliance-auditor.md` | UN R155/R156 合规审计 |

#### 3.3.4 ADAS 感知 Agents（agents/adas/）

覆盖自动驾驶感知全栈：
- 传感器融合（摄像头、激光雷达、毫米波雷达）
- 目标检测与跟踪
- 深度估计与语义分割
- 感知算法验证
- SOTIF（ISO 21448）合规

#### 3.3.5 电池管理 Agents（agents/battery/）

专注 EV 电池系统：
- BMS 算法开发（SOC/SOH 估算）
- 电池热管理系统
- 电池安全分析（UN 38.3）
- 电池数据分析与寿命预测

#### 3.3.6 车辆诊断 Agents（agents/diagnostics/）

覆盖全链路诊断：
- UDS（ISO 14229）协议实现
- OBD-II 故障码管理
- DoIP 以太网诊断
- ECU 刷写（Flash Programming）
- ODX/PDX 数据处理

#### 3.3.7 AI ECU Agents（agents/ai-ecu/）

面向车端 AI 推理：
- 神经网络模型优化（量化、剪枝）
- NPU/GPU 异构计算调度
- 实时推理框架集成
- 模型安全与隐私保护

#### 3.3.8 HPC 平台 Agents（agents/hpc-platform/）

高性能计算平台：
- 多核异构处理器调度（ARM Cortex-A/R/M + RISC-V）
- Hypervisor 虚拟化（Type-1: Xen/KVM）
- 内存管理（NUMA 优化）
- 实时性保障（PREEMPT-RT）

#### 3.3.9 其他领域 Agents

| 目录 | 领域 | 主要功能 |
|------|------|---------|
| `agents/autosar/` | AUTOSAR | Classic/Adaptive 架构配置 |
| `agents/qnx/` | QNX | 实时操作系统开发 |
| `agents/safety/` | 功能安全 | ASIL 分配、FTA/FMEA |
| `agents/sotif/` | SOTIF | 预期功能安全分析 |
| `agents/v2x/` | V2X | 车路协同通信（DSRC/C-V2X） |
| `agents/cloud/` | 云端 | 车云通信、OTA 更新 |
| `agents/testing/` | 测试 | HIL/SIL 测试自动化 |
| `agents/mbd/` | MBD | 模型驱动开发（MATLAB/Simulink） |
| `agents/sdv-platform/` | SDV | 软件定义汽车平台 |
| `agents/zonal-architecture/` | 区域架构 | Zonal ECU 架构设计 |
| `agents/powertrain-chassis/` | 动力底盘 | 发动机/变速箱/制动控制 |
| `agents/cockpit/` | 座舱 | 智能座舱 HMI/IVI |
| `agents/ev-systems/` | 电驱系统 | 电机控制、充电管理 |
| `agents/ml-analytics/` | ML分析 | 车辆数据机器学习 |
| `agents/kubernetes/` | 容器化 | K8s 容器编排 |
| `agents/china-compliance/` | 中国合规 | GB标准、CATARC 法规 |

---

## 4. 核心组件：Commands（命令）

### 4.1 概念说明

Commands 是可直接在 Claude Code 中执行的预定义命令。每个命令封装了特定任务的完整执行逻辑，支持参数化调用。

### 4.2 命令命名规范

```
automotive-<领域>-<动作>-<目标>
```

示例：
- `automotive-safety-analyze-asil` — 执行 ASIL 等级分析
- `automotive-diag-generate-uds` — 生成 UDS 诊断代码
- `automotive-autosar-configure-rte` — 配置 AUTOSAR RTE

### 4.3 命令目录总览（40+ 目录，200+ 命令）

#### 通用命令（commands/general/）

| 命令 | 功能 |
|------|------|
| `automotive-review` | 汽车软件代码审查 |
| `automotive-generate` | 代码生成（含标准合规） |
| `automotive-document` | 技术文档自动生成 |
| `automotive-analyze` | 架构与代码分析 |

#### 安全命令（commands/safety/）

| 命令 | 功能 |
|------|------|
| `automotive-safety-hara` | 危害分析与风险评估 |
| `automotive-safety-asil` | ASIL 分配与分解 |
| `automotive-safety-fmea` | FMEA 失效模式分析 |
| `automotive-safety-fta` | 故障树分析 |
| `automotive-safety-audit` | ISO 26262 合规审计 |
| `automotive-safety-dfa` | 相关故障分析 |

#### 诊断命令（commands/diagnostics/）

| 命令 | 功能 |
|------|------|
| `automotive-diag-uds` | UDS 服务实现 |
| `automotive-diag-obd2` | OBD-II 数据解析 |
| `automotive-diag-dtc` | DTC 故障码管理 |
| `automotive-diag-doip` | DoIP 以太网诊断 |
| `automotive-diag-flash` | ECU 刷写编程（7步流程） |

#### AUTOSAR 命令（commands/autosar/）

| 命令 | 功能 |
|------|------|
| `automotive-autosar-classic` | AUTOSAR Classic 配置 |
| `automotive-autosar-adaptive` | Adaptive AUTOSAR 开发 |
| `automotive-autosar-rte` | RTE 运行时环境生成 |
| `automotive-autosar-com` | 通信矩阵配置 |
| `automotive-autosar-arxml` | ARXML 文件解析与生成 |

#### 测试命令（commands/testing/）

| 命令 | 功能 |
|------|------|
| `automotive-test-hil` | HIL 测试配置 |
| `automotive-test-sil` | SIL 软件仿真测试 |
| `automotive-test-unit` | 单元测试生成 |
| `automotive-test-coverage` | MC/DC 覆盖率分析 |
| `automotive-test-regression` | 回归测试管理 |

#### 网络安全命令（commands/security/）

| 命令 | 功能 |
|------|------|
| `automotive-sec-tara` | TARA 威胁分析 |
| `automotive-sec-pentest` | 渗透测试框架 |
| `automotive-sec-secureboot` | 安全启动配置 |
| `automotive-sec-ids` | 入侵检测规则生成 |
| `automotive-sec-crypto` | 密码学方案实现 |

#### 其他领域命令

| 目录 | 示例命令 | 功能概述 |
|------|---------|---------|
| `commands/adas/` | `automotive-adas-perception` | 感知算法开发 |
| `commands/battery/` | `automotive-battery-bms` | BMS 算法实现 |
| `commands/mbd/` | `automotive-mbd-simulink` | Simulink 代码生成 |
| `commands/network/` | `automotive-net-can` | CAN/LIN/FlexRay 配置 |
| `commands/v2x/` | `automotive-v2x-dsrc` | V2X 消息处理 |
| `commands/cloud/` | `automotive-cloud-ota` | OTA 更新管理 |
| `commands/qnx/` | `automotive-qnx-rtos` | QNX 实时任务开发 |
| `commands/embedded/` | `automotive-embedded-bsp` | BSP 驱动开发 |
| `commands/powertrain/` | `automotive-pt-engine` | 发动机控制算法 |
| `commands/chassis/` | `automotive-chassis-abs` | ABS/ESC 控制 |
| `commands/cockpit/` | `automotive-cockpit-hmi` | HMI 界面开发 |
| `commands/ev/` | `automotive-ev-motor` | 电机控制算法 |
| `commands/hil-sil/` | `automotive-hilsil-setup` | HIL/SIL 环境配置 |
| `commands/kubernetes/` | `automotive-k8s-deploy` | 容器化部署 |
| `commands/llm-council/` | `automotive-council-debate` | 多模型辩论决策 |

### 4.4 LLM Council 专属命令（commands/llm-council/）

| 脚本 | 功能 |
|------|------|
| `council-debate.sh` | 发起 Claude + GPT 多轮辩论 |
| `council-decide.sh` | 生成架构决策记录（ADR） |
| `council-review.sh` | 多模型代码审查（文件/PR/commit） |

---

## 5. 核心组件：Skills（技能）

### 5.1 概念说明

Skills 是细粒度的专业知识单元，封装了特定技术领域的深度知识、最佳实践和代码模板。Skills 被 Agents 调用以完成具体的专业任务。

### 5.2 Skill 目录（75+ 技能）

#### 网络安全技能（skills/automotive-cybersecurity/）

| 技能文件 | 功能 |
|---------|------|
| `can-ids-engine.md` | CAN 总线入侵检测引擎（基线学习 + 异常检测） |
| `iso-21434-tara.md` | ISO 21434 TARA 威胁分析工具（风险矩阵） |
| `penetration-testing.md` | 渗透测试框架（CAN 模糊测试/蓝牙/固件逆向） |
| `secure-boot-chain.md` | 安全启动链（NXP HAB/Renesas/AURIX） |
| `misra-fuzzing.md` | MISRA C 合规 + LibFuzzer 集成 |
| `v2x-pki.md` | V2X PKI 管理（假名证书 + HSM 集成） |

#### 诊断技能（skills/automotive-diagnostics/）

| 技能文件 | 功能 |
|---------|------|
| `uds-implementation.md` | UDS ISO 14229 完整实现 |
| `obd2-decoder.md` | OBD-II Mode 01-0A（含全 PID 解码） |
| `dtc-management.md` | DTC 管理系统（J2012 标准数据库） |
| `doip-client.md` | DoIP 以太网诊断客户端 |
| `odx-parser.md` | ODX/PDX 数据解析器 |
| `ecu-flash.md` | ECU 刷写编程（7步标准流程） |
| `canoe-integration.md` | CANoe/CAPL/python-uds 工具集成 |

#### ADAS 技能（skills/automotive-adas/）

- 传感器融合算法（扩展卡尔曼滤波、粒子滤波）
- 目标检测（YOLOv8/SSD 优化实现）
- 点云处理（PCL/Open3D）
- 语义分割（DeepLab、SegFormer）
- 感知精度评估（mAP、NDS）

#### EV 动力系统技能（skills/automotive-powertrain-chassis/）

- 电机控制（FOC 磁场定向控制）
- 制动能量回收（再生制动算法）
- 热管理协调控制
- NVH 振动噪声分析

#### ML 分析技能（skills/automotive-ml/）

- 车辆数据特征工程
- 预测性维护模型（LSTM/Transformer）
- 异常检测（Isolation Forest/Autoencoder）
- 模型性能评估与部署

#### HPC 平台技能（skills/automotive-hpc/）

- 异构计算调度（CPU/GPU/NPU）
- 实时性分析（WCET 最坏执行时间）
- 内存安全（MISRA/CERT-C）
- 功耗优化

#### 中国标准技能

| 技能目录 | 覆盖标准 |
|---------|---------|
| `skills/automotive-china-l2-adas-compliance/` | GB/T L2 自动驾驶辅助系统 |
| `skills/automotive-china-l3-ads-compliance/` | GB/T L3 自动驾驶系统 |
| `skills/automotive-china-parking-compliance/` | GB/T 自动泊车系统 |
| `skills/automotive-china-standards-overview/` | 中国汽车标准体系全览 |

---

## 6. 核心组件：Knowledge Base（知识库）

### 6.1 概述

知识库包含 **507+ 汽车参考文档**，约 **2,500+ 页**内容，采用 5 级层次结构组织。

### 6.2 文档分级

| 层级 | 类型 | 页数 |
|------|------|------|
| Level 1 | Overview（概述） | 1-2页 |
| Level 2 | Conceptual（概念） | 5-10页 |
| Level 3 | Detailed（详细） | 20-50页 |
| Level 4 | Reference（参考） | 10-100页 |
| Level 5 | Advanced（高级） | 30-100页 |

### 6.3 四大分类

#### 6.3.1 Standards（标准文档 — 75篇）

| 标准 | 文档数 | 状态 |
|------|--------|------|
| AUTOSAR Classic Platform | 5 | ✅ 完成 |
| AUTOSAR Adaptive Platform | 5 | ⚠ 进行中 |
| ISO 26262 功能安全 | 5 | ⚠ 进行中 |
| ASPICE | 5 | 规划中 |
| ISO 21434 | 5 | 规划中 |
| UN R155/R156 | 各5 | 规划中 |
| SOTIF ISO 21448 | 5 | 规划中 |
| MISRA C/C++ | 各5 | 规划中 |
| ISO 11898 CAN | 5 | 规划中 |
| ISO 14229 UDS | 5 | 规划中 |

#### 6.3.2 Technologies（技术文档 — 225篇）

| 类别 | 篇数 | 内容 |
|------|------|------|
| 操作系统 | 25 | Yocto（✅完成）、Android Auto、QNX、FreeRTOS、Zephyr |
| 通信协议 | 50 | CAN/CAN FD、LIN、FlexRay、Automotive Ethernet、SOME/IP、DoIP、DDS、V2X |
| 中间件/框架 | 40 | ROS 2、Eclipse iceoryx、CycloneDDS、Zenoh、eCAL |
| 安全/密码学 | 30 | OpenSSL、Botan、TPM 2.0、PKCS#11、TrustZone |
| 开发工具 | 35 | Vector Tools、MATLAB/Simulink、ETAS、dSPACE |
| 仿真测试 | 25 | CARLA、Prescan、MATLAB/Simulink Test |
| 数据存储 | 20 | Apache IoTDB、InfluxDB、SQLite |

#### 6.3.3 Processes（流程文档 — 40篇）

- APQP、PPAP、FMEA
- TARA、HAZOP、FTA
- Systems Engineering、Requirements Management
- CI/CD for Automotive、DevSecOps

#### 6.3.4 Tools（工具文档 — 167篇）

覆盖 300+ 汽车工具的检测、安装、配置与对比：
- Vector CANoe/CANalyzer
- ETAS INCA/HSP
- dSPACE HIL/RCP
- MATLAB/Simulink
- Python-CAN、cantools、python-uds

### 6.4 知识库路径

```
knowledge-base/
├── INDEX.md              # 完整索引（507+ 文档）
├── README.md             # 知识库使用指南
├── standards/            # 标准文档
├── technologies/         # 技术文档
├── processes/            # 流程文档
└── tools/                # 工具文档
```

---

## 7. 核心组件：Rules（规则）

### 7.1 概述

Rules 是注入到 Claude Code 上下文中的强制性规范约束，确保生成的代码符合汽车行业标准。

### 7.2 规则目录（37+ 规则文件）

#### 编码规范（rules/coding-standards/）— 12个文件

| 文件 | 内容 |
|------|------|
| `misra-c-2012.md` | MISRA C 2012 规则（全部 175 条） |
| `misra-cpp-2008.md` | MISRA C++ 2008 规则 |
| `autosar-cpp14.md` | AUTOSAR C++14 编码规则 |
| `cert-c.md` | CERT C 安全编码标准 |
| `cert-cpp.md` | CERT C++ 安全编码标准 |
| `iso26262-sw-coding.md` | ISO 26262 软件编码规范 |
| `adaptive-autosar-coding.md` | Adaptive AUTOSAR 编码规范 |

#### 安全标准（rules/safety-standards/）— 8个文件

| 文件 | 内容 |
|------|------|
| `iso26262-asil-decomposition.md` | ASIL 分解规则 |
| `iso26262-hara.md` | HARA 执行规则 |
| `aspice-level2.md` | ASPICE Level 2 过程要求 |
| `sotif-analysis.md` | SOTIF 性能限制分析 |
| `functional-safety-plan.md` | 功能安全计划模板 |

#### 安全规范（rules/security-standards/）— 6个文件

- `iso21434-tara.md` — TARA 执行规则
- `un-r155-compliance.md` — UN R155 合规检查清单
- `secure-coding-embedded.md` — 嵌入式安全编码规则
- `vehicle-crypto.md` — 车辆密码学规范

#### 测试规范（rules/testing-standards/）— 3个文件

- `mc-dc-coverage.md` — MC/DC 覆盖率要求
- `hil-test-standards.md` — HIL 测试规范
- `unit-test-automotive.md` — 单元测试规范

#### 流程规范（rules/process-standards/）

- ASPICE 过程属性要求
- 变更管理规则
- 文档规范

#### 中国标准（rules/china-standards/）

- GB/T L2 ADAS 合规规则
- GB/T L3 ADS 合规规则
- CATARC 认证要求
- 工信部法规要求

---

## 8. 核心组件：Hooks（钩子）

### 8.1 概述

Hooks 是集成到 Git 工作流中的自动化检查脚本，确保每次代码提交都符合汽车行业规范。

### 8.2 钩子目录

```
hooks/
├── pre-commit/       # 提交前：MISRA 检查、安全扫描
├── pre-push/         # 推送前：完整测试套件
├── pre-merge/        # 合并前：ASPICE 合规检查
├── post-commit/      # 提交后：文档同步
└── post-deploy/      # 部署后：OTA 验证
```

### 8.3 关键 Pre-Commit 检查

1. MISRA C/C++ 静态分析
2. ISO 26262 安全注释完整性
3. 密码学使用合规（禁止弱算法）
4. 敏感信息扫描（密钥/证书）
5. AUTOSAR 接口一致性

---

## 9. LLM Council 多模型协作框架

### 9.1 概述

LLM Council 是本工具包的核心创新之一，通过 **Claude Opus 4.6**（Anthropic）与 **GPT-5.4**（Azure OpenAI）的多轮辩论达成工程决策共识。

### 9.2 适用场景

| 任务类型 | 说明 |
|---------|------|
| 架构决策评审 | 对重要架构选型进行多模型辩论 |
| 安全关键代码审查 | ASIL-D 级代码的双模型审查 |
| 技术方案选型 | 对比多个技术方案的优劣 |
| 标准合规验证 | 复杂标准条款的解释与应用 |
| 风险评估 | TARA/HARA 多视角分析 |

### 9.3 工作流程

```
输入: 技术问题/代码/架构图
    ↓
Round 1: Claude Opus 4.6 分析（深度推理）
    ↓
Round 2: GPT-5.4 评审与反驳（独立视角）
    ↓
Round 3: Claude Opus 4.6 综合修订
    ↓
Round N: 直至达成共识（默认最多5轮）
    ↓
输出: 架构决策记录（ADR）+ 共识结论
```

### 9.4 成本估算

| 请求类型 | 每轮成本 | 说明 |
|---------|---------|------|
| 标准分析 | ~$0.04 | 3轮辩论 |
| 代码审查 | ~$0.08 | 含完整代码上下文 |
| 架构决策 | ~$0.12 | 5轮深度分析 |

### 9.5 配置参数（agents/core/llm-council.yaml）

```yaml
models:
  primary: claude-opus-4-6
  secondary: gpt-5.4-azure
  
debate:
  max_rounds: 5
  consensus_threshold: 0.85
  
output:
  format: ADR  # Architecture Decision Record
  include_dissent: true  # 保留少数意见
```

---

## 10. 编排框架（Orchestration）

### 10.1 概述

编排框架提供 41 种多智能体协作模式，管理复杂工程任务的 Agent 协作流程。

### 10.2 核心编排模式

| 模式 | 文件 | 适用场景 |
|------|------|---------|
| 自适应调试 | `adaptive-orchestrator.yaml` | 动态调整调试策略 |
| 任务竞标 | `auction-based.yaml` | 并行任务分配 |
| 变更传播 | `change-propagator.yaml` | 跨模块变更影响分析 |
| 协作编辑 | `collaborative-editing.yaml` | 多 Agent 并发开发 |
| 合规审计 | `compliance-auditor.yaml` | 多标准并行合规检查 |
| 上下文压缩 | `context-compressor.yaml` | 长上下文摘要 |
| 专家委员会 | `expert-panel.yaml` | 多领域专家会审 |
| 渐进式改进 | `incremental-refiner.yaml` | 迭代优化代码 |
| 知识综合 | `knowledge-synthesizer.yaml` | 跨文档知识融合 |
| 并行分析 | `parallel-analyzer.yaml` | 多维度并行分析 |

### 10.3 编排模式选择指南

```
任务复杂度评估
    │
    ├── 单一领域、明确任务 → 直接调用对应 Agent
    │
    ├── 跨领域协作（安全+网络安全）→ expert-panel 模式
    │
    ├── 大型代码审查 → parallel-analyzer 模式
    │
    ├── 架构重构 → change-propagator 模式
    │
    └── 高风险决策（ASIL-D）→ LLM Council 模式
```

---

## 11. 工具适配层（Tool Adapter）

### 11.1 概述

工具适配器提供商业工具与开源工具之间的统一抽象接口，支持无缝迁移，年节约成本估算达 **$310,000**。

### 11.2 支持工具矩阵

| 工具类别 | 商业工具 | 开源替代 |
|---------|---------|---------|
| 总线分析 | Vector CANoe | python-can + cantools |
| 标定工具 | ETAS INCA | openMCU-calibration |
| HIL 系统 | dSPACE HIL | CARMaker/IPG |
| 模型开发 | MATLAB/Simulink | Scilab/OpenModelica |
| 需求管理 | IBM DOORS | OpenFAST + Polarion |
| 测试管理 | JIRA Xray | pytest-automotive |

### 11.3 工具检测（scripts/detect-tools.sh）

```bash
# 自动检测已安装的汽车工具
./scripts/detect-tools.sh

# 输出示例
[✓] Vector CANoe 17.0 - /opt/vector/canoe
[✓] Python-CAN 4.3.1 - pip installed
[✗] MATLAB R2024b - NOT FOUND
[~] ETAS INCA - Alternative available: openMCU
```

---

## 12. 各领域Agent详解

### 12.1 功能安全 Agent（ISO 26262）

**激活命令**: `/automotive-safety-analyze`

**核心能力**:
- HARA（危害分析与风险评估）执行
- ASIL 等级确定（QM/A/B/C/D）
- 安全目标制定
- 功能安全需求派生
- 安全案例（Safety Case）构建（GSN/CAE 符号）
- ISO 26262 Part 6 软件级合规审查

**输出示例**:
```
HARA 结果:
  危害场景: H-01 意外加速
  严重度 (S): S3 - 危及生命
  暴露度 (E): E4 - 高概率
  可控性 (C): C3 - 难以控制
  → ASIL 等级: ASIL-D

安全目标: SG-01 防止意外加速
  → 功能安全需求 FSR-001...FSR-005
```

### 12.2 网络安全 Agent（ISO 21434）

**激活命令**: `/automotive-security-tara`

**核心能力**:
- TARA（威胁分析与风险评估）执行
- 威胁场景识别（STRIDE 方法）
- 风险值计算（影响 × 可行性）
- 安全概念设计
- CAN/ETH/BLE 攻击面分析

**TARA 风险矩阵**:

| 影响 \ 可行性 | 低 | 中 | 高 |
|-------------|----|----|-----|
| **低** | Risk-1 | Risk-2 | Risk-3 |
| **中** | Risk-2 | Risk-3 | Risk-4 |
| **高** | Risk-3 | Risk-4 | Risk-5 |

### 12.3 ADAS 感知 Agent

**激活命令**: `/automotive-adas-perception`

**核心能力**:
- 多传感器融合架构设计
- 感知算法实现（PyTorch/TensorRT）
- ROS 2 节点开发
- SOTIF 性能边界分析
- 感知测试场景生成

### 12.4 诊断 Agent（UDS/OBD-II）

**激活命令**: `/automotive-diag-uds`

**UDS 服务支持**:

| 服务 ID | 服务名称 | 功能 |
|--------|---------|------|
| 0x10 | DiagnosticSessionControl | 诊断会话切换 |
| 0x11 | ECUReset | ECU 复位 |
| 0x14 | ClearDiagnosticInformation | 清除 DTC |
| 0x19 | ReadDTCInformation | 读取故障码 |
| 0x22 | ReadDataByIdentifier | 读取数据 |
| 0x27 | SecurityAccess | 安全访问解锁 |
| 0x2E | WriteDataByIdentifier | 写入数据 |
| 0x31 | RoutineControl | 例程控制 |
| 0x34-0x37 | Download/Upload | 数据传输 |

---

## 13. 配置参考

### 13.1 环境变量（.env.example）

```bash
# AI 模型配置
ANTHROPIC_API_KEY=sk-ant-...           # Claude API 密钥
AZURE_OPENAI_API_KEY=...               # Azure OpenAI（LLM Council）
AZURE_OPENAI_ENDPOINT=https://...      # Azure 端点

# 工具配置
CANOE_LICENSE_SERVER=192.168.1.100     # CANoe 授权服务器
MATLAB_LICENSE_FILE=/opt/matlab/lic    # MATLAB 授权文件
ETAS_INCA_PATH=/opt/etas/inca         # INCA 安装路径

# 项目配置
AUTOMOTIVE_PROJECT_ROOT=/workspace    # 项目根目录
AUTOMOTIVE_LOG_LEVEL=INFO             # 日志级别
SAFETY_CRITICAL_MODE=true             # 安全关键模式
```

### 13.2 CLAUDE.md 配置

`CLAUDE.md` 是 Claude Code 的项目级配置文件，定义了工作行为规范：

```markdown
# 汽车软件工程 Claude 配置

## 代码生成规则
- 所有 C 代码遵循 MISRA C:2012
- 安全关键函数必须添加 ASIL 注释
- 禁止使用动态内存分配（堆内存）

## 标准参考
- 功能安全: ISO 26262:2018
- 网络安全: ISO/SAE 21434:2021
- 编码: AUTOSAR C++14

## 输出格式
- 代码审查: 按标准条款引用
- 安全分析: 使用 GSN 符号
```

### 13.3 pyproject.toml 关键配置

```toml
[tool.automotive-agents]
version = "0.1.0"
safety_mode = "ISO26262"
default_asil = "QM"

[tool.black]
line-length = 79  # 嵌入式风格

[tool.ruff]
select = ["E", "W", "MISRA"]  # 启用 MISRA 规则检查

[tool.pytest.ini_options]
testpaths = ["tests"]
coverage_target = 80  # 安全关键代码要求 100%
```

---

## 14. 项目目录结构参考

```
automotive-claude-code-agents/
│
├── agents/                    # 智能体定义
│   ├── core/                 # 核心调度（LLM Council、路由器）
│   ├── orchestration/        # 41种编排模式
│   ├── functional-safety/    # ISO 26262
│   ├── cybersecurity/        # ISO 21434 / UN R155
│   ├── adas/                 # 自动驾驶感知
│   ├── battery/              # 电池管理
│   ├── diagnostics/          # 车辆诊断
│   ├── autosar/              # AUTOSAR 架构
│   ├── qnx/                  # QNX RTOS
│   ├── ev-systems/           # 电驱系统
│   ├── hpc-platform/         # 高性能计算
│   ├── ai-ecu/               # AI 推理 ECU
│   ├── china-compliance/     # 中国标准合规
│   └── ...                   # 其他25+领域
│
├── commands/                  # 可执行命令
│   ├── general/              # 通用命令
│   ├── safety/               # 安全命令
│   ├── security/             # 网络安全命令
│   ├── diagnostics/          # 诊断命令
│   ├── autosar/              # AUTOSAR 命令
│   ├── testing/              # 测试命令
│   ├── llm-council/          # 多模型命令
│   └── ...                   # 其他35+目录
│
├── skills/                    # 技能知识单元（75+）
│   ├── automotive-cybersecurity/
│   ├── automotive-diagnostics/
│   ├── automotive-adas/
│   ├── automotive-hpc/
│   ├── automotive-ml/
│   ├── automotive-china-*-compliance/
│   └── ...
│
├── knowledge-base/            # 知识库（507+文档）
│   ├── standards/
│   ├── technologies/
│   ├── processes/
│   └── tools/
│
├── rules/                     # 规则约束（37+文件）
│   ├── coding-standards/
│   ├── safety-standards/
│   ├── security-standards/
│   ├── testing-standards/
│   ├── process-standards/
│   └── china-standards/
│
├── hooks/                     # Git 自动化钩子
├── scripts/                   # 生成与管理脚本
├── examples/                  # 示例代码
├── docs/                      # 项目文档
├── tests/                     # 测试套件
├── workflows/                 # CI/CD 工作流
├── kubernetes/                # K8s 部署
├── helm/                      # Helm Charts
├── terraform/                 # 基础设施即代码
└── monitoring/                # Prometheus 监控
```

---

## 15. 标准符合性矩阵

| 组件 | ISO 26262 | ISO 21434 | AUTOSAR | ASPICE | MISRA | UN R155 | GB/T |
|------|-----------|-----------|---------|--------|-------|---------|------|
| Agents/safety | ✅ 全覆盖 | — | ✅ | ✅ | — | — | — |
| Agents/cybersecurity | — | ✅ 全覆盖 | — | ✅ | — | ✅ | — |
| Agents/autosar | ✅ | — | ✅ 全覆盖 | ✅ | ✅ | — | — |
| Rules/coding | ✅ | ✅ | ✅ | — | ✅ 全覆盖 | — | — |
| Rules/safety | ✅ 全覆盖 | — | — | ✅ | — | — | — |
| Rules/china | — | — | — | — | — | — | ✅ 全覆盖 |
| Skills/cybersecurity | — | ✅ | — | — | ✅ | ✅ | — |
| Skills/diagnostics | — | — | ✅ | — | — | — | — |
| LLM Council | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

---

*本说明书根据项目代码库自动生成，版本 v1.0.0*  
*如有疑问请参考 [使用教程手册](AUTOMOTIVE_AGENTS_TUTORIAL.md)*
