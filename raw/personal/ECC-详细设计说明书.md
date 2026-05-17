# Everything Claude Code (ECC) 详细设计说明书

> **版本：** 2.0.0-rc.1  
> **文档版本：** 1.0.0  
> **编写日期：** 2026-05-12  
> **适用范围：** ECC 开发人员、贡献者、系统集成工程师

---

## 目录

1. [Agents 子系统详细设计](#1-agents-子系统详细设计)
2. [Skills 子系统详细设计](#2-skills-子系统详细设计)
3. [Commands 子系统详细设计](#3-commands-子系统详细设计)
4. [Hooks 子系统详细设计](#4-hooks-子系统详细设计)
5. [Rules 子系统详细设计](#5-rules-子系统详细设计)
6. [MCP 集成层详细设计](#6-mcp-集成层详细设计)
7. [CLI 工具详细设计](#7-cli-工具详细设计)
8. [安装系统详细设计](#8-安装系统详细设计)
9. [数据模型设计](#9-数据模型设计)
10. [工作流程设计](#10-工作流程设计)
11. [国际化设计](#11-国际化设计)
12. [扩展点设计规范](#12-扩展点设计规范)

---

## 1. Agents 子系统详细设计

### 1.1 Agent 定义规范

每个 Agent 以 Markdown 文件存储在 `agents/` 目录，遵循统一的文档结构规范。

**标准 Agent 文件结构：**

```markdown
# [Agent Display Name]

## Role（角色定义）
简洁描述该 Agent 的核心职责和专业边界（1-3 句话）。

## When to Use（使用时机）
列出触发该 Agent 的具体场景条件：
- 场景 1
- 场景 2

## Workflow（工作流程）
分步骤描述 Agent 的执行流程：
1. 步骤 1：[动作描述]
2. 步骤 2：[动作描述]
3. 步骤 3：[动作描述]

## Output Format（输出格式）
描述 Agent 输出的标准格式和结构。

## Constraints（约束条件）
列出 Agent 必须遵守的限制和禁止行为。
```

### 1.2 全量 Agent 清单与设计说明

#### 规划与设计类

**`planner`（任务规划师）**
- **职责**：将复杂功能需求分解为可执行的实施计划
- **触发条件**：用户提出复杂功能请求；多步骤任务；涉及多个文件/模块的修改
- **核心工作流**：
  1. 分析需求，识别所有受影响的组件
  2. 识别技术风险和依赖关系
  3. 将任务分解为带优先级的子任务列表
  4. 为每个子任务估算工作量
  5. 输出结构化实施计划

**`architect`（系统架构师）**
- **职责**：系统设计决策、可扩展性评估、架构模式选择
- **触发条件**：新系统/子系统设计；架构重构；技术选型决策
- **设计原则**：高内聚低耦合；可扩展性优先；渐进式演进

**`code-architect`（代码架构师）**
- **职责**：代码层面的架构设计，模块划分、接口设计、依赖关系
- **区别于 architect**：关注代码结构而非系统结构

**`chief-of-staff`（首席协调员）**
- **职责**：多 Agent 任务协调，任务分发给专项 Agent，汇聚结果
- **编排模式**：支持并行/顺序/条件分发模式

#### 代码质量类

**`code-reviewer`（代码审查员）**
- **职责**：全面的代码质量审查
- **审查维度**：
  - 代码可读性和命名规范
  - 函数大小（< 50 行）和文件大小（< 800 行）
  - 嵌套深度（不超过 4 层）
  - 错误处理完整性
  - 不可变性原则
  - 硬编码值检测
- **严重级别**：CRITICAL > HIGH > MEDIUM > LOW > INFO
- **触发条件**：代码编写或修改后立即触发

**`tdd-guide`（TDD 向导）**
- **职责**：指导测试驱动开发流程
- **工作流**：
  1. RED 阶段：先编写失败测试
  2. GREEN 阶段：编写最小通过实现
  3. REFACTOR 阶段：重构代码，保持测试绿色
  4. 验证覆盖率 ≥ 80%
- **触发条件**：新功能开发；Bug 修复

**`refactor-cleaner`（重构清理员）**
- **职责**：识别和清除死代码、重复代码、技术债务
- **重构策略**：消除重复（DRY）；提取通用函数；简化复杂逻辑

**`performance-optimizer`（性能优化师）**
- **职责**：识别性能瓶颈，提供优化建议
- **分析维度**：算法复杂度；内存使用；I/O 效率；缓存策略

**`type-design-analyzer`（类型设计分析师）**
- **职责**：TypeScript/强类型语言的类型系统设计审查
- **关注点**：类型精确性；泛型使用；类型安全性

#### 安全审查类

**`security-reviewer`（安全审查员）**
- **职责**：安全漏洞检测和修复建议
- **检查清单**：
  ```
  □ 无硬编码密钥/密码/令牌
  □ SQL 注入防护（参数化查询）
  □ XSS 防护（输出转义）
  □ CSRF 保护
  □ 认证/授权验证
  □ 所有端点有速率限制
  □ 错误消息不泄露敏感信息
  □ 输入验证（系统边界处）
  ```
- **强制规则**：发现 CRITICAL 问题必须停止并立即处理

**`healthcare-reviewer`（医疗合规审查员）**
- **职责**：医疗软件合规性审查（HIPAA、HL7、FHIR）
- **专项检查**：PHI 数据处理；审计日志；访问控制

#### 语言专项审查类

所有语言审查 Agent 遵循相同的基础审查框架，在此之上添加语言特定检查项：

| Agent | 语言 | 特定检查项 |
|-------|------|----------|
| `typescript-reviewer` | TypeScript/JavaScript | 类型安全、async/await、ESM 规范 |
| `python-reviewer` | Python | PEP 8、类型提示、虚拟环境 |
| `rust-reviewer` | Rust | 所有权、借用检查、错误处理（Result/Option）|
| `go-reviewer` | Go | goroutine 使用、channel 设计、error 包装 |
| `java-reviewer` | Java | Spring Boot 规范、Maven/Gradle 依赖 |
| `kotlin-reviewer` | Kotlin | 协程使用、空安全、扩展函数 |
| `swift-reviewer` | Swift | 并发模型（Actor）、SwiftUI 模式 |
| `cpp-reviewer` | C/C++ | 内存管理、RAII、现代 C++ 规范 |
| `csharp-reviewer` | C# | .NET 规范、异步模式、LINQ |
| `flutter-reviewer` | Flutter/Dart | Widget 设计、状态管理、Dart 规范 |
| `fastapi-reviewer` | FastAPI/Python | 路由设计、依赖注入、Pydantic 模型 |

#### 构建修复类

所有构建修复 Agent 遵循相同的诊断框架：

```
1. 解析错误信息 → 识别根因类型
2. 查找相关代码位置
3. 应用最小化修复
4. 验证修复后构建成功
5. 检查是否引入新问题
```

| Agent | 适用场景 |
|-------|---------|
| `build-error-resolver` | 通用构建错误 |
| `rust-build-resolver` | Cargo 构建、借用检查错误 |
| `go-build-resolver` | Go 模块、导入路径错误 |
| `java-build-resolver` | Maven/Gradle 构建失败 |
| `kotlin-build-resolver` | Kotlin/Gradle 编译错误 |
| `cpp-build-resolver` | CMake/Make 构建失败 |
| `swift-build-resolver` | Xcode/SPM 构建失败 |
| `dart-build-resolver` | Flutter/Dart 构建失败 |
| `pytorch-build-resolver` | PyTorch CUDA/训练错误 |

#### 测试类

**`e2e-runner`（E2E 测试执行者）**
- **职责**：Playwright E2E 测试设计与执行
- **工作流**：
  1. 识别关键用户路径
  2. 设计 Page Object Model（POM）
  3. 编写测试用例
  4. 配置 CI/CD 集成
  5. 处理不稳定测试（flaky tests）

**`pr-test-analyzer`（PR 测试分析师）**
- **职责**：分析 PR 变更，识别需要新增或修改的测试
- **输出**：测试缺口报告，建议测试案例

#### 文档类

**`doc-updater`（文档更新员）**
- **职责**：同步代码变更到相关文档
- **文档范围**：README、API 文档、代码注释、Codemaps

**`docs-lookup`（文档查询员）**
- **职责**：通过 Context7 MCP 查询最新的库和框架文档
- **触发条件**：用户询问 API 用法；框架配置；版本特性

#### 运维类

**`loop-operator`（循环操作员）**
- **职责**：安全管理和监控自主代理循环执行
- **功能**：
  - 检测循环停滞（stall detection）
  - 安全干预机制
  - 循环状态持久化
  - 超时控制

**`harness-optimizer`（Harness 优化师）**
- **职责**：优化 ECC 在各 harness 框架上的配置
- **优化维度**：可靠性、成本、吞吐量

#### 专业领域类

**`database-reviewer`（数据库审查员）**
- **职责**：PostgreSQL/Supabase 数据库设计审查
- **审查内容**：Schema 设计、查询优化、索引策略、N+1 问题

**`seo-specialist`（SEO 专家）**
- **职责**：前端和内容的 SEO 优化
- **检查项**：结构化数据、元标签、性能指标、可访问性

**`a11y-architect`（无障碍架构师）**
- **职责**：WCAG 合规性审查和无障碍设计
- **标准**：WCAG 2.1 AA 级别

**GAN 三件套（gan-planner / gan-generator / gan-evaluator）**
- **职责**：GAN 模型的规划、生成和评估完整工作流

**开源三件套（opensource-forker / opensource-packager / opensource-sanitizer）**
- **职责**：Fork 开源项目、打包发布、安全清理（移除敏感数据）

---

## 2. Skills 子系统详细设计

### 2.1 Skill 文件结构规范

每个 Skill 以目录形式存储在 `skills/` 下，目录内必须包含主定义文件：

```
skills/
└── skill-name/
    ├── skill.md          # 主定义文件（必需）
    ├── README.md         # 详细说明（可选）
    └── examples/         # 使用示例（可选）
```

**skill.md 标准结构：**

```markdown
# [Skill Name]

## When to Use（使用时机）
描述何时激活此技能。

## Prerequisites（前置条件）
- 依赖的工具、框架或配置
- 所需权限

## Steps（执行步骤）
### Phase 1: [阶段名称]
1. 具体操作步骤
2. ...

### Phase 2: [阶段名称]
...

## Verification（验证方法）
如何验证技能执行成功的检查清单。

## Common Pitfalls（常见陷阱）
已知问题和规避方法。
```

### 2.2 核心通用技能详细设计

#### `tdd-workflow`（TDD 工作流）

**三阶段执行模型：**

```
Phase 1 - RED（红灯）
├── 分析功能需求
├── 确定测试边界（单元/集成/E2E）
├── 编写测试用例（未实现，预期失败）
└── 运行测试，确认失败

Phase 2 - GREEN（绿灯）
├── 编写最小实现代码
├── 运行测试，确认通过
└── 不过度优化

Phase 3 - REFACTOR（重构）
├── 改善代码结构（不改变行为）
├── 确认测试仍然通过
├── 检查代码覆盖率 ≥ 80%
└── 运行代码审查
```

#### `security-review`（安全审查）

**审查维度矩阵：**

| 类别 | 检查项 | 严重度 |
|------|--------|--------|
| 认证 | JWT 验证、会话管理 | CRITICAL |
| 授权 | RBAC 实施、权限检查 | CRITICAL |
| 输入验证 | XSS、SQLi、命令注入 | CRITICAL |
| 密钥管理 | 硬编码检测、轮换机制 | CRITICAL |
| 传输安全 | HTTPS 强制、证书验证 | HIGH |
| 日志安全 | 敏感数据脱敏 | HIGH |
| 依赖安全 | 已知 CVE 扫描 | HIGH |
| 错误处理 | 信息泄露防护 | MEDIUM |

#### `coding-standards`（编码规范）

**文件组织规范：**
- 文件大小：典型 200-400 行，最大 800 行
- 函数大小：最大 50 行
- 嵌套深度：最大 4 层
- 文件组织：按功能/领域组织，而非按类型

**命名规范：**
```
类/接口:    PascalCase     → UserRepository
函数/变量:  camelCase      → getUserById
常量:       UPPER_SNAKE    → MAX_RETRY_COUNT
文件名:     kebab-case     → user-repository.ts
目录名:     kebab-case     → auth-service/
```

#### `e2e-testing`（E2E 测试）

**Page Object Model 结构：**
```typescript
// 标准 POM 结构
class LoginPage {
  constructor(private page: Page) {}
  
  async navigate() { ... }
  async fillCredentials(email: string, password: string) { ... }
  async submit() { ... }
  async getErrorMessage() { ... }
}
```

**测试结构规范：**
```typescript
test.describe('功能模块', () => {
  test.beforeEach(async ({ page }) => { /* 测试前置 */ });
  
  test('正常流程', async ({ page }) => { /* 主路径 */ });
  test('边界条件', async ({ page }) => { /* 边界处理 */ });
  test('错误处理', async ({ page }) => { /* 异常路径 */ });
});
```

#### `git-workflow`（Git 工作流）

**提交信息规范（Conventional Commits）：**
```
<type>(<scope>): <description>

Types:
  feat     - 新功能
  fix      - Bug 修复
  refactor - 代码重构（不添加功能，不修复 bug）
  docs     - 文档更新
  test     - 测试相关
  chore    - 构建/工具变更
  perf     - 性能优化
  ci       - CI/CD 配置

示例：
  feat(auth): add JWT refresh token rotation
  fix(api): resolve null pointer in user service
  docs(readme): update installation guide
```

**PR 工作流：**
1. 分析完整提交历史
2. 撰写全面的 PR 摘要
3. 包含测试计划
4. 使用 `git push -u` 推送

### 2.3 语言框架技能详细设计

#### `frontend-patterns`（前端开发模式）

**组件设计原则：**
```typescript
// ✅ 推荐：组合式组件设计
const UserProfile = ({ userId }: { userId: string }) => {
  const user = useUser(userId);
  return <UserCard user={user} />;
};

// ❌ 避免：过大的单一组件
const GiantComponent = () => {
  // 500+ 行的混合逻辑
};
```

**状态管理策略：**
- 组件本地状态：`useState`
- 服务端状态：React Query / SWR
- 全局 UI 状态：Zustand / Jotai
- 表单状态：React Hook Form

#### `backend-patterns`（后端开发模式）

**Repository 模式：**
```typescript
interface UserRepository {
  findAll(filter?: UserFilter): Promise<User[]>;
  findById(id: string): Promise<User | null>;
  create(data: CreateUserDTO): Promise<User>;
  update(id: string, data: UpdateUserDTO): Promise<User>;
  delete(id: string): Promise<void>;
}
```

**API 响应格式（标准 Envelope）：**
```typescript
interface ApiResponse<T> {
  success: boolean;
  data: T | null;
  error: string | null;
  meta?: {
    page: number;
    limit: number;
    total: number;
  };
}
```

#### `api-design`（API 设计规范）

**REST 资源命名：**
```
GET    /users              # 列表
GET    /users/{id}         # 详情
POST   /users              # 创建
PUT    /users/{id}         # 全量更新
PATCH  /users/{id}         # 部分更新
DELETE /users/{id}         # 删除

# 嵌套资源
GET    /users/{id}/posts
POST   /users/{id}/posts

# 操作
POST   /users/{id}/activate
POST   /orders/{id}/cancel
```

**HTTP 状态码规范：**
```
200 OK             - 成功（GET/PUT/PATCH）
201 Created        - 创建成功（POST）
204 No Content     - 成功无响应体（DELETE）
400 Bad Request    - 请求参数错误
401 Unauthorized   - 未认证
403 Forbidden      - 无权限
404 Not Found      - 资源不存在
409 Conflict       - 资源冲突
422 Unprocessable  - 业务验证失败
429 Too Many       - 速率限制
500 Server Error   - 服务器内部错误
```

### 2.4 AI/LLM 专项技能详细设计

#### `eval-harness`（评估框架）

**EDD（Eval-Driven Development）流程：**
```
1. 定义评估指标（精确度、召回率、延迟、成本）
2. 构建测试数据集
3. 建立基线性能
4. 实施改进
5. 评估改进效果
6. 迭代优化
```

#### `continuous-learning`（持续学习）

**知识捕获策略：**
- 个人调试笔记 → 自动记忆（auto memory）
- 团队/项目知识（架构决策、API 变更）→ 项目文档
- 不重复已有文档中的信息
- 不确定放置位置时先询问

#### `dmux-workflows`（多代理并行工作流）

**并行 Agent 启动模式：**
```bash
# 在多个 tmux pane 中启动并行 agent
dmux spawn frontend-agent "实现登录页面"
dmux spawn backend-agent "实现登录 API"
dmux spawn test-agent "编写登录测试"
dmux sync  # 等待所有 agent 完成
```

---

## 3. Commands 子系统详细设计

### 3.1 Command 文件结构

```markdown
# /command-name

## Description
命令的简短描述（一句话）。

## Usage
```
/command-name [arguments]
```

## What This Does
详细说明命令执行的操作，以及它调用的 skills/agents。

## Arguments
- `--arg1`: 参数说明
- `--arg2`: 参数说明（可选）

## Examples
```
/command-name --arg1 value
```
```

### 3.2 Command 到 Skill/Agent 映射表

| Command | 主要调用的 Skill/Agent | 功能描述 |
|---------|----------------------|---------|
| `/plan` | planner agent | 生成功能实施计划 |
| `/multi-plan` | planner + architect | 多模块并行规划 |
| `/feature-dev` | tdd-guide + code-reviewer | 完整功能开发流 |
| `/code-review` | code-reviewer agent | 代码质量审查 |
| `/review-pr` | code-reviewer + security-reviewer | PR 综合审查 |
| `/build-fix` | build-error-resolver | 构建错误修复 |
| `/test-coverage` | tdd-guide + e2e-runner | 测试覆盖率提升 |
| `/rust-build` | rust-build-resolver | Rust 构建修复 |
| `/rust-review` | rust-reviewer | Rust 代码审查 |
| `/rust-test` | tdd-guide (Rust) | Rust 测试编写 |
| `/go-build` | go-build-resolver | Go 构建修复 |
| `/go-review` | go-reviewer | Go 代码审查 |
| `/kotlin-build` | kotlin-build-resolver | Kotlin 构建修复 |
| `/loop-start` | loop-operator | 启动自主循环 |
| `/loop-status` | loop-operator | 检查循环状态 |
| `/save-session` | session management | 保存当前会话 |
| `/resume-session` | session management | 恢复历史会话 |
| `/sessions` | session management | 列出所有会话 |
| `/auto-update` | ECC CLI | 更新 ECC 到最新版 |
| `/prune` | ECC CLI | 清理未使用组件 |
| `/quality-gate` | code-reviewer + security-reviewer | 质量门控检查 |
| `/hookify` | Hook 管理 | 交互式 Hook 配置 |
| `/prp-prd` | product-capability skill | 生成 PRD 文档 |
| `/prp-plan` | planner + architect | 基于 PRD 生成计划 |
| `/prp-implement` | tdd-guide + code-reviewer | PRD 到代码实现 |
| `/prp-pr` | doc-updater | 生成 PR 描述 |
| `/update-docs` | doc-updater | 同步文档更新 |
| `/refactor-clean` | refactor-cleaner | 代码重构清理 |
| `/jira` | Jira MCP | Jira 任务管理 |

### 3.3 多代理 Commands 设计

`/multi-*` 系列命令支持并行 Agent 编排：

```
/multi-plan    → 并行调用 planner + architect
/multi-execute → 将任务分发给多个专项 Agent 并行执行
/multi-frontend → 并行前端相关 Agent（设计+实现+测试）
/multi-backend  → 并行后端相关 Agent
/multi-workflow → 完整并行开发工作流
```

---

## 4. Hooks 子系统详细设计

### 4.1 hooks.json 配置结构

```json
{
  "hooks": [
    {
      "id": "unique-hook-id",
      "description": "Hook 用途描述",
      "event": "PreToolUse | PostToolUse | PreCompact | Notification | Stop",
      "matcher": {
        "tool_name": "工具名称（可选，支持通配符）",
        "condition": "附加条件表达式（可选）"
      },
      "action": {
        "type": "script | command | notification",
        "script": "执行脚本路径（type=script 时）",
        "command": "执行命令（type=command 时）",
        "message": "通知消息（type=notification 时）"
      },
      "profile": ["minimal", "developer", "full"],
      "enabled": true
    }
  ]
}
```

### 4.2 内置 Hook 设计

#### 安全扫描 Hook（PreToolUse）

```json
{
  "id": "security-scan-pre-write",
  "event": "PreToolUse",
  "matcher": {
    "tool_name": "write_file|create_file|edit_file"
  },
  "action": {
    "type": "script",
    "script": "scripts/hooks/security-scan.js"
  }
}
```

**安全扫描脚本检查项：**
- 正则匹配硬编码密钥模式（API_KEY=, password=, token= 等）
- 检测私钥格式（-----BEGIN PRIVATE KEY-----）
- 警告已知不安全函数调用

#### 代码格式化 Hook（PostToolUse）

```json
{
  "id": "prettier-format-post-write",
  "event": "PostToolUse",
  "matcher": {
    "tool_name": "write_file|create_file",
    "condition": "file_extension in ['.ts', '.js', '.tsx', '.jsx', '.json']"
  },
  "action": {
    "type": "command",
    "command": "npx prettier --write {{file_path}}"
  }
}
```

#### 任务完成通知 Hook（Notification）

```json
{
  "id": "task-complete-notification",
  "event": "Notification",
  "action": {
    "type": "notification",
    "message": "ECC 任务已完成，请查看结果"
  }
}
```

### 4.3 Hook Profile 配置

```bash
# ~/.bashrc 或 ~/.zshrc
export ECC_HOOK_PROFILE=developer  # 推荐值

# 可用 Profile：
# minimal   - 仅核心安全扫描
# developer - 安全 + 格式化 + 通知
# full      - 所有 hooks（含 hooks-runtime 扩展）
# security  - 仅安全相关 hooks
# custom    - 自定义组合
```

### 4.4 Hookify 交互式配置

`/hookify` 命令提供交互式向导配置 Hook：

```
ECC Hookify 向导
================
1. 选择 Hook 配置文件 (Profile)
   > minimal / developer / full / custom

2. 选择要启用的 Hook 类别：
   [x] 安全扫描
   [x] 代码格式化
   [ ] 自动测试
   [x] 完成通知

3. 配置目标平台：
   > claude / codex / cursor / all

4. 写入配置
   → ~/.claude/settings.json
   → ECC 状态记录
```

---

## 5. Rules 子系统详细设计

### 5.1 Rules 目录结构

```
rules/
├── common/
│   ├── coding-style.md       # 通用编码风格
│   ├── security.md           # 安全规范
│   ├── testing.md            # 测试要求
│   ├── git.md                # Git 规范
│   └── documentation.md     # 文档规范
├── typescript/
│   ├── coding-style.md       # TS 编码风格
│   ├── patterns.md           # TS 设计模式
│   └── testing.md            # TS 测试规范
├── python/
│   ├── coding-style.md       # Python 风格（PEP 8+）
│   └── testing.md            # pytest 规范
├── rust/
│   ├── coding-style.md       # Rust 风格
│   └── ownership.md          # 所有权规则
├── go/
│   ├── coding-style.md       # Go 风格
│   └── concurrency.md        # 并发安全
├── java/
│   └── coding-style.md       # Java/Spring 规范
├── kotlin/
│   └── coding-style.md       # Kotlin 规范
├── cpp/
│   ├── coding-style.md       # C/C++ 规范
│   └── memory.md             # 内存安全
└── ...                       # 其他语言
```

### 5.2 通用安全规则详细内容

**`rules/common/security.md` 核心规则：**

```markdown
## 凭据安全
- 永远不要硬编码：API 密钥、密码、令牌、私钥
- 使用环境变量：process.env.API_KEY
- 启动时验证必需的环境变量
- 立即轮换任何已暴露的密钥

## 输入验证
- 在所有系统边界处验证输入
- 使用 Schema 验证（Zod、Joi、Pydantic 等）
- 快速失败并给出清晰的错误消息
- 永远不要信任外部数据

## SQL 安全
- 始终使用参数化查询
- 永远不要拼接用户输入到 SQL 字符串
- 使用 ORM 并了解它的 N+1 问题

## XSS 防护
- 净化所有 HTML 输出
- 对用户内容使用 Content Security Policy
- 使用框架内置的 XSS 保护

## 认证和授权
- 每个路由验证身份认证
- 每个操作验证授权权限
- 会话令牌安全存储和传输
- 实施速率限制

## 错误处理
- 永远不要向用户暴露内部错误信息
- 服务器端记录详细上下文
- 向用户显示友好消息
```

### 5.3 Rules 注入机制

Rules 文件通过安装流程被注入到 AI 代理框架的上下文中：

1. **Claude Code**：通过 `CLAUDE.md` 或 `.claude/rules/` 目录
2. **Codex**：通过 `AGENTS.md` 文件（所有 Rules 合并注入）
3. **Cursor**：通过 `.cursorrules` 文件

安装时根据 Profile 和 Target 选择要注入的规则集。

---

## 6. MCP 集成层详细设计

### 6.1 MCP 配置文件结构

**`.mcp.json`（项目级配置）：**
```json
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "@org/mcp-server-name"],
      "env": {
        "API_KEY": "${SERVER_API_KEY}"
      }
    }
  }
}
```

### 6.2 核心 MCP 服务器详细配置

#### Exa（神经网络搜索）
```json
{
  "exa": {
    "command": "npx",
    "args": ["-y", "exa-mcp-server"],
    "env": {
      "EXA_API_KEY": "${EXA_API_KEY}"
    }
  }
}
```
**提供工具：** `exa_search`、`exa_find_similar`、`exa_get_contents`

#### Context7（实时文档查询）
```json
{
  "context7": {
    "command": "npx",
    "args": ["-y", "@upstash/context7-mcp"]
  }
}
```
**提供工具：** `resolve-library-id`、`get-library-docs`

#### GitHub
```json
{
  "github": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-github"],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
    }
  }
}
```
**提供工具：** `create_issue`、`create_pull_request`、`search_repositories` 等

#### SQLite（本地状态存储）
```json
{
  "sqlite": {
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-sqlite", "--db-path", "~/.ecc/state.db"]
  }
}
```

#### fal.ai（AI 媒体生成）
```json
{
  "fal-ai": {
    "command": "npx",
    "args": ["-y", "@fal-ai/mcp-server"],
    "env": {
      "FAL_KEY": "${FAL_AI_API_KEY}"
    }
  }
}
```
**提供工具：** 图像生成、视频生成、音频生成

### 6.3 MCP 使用模式

**在 Skill 中调用 MCP 工具：**
```markdown
## Steps
1. 使用 context7 查询最新 React 文档：
   `resolve-library-id → get-library-docs`
2. 基于文档实现组件...
```

**在 Agent 中调用 MCP 工具：**
```markdown
## Workflow
1. 调用 exa_search 搜索相关代码示例
2. 调用 github.search_code 查找类似实现
3. 综合结果提供建议
```

---

## 7. CLI 工具详细设计

### 7.1 主 CLI 入口：`scripts/ecc.js`

**命令解析架构：**
```javascript
// 命令路由表
const commands = {
  'install':       installApply,
  'plan':          installPlan,
  'catalog':       catalog,
  'consult':       consult,
  'list-installed': listInstalled,
  'doctor':        doctor,
  'repair':        repair,
  'auto-update':   autoUpdate,
  'status':        status,
  'sessions':      sessions,
  'session-inspect': sessionInspect,
  'loop-status':   loopStatus,
  'uninstall':     uninstall,
};
```

**全局选项：**
```
--target     安装目标平台 (claude|codex|cursor|opencode|gemini)
--profile    安装配置集 (minimal|developer|full|custom)
--modules    指定模块 ID 列表
--dry-run    预览不执行
--verbose    详细输出
--yes, -y    自动确认所有提示
```

### 7.2 安装运行时：`scripts/install-apply.js`

**核心功能流程：**

```javascript
async function installApply(options) {
  // 1. 解析安装模式
  const mode = detectInstallMode(options);
  // mode: 'legacy-language' | 'profile' | 'explicit-modules'
  
  // 2. 解析目标模块列表
  const modules = await resolveModules(mode, options);
  
  // 3. 解析目标平台
  const target = options.target || detectCurrentHarness();
  
  // 4. 计算目标文件路径
  const fileMappings = computeFileMappings(modules, target);
  
  // 5. 执行文件复制
  await copyFiles(fileMappings, { dryRun: options.dryRun });
  
  // 6. 写入 SQLite 状态
  await writeInstallState(modules, target, fileMappings);
  
  // 7. 输出安装报告
  printInstallReport(fileMappings);
}
```

### 7.3 诊断工具：`doctor` 命令

**检查项目：**
```
ECC Doctor 诊断结果
==================
✅ Node.js 版本: 20.10.0 (≥18.0 要求)
✅ ECC CLI: 2.0.0-rc.1
✅ 安装状态数据库: ~/.ecc/state.db (正常)
⚠️  漂移文件: ~/.claude/agents/planner.md (本地已修改)
❌ 缺失文件: ~/.claude/hooks/security-scan.js
✅ Claude Code 配置: 正常
⚠️  MCP 配置: EXA_API_KEY 未设置
```

**修复建议：**
- 漂移文件 → 运行 `ecc repair --drift`
- 缺失文件 → 运行 `ecc repair --missing`
- 环境变量 → 设置 `export EXA_API_KEY=...`

### 7.4 会话管理：`sessions` 命令

**会话数据模型：**
```typescript
interface EccSession {
  id: string;
  created_at: Date;
  updated_at: Date;
  harness: string;           // claude|codex|cursor
  project_path: string;
  checkpoint: {
    task_description: string;
    progress: string;
    next_steps: string[];
    files_modified: string[];
  };
  metadata: Record<string, unknown>;
}
```

---

## 8. 安装系统详细设计

### 8.1 Profile 内容定义

**`minimal` Profile 内容：**
```yaml
skills:
  - tdd-workflow
  - coding-standards
  - security-review
  - git-workflow

rules:
  - common/security.md
  - common/testing.md
  - common/coding-style.md

agents:
  - planner
  - code-reviewer
  - build-error-resolver

hooks: []   # 不安装 hooks

mcp: []     # 不安装 MCP
```

**`developer` Profile 内容：**
```yaml
extends: minimal

skills:
  - e2e-testing
  - backend-patterns
  - frontend-patterns
  - api-design
  - deployment-patterns

rules:
  - typescript/*        # 根据项目语言选择
  - python/*
  # 等其他语言规则...

agents:
  - architect
  - security-reviewer
  - tdd-guide
  - doc-updater
  - typescript-reviewer  # 根据项目语言选择
  - e2e-runner

hooks:
  - security-scan-pre-write
  - prettier-format-post-write

mcp:
  - context7
  - sqlite
```

**`full` Profile 内容：**
```yaml
extends: developer

# 包含所有 200+ Skills
skills: "*"

# 包含所有 53 Agents
agents: "*"

# 包含所有 Hooks（含 hooks-runtime）
hooks: "*"

# 包含所有 14 个 MCP 配置
mcp: "*"
```

### 8.2 选择性安装架构

**Manifest 驱动的选择性安装（v1.9+）：**

```json
// manifests/install-manifest.json
{
  "version": "2.0.0",
  "components": [
    {
      "id": "skill:tdd-workflow",
      "type": "skill",
      "path": "skills/tdd-workflow/skill.md",
      "targets": ["claude", "codex", "cursor", "opencode"],
      "profiles": ["minimal", "developer", "full"],
      "tags": ["testing", "development"]
    },
    {
      "id": "agent:planner",
      "type": "agent",
      "path": "agents/planner.md",
      "targets": ["claude"],
      "profiles": ["minimal", "developer", "full"]
    }
  ]
}
```

**Target 路径映射：**

| 组件类型 | claude target | codex target | cursor target |
|---------|--------------|-------------|--------------|
| agents | `~/.claude/agents/` | `AGENTS.md`（合并） | N/A |
| skills | `~/.claude/skills/` | `~/.codex/skills/` | `~/.cursor/skills/` |
| rules | `~/.claude/rules/` | `AGENTS.md`（合并） | `.cursorrules`（合并）|
| hooks | `~/.claude/settings.json` | N/A | N/A |
| mcp | `~/.claude/mcp.json` | N/A | `.cursor/mcp.json` |

### 8.3 状态存储设计

**SQLite 表结构：**

```sql
-- 安装记录表
CREATE TABLE installations (
  id          TEXT PRIMARY KEY,
  component_id TEXT NOT NULL,
  component_type TEXT NOT NULL,
  target      TEXT NOT NULL,
  source_path TEXT NOT NULL,
  dest_path   TEXT NOT NULL,
  installed_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  checksum    TEXT NOT NULL
);

-- 会话表
CREATE TABLE sessions (
  id          TEXT PRIMARY KEY,
  harness     TEXT NOT NULL,
  project_path TEXT,
  checkpoint  TEXT,  -- JSON
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 学习记录表
CREATE TABLE learnings (
  id          TEXT PRIMARY KEY,
  category    TEXT NOT NULL,
  content     TEXT NOT NULL,
  context     TEXT,
  created_at  DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

---

## 9. 数据模型设计

### 9.1 核心数据流

```
用户指令
  │
  ▼ 解析
Claude Code 主 Agent
  │
  ├── 读取 CLAUDE.md（全局规则和配置）
  ├── 读取 agents/*.md（可用 Agent 清单）
  ├── 读取 skills/（可用 Skills 清单）
  │
  ▼ 决策
选择 Agent/Skill
  │
  ├── Agent：子代理执行（独立上下文）
  └── Skill：注入工作流步骤（当前上下文）
        │
        ▼ 执行
  工具调用（read_file, write_file, execute_command）
        │
        ▼ Hook 触发
  PreToolUse → 执行 → PostToolUse
        │
        ▼ 结果
  更新 SQLite 状态 → 返回用户
```

### 9.2 CLAUDE.md 配置文件设计

```markdown
# Project Configuration

## ECC Version
2.0.0-rc.1

## Installed Profiles
developer

## Active Language
typescript

## Project Context
[项目特定信息]

## Available Agents
[自动生成的 Agent 清单]

## Key Commands
[常用命令速查]
```

---

## 10. 工作流程设计

### 10.1 标准功能开发工作流

```
/feature-dev "实现用户注册功能"
     │
     ▼
[planner agent]
  ├── 分析需求：用户名、邮箱、密码、验证
  ├── 识别组件：API 路由、Service、Repository、Model
  ├── 制定计划：4 个子任务，预估 2h
  └── 输出：结构化实施计划
     │
     ▼
[tdd-guide skill + typescript-reviewer]
  ├── RED: 编写注册 API 测试
  │   └── POST /auth/register
  ├── GREEN: 实现最小注册逻辑
  │   ├── 输入验证（email格式、密码强度）
  │   ├── 用户已存在检查
  │   ├── 密码哈希（bcrypt）
  │   └── 创建用户记录
  └── REFACTOR: 提取验证工具函数
     │
     ▼
[security-reviewer agent]
  ├── ✅ 密码正确哈希（bcrypt, cost≥12）
  ├── ✅ 邮箱格式验证
  ├── ⚠️ 缺少速率限制（建议添加）
  └── ✅ 无敏感信息泄露
     │
     ▼
[code-reviewer agent]
  ├── ✅ 函数大小合规（<50行）
  ├── ✅ 错误处理完整
  └── ✅ 命名规范一致
     │
     ▼
[PostToolUse Hook]
  ├── Prettier 格式化
  └── 完成通知
```

### 10.2 Bug 修复工作流

```
"修复登录时偶发 500 错误"
     │
     ▼
[code-explorer agent]
  ├── 搜索相关代码
  ├── 追踪错误堆栈
  └── 定位根因
     │
     ▼
[tdd-guide skill]
  ├── RED: 编写复现 bug 的测试
  ├── GREEN: 修复最小变更
  └── REFACTOR: 确认无副作用
     │
     ▼
[code-reviewer + security-reviewer]
  └── 验证修复不引入新问题
```

### 10.3 代码审查工作流

```
/review-pr
     │
     ▼
[code-reviewer agent]
  ├── 全量扫描变更文件
  ├── 分类问题（CRITICAL/HIGH/MEDIUM/LOW）
  └── 生成审查报告
     │
     ▼ 并行
[security-reviewer]     [typescript-reviewer]
  ├── 安全漏洞检查      ├── 类型安全检查
  └── 敏感信息扫描      └── TS 最佳实践
     │
     ▼ 汇聚
  综合审查报告
  ├── CRITICAL 问题（必须修复）
  ├── HIGH 问题（强烈建议修复）
  ├── MEDIUM 问题（建议修复）
  └── 优点（值得肯定的地方）
```

---

## 11. 国际化设计

### 11.1 多语言文档结构

ECC 提供 7 种语言的完整文档翻译：

```
docs/
├── ja-JP/     # 日语
├── ko-KR/     # 韩语
├── pt-BR/     # 葡萄牙语（巴西）
├── ru/        # 俄语
├── tr/        # 土耳其语
├── zh-CN/     # 简体中文
└── zh-TW/     # 繁体中文
```

每种语言包含：

| 文件/目录 | 内容 |
|---------|------|
| `README.md` | 主文档翻译 |
| `AGENTS.md` | Agent 配置文档翻译 |
| `agents/` | 各 Agent 说明文档翻译 |
| `commands/` | 各命令说明翻译 |
| `skills/` | 各技能说明翻译 |
| `rules/` | 规则文档翻译 |

### 11.2 本地化规范

- 代码片段不翻译（保持英文）
- 技术术语保留原文，括号内提供翻译
- 示例代码中的注释可翻译
- 版本信息、日期、链接不翻译

---

## 12. 扩展点设计规范

### 12.1 创建新 Skill 规范

```bash
# 1. 创建技能目录
mkdir skills/my-skill

# 2. 创建技能文件（遵循标准结构）
cat > skills/my-skill/skill.md << 'EOF'
# My Skill Name

## When to Use
描述何时使用此技能...

## Prerequisites
- 前置条件列表

## Steps
### Phase 1: 准备
1. 步骤一
2. 步骤二

## Verification
- [ ] 验证项一
- [ ] 验证项二
EOF

# 3. 在 manifest 中注册（可选，用于选择性安装）
# 编辑 manifests/install-manifest.json 添加条目
```

### 12.2 创建新 Agent 规范

```bash
# 1. 创建 agent 文件
cat > agents/my-agent.md << 'EOF'
# My Agent Name

## Role
明确的角色定义（1-2 句话）...

## When to Use
- 触发场景 1
- 触发场景 2

## Workflow
1. 第一步操作
2. 第二步操作
3. 输出结果

## Output Format
[描述输出格式]

## Constraints
- 约束条件 1
- 不允许的行为
EOF

# 2. 在 AGENTS.md 和 CLAUDE.md 中更新 Agent 清单
```

### 12.3 添加自定义 Hook 规范

```javascript
// hooks/my-hook.js
module.exports = async function myHook(context) {
  const { tool_name, tool_input, event_type } = context;
  
  // 执行 hook 逻辑
  if (shouldIntervene(tool_input)) {
    return {
      action: 'block',
      reason: '安全策略阻止此操作'
    };
  }
  
  return { action: 'allow' };
};
```

**在 hooks.json 中注册：**
```json
{
  "id": "my-custom-hook",
  "event": "PreToolUse",
  "matcher": { "tool_name": "write_file" },
  "action": {
    "type": "script",
    "script": "hooks/my-hook.js"
  },
  "profile": ["developer", "full"]
}
```

### 12.4 添加新 MCP 服务器规范

```json
// mcp-configs/my-service.json
{
  "server_name": "my-service",
  "description": "我的服务描述",
  "command": "npx",
  "args": ["-y", "@my-org/my-mcp-server"],
  "env": {
    "MY_API_KEY": "${MY_SERVICE_API_KEY}"
  },
  "required_env": ["MY_SERVICE_API_KEY"],
  "tools": [
    "tool_one",
    "tool_two"
  ]
}
```

---

## 附录

### A. 核心文件索引

| 文件/路径 | 用途 |
|---------|------|
| `CLAUDE.md` | Claude Code 主配置文件，包含 ECC 核心行为规范 |
| `AGENTS.md` | Codex/通用 Agent 配置文件 |
| `agent.yaml` | Agent 清单元数据 |
| `hooks/hooks.json` | Hook 规则配置 |
| `scripts/ecc.js` | ECC CLI 主入口 |
| `scripts/install-apply.js` | 安装运行时核心 |
| `.mcp.json` | 项目级 MCP 服务器配置 |
| `manifests/` | 安装清单定义 |
| `VERSION` | 当前版本号 |
| `CHANGELOG.md` | 版本变更记录 |

### B. 性能设计考量

**上下文窗口管理：**
- 避免在上下文窗口使用率 >80% 时执行大型重构
- 使用 `strategic-compact` skill 进行手动上下文压缩
- 会话状态持久化到 SQLite 以支持跨会话续作

**Token 消耗优化：**
- `token-budget-advisor` skill 提供 token 消耗评估
- `context-budget` skill 管理上下文预算
- 大型任务分解为多个上下文独立的子任务

### C. 测试设计规范

**测试文件组织：**
```
tests/
├── unit/          # 单元测试（≥80% 覆盖率）
├── integration/   # 集成测试
└── e2e/           # E2E 测试（Playwright）
```

**测试命名约定：**
```typescript
describe('[模块名]', () => {
  describe('[函数名]', () => {
    it('should [预期行为] when [条件]', () => {
      // ...
    });
  });
});
```
