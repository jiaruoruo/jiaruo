# Everything Claude Code (ECC) 应用教程手册

> **版本：** 2.0.0-rc.1  
> **文档版本：** 1.0.0  
> **编写日期：** 2026-05-12  
> **适用范围：** ECC 新用户、日常使用者、高级用户

---

## 目录

1. [快速入门（5分钟上手）](#1-快速入门5分钟上手)
2. [安装指南](#2-安装指南)
3. [基础使用入门](#3-基础使用入门)
4. [Agents 使用指南](#4-agents-使用指南)
5. [Skills 使用指南](#5-skills-使用指南)
6. [Commands 使用指南](#6-commands-使用指南)
7. [Hooks 配置指南](#7-hooks-配置指南)
8. [MCP 集成使用](#8-mcp-集成使用)
9. [典型场景实战教程](#9-典型场景实战教程)
10. [会话管理与持久化](#10-会话管理与持久化)
11. [ECC 维护管理](#11-ecc-维护管理)
12. [故障排除手册](#12-故障排除手册)
13. [常见问题解答（FAQ）](#13-常见问题解答faq)

---

## 1. 快速入门（5分钟上手）

### 1.1 ECC 是什么？

ECC（Everything Claude Code）是一个**AI 代理增强框架**，为 Claude Code、Codex、Cursor 等 AI 编码工具注入专业化的工程师能力。

简单来说，安装 ECC 后，你的 AI 编码助手将从"通用助手"升级为"专业工程师团队"：

- 🎯 **任务规划师**：帮你分解复杂任务，制定实施计划
- 🔍 **代码审查员**：自动检查代码质量、安全漏洞
- 🧪 **TDD 向导**：强制遵循测试驱动开发流程
- 🔒 **安全审查员**：检测密钥泄露、注入漏洞等安全问题
- 🌐 **12+ 语言专家**：TypeScript、Python、Rust、Go 等语言的专项审查

### 1.2 一分钟安装

**macOS / Linux：**
```bash
git clone https://github.com/jiaruoruo/everything-claude-code.git
cd everything-claude-code
./install.sh --profile developer --target claude
```

**Windows（PowerShell）：**
```powershell
git clone https://github.com/jiaruoruo/everything-claude-code.git
cd everything-claude-code
.\install.ps1 --profile developer --target claude
```

**通过 npm（推荐）：**
```bash
npx everything-claude-code install --profile developer --target claude
```

### 1.3 验证安装成功

安装完成后，在 Claude Code 中输入：
```
我需要实现一个用户登录功能
```

如果看到 ECC 自动调用 `planner` 代理制定实施计划，说明安装成功！

---

## 2. 安装指南

### 2.1 系统要求

| 要求 | 最低版本 | 推荐版本 |
|------|---------|---------|
| Node.js | 18.0 | 20.x LTS |
| npm | 8.0 | 最新 |
| Git | 2.x | 最新 |
| 操作系统 | Windows 10 / macOS 12 / Ubuntu 20.04 | 最新 LTS |

验证 Node.js 版本：
```bash
node --version  # 应显示 v18.0.0 或更高
```

### 2.2 安装方式详解

#### 方式一：插件安装（Claude Code 插件市场，最推荐）

在 Claude Code 中执行：
```
/plugin marketplace add ecc
/plugin install ecc@ecc
```

优点：自动更新，最简单，无需 Git 克隆。

#### 方式二：Shell 脚本安装

```bash
# 克隆仓库
git clone https://github.com/jiaruoruo/everything-claude-code.git
cd everything-claude-code

# Linux/macOS
./install.sh --profile developer --target claude

# Windows PowerShell
.\install.ps1 --profile developer --target claude
```

#### 方式三：npx 安装（无需克隆）

```bash
# 直接通过 npx 运行
npx everything-claude-code install --profile developer --target claude
```

#### 方式四：全局 CLI 安装

```bash
# 安装 ECC CLI 为全局命令
npm install -g everything-claude-code

# 然后使用 ecc 命令
ecc install --profile developer --target claude
```

### 2.3 安装 Profile 选择

根据你的需求选择合适的安装 Profile：

#### `minimal` - 最小安装（适合快速体验）

包含内容：
- 核心 Skills：tdd-workflow、coding-standards、security-review、git-workflow
- 基础规则：安全、测试、编码规范
- 核心 Agents：planner、code-reviewer、build-error-resolver
- **不包含** Hooks 和 MCP 配置

```bash
./install.sh --profile minimal --target claude
```

#### `developer` - 开发者安装（推荐日常使用）

包含 minimal 的所有内容，额外增加：
- 完整 Agents 集合（含安全、测试、语言专项）
- E2E 测试、后端/前端模式 Skills
- 安全扫描和格式化 Hooks
- Context7 和 SQLite MCP 配置

```bash
./install.sh --profile developer --target claude
```

#### `full` - 完整安装（高级用户）

包含所有 200+ Skills、53 个 Agents、完整 Hooks 套件和 14 套 MCP 配置。

```bash
./install.sh --profile full --target claude
```

### 2.4 安装目标平台选择

| `--target` 值 | 适用平台 | 说明 |
|-------------|---------|------|
| `claude` | Claude Code | 默认推荐 |
| `codex` | OpenAI Codex | 合并到 AGENTS.md |
| `cursor` | Cursor IDE | 合并到 .cursorrules |
| `opencode` | OpenCode | 支持 |
| `gemini` | Google Gemini | 支持 |

### 2.5 语言专项安装（传统模式）

如果你只需要特定语言的支持：

```bash
# TypeScript 项目
./install.sh typescript

# Python 项目
./install.sh python

# Rust 项目
./install.sh rust

# Go 项目
./install.sh golang

# 多语言项目
./install.sh typescript python golang

# 全部语言
./install.sh full
```

### 2.6 查看安装计划（干跑模式）

安装前先预览将要安装的内容：
```bash
# 查看安装计划（不实际执行）
ecc plan --profile developer --target claude

# 查看可用组件目录
ecc catalog
```

### 2.7 安装后验证

```bash
# 检查安装状态
ecc doctor

# 查看已安装组件
ecc list-installed

# 查看安装状态摘要
ecc status
```

---

## 3. 基础使用入门

### 3.1 ECC 的工作原理

ECC 安装后会在你的 AI 代理框架（Claude Code 等）中注入：
1. **Agent 文件**（`~/.claude/agents/`）：让 Claude Code 知道有哪些专用代理可用
2. **Skill 文件**（通过 CLAUDE.md 引用）：提供专业工作流程指导
3. **Rule 文件**（`~/.claude/rules/`）：始终生效的编码规范约束
4. **Hook 配置**（`~/.claude/settings.json`）：自动化触发器

你**不需要主动调用** ECC，它会在合适的时机自动激活。

### 3.2 ECC 的三种工作模式

#### 模式一：自动触发（推荐，无感使用）

当你向 Claude Code 提出请求时，ECC 自动判断应该调用哪个 Agent 或 Skill：

```
你：帮我实现一个购物车功能

Claude Code (ECC增强版) 自动响应：
→ 识别为复杂任务
→ 自动调用 planner agent 分解任务
→ 调用 tdd-guide skill 指导 TDD 开发
→ 代码完成后自动触发 code-reviewer
```

#### 模式二：命令触发（精确控制）

通过斜杠命令明确调用特定工作流：

```
/plan 实现用户登录系统      # 调用规划工作流
/code-review               # 审查当前代码
/feature-dev 添加搜索功能   # 完整功能开发流
/build-fix                 # 修复构建错误
```

#### 模式三：手动触发 Agent

直接在对话中要求使用特定 Agent：

```
你：使用 security-reviewer 检查这段代码的安全问题
你：请用 planner 帮我制定重构计划
你：用 typescript-reviewer 审查我的 TypeScript 代码
```

### 3.3 理解 ECC 输出格式

ECC 的各类 Agent 都有标准化的输出格式：

**代码审查输出示例：**
```
## 代码审查报告

### ⛔ CRITICAL（必须修复）
- [行 42] 硬编码 API 密钥: `const API_KEY = "sk-xxx..."`
  → 修复：使用 process.env.API_KEY

### ⚠️ HIGH（强烈建议）
- [行 78] 缺少 SQL 参数化查询
  → 修复：使用 db.query('SELECT * FROM users WHERE id = ?', [userId])

### 💡 MEDIUM（建议）
- [行 95] 函数超过 50 行（当前 67 行）
  → 建议：提取 validateInput() 函数

### ✅ 优点
- 错误处理完整
- 命名规范一致
- 测试覆盖率 82%
```

---

## 4. Agents 使用指南

### 4.1 规划类 Agents

#### `planner` — 任务规划师

**适用场景：** 新功能开发、架构重构、多步骤复杂任务

```
你：我需要为博客系统添加评论功能，包括评论树状结构和点赞

planner 会输出：
═══════════════════════════════
实施计划：博客评论系统

阶段 1：数据模型设计
  任务 1.1：设计 Comment Schema（含自引用关系）
  任务 1.2：设计 Like Schema（多态关联）
  预估：30 分钟

阶段 2：API 设计与实现
  任务 2.1：GET /posts/:id/comments（树状）
  任务 2.2：POST /posts/:id/comments
  任务 2.3：POST /comments/:id/like
  预估：2 小时

阶段 3：前端组件
  任务 3.1：CommentTree 组件
  任务 3.2：CommentItem 组件（含点赞）
  预估：1.5 小时

依赖关系：2.1 需要 1.1 完成；3.1 需要 2.x 完成
风险：树状查询可能有 N+1 问题，建议使用递归 CTE
═══════════════════════════════
```

**使用技巧：**
- 越详细的需求描述，规划越精准
- 可以指定技术栈：`使用 Next.js + PostgreSQL 实现...`
- 可以设置约束：`需要在 3 天内完成...`

#### `architect` — 系统架构师

**适用场景：** 系统设计决策、选择技术方案、架构评审

```
你：我们的系统需要支持百万级用户的实时通知，应该怎么设计？

architect 会提供：
- 技术方案对比（WebSocket vs SSE vs Long Polling）
- 推荐方案及理由
- 系统组件图
- 关键设计决策清单
- 潜在瓶颈和扩展策略
```

### 4.2 代码质量类 Agents

#### `code-reviewer` — 代码审查员

**适用场景：** 提交代码前、完成功能后、PR 合并前

```
你：请审查 src/auth/login.ts

# 或者让它自动检查当前工作区
你：审查我刚刚写的代码
```

**审查维度（自动全覆盖）：**
- ✅ 函数大小（< 50 行）
- ✅ 文件大小（< 800 行）
- ✅ 嵌套深度（≤ 4 层）
- ✅ 命名规范
- ✅ 错误处理
- ✅ 不可变性原则
- ✅ 硬编码值检测

#### `tdd-guide` — TDD 向导

**适用场景：** 每次编写新功能时

```
你：使用 TDD 实现一个 validateEmail 函数

tdd-guide 会指导你：
1. 先问：测试了哪些情况？
2. 协助编写测试用例（RED）
3. 提示写最小实现（GREEN）
4. 建议重构方向（REFACTOR）
5. 检查覆盖率是否 ≥ 80%
```

**TDD 三步法口诀：**
- **红**：先写测试，运行应该失败
- **绿**：写最小代码使测试通过
- **重构**：改善代码，测试仍然通过

#### `security-reviewer` — 安全审查员

**关键规则：** 遇到 CRITICAL 级别问题，必须立即停止开发并修复！

```
你：安全检查 src/api/payment.ts

# 常见发现示例：
⛔ CRITICAL: 硬编码 Stripe 密钥
   → 立即将密钥移到环境变量并轮换已暴露的密钥

⛔ CRITICAL: SQL 注入漏洞（第 45 行）
   → 改用参数化查询

⚠️ HIGH: 缺少 CSRF Token 验证
   → 添加 csrf-protection 中间件
```

### 4.3 语言专项 Agents

#### TypeScript 专项

```
你：typescript-reviewer 帮我检查这个 React 组件的类型设计

检查内容包括：
- 类型是否过于宽泛（避免 any）
- 泛型使用是否合理
- 可选属性是否都有默认值处理
- async 函数的错误类型处理
- Props 类型是否明确
```

#### Python 专项

```
你：python-reviewer 审查 api/views.py

检查内容包括：
- PEP 8 规范
- 类型提示完整性
- 函数文档字符串
- Django 安全最佳实践（如果是 Django 项目）
```

#### Rust 专项

```
你：rust-reviewer 检查 src/lib.rs

检查内容包括：
- 所有权和借用是否正确
- 错误处理（Result/Option 的正确使用）
- 不安全代码（unsafe block）的合理性
- 性能问题（不必要的 clone）
```

### 4.4 构建修复类 Agents

**遇到构建错误时，直接粘贴错误信息：**

```
你：构建失败，错误信息如下：
error[E0382]: borrow of moved value: `user`
  --> src/main.rs:15:20
   |
12 |     let user = get_user(id);
   |         ---- move occurs because `user` has type `User`
15 |     process(user);
   |             ^^^^ value borrowed here after move

# rust-build-resolver 会：
# 1. 分析所有权问题
# 2. 解释错误原因
# 3. 提供修复方案（clone、引用、或重构）
# 4. 验证修复后没有新错误
```

### 4.5 专业领域 Agents

#### `database-reviewer` — 数据库专家

```
你：帮我检查这个 SQL 查询的性能问题

SELECT u.*, p.* FROM users u
JOIN posts p ON u.id = p.user_id
WHERE u.status = 'active'

# 会检查：
# - 是否有 N+1 查询问题
# - 缺少索引的字段
# - SELECT * 的性能影响
# - 是否可以使用子查询优化
```

#### `e2e-runner` — E2E 测试专家

```
你：为用户登录流程编写 Playwright E2E 测试

e2e-runner 会生成：
1. tests/e2e/auth/login.spec.ts（使用 Page Object Model）
2. pages/LoginPage.ts（页面对象）
3. playwright.config.ts（测试配置）
4. CI/CD 集成配置
```

---

## 5. Skills 使用指南

### 5.1 Skills 的激活方式

Skills 是工作流定义，可以通过以下方式激活：

**方式 1：自然语言描述任务（最常用）**
```
你：我要实现一个 REST API 接口

→ ECC 自动匹配 api-design skill 和 tdd-workflow skill
```

**方式 2：直接引用技能名称**
```
你：使用 tdd-workflow 开发用户注册功能
你：按照 coding-standards skill 检查我的代码
```

**方式 3：通过命令触发对应 Skill**
```
/feature-dev 实现购物车  → 触发 tdd-workflow + security-review skills
/code-review            → 触发 coding-standards skill
```

### 5.2 核心 Skills 详解

#### `tdd-workflow` — 测试驱动开发工作流

这是最重要的 Skill，**强烈建议每次开发新功能都使用**。

**完整工作流示例：**

```
步骤 1（RED）：先写测试
你：我要实现 calculateDiscount(price, discountCode) 函数

tdd-workflow 指导：
"先告诉我测试场景：
1. 有效折扣码（如 SAVE10 = 10% off）
2. 无效折扣码
3. 价格为 0 的边界情况
4. 折扣码过期情况"

→ 你写测试，运行，看到红色失败

步骤 2（GREEN）：最小实现
"现在写最小化的实现让测试通过"

→ 你写实现，运行，看到绿色通过

步骤 3（REFACTOR）：重构优化
"检查覆盖率，提取 isValidCode 辅助函数，
处理边界情况"

→ 重构后测试仍然通过，覆盖率 ≥ 80%
```

#### `security-review` — 安全审查工作流

**在以下情况务必使用：**
- 处理用户认证/授权
- 涉及数据库查询
- 处理文件上传
- 处理支付信息
- 任何涉及外部输入的地方

```
你：我刚完成了用户登录 API，请用 security-review skill 检查

安全检查流程：
□ 密码是否正确哈希（bcrypt/argon2）
□ SQL 查询是否参数化
□ 是否限制失败登录次数（速率限制）
□ JWT 令牌是否安全配置
□ 错误消息是否泄露用户信息
□ 是否有 CSRF 保护
```

#### `coding-standards` — 编码规范

在代码审查前使用，确保符合团队规范：

```
你：检查 src/services/ 下的代码是否符合编码规范

coding-standards 检查：
✅ 文件大小（< 800 行）
✅ 函数大小（< 50 行）
✅ 嵌套深度（≤ 4 层）
✅ 命名规范（camelCase/PascalCase 等）
❌ src/services/user.ts 第 234 行：函数过长（87 行）
❌ src/services/order.ts 第 78 行：嵌套 5 层
```

#### `git-workflow` — Git 工作流

确保提交信息规范和 PR 质量：

```
你：帮我写这次提交的提交信息（新增了用户登录功能，修复了 JWT 验证 bug）

git-workflow 建议：
feat(auth): implement user login with JWT
fix(auth): resolve JWT validation edge case on token expiry

# 更复杂的多文件修改：
feat(auth): add user login system

- Implement POST /auth/login endpoint
- Add JWT generation and validation
- Add bcrypt password hashing
- Add rate limiting (5 attempts per 15 min)
- Add comprehensive test coverage (87%)

Closes #123
```

#### `e2e-testing` — E2E 测试工作流

为关键用户流程编写端到端测试：

```
你：为"用户注册→登录→修改密码"流程编写 E2E 测试

e2e-testing skill 会指导：
1. 安装 Playwright：npm install @playwright/test
2. 创建页面对象模型（POM）
3. 编写测试场景
4. 配置 CI/CD 集成
5. 处理测试数据隔离
```

### 5.3 框架专项 Skills

#### 前端框架

```
# Next.js 项目
你：按照 nextjs-turbopack skill 配置项目

# React 组件开发
你：使用 frontend-patterns skill 审查这个 React 组件

# Vue/Nuxt 项目
你：使用 nuxt4-patterns 检查我的 Nuxt 配置
```

#### 后端框架

```
# Node.js/Express
你：使用 backend-patterns skill 设计用户服务

# FastAPI
你：使用 fastapi-patterns 审查我的 FastAPI 路由

# Django
你：使用 django-patterns + django-security 检查视图层

# Spring Boot
你：使用 springboot-patterns 审查我的 Controller 层
```

#### 数据库

```
# PostgreSQL
你：使用 postgres-patterns 优化这个查询

# 数据库迁移
你：使用 database-migrations skill 帮我写迁移脚本
```

### 5.4 AI/LLM 专项 Skills

#### `deep-research` — 深度研究

```
你：使用 deep-research skill 调研"React 状态管理库的最新对比（2026）"

deep-research 会：
1. 使用 Firecrawl MCP 抓取相关文章
2. 使用 Exa MCP 搜索最新资料
3. 综合分析，生成对比报告
4. 附上信息来源
```

#### `dmux-workflows` — 多代理并行

```
你：使用 dmux-workflows 并行实现前端和后端

dmux 会在多个终端面板中启动：
- Panel 1: frontend-agent（实现 React 页面）
- Panel 2: backend-agent（实现 API）
- Panel 3: test-agent（编写集成测试）
所有代理并行工作，然后合并结果
```

#### `eval-harness` — AI 评估框架

```
你：使用 eval-harness 评估我的 LLM 提示词效果

eval-harness 会：
1. 定义评估指标
2. 构建测试数据集
3. 运行基准测试
4. 分析改进方向
```

---

## 6. Commands 使用指南

### 6.1 命令速查表

在 Claude Code 中直接输入以下命令：

#### 规划与开发

```bash
/plan [功能描述]          # 生成实施计划
/feature-dev [功能描述]   # 完整 TDD 功能开发
/multi-plan [描述]        # 多模块并行规划
```

#### 代码质量

```bash
/code-review              # 审查当前代码
/review-pr                # 审查 PR 变更
/quality-gate             # 质量门控检查（阻断级）
/refactor-clean           # 重构清理
```

#### 测试

```bash
/test-coverage            # 提升测试覆盖率
/rust-test                # Rust 测试编写
/go-test                  # Go 测试编写
/kotlin-test              # Kotlin 测试编写
```

#### 构建修复

```bash
/build-fix                # 通用构建错误修复
/rust-build               # Rust 构建修复
/go-build                 # Go 构建修复
/kotlin-build             # Kotlin/Gradle 构建修复
/cpp-build                # C/C++ 构建修复
/flutter-build            # Flutter 构建修复
/gradle-build             # Gradle 构建修复
```

#### 语言审查

```bash
/rust-review              # Rust 代码审查
/go-review                # Go 代码审查
/cpp-review               # C/C++ 代码审查
/python-review            # Python 代码审查
/kotlin-review            # Kotlin 代码审查
/flutter-review           # Flutter 代码审查
/fastapi-review           # FastAPI 代码审查
```

#### 会话管理

```bash
/save-session             # 保存当前工作状态
/resume-session           # 恢复上次工作状态
/sessions                 # 查看所有会话列表
/checkpoint               # 创建工作检查点
```

#### 自主循环

```bash
/loop-start [任务]        # 启动自主代理循环
/loop-status              # 查看循环状态
/santa-loop               # 自主测试修复循环
```

#### ECC 管理

```bash
/auto-update              # 更新 ECC 到最新版
/prune                    # 清理未使用组件
/hookify                  # 交互式配置 Hooks
/hookify-list             # 查看所有 Hook
/hookify-configure        # 配置指定 Hook
```

#### PRD/文档工作流

```bash
/prp-prd [功能]           # 生成 PRD 文档
/prp-plan                 # 基于 PRD 生成实施计划
/prp-implement            # PRD 驱动的代码实现
/prp-pr                   # 生成 PR 描述
/prp-commit               # 生成标准提交信息
/update-docs              # 同步更新文档
/update-codemaps          # 更新代码地图
```

#### 工具集成

```bash
/jira [任务]              # Jira 任务操作
/pm2 [命令]               # PM2 进程管理
/setup-pm                 # 配置项目管理工具
/model-route              # 智能路由 AI 模型选择
```

### 6.2 命令使用最佳实践

**💡 提供上下文越多，效果越好：**

```bash
# 一般：
/plan 添加搜索功能

# 更好：
/plan 为电商系统添加商品搜索功能，
      使用 Elasticsearch，
      需要支持全文搜索、过滤和排序，
      项目是 Node.js + TypeScript
```

**💡 链式使用命令：**

```bash
# 完整功能开发流程
1. /plan 设计购物车功能
2. /feature-dev 实现购物车
3. /code-review
4. /review-pr
5. /prp-pr 生成 PR 描述
```

---

## 7. Hooks 配置指南

### 7.1 什么是 Hooks？

Hooks 是自动触发的操作，在你的代码操作前后自动执行。例如：
- **写文件前**：自动扫描是否包含密钥
- **写文件后**：自动运行 Prettier 格式化
- **任务完成**：发送桌面通知

### 7.2 配置 Hook Profile

```bash
# 在 ~/.bashrc 或 ~/.zshrc 中设置
export ECC_HOOK_PROFILE=developer

# Profile 选项：
# minimal   - 仅安全扫描（最轻量）
# developer - 安全 + 格式化 + 通知（推荐）
# full      - 所有 hooks
# security  - 仅安全相关
# off       - 禁用所有 hooks（调试用）
```

立即生效：
```bash
source ~/.bashrc  # Linux/macOS
# 或重启 Claude Code
```

### 7.3 使用 Hookify 交互式配置

在 Claude Code 中运行：
```
/hookify
```

按照向导选择：
```
🪝 ECC Hookify 配置向导
========================

请选择 Hook Profile:
  1. minimal   (推荐：仅安全扫描)
  2. developer (推荐：安全+格式化+通知)  ← 选择这个
  3. full      (所有功能)
  4. custom    (自定义)

请选择要启用的 Hook：
  [x] ⛔ 安全扫描（写文件前扫描密钥）
  [x] ✨ 代码格式化（写 TS/JS 后自动 Prettier）
  [ ] 🧪 自动测试（修改后自动运行测试）
  [x] 🔔 任务完成通知

配置目标: claude
写入完成 → ~/.claude/settings.json
```

### 7.4 查看和管理 Hooks

```
/hookify-list       # 查看所有 Hook 及状态
/hookify-configure  # 修改特定 Hook 配置
/hookify-help       # 查看 Hook 帮助
```

### 7.5 临时禁用 Hooks

```bash
# 单次操作禁用（调试时使用）
export ECC_HOOK_PROFILE=off

# 或在 Claude Code 中
你：临时禁用 ECC Hooks
```

---

## 8. MCP 集成使用

### 8.1 什么是 MCP？

MCP（Model Context Protocol）让 AI 代理直接访问外部工具和服务，例如：
- 搜索引擎（Exa）
- 文档查询（Context7）
- 代码仓库（GitHub）
- 数据库（SQLite）

### 8.2 配置 MCP 服务器

ECC 安装了 `.mcp.json` 配置文件，你需要设置对应的 API 密钥：

```bash
# 在 .env 文件或系统环境变量中设置
EXA_API_KEY=your_exa_api_key
GITHUB_TOKEN=your_github_token
FAL_AI_API_KEY=your_fal_key

# 验证 MCP 配置
ecc doctor  # 会提示哪些 MCP 密钥未配置
```

### 8.3 核心 MCP 功能使用

#### Exa 神经搜索

```
你：用 Exa 搜索"React 18 concurrent features best practices"

→ 自动调用 exa_search，返回相关技术文章
→ 自动调用 exa_get_contents，获取文章内容
→ 综合分析后给出建议
```

#### Context7 文档查询

```
你：查询 React Query v5 的 useQuery hook 使用方法

→ 自动调用 context7 查询最新文档
→ 返回最新 API 文档和示例代码
（优于使用训练数据，因为获取的是最新文档）
```

#### GitHub 集成

```
你：在 GitHub 上为这个 bug 创建 Issue

→ 自动调用 github.create_issue
→ 填写标题、描述、标签
→ 返回 Issue URL
```

#### fal.ai 媒体生成

```
你：生成一张"现代简约的登录页面设计稿"图片

→ 自动调用 fal.ai 图像生成
→ 返回生成的设计稿图片
```

---

## 9. 典型场景实战教程

### 场景一：全新功能开发（从零到一）

**目标：** 为博客系统实现"文章标签"功能

```
步骤 1：规划
/plan 为博客系统实现文章标签功能，
      支持多标签、标签搜索、标签云，
      使用 PostgreSQL + Next.js

[planner 生成详细实施计划]

步骤 2：TDD 开发
/feature-dev 实现标签 CRUD API

[tdd-guide 指导]：
  RED: 编写 POST /tags 测试 → 失败
  GREEN: 实现 TagController + TagService → 通过
  REFACTOR: 提取验证逻辑 → 通过

步骤 3：安全检查
[security-reviewer 自动触发]：
  ✅ 输入验证正确（标签名长度、字符集）
  ⚠️ 建议添加标签数量限制（防 DoS）

步骤 4：代码审查
[code-reviewer 自动触发]：
  ✅ 全部通过

步骤 5：E2E 测试
/test-coverage
[e2e-runner]：
  生成 tests/e2e/tags.spec.ts

步骤 6：提交
/prp-commit

输出：feat(blog): add article tag system with CRUD and search
```

### 场景二：遗留代码重构

**目标：** 重构一个 800 行的"上帝类"

```
步骤 1：分析现状
你：分析 src/services/LegacyOrderService.ts 的问题

[code-reviewer + refactor-cleaner 联合分析]：
  - 发现 15 个职责混合的方法
  - 建议拆分为：OrderCreator, OrderValidator,
    OrderNotifier, OrderPersistence

步骤 2：制定重构计划
/plan 重构 LegacyOrderService.ts，
      按职责拆分，保持测试通过

[planner 输出安全重构路径]

步骤 3：逐步重构（先写测试，再重构）
/feature-dev 提取 OrderValidator 类

每次重构步骤：
  - 先写/补充测试（确保覆盖当前行为）
  - 提取代码
  - 验证测试仍然通过
  - 代码审查

步骤 4：清理死代码
/refactor-clean
[refactor-cleaner]：移除废弃方法，清理注释

步骤 5：最终验证
/quality-gate
[质量门控]：所有指标达标
```

### 场景三：修复生产 Bug

**目标：** 修复"用户购买后偶发订单状态不更新"的 Bug

```
步骤 1：分析 Bug
你：生产环境报告：用户完成支付后，
    约 3% 的情况下订单状态不更新为"已支付"。
    错误日志：[粘贴日志]

[code-explorer agent]：
  - 分析可能的竞态条件
  - 检查事务处理逻辑
  - 发现：Webhook 和轮询更新存在竞态

步骤 2：TDD 修复
使用 tdd-guide：
  RED: 编写复现竞态条件的测试
  GREEN: 添加数据库乐观锁
  REFACTOR: 确认无副作用

步骤 3：安全验证
[security-reviewer]：确认修复不引入新漏洞

步骤 4：提交
/prp-commit fix(order): resolve race condition in payment status update
```

### 场景四：代码库接手（新加入项目）

**目标：** 快速了解一个陌生代码库

```
步骤 1：代码库探索
你：使用 codebase-onboarding skill 帮我了解这个项目

[code-explorer + docs-lookup]：
  - 生成项目结构总结
  - 识别核心模块
  - 标注关键入口点
  - 列出主要依赖

步骤 2：架构分析
你：architect 分析这个系统的架构模式

[architect]：
  - 识别设计模式
  - 画出模块依赖图
  - 指出技术债务

步骤 3：代码质量扫描
/code-review

[code-reviewer]：
  - 生成代码质量报告
  - 标注高风险区域

步骤 4：建立知识地图
/update-codemaps

[doc-updater]：
  - 生成代码地图文档
  - 为关键函数添加注释
```

### 场景五：性能优化

**目标：** 优化 API 响应时间从 2s 降至 200ms

```
步骤 1：性能分析
你：performance-optimizer 分析这些慢查询：[日志]

[performance-optimizer + database-reviewer]：
  - 识别 N+1 查询（3 处）
  - 发现缺少索引（2 个字段）
  - 识别不必要的序列化

步骤 2：优化方案
[architect]：建议添加 Redis 缓存层

步骤 3：实施优化
/feature-dev 添加 Redis 查询缓存

步骤 4：验证效果
你：benchmark skill 对比优化前后性能

[benchmark]：
  优化前：平均 1987ms
  优化后：平均 143ms
  提升：93%
```

### 场景六：多语言团队协作（同时使用多种语言）

```
# 前端 TypeScript 审查
/code-review
→ typescript-reviewer 自动激活

# 后端 Go 审查  
/go-review
→ go-reviewer 激活

# 数据科学 Python
/python-review
→ python-reviewer 激活

# 一次性审查所有语言
你：审查整个项目（前端 TS + 后端 Go + 数据脚本 Python）

→ ECC 自动识别文件类型，调用对应语言审查器
→ 生成综合审查报告
```

---

## 10. 会话管理与持久化

### 10.1 为什么需要会话管理？

长时间工作或跨天任务时，AI 代理的上下文会被清除。ECC 的会话管理功能让你：
- 保存当前工作进度
- 明天继续昨天的任务
- 在不同机器上恢复工作

### 10.2 保存工作状态

```
# 明确保存当前进度
/save-session

# ECC 会记录：
# - 当前任务描述
# - 已完成的步骤
# - 下一步计划
# - 修改的文件列表
# - 未解决的问题

# 或者在工作关键节点创建检查点
/checkpoint 完成了 UserService 的重构，下一步是 OrderService
```

### 10.3 恢复工作状态

```
# 查看所有保存的会话
/sessions

输出：
#  ID       时间              项目        任务
1  sess_001  今天 14:30       ecommerce   购物车重构（进行中）
2  sess_002  昨天 18:45       blog-api    评论系统（已完成）
3  sess_003  3天前 10:20      auth-svc    JWT 升级（待续）

# 恢复特定会话
/resume-session sess_001

ECC 会立即提供：
"上次你在重构购物车模块，已完成 CartItem 类提取，
下一步是 CartValidator，当时遇到的问题是..."
```

### 10.4 跨机器会话同步

```bash
# 导出会话（如需要在其他机器继续）
ecc sessions export sess_001 > cart-refactor-session.json

# 在另一台机器导入
ecc sessions import cart-refactor-session.json
```

---

## 11. ECC 维护管理

### 11.1 更新 ECC

```bash
# 方式 1：通过命令（推荐）
/auto-update

# 方式 2：通过 CLI
ecc auto-update

# 方式 3：手动更新
cd /path/to/everything-claude-code
git pull origin main
./install.sh --profile developer --target claude
```

### 11.2 系统诊断

```bash
# 运行完整诊断
ecc doctor

# 典型输出：
✅ Node.js: v20.10.0
✅ ECC CLI: 2.0.0-rc.1
✅ Claude Code: 已配置
✅ 安装数据库: 正常 (247 个组件)
⚠️  漂移文件: agents/planner.md (本地已修改)
❌ MCP: EXA_API_KEY 未设置
⚠️  Hook Profile: 未设置 ECC_HOOK_PROFILE

建议操作：
  → ecc repair --drift     修复漂移文件
  → export EXA_API_KEY=... 设置 Exa 密钥
  → export ECC_HOOK_PROFILE=developer
```

### 11.3 修复漂移文件

当 ECC 文件被意外修改或与最新版本不一致时：

```bash
# 修复所有漂移文件（恢复到 ECC 标准版本）
ecc repair --drift

# 仅修复缺失文件
ecc repair --missing

# 查看哪些文件漂移
ecc doctor --check-drift
```

### 11.4 清理未使用组件

```bash
# 查看可以清理的组件
ecc prune --dry-run

# 执行清理
ecc prune

# 或通过命令
/prune
```

### 11.5 卸载 ECC

```bash
# 卸载所有 ECC 管理的文件
ecc uninstall

# 卸载特定 target 的文件
ecc uninstall --target claude

# 卸载特定组件
ecc uninstall --modules agent:planner,skill:tdd-workflow
```

---

## 12. 故障排除手册

### 12.1 安装问题

**问题：`./install.sh: Permission denied`**
```bash
chmod +x install.sh
./install.sh --profile developer
```

**问题：`npm install` 失败**
```bash
# 清理缓存重试
npm cache clean --force
npm install

# 或使用 yarn
yarn install
```

**问题：安装后 Claude Code 没有变化**
```bash
# 验证安装路径
ecc list-installed

# 检查 Claude Code 配置目录
ls ~/.claude/agents/

# 重新安装
ecc install --profile developer --target claude --force
```

### 12.2 Hooks 问题

**问题：Hooks 不触发**
```bash
# 检查 Hook Profile 设置
echo $ECC_HOOK_PROFILE   # 应该不为空

# 检查 Claude Code settings.json
cat ~/.claude/settings.json | grep -A 5 "hooks"

# 查看 Hook 状态
/hookify-list
```

**问题：代码格式化 Hook 太慢**
```bash
# 切换到 minimal profile 减少 hooks
export ECC_HOOK_PROFILE=minimal
```

**问题：安全扫描误报**
```bash
# 临时关闭安全扫描 hook（调试时使用）
export ECC_HOOK_PROFILE=off

# 或修改 hooks/hooks.json 中的 enabled: false
```

### 12.3 Agent 问题

**问题：Agent 没有按预期调用**
```
# 明确要求使用特定 Agent
你：请使用 planner agent（不是其他方式）来规划这个任务

# 或者直接使用命令
/plan 任务描述
```

**问题：Agent 输出质量不佳**
```
# 提供更多上下文
你：使用 code-reviewer 审查 src/auth/login.ts，
    这是一个 Node.js + TypeScript 项目，
    使用 bcrypt 做密码哈希，JWT 做认证，
    重点检查认证逻辑是否安全
```

### 12.4 MCP 问题

**问题：MCP 工具不可用**
```bash
# 检查 API 密钥
ecc doctor

# 检查 .mcp.json 配置
cat .mcp.json

# 测试 MCP 连接
ecc status --mcp
```

**问题：Exa 搜索返回空结果**
```bash
# 确认 API 密钥有效
echo $EXA_API_KEY

# 测试 API 连通性
curl -H "x-api-key: $EXA_API_KEY" https://api.exa.ai/search \
  -d '{"query": "test"}' -H "Content-Type: application/json"
```

### 12.5 性能问题

**问题：Claude Code 响应变慢（安装 ECC 后）**
```bash
# 切换到 minimal profile
export ECC_HOOK_PROFILE=minimal

# 如果还是慢，检查安装的组件数量
ecc list-installed | wc -l

# 考虑使用精简安装
ecc install --profile minimal --target claude
```

**问题：上下文窗口用尽（长会话）**
```
# 使用 strategic-compact skill 手动压缩
你：使用 strategic-compact skill 压缩当前上下文

# 或保存会话，开新对话
/save-session
# 重新打开 Claude Code，然后
/resume-session
```

### 12.6 版本兼容问题

**问题：升级 ECC 后某些功能失效**
```bash
# 查看变更日志
cat CHANGELOG.md

# 检查是否有破坏性变更
ecc doctor

# 如需回滚
git checkout v1.9.0
./install.sh --profile developer --target claude
```

---

## 13. 常见问题解答（FAQ）

**Q1：ECC 会影响 AI 的创造力吗？**

A：不会。ECC 设置的是**工程实践约束**，不是创意约束。它会确保代码安全、有测试、符合规范，但不会限制技术方案的选择。

**Q2：ECC 的 Agent 和 Skill 有什么区别？**

A：
- **Agent**：专门的 AI 子代理，有独立的执行上下文，适合需要深度专注于特定领域的任务
- **Skill**：工作流程定义，注入到当前对话上下文，更适合指导性的步骤流程

简单理解：Agent 是"专家顾问"，Skill 是"操作手册"。

**Q3：我需要每次都手动调用 ECC 吗？**

A：不需要。ECC 设计为**自动感知触发**。当你的请求匹配特定模式时（如"实现某功能"、"修复某错误"），ECC 会自动激活对应的 Agent 或 Skill。

**Q4：ECC 会收集我的代码数据吗？**

A：不会。ECC 是完全本地化的工具。所有组件文件都安装在你的本地机器上。ECC 不包含任何数据收集或上报机制。

**Q5：为什么我应该用 Skills 而不是 Commands？**

A：
- **Skills**（技能）：主要工作流界面，功能完整，持续更新
- **Commands**（命令）：历史兼容的入口点，底层调用对应 Skill

如果你习惯了 `/code-review` 这样的命令，继续使用完全没问题。如果你想获得最新功能，直接描述任务让 ECC 自动匹配 Skill 更好。

**Q6：可以只安装特定语言的支持吗？**

A：可以。使用语言模式安装：
```bash
./install.sh typescript python  # 只安装 TS 和 Python 支持
./install.sh rust golang        # 只安装 Rust 和 Go 支持
```

**Q7：ECC 支持哪些 AI 框架？**

A：Claude Code、OpenAI Codex、Cursor IDE、OpenCode、Google Gemini。使用 `--target` 参数指定。

**Q8：团队如何统一使用 ECC？**

A：
1. 在项目仓库根目录保留 ECC 配置文件（`.mcp.json`，`CLAUDE.md`）
2. 团队成员各自安装 ECC：`./install.sh --profile developer`
3. 在 `CONTRIBUTING.md` 中说明 ECC 使用规范
4. 可以通过 `rules/` 目录添加项目特定的规则

**Q9：安装 full profile 会不会太重？**

A：full profile 包含 200+ Skills 和 53 个 Agents，文件数量多但每个文件都是轻量的 Markdown 文件。对 Claude Code 的响应速度影响微乎其微。如果有顾虑，developer profile 已经覆盖了 95% 的日常使用场景。

**Q10：如何贡献新的 Skill 或 Agent？**

A：
1. Fork 仓库
2. 在 `skills/your-skill/` 创建 Skill（遵循 skill.md 规范）
3. 或在 `agents/` 创建 Agent（遵循 Agent 规范）
4. 提交 PR，在描述中说明用途和测试方法

参考 `CONTRIBUTING.md` 获取详细贡献指南。

**Q11：ECC 2.0 Rust 重写版什么时候发布？**

A：ECC 2.0 核心使用 Rust 重写正处于 Alpha 阶段（`ecc2/` 目录）。主要目标是提升安装速度和状态管理性能。具体时间表参考 `CHANGELOG.md` 和 GitHub Releases。

**Q12：如何获取帮助？**

A：
- 查看本教程和 `TROUBLESHOOTING.md`
- 运行 `ecc doctor` 获取系统诊断
- 在 Claude Code 中询问：`ECC 的 X 功能怎么使用？`
- 提交 GitHub Issue

---

## 附录

### A. 快速参考卡片

```
ECC 快速参考
═══════════════════════════════════════════

安装：
  ./install.sh --profile developer --target claude
  ecc doctor                 # 检查状态

最常用命令：
  /plan [任务]               # 规划
  /feature-dev [功能]        # TDD 开发
  /code-review               # 审查代码
  /build-fix                 # 修复构建
  /save-session              # 保存进度
  /auto-update               # 更新 ECC

最常用 Agents（直接说话即可）：
  planner        任务规划
  code-reviewer  代码审查
  security-reviewer 安全检查
  tdd-guide      TDD 指导
  [language]-reviewer  语言审查

重要规则（始终遵循）：
  ⛔ 永不硬编码密钥
  ✅ 先写测试再写代码
  ✅ 函数 < 50 行
  ✅ 覆盖率 ≥ 80%

Hook Profile：
  export ECC_HOOK_PROFILE=developer

═══════════════════════════════════════════
```

### B. 推荐工作流

**日常开发工作流（推荐）：**

```
1. 开始新功能前：/plan [功能描述]
2. 编写代码时：   遵循 tdd-workflow（先测试）
3. 完成后：       自动触发 code-reviewer
4. 提交前：       /review-pr 或 /quality-gate
5. 写提交信息：   /prp-commit
6. 结束工作：     /save-session
```

**每日开始工作流：**
```
1. /resume-session     # 恢复上次工作
2. ecc doctor          # 确认系统正常
3. /auto-update        # 检查 ECC 更新（每周一次即可）
```

### C. ECC 文档导航

| 文档 | 内容 | 适用读者 |
|------|------|---------|
| 本文档（应用教程手册）| 使用指南、实战教程 | 所有用户 |
| ECC-架构设计说明书 | 系统架构、设计原则 | 架构师、技术负责人 |
| ECC-详细设计说明书 | 模块详细设计、扩展规范 | 开发者、贡献者 |
| README.md | 英文快速开始 | 初次接触者 |
| README.zh-CN.md | 中文快速开始 | 中文用户 |
| TROUBLESHOOTING.md | 故障排除 | 遇到问题时 |
| CONTRIBUTING.md | 贡献指南 | 贡献者 |
| CHANGELOG.md | 版本历史 | 了解新功能 |
| SECURITY.md | 安全政策 | 安全团队 |
