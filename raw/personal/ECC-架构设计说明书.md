# Everything Claude Code (ECC) 架构设计说明书

> **版本：** 2.0.0-rc.1  
> **文档版本：** 1.0.0  
> **编写日期：** 2026-05-12  
> **适用范围：** ECC 系统架构师、开发人员、技术评估人员

---

## 目录

1. [系统概述](#1-系统概述)
2. [设计目标与原则](#2-设计目标与原则)
3. [整体架构](#3-整体架构)
4. [核心层次架构](#4-核心层次架构)
5. [核心模块说明](#5-核心模块说明)
6. [模块交互关系](#6-模块交互关系)
7. [技术选型](#7-技术选型)
8. [安装与部署架构](#8-安装与部署架构)
9. [扩展架构](#9-扩展架构)
10. [安全架构](#10-安全架构)

---

## 1. 系统概述

### 1.1 项目背景

**Everything Claude Code（ECC）** 起源于 Anthropic 黑客马拉松获奖项目，经过 10+ 个月的高强度生产环境验证和打磨，发展为一套成熟的 AI 代理框架性能优化系统。

ECC 的核心定位是：**AI 代理编排框架的"操作系统增强层"**。它通过为 Claude Code、Codex、Cursor、OpenCode、Gemini 等 AI 代理框架注入专业化的代理、技能、命令、规则和自动化钩子，将 AI 编码助手从通用对话工具转化为具备专业工程师级能力的智能开发平台。

### 1.2 系统规模

| 维度 | 数量 |
|------|------|
| 专用子代理（Agents） | 53 个 |
| 工作流技能（Skills） | 200+ 个 |
| 命令（Commands / Shims） | 69 个 |
| 支持语言生态系统 | 12+ 种 |
| MCP 服务器配置 | 14 套 |
| 国际化支持 | 7 种语言 |

### 1.3 适用场景

- **个人开发者**：通过 minimal profile 快速获得生产级 AI 辅助编码能力
- **团队协作**：通过 developer/full profile 统一团队 AI 工作流标准
- **企业级部署**：通过 harness 支持在 Claude Code、Codex、Cursor 等多个平台上一致运行
- **AI 系统集成商**：通过 MCP 配置扩展 AI 工具生态

---

## 2. 设计目标与原则

### 2.1 设计目标

| 目标 | 描述 |
|------|------|
| **跨框架兼容性** | 支持 Claude Code、Codex、Cursor、OpenCode、Gemini 等主流 AI 代理框架 |
| **模块化可插拔** | 所有组件独立可选，支持按需安装 |
| **生产就绪** | 10+ 个月真实工程场景验证，所有组件经过实战检验 |
| **安全优先** | 内置安全审查、凭据保护、输入验证机制 |
| **持续演进** | 支持 auto-update、持续学习和知识积累 |
| **可观测性** | 内置 Dashboard、会话管理、状态追踪能力 |

### 2.2 核心设计原则

#### 原则 1：Agent-First（代理优先）
所有复杂任务委托给专用代理处理。系统设计遵循"单一职责"原则，每个代理只负责一个专业领域。

#### 原则 2：Skills-First（技能优先）
`skills/` 目录是主要工作流界面。`commands/` 仅作为历史兼容的 shim 层保留。新功能首先在 `skills/` 中实现。

#### 原则 3：Immutability（不可变性）
所有状态变更通过创建新对象实现，禁止直接修改现有对象。

#### 原则 4：Test-Driven（测试驱动）
最低 80% 代码覆盖率，遵循 Red-Green-Refactor 循环。

#### 原则 5：Security-First（安全优先）
永不硬编码密钥。所有用户输入在系统边界处验证。提交前必须通过安全审查。

#### 原则 6：Plan Before Execute（先规划后执行）
复杂功能开始前必须使用 planner agent 制定计划。

---

## 3. 整体架构

### 3.1 架构全景图

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        ECC 系统架构全景图                                  │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                     用户 / 开发者                                 │    │
│  └───────────────────────────┬─────────────────────────────────────┘    │
│                              │  自然语言指令 / 命令                        │
│  ┌───────────────────────────▼─────────────────────────────────────┐    │
│  │              AI 代理框架层（Harness Layer）                        │    │
│  │   Claude Code │ Codex │ Cursor │ OpenCode │ Gemini             │    │
│  └───────┬───────────────────┬──────────────────────┬─────────────┘    │
│          │                   │                      │                   │
│  ┌───────▼───────┐  ┌────────▼────────┐  ┌─────────▼─────────┐        │
│  │  Agents 层    │  │   Skills 层     │  │  Commands 层       │        │
│  │  53 专用代理  │  │  200+ 工作流技能 │  │  69 指令（兼容层）  │        │
│  └───────┬───────┘  └────────┬────────┘  └─────────┬─────────┘        │
│          │                   │                      │                   │
│  ┌───────▼───────────────────▼──────────────────────▼─────────────┐    │
│  │                     核心运行时层                                  │    │
│  │   Hooks 自动化  │  Rules 规则引擎  │  MCP 协议集成              │    │
│  └───────┬─────────────────────────────────────┬───────────────────┘    │
│          │                                     │                        │
│  ┌───────▼──────────────────┐       ┌──────────▼──────────────────┐    │
│  │     CLI 工具层           │       │      外部生态集成层            │    │
│  │  ecc install/plan/doctor │       │  MCP Servers / APIs / Tools │    │
│  └───────┬──────────────────┘       └─────────────────────────────┘    │
│          │                                                              │
│  ┌───────▼──────────────────────────────────────────────────────┐      │
│  │                   数据存储层                                    │      │
│  │    SQLite 状态存储  │  Sessions  │  安装记录  │  学习记录       │      │
│  └──────────────────────────────────────────────────────────────┘      │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### 3.2 层次说明

| 层次 | 职责 | 核心组件 |
|------|------|---------|
| **用户层** | 开发者通过自然语言或命令与系统交互 | — |
| **Harness 层** | AI 代理框架，ECC 的宿主环境 | Claude Code, Codex, Cursor 等 |
| **Agents 层** | 53 个专用子代理，处理特定领域任务 | planner, architect, code-reviewer 等 |
| **Skills 层** | 200+ 工作流技能，主要功能界面 | tdd-workflow, security-review 等 |
| **Commands 层** | 69 个历史兼容指令 shim | /plan, /code-review 等 |
| **核心运行时层** | Hooks 自动化、Rules 规则引擎、MCP 集成 | hooks.json, rules/, mcp-configs/ |
| **CLI 工具层** | 安装、诊断、管理工具 | scripts/ecc.js |
| **外部生态层** | 外部 MCP 服务器、API、第三方工具 | Exa, Firecrawl, GitHub 等 |
| **数据存储层** | 状态持久化 | SQLite, JSON 文件 |

---

## 4. 核心层次架构

### 4.1 Agents 层架构

```
                    ┌─────────────────────────────────────────┐
                    │           Agents 层 (53 代理)            │
                    └─────────────────┬───────────────────────┘
                                      │
         ┌────────────────────────────┼─────────────────────────────┐
         │                            │                             │
┌────────▼──────────┐    ┌────────────▼───────────┐   ┌────────────▼──────────┐
│  规划与设计代理    │    │   代码质量代理           │   │   语言专项代理         │
├───────────────────┤    ├────────────────────────┤   ├───────────────────────┤
│ planner           │    │ code-reviewer          │   │ typescript-reviewer   │
│ architect         │    │ security-reviewer      │   │ python-reviewer       │
│ code-architect    │    │ tdd-guide              │   │ rust-reviewer         │
│ chief-of-staff    │    │ refactor-cleaner       │   │ go-reviewer           │
│                   │    │ performance-optimizer  │   │ java-reviewer         │
│                   │    │ type-design-analyzer   │   │ kotlin-reviewer       │
│                   │    │                        │   │ swift-reviewer        │
│                   │    │                        │   │ cpp-reviewer          │
└───────────────────┘    └────────────────────────┘   └───────────────────────┘

┌───────────────────┐    ┌────────────────────────┐   ┌───────────────────────┐
│  构建修复代理      │    │   专业领域代理           │   │   运维代理            │
├───────────────────┤    ├────────────────────────┤   ├───────────────────────┤
│ build-error-      │    │ database-reviewer      │   │ loop-operator         │
│   resolver        │    │ e2e-runner             │   │ harness-optimizer     │
│ rust-build-       │    │ security-reviewer      │   │ doc-updater           │
│   resolver        │    │ healthcare-reviewer    │   │ docs-lookup           │
│ go-build-         │    │ seo-specialist         │   │ code-explorer         │
│   resolver        │    │ network-troubleshooter │   │ pr-test-analyzer      │
│ java/kotlin/      │    │ gan-planner/generator  │   │ silent-failure-hunter │
│ cpp/swift/dart    │    │ a11y-architect         │   │ opensource-forker/    │
│ build-resolvers   │    │ fastapi-reviewer       │   │   packager/sanitizer  │
└───────────────────┘    └────────────────────────┘   └───────────────────────┘
```

### 4.2 Skills 层架构

```
                    ┌─────────────────────────────────────────┐
                    │         Skills 层 (200+ 技能)            │
                    └─────────────────┬───────────────────────┘
                                      │
    ┌─────────────────┬───────────────┼─────────────────┬────────────────┐
    │                 │               │                 │                │
┌───▼───────┐  ┌──────▼──────┐  ┌───▼───────┐  ┌─────▼──────┐  ┌──────▼──────┐
│ 通用开发   │  │ 语言框架    │  │ 专业领域  │  │ DevOps运维 │  │ AI/LLM专项 │
│ 技能域    │  │ 技能域      │  │ 技能域    │  │ 技能域     │  │ 技能域     │
├───────────┤  ├─────────────┤  ├───────────┤  ├────────────┤  ├────────────┤
│tdd-workflow│  │frontend-   │  │security-  │  │deployment- │  │eval-harness│
│coding-    │  │  patterns  │  │  review   │  │  patterns  │  │continuous- │
│ standards │  │backend-    │  │api-design │  │docker-     │  │  learning  │
│e2e-testing│  │  patterns  │  │database-  │  │  patterns  │  │deep-       │
│git-workflow│  │nextjs-     │  │  migration│  │git-workflow│  │  research  │
│security-  │  │  turbopack │  │hipaa-     │  │pm2         │  │exa-search  │
│  review   │  │react/vue/  │  │compliance │  │            │  │fal-ai-media│
│           │  │ nuxt/vite  │  │healthcare-│  │            │  │dmux-       │
│           │  │golang/rust │  │  patterns │  │            │  │ workflows  │
│           │  │ /python/.. │  │           │  │            │  │            │
└───────────┘  └─────────────┘  └───────────┘  └────────────┘  └────────────┘
```

### 4.3 Hooks 系统架构

```
┌──────────────────────────────────────────────────────────────┐
│                       Hooks 系统架构                          │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌───────────────────────────────────────────────────────┐  │
│  │                   事件触发点                            │  │
│  │  PreToolUse │ PostToolUse │ PreCompact │ Notification │  │
│  └──────────────────────┬────────────────────────────────┘  │
│                         │                                   │
│  ┌──────────────────────▼────────────────────────────────┐  │
│  │                 hooks.json 路由表                       │  │
│  │  匹配器: tool_name, event_type, context              │  │
│  └──────────────────────┬────────────────────────────────┘  │
│                         │                                   │
│    ┌────────────────────┼────────────────────┐             │
│    │                    │                    │             │
│  ┌─▼──────────────┐  ┌──▼──────────────┐  ┌─▼────────────┐│
│  │ 安全扫描 Hook  │  │ 代码格式化 Hook │  │ 通知 Hook   ││
│  │ (安全检查)     │  │ (Prettier/ESLint)│  │ (完成提醒)   ││
│  └────────────────┘  └─────────────────┘  └──────────────┘│
│                                                              │
│  ECC_HOOK_PROFILE 环境变量控制 Hook 激活组合                  │
└──────────────────────────────────────────────────────────────┘
```

### 4.4 安装系统架构

```
┌──────────────────────────────────────────────────────────────────────┐
│                        安装系统架构                                    │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                     入口层                                    │   │
│  │  install.sh (Linux/macOS)  │  install.ps1 (Windows)         │   │
│  │  npx 方式  │  /plugin install 方式                           │   │
│  └────────────────────────────┬─────────────────────────────────┘   │
│                               │                                     │
│  ┌────────────────────────────▼─────────────────────────────────┐   │
│  │                 scripts/install-apply.js                     │   │
│  │                     核心安装运行时                             │   │
│  │                                                              │   │
│  │  ┌─────────────────────────────────────────────────────┐    │   │
│  │  │              安装模式解析                             │    │   │
│  │  │  传统语言模式 │ Profile 模式 │ 显式模块模式           │    │   │
│  │  └─────────────────────────┬───────────────────────────┘    │   │
│  │                            │                                 │   │
│  │  ┌─────────────────────────▼───────────────────────────┐    │   │
│  │  │              Profile 系统                            │    │   │
│  │  │  minimal │ developer │ full │ custom                │    │   │
│  │  └─────────────────────────┬───────────────────────────┘    │   │
│  │                            │                                 │   │
│  │  ┌─────────────────────────▼───────────────────────────┐    │   │
│  │  │              Target 选择器                           │    │   │
│  │  │  claude │ codex │ cursor │ opencode │ gemini        │    │   │
│  │  └─────────────────────────┬───────────────────────────┘    │   │
│  │                            │                                 │   │
│  │  ┌─────────────────────────▼───────────────────────────┐    │   │
│  │  │              文件复制 + 状态写入                      │    │   │
│  │  │  SQLite 状态存储 (ecc-state.db)                     │    │   │
│  │  └─────────────────────────────────────────────────────┘    │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 5. 核心模块说明

### 5.1 Agents 模块

**定义：** 专用子代理是具有明确职责边界的 AI 代理实例，通过 `.claude-agent` 或 `agents/*.md` 文件定义其行为约束、能力边界和工作流程。

**分类体系：**

| 分类 | 代理名称 | 主要职责 |
|------|---------|---------|
| **规划设计** | planner, architect, code-architect, chief-of-staff | 需求分析、架构设计、任务分解 |
| **代码质量** | code-reviewer, tdd-guide, refactor-cleaner, type-design-analyzer | 代码审查、TDD、重构 |
| **安全** | security-reviewer, healthcare-reviewer | 漏洞检测、合规审查 |
| **语言专项** | typescript/python/rust/go/java/kotlin/swift/cpp-reviewer | 各语言最佳实践审查 |
| **构建修复** | build-error-resolver, *-build-resolver | 构建错误诊断与修复 |
| **测试** | e2e-runner, tdd-guide, pr-test-analyzer | 测试生成与执行 |
| **文档** | doc-updater, docs-lookup | 文档维护与查询 |
| **运维** | loop-operator, harness-optimizer, performance-optimizer | 系统运营优化 |
| **专业领域** | database-reviewer, seo-specialist, a11y-architect, gan-* | 特定领域专家 |
| **开源工作流** | opensource-forker, opensource-packager, opensource-sanitizer | 开源项目管理 |

**Agent 文件结构：**
```markdown
# [Agent Name]
## Role
[角色定义]
## Triggers  
[触发条件]
## Workflow
[工作流程步骤]
## Constraints
[约束条件]
```

### 5.2 Skills 模块

**定义：** 技能是可复用的工作流能力包，每个技能封装了特定领域的最佳实践、工作步骤和验证标准。

**技能域划分：**

| 技能域 | 代表技能 | 覆盖范围 |
|--------|---------|---------|
| **通用开发** | tdd-workflow, coding-standards, e2e-testing, git-workflow | 编码规范、测试、版本控制 |
| **前端** | frontend-patterns, nextjs-turbopack, design-system, vite-patterns | 前端框架与工具 |
| **后端** | backend-patterns, api-design, database-migrations | 服务端设计模式 |
| **语言生态** | golang-patterns, rust-patterns, python-patterns, kotlin-patterns | 12+ 语言最佳实践 |
| **安全合规** | security-review, hipaa-compliance, django-security | 安全审计与合规 |
| **AI/LLM** | eval-harness, deep-research, continuous-learning, dmux-workflows | AI 辅助开发 |
| **DevOps** | deployment-patterns, docker-patterns, ci/cd | 基础设施与运维 |
| **专业领域** | healthcare-*, finance-*, customs-* | 行业特定知识 |

**技能文件结构：**
```markdown
# [Skill Name]
## Context
[适用场景]
## Prerequisites  
[前置条件]
## Steps
[执行步骤]
## Verification
[验证方法]
## Examples
[使用示例]
```

### 5.3 Commands 模块

**定义：** Commands 是 ECC v1.x 时代的斜杠命令系统，在 v2.0 中作为历史兼容层保留，为已有工作流提供向后兼容的入口。

**架构说明：**
- `commands/` 中的文件是 skills 的**入口 shim**，不包含业务逻辑
- 每个 command 本质上是调用对应 skill 或 agent 的路由
- 新功能应直接在 `skills/` 中实现，而不是添加新 command

**关键命令分类：**

| 分类 | 命令 | 对应能力 |
|------|------|---------|
| **规划** | /plan, /multi-plan | 调用 planner agent |
| **开发** | /feature-dev, /prp-implement | 调用 tdd-guide + code-reviewer |
| **代码审查** | /code-review, /review-pr | 调用 code-reviewer agent |
| **测试** | /test-coverage, /rust-test 等 | 调用各语言测试框架 |
| **构建** | /build-fix, /rust-build 等 | 调用 build-error-resolver |
| **运维** | /loop-start, /loop-status, /pm2 | 运维工具调用 |
| **会话管理** | /save-session, /resume-session, /sessions | 会话持久化 |
| **Hookify** | /hookify, /hookify-configure | Hook 管理 |
| **ECC 管理** | /auto-update, /prune, /quality-gate | ECC 自身维护 |

### 5.4 Hooks 模块

**定义：** Hooks 是事件驱动的自动化触发器，在特定工具调用或生命周期事件时自动执行预定义操作。

**核心配置文件：** `hooks/hooks.json`

**触发时机：**

| 事件类型 | 触发时机 | 典型用途 |
|---------|---------|---------|
| `PreToolUse` | 工具调用前 | 安全检查、权限验证 |
| `PostToolUse` | 工具调用后 | 格式化、测试触发 |
| `PreCompact` | 上下文压缩前 | 状态保存 |
| `Notification` | 长任务完成通知 | 用户提醒 |
| `Stop` | 代理停止时 | 清理工作 |

**Hook Profile 系统：**
通过 `ECC_HOOK_PROFILE` 环境变量控制激活哪些 Hook 组合：
```bash
# 激活特定 profile
export ECC_HOOK_PROFILE=security  # 安全扫描模式
export ECC_HOOK_PROFILE=minimal   # 最小化模式
export ECC_HOOK_PROFILE=full      # 全功能模式
```

### 5.5 Rules 模块

**定义：** Rules 是始终生效的行为约束规则，注入到 AI 代理的系统提示中，确保代理始终遵循最佳实践。

**规则目录结构：**
```
rules/
├── common/          # 通用规则（所有语言）
│   ├── security.md  # 安全规范
│   ├── testing.md   # 测试要求
│   └── coding.md    # 编码规范
├── typescript/      # TypeScript 专项规则
├── python/          # Python 专项规则
├── rust/            # Rust 专项规则
├── go/              # Go 专项规则
├── java/            # Java 专项规则
├── kotlin/          # Kotlin 专项规则
├── cpp/             # C/C++ 专项规则
└── ...              # 其他语言
```

### 5.6 MCP 集成模块

**定义：** Model Context Protocol (MCP) 是 Anthropic 定义的 AI 工具集成协议，ECC 通过 `mcp-configs/` 提供 14 套预配置的 MCP 服务器集成。

**核心 MCP 集成：**

| MCP 服务器 | 能力 | 使用场景 |
|-----------|------|---------|
| Exa | 神经网络搜索引擎 | 代码搜索、技术研究 |
| Firecrawl | Web 内容抓取 | 文档获取、API 研究 |
| GitHub | GitHub API 集成 | PR 管理、代码分析 |
| Context7 | 实时文档查询 | API 参考、框架文档 |
| SQLite | 本地数据库 | 状态存储、学习记录 |
| Browser | 浏览器自动化 | E2E 测试、Web 验证 |
| fal.ai | AI 媒体生成 | 图像/视频/音频生成 |

---

## 6. 模块交互关系

### 6.1 任务执行数据流

```
用户输入 "实现登录功能"
        │
        ▼
AI 框架 (Claude Code)
        │
        ├─── 识别到复杂任务
        │         │
        │         ▼
        │    planner agent
        │    ┌─────────────────────────┐
        │    │ 1. 分析需求              │
        │    │ 2. 制定实施计划          │
        │    │ 3. 识别依赖和风险        │
        │    │ 4. 分解为子任务          │
        │    └────────────┬────────────┘
        │                 │
        ├─── 调用 tdd-guide skill
        │         │
        │         ▼
        │    TDD 工作流
        │    ┌─────────────────────────┐
        │    │ RED: 先写测试           │
        │    │ GREEN: 最小实现          │
        │    │ REFACTOR: 优化          │
        │    └────────────┬────────────┘
        │                 │
        ├─── 调用 code-reviewer agent
        │         │
        │         ▼
        │    代码审查
        │    ┌─────────────────────────┐
        │    │ 检查代码质量            │
        │    │ 安全扫描                │
        │    │ 性能评估                │
        │    └────────────┬────────────┘
        │                 │
        └─── PostToolUse Hook 触发
                  │
                  ▼
             格式化 + 通知
```

### 6.2 代理编排模式

**顺序编排（Sequential）：**
```
planner → tdd-guide → code-reviewer → security-reviewer → doc-updater
```

**并行编排（Parallel）：**
```
typescript-reviewer ─┐
security-reviewer   ─┼──→ 汇总结果 → 修复建议
performance-optim.  ─┘
```

**递归编排（Recursive）：**
```
chief-of-staff → 分配子任务 → 各专项代理 → 结果聚合 → chief-of-staff
```

### 6.3 Skills 与 Agents 协作关系

```
Skill (工作流定义)          Agent (执行主体)
┌──────────────────┐        ┌──────────────────┐
│  tdd-workflow    │──调用──│  tdd-guide       │
│  security-review │──调用──│  security-reviewer│
│  e2e-testing     │──调用──│  e2e-runner      │
│  api-design      │──调用──│  architect       │
└──────────────────┘        └──────────────────┘
        │                           │
        └──────────┬────────────────┘
                   │
                   ▼
          命令层 (Commands)
         作为统一入口 shim
```

---

## 7. 技术选型

### 7.1 运行时技术

| 组件 | 技术选型 | 版本要求 | 选型理由 |
|------|---------|---------|---------|
| **CLI 运行时** | Node.js | ≥18.0 | 跨平台兼容、npm 生态丰富 |
| **包管理** | npm / yarn | — | 广泛兼容性 |
| **状态存储** | SQLite (better-sqlite3) | — | 零依赖、本地优先 |
| **Shell 脚本** | Bash + PowerShell | — | 跨平台支持 |
| **ECC 2.0 核心** | Rust | stable | 高性能、内存安全 |

### 7.2 AI 协议与集成

| 协议/规范 | 用途 | 支持状态 |
|---------|------|---------|
| **Claude Code API** | 主要宿主框架 | ✅ 完整支持 |
| **MCP (Model Context Protocol)** | 工具集成协议 | ✅ 14 套配置 |
| **OpenAI Codex** | 兼容框架 | ✅ 支持 |
| **Cursor API** | 兼容框架 | ✅ 支持 |
| **OpenCode** | 兼容框架 | ✅ 支持 |

### 7.3 代码规范工具

| 工具 | 配置文件 | 用途 |
|------|---------|------|
| **ESLint** | `eslint.config.js` | JavaScript/TypeScript 静态分析 |
| **Prettier** | `.prettierrc` | 代码格式化 |
| **Commitlint** | `commitlint.config.js` | 提交信息规范 |
| **markdownlint** | `.markdownlint.json` | Markdown 格式检查 |

---

## 8. 安装与部署架构

### 8.1 安装 Profile 体系

```
┌─────────────────────────────────────────────────────────┐
│                    安装 Profile 体系                     │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  minimal profile           developer profile            │
│  ┌─────────────────┐       ┌─────────────────────────┐  │
│  │ • 核心 Skills   │       │ • 所有 minimal 内容     │  │
│  │ • 基础 Rules    │       │ • 语言专项 Rules        │  │
│  │ • 核心 Agents  │       │ • 完整 Agents 集合      │  │
│  │ • 无 Hooks     │       │ • 基础 Hooks            │  │
│  └─────────────────┘       │ • MCP 配置              │  │
│                            └─────────────────────────┘  │
│                                                         │
│  full profile                                           │
│  ┌─────────────────────────────────────────────────┐   │
│  │ • 所有 developer 内容                           │   │
│  │ • 完整 Hooks 套件（含 hooks-runtime）           │   │
│  │ • 所有 MCP 配置                                │   │
│  │ • Dashboard GUI                               │   │
│  │ • 所有 200+ Skills                            │   │
│  └─────────────────────────────────────────────────┘   │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 8.2 多平台部署架构

```
┌──────────────────────────────────────────────────────────────┐
│                      ECC 多平台部署                            │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ECC 源仓库                                                   │
│       │                                                      │
│       ├──→ ~/.claude/           (Claude Code target)         │
│       │    ├── agents/                                       │
│       │    ├── commands/                                     │
│       │    ├── hooks/                                        │
│       │    └── settings.json                                 │
│       │                                                      │
│       ├──→ ~/.codex/            (Codex target)               │
│       │    ├── skills/                                       │
│       │    └── rules/                                        │
│       │                                                      │
│       ├──→ ~/.cursor/rules/     (Cursor target)              │
│       │    └── rules/                                        │
│       │                                                      │
│       └──→ Project-local/       (项目级安装)                  │
│            ├── .claude/                                      │
│            └── [project-specific config]                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. 扩展架构

### 9.1 新 Skill 扩展点

```
skills/
└── my-custom-skill/
    ├── skill.md          # 技能定义文件
    └── examples/         # 使用示例（可选）
```

按照 ECC skill 模板规范编写 `skill.md`，执行 `ecc install` 后自动集成。

### 9.2 新 Agent 扩展点

在 `agents/` 目录下创建 `my-agent.md`，定义代理角色、触发条件、工作流程和约束条件。

### 9.3 自定义 Hook 扩展点

在 `hooks/hooks.json` 中添加新的 hook 规则，支持匹配特定工具名称、事件类型和上下文条件。

### 9.4 MCP 服务器扩展点

在 `mcp-configs/` 中添加新的 MCP 服务器配置文件，格式遵循 MCP JSON Schema 规范。

---

## 10. 安全架构

### 10.1 多层安全机制

```
┌────────────────────────────────────────────────────────┐
│                    ECC 安全架构                         │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Layer 1: 规则层安全（Rules Security）                  │
│  ┌────────────────────────────────────────────────┐   │
│  │ rules/common/security.md                       │   │
│  │ • 禁止硬编码密钥/密码/令牌                       │   │
│  │ • 强制参数化查询（防 SQL 注入）                  │   │
│  │ • 强制输入验证（系统边界处）                     │   │
│  │ • XSS 防护（HTML 内容必须消毒）                  │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  Layer 2: 代理层安全（Agent Security）                  │
│  ┌────────────────────────────────────────────────┐   │
│  │ security-reviewer agent                        │   │
│  │ • 提交前漏洞扫描                               │   │
│  │ • CRITICAL/HIGH 问题阻断                       │   │
│  │ • 密钥轮换建议                                 │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  Layer 3: Hook 层安全（Hook Security）                  │
│  ┌────────────────────────────────────────────────┐   │
│  │ PreToolUse Hook                                │   │
│  │ • 工具调用前安全检查                            │   │
│  │ • 危险操作拦截                                 │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
│  Layer 4: 安装层安全（Install Security）                │
│  ┌────────────────────────────────────────────────┐   │
│  │ AgentShield（v1.6+ 集成）                      │   │
│  │ • 安装包完整性验证                             │   │
│  │ • 供应链安全检查                               │   │
│  └────────────────────────────────────────────────┘   │
│                                                        │
└────────────────────────────────────────────────────────┘
```

### 10.2 凭据管理规范

- **禁止**：代码中任何形式的硬编码密钥
- **要求**：所有密钥通过环境变量或密钥管理系统传入
- **验证**：启动时校验必需密钥是否存在
- **轮换**：发现暴露密钥立即轮换

### 10.3 数据安全

- SQLite 状态库仅存储安装元数据，不存储用户代码
- MCP 配置不包含实际凭据（使用环境变量引用）
- `.gitignore` 和 `.npmignore` 确保敏感配置不被意外发布

---

## 附录

### A. 版本演进路线图

| 版本 | 时间 | 核心里程碑 |
|------|------|----------|
| v1.0 | 2025-06 | 初始黑客马拉松版本 |
| v1.4.0 | 2026-02 | 多语言规则、交互式安装向导 |
| v1.6.0 | 2026-02 | AgentShield 安全审计、GitHub Marketplace |
| v1.7.0 | 2026-02 | Codex 支持、frontend-slides skill |
| v1.8.0 | 2026-03 | Harness 优先发布、Hook 运行时控制 |
| v1.9.0 | 2026-03 | 选择性安装架构、SQLite 状态存储 |
| v2.0.0-rc.1 | 2026-04 | Dashboard GUI、ECC 2.0 Alpha (Rust) |

### B. 术语表

| 术语 | 定义 |
|------|------|
| **Harness** | AI 代理框架宿主环境（Claude Code、Codex 等） |
| **Agent** | 专用子代理，具有明确职责的 AI 代理实例 |
| **Skill** | 可复用工作流技能包 |
| **Command** | 历史兼容斜杠命令（v2.0 中为 shim） |
| **Hook** | 事件驱动自动化触发器 |
| **Profile** | 安装配置集（minimal/developer/full） |
| **MCP** | Model Context Protocol，AI 工具集成协议 |
| **Target** | 安装目标平台（claude/codex/cursor 等） |
| **Shim** | 向后兼容的薄包装层 |
