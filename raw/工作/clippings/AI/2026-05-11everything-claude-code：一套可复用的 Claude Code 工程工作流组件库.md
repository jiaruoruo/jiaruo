---
created: 2026-05-11T21:21:38 (UTC +08:00)
tags: []
source: http://www.uml.org.cn/ai/202602054.asp
author: 
---

# everything-claude-code：一套可复用的 Claude Code 工程工作流组件库

> ## Excerpt
> 

---
|                                                     **编辑推荐:**                                                     |
|---------------------------------------------------------------------------------------------------------------|
| 本文主要介绍了一套可复用的 Claude Code 工程工作流组件库：everything-claude-code相关知识。希望对你的学习有帮助。<br>本文来自于微信公众号AI贺贺，由火龙果软件Alice编辑，推荐。 |

![](http://www.uml.org.cn/ai/images/2026020514.png)

全文总结封面图

这个项目是什么

everything-claude-code 是一个面向 Claude Code（Anthropic 官方 CLI 编程助手） 的“全家桶”配置仓库/插件：把常用的 agents（子代理）、skills（工作流技能）、slash commands（斜杠命令）、rules（规则约束）、hooks（事件钩子自动化）、以及 MCP server 配置示例集中在一起，提供一套可直接复用的工程化工作流。

它更像是一个“可安装的 Claude Code 插件 + 参考实现集合”，目标是让 Claude Code 在真实项目里更像一个具备流程纪律的工程助手，而不是只会临时回答问题的聊天机器人。

README 的定位："This repo is the raw code only. The guides explain everything." —— 仓库提供的是配置与代码本体，配套指南负责讲清楚方法论与使用方式。

核心作用/解决什么问题

1.把高频工程能力产品化：将规划、架构评审、代码评审、安全审查、E2E、TDD 等能力沉淀为可调用的 agents/skills/commands。

2.把“怎么用 Claude Code”固化为流程：通过 rules + commands + hooks，将“先计划/先测试/再实现/再验证”的做事方式变成工具行为，而不是依赖使用者记忆。

3.减少跨项目迁移成本：提供一套通用的目录结构与可拷贝配置（手动安装）或插件安装方式（推荐）。

4.统一工具链与脚本习惯：内置包管理器选择/配置逻辑（npm/pnpm/yarn/bun 自动探测），以及测试运行脚本与示例。

主要组成（仓库结构概览 + 参考清单）

说明：以下清单主要依据该仓库 README 与目录命名进行盘点，用于“我该什么时候用什么”的速查。若你需要更精确的行为细节，建议再打开对应 .md 文件看提示词/约束原文。

.claude-plugin/（插件包装）

-   plugin.json：Claude Code 插件元数据（入口、包含哪些资源等）。
-   marketplace.json：marketplace 相关信息。

agents/（子代理：把任务委派给专职角色）

|        **Agent 文件**         |            **什么时候用**             |             **你会得到什么**             |
|-------------------------|------------------------------|--------------------------------|
|       planner.md        |   需求不清晰、要做一个功能/改造，且涉及多步实现时   |    分步骤实现计划、关键文件定位、风险点与验收口径     |
|      architect.md       |  需要做架构取舍（模块边界、扩展性、性能、技术选型）时  |      设计方案、权衡点、建议的目录/接口形态       |
|      tdd-guide.md       |  想用 TDD 写新功能/修 bug（先测试后实现）时  |      测试优先的落地步骤与覆盖率/边界用例建议      |
|    code-reviewer.md     |    写完一段代码（提交/PR 前）想做质量审查时    |  可维护性/一致性/潜在 bug/风格问题清单与修改建议   |
|  security-reviewer.md   | 涉及用户输入、鉴权、网络请求、文件处理、密钥/隐私数据时 |  OWASP 风险点、注入/越权/敏感信息等漏洞排查建议   |
| build-error-resolver.md | CI/本地 build 报错（TS/依赖/构建链路）时  |       最小改动修复编译/构建错误、定位原因       |
|      e2e-runner.md      |  关键用户路径需要端到端回归（Playwright）时  | 生成/维护/执行 E2E 用例与产物（截图/trace 等） |
|   refactor-cleaner.md   |     想删死代码、合并重复实现、降低维护成本时     |       基于工具的死代码扫描与安全删改建议        |
|     doc-updater.md      |  改了代码想同步文档/README/codemap 时  |        更新文档、补齐使用说明/变更点         |

skills/（技能：把方法论沉淀成可复用流程）

|       **Skill 目录**       |          **适用场景（怎么选）**           |           **覆盖内容**            |
|----------------------|------------------------------|---------------------------|
|  coding-standards/   |       你希望团队/项目有一致的编码规范       | TypeScript/JS/通用代码规范与最佳实践 |
|  backend-patterns/   |    做 API、服务端逻辑、数据库/缓存/队列等    |  后端架构模式、API 设计、性能与可维护性建议  |
|  frontend-patterns/  | 做 React/Next.js UI、状态管理、性能优化 |        前端工程模式与常见坑位        |
|    tdd-workflow/     |         想严格执行“测试先行”          |   TDD 流程、测试分层、覆盖率目标/策略    |
|   security-review/   |        做安全评估/上线前安全检查         |     安全检查清单、常见漏洞与修复建议      |
|  strategic-compact/  |      上下文变长、模型开始“遗忘/跑偏”       |      何时手动压缩、如何保留关键信息      |
| continuous-learning/ |      想把一次次会话产出沉淀成可复用模式       |    从会话提炼规则/技能的流程（偏方法论）    |
|  verification-loop/  |        想避免“说改好了但没验证”         |   验证闭环（跑测试/检查输出/给证据）流程    |
|    eval-harness/     |        需要做更系统的评估/回归框架        |     会话/修改的评估方法与框架化建议      |

commands/（斜杠命令：一键触发预设工作流）

|    **Command 文件**     |      **触发命令**       |      **什么时候用**       |          **会做什么**           |
|-------------------|-----------------|------------------|-------------------------|
|      tdd.md       |      /tdd       | 新功能/修 bug 想走 TDD |  引导“先写测试→最小实现→再重构/补边界”  |
|      plan.md      |      /plan      |      动手前先规划      |    产出实现计划、文件定位、验收标准     |
|      e2e.md       |      /e2e       |      关键路径回归      | 生成/运行 Playwright E2E 测试 |
|  code-review.md   |  /code-review   |  改完代码需要 review   |     启动评审流程（质量/一致性）      |
|   build-fix.md    |   /build-fix    | build/tsc/CI 报错  |      定位并做最小修复以恢复构建      |
| refactor-clean.md | /refactor-clean |      清理/重构       |      扫描死代码、收敛重复实现       |
|    verify.md y    |     /verif      |  改完要给出“已验证”的证据   |     跑测试/检查关键命令输出并汇总     |
|   checkpoint.md   |   /checkpoint   |  需要保存阶段性状态/验证点   |    记录当前状态，便于回滚思路或继续     |
|     learn.md      |     /learn      |  需要把本次会话经验沉淀下来   |     提炼可复用模式（面向未来复用）     |
|    setup-pm.md    |    /setup-pm    |   项目包管理器混乱/不统一   | 探测并配置 npm/pnpm/yarn/bun |

rules/（规则：常驻约束，限制助手行为）

|     **Rule 文件**     |    **作用**    |        **典型内容**        |
|-----------------|----------|--------------------|
|   security.md   |   安全底线   | 禁止泄漏密钥、避免注入/不安全操作等 |
| coding-style.md | 代码风格一致性  |    目录组织、命名、可读性等    |
|   testing.md    |   测试纪律   |   TDD/覆盖率目标/测试要求   |
| git-workflow.md | Git 流程规范 |   提交信息、分支/PR 习惯    |
|    agents.md    |  代理使用策略  |     何时委派、如何拆任务     |
| performance.md  | 性能与上下文管理 | 工具/模型选择、上下文窗口管理建议  |

hooks/ + scripts/hooks/（钩子：在关键事件点自动化）

-   hooks/hooks.json：Claude Code hooks 总配置（如 PreToolUse / PostToolUse / Stop 等事件）。
-   hooks/memory-persistence/：会话“记忆持久化”相关 hook（偏方法论与自动化）。
-   hooks/strategic-compact/：上下文压缩建议相关 hook。
-   scripts/hooks/*.js（Node 实现，跨平台）：
    -   session-start.js：会话开始加载上下文/状态。
    -   session-end.js：会话结束保存状态。
    -   pre-compact.js：压缩前保存状态/准备。
    -   suggest-compact.js：输出“战略性压缩”建议。
    -   evaluate-session.js：会话评估/提炼模式。

其他支撑目录

-   scripts/lib/：工具函数与包管理器探测逻辑（如 package-manager.js）。
-   mcp-configs/mcp-servers.json：MCP server 配置模板集合（把外部服务接进 Claude Code）。
-   tests/：测试用例与 tests/run-all.js。
-   contexts/：场景化上下文注入（dev.md/review.md/research.md）。
-   examples/：示例 CLAUDE.md 等。

它是如何工作的（概念协作）

-   commands（斜杠命令）：把一次“工作流动作”封装成可触发的命令（例如 plan/tdd/review）。
-   skills（技能）：承载“怎么做”的方法论与检查清单，可被命令或 agent 调用。
-   agents（子代理）：把复杂任务拆分给专用角色（规划/评审/测试/安全等），提高产出质量与一致性。
-   rules（规则）：限制/规范助手行为，避免跑偏（例如禁止某些危险操作、要求先读代码再改等）。
-   hooks（钩子）：在 Claude Code 的事件点自动执行脚本，进一步把流程自动化（比如在工具调用前后记录信息、提醒上下文窗口管理等）。

安装/使用方式（README 提供的两种路线）

1) 推荐：作为 Claude Code 插件安装

-   /plugin marketplace add affaan-m/everything-claude-code
-   /plugin install everything-claude-code@everything-claude-code

也可以在 ~/.claude/settings.json 里配置额外 marketplace 并启用插件（README 有 JSON 示例）。

2) 手动安装（按需拷贝）

-   将 agents/ rules/ commands/ skills/ 拷贝到 ~/.claude/ 对应目录
-   将 hooks/hooks.json 合并进 ~/.claude/settings.json
-   将 mcp-configs/mcp-servers.json 中需要的 MCP server 配置拷贝到 ~/.claude.json（并替换密钥占位符）

额外：包管理器自动探测/设置

仓库内置包管理器选择逻辑，支持：

-   环境变量 CLAUDE_PACKAGE_MANAGER
-   node scripts/setup-package-manager.js --global|--project|--detect
-   Claude Code 命令 /setup-pm

Claude Code 概念速查：触发场景 + 怎么用

![](http://www.uml.org.cn/ai/images/2026020524.png)

Claude Code 组件机制总览

![](http://www.uml.org.cn/ai/images/2026020534.png)

Claude Code Hooks 触发生命周期

![](http://www.uml.org.cn/ai/images/2026020544.png)

Skills：触发、配置与运行

![](http://www.uml.org.cn/ai/images/2026020554.png)

everything-claude-code：目录结构与映射

![](http://www.uml.org.cn/ai/images/2026020564.png)

Claude Code：组件选型决策树

这一节补充 Claude Code 里几个核心概念（skills / subagents / hooks / rules / commands）在什么场景会被触发、以及你该怎么用。这能帮助你把 everything-claude-code 这类“组件仓库”对齐到 Claude Code 的官方机制。

1) Skills（技能 / 自定义 slash command）

它是什么

-   一个目录 .../skills/<skill-name>/SKILL.md（必须）+ 可选的 supporting files。
-   SKILL.md 顶部 YAML frontmatter 里的 name 决定了命令名 /skill-name；description 用于让 Claude 判断何时自动加载。
-   Claude Code 文档说明：Custom slash commands 已合并进 skills，所以 .claude/commands/review.md 与 .claude/skills/review/SKILL.md 都可以提供 /review，但 skill 优先。

什么时候触发

-   手动触发：你在对话里输入 /skill-name ...args。
-   模型自动触发：当 skill 的 description 与用户问题/上下文匹配，且没有设置 disable-model-invocation: true 时。

怎么用（实操要点）

-   通过 frontmatter 控制“谁能触发”：
    -   disable-model-invocation: true：只允许你手动 /name 触发（适合有副作用的流程，如 deploy/commit）。
    -   user-invocable: false：从 / 菜单隐藏；通常用于“背景知识型 skill”。
-   通过 allowed-tools 限制 skill 执行期的工具权限（例如只读）。
-   通过 $ARGUMENTS 接收 /skill-name 后的参数。
-   支持 context: fork + agent: Explore/Plan/... 让 skill 在隔离子代理里跑（适合大吞吐研究）。

典型选择指南

-   你要“可复用的一段流程/提示词（可能带参数）”→ 用 Skill。
-   你要“这次任务专门找文件/总结，不想污染主上下文”→ 用 context: fork 的 Skill 或直接用 Subagent。

2) Subagents（子代理 / Task tool）

它是什么

-   专用 AI 助手，独立上下文窗口 + 自己的系统提示词 + 可配置工具权限/模型。
-   既有内置（Explore/Plan/general-purpose 等），也可在 .claude/agents/、~/.claude/agents/ 或插件里定义自定义 subagent。

什么时候触发

-   Claude 会依据 subagent 的 description 自动委派（delegation）。
-   你也可以显式要求：例如“用 code-reviewer subagent 看一下最近改动”。

怎么用（实操要点）

-   内置 subagents（官方定义）：
    -   Explore：快速、只读，擅长 Glob/Grep/Read 做代码库探索（文档：read-only tools，拒绝 Write/Edit）。
    -   Plan：计划模式下做研究（只读），用于产出计划前的代码检索。
    -   general-purpose：需要读写改动 + 多步操作时。

-   Subagent frontmatter（自定义 agent）里可配置：
    -   tools / disallowedTools：白名单/黑名单工具。
    -   permissionMode：default / acceptEdits / dontAsk / bypassPermissions / plan。
    -   skills：把某些 skills 全文预加载进 subagent 上下文（注意：subagents 不继承主对话 skills，需要显式列）。

-   子代理适合隔离“高输出任务”（跑测试、拉大量 diff、分析日志等），只把摘要回传主对话。

3) Hooks（事件钩子：自动化）

它是什么

-   在 Claude Code session 生命周期的特定事件点自动执行：
    -   type: command（执行 shell 命令脚本）
    -   type: prompt（LLM 评估，输出 JSON 决定 allow/block 等）

-   可配置位置：用户级 ~/.claude/settings.json、项目级 .claude/settings.json、插件 hooks 等。

什么时候触发（官方生命周期）

|              **Hook**               |          **触发时机**           |
|---------------------------------|-------------------------|
|          SessionStart           |         会话开始/恢复         |
|        UserPromptSubmit         | 用户提交 prompt（Claude 处理前） |
|           PreToolUse            |          工具调用前          |
|        PermissionRequest        |         出现权限弹窗时         |
| PostToolUse/ PostToolUseFailure |        工具成功/失败后         |
|   SubagentStart/ SubagentStop   |        子代理启动/结束         |
|              Stop               |     Claude 本轮回复结束时      |
|           PreCompact            |        compact 前        |
|           SessionEnd            |          会话结束           |
|          Notification           |    Claude Code 发通知时     |

怎么用（实操要点）

-   matcher 用来匹配工具名（如 Write|Edit）或用正则匹配 MCP tool（如 mcp__memory__.*）。
-   SessionStart、UserPromptSubmit 等可以向对话注入额外上下文（stdout/additionalContext）。
-   PreToolUse 可以通过 JSON 输出做 permissionDecision: allow/deny/ask，实现“自动放行/拦截/要求确认”。
-   强提醒：hooks 能执行任意命令，有安全风险；要严格审计。

4) Rules（规则约束）

它是什么

-   一组“长期有效的行为约束/偏好”，通常作为系统提示词的一部分存在（在 everything-claude-code 里是 rules/*.md）。

什么时候生效

-   只要规则文件被加载进当前会话/插件配置的有效范围，就会持续影响 Claude 的行为（不像 skill 需要触发）。

怎么用（实操要点）

-   把规则分成：安全底线、代码风格、测试纪律、git 流程、代理使用策略、性能/上下文管理。
-   规则适合写“永远要这样做”的东西；一次性流程用 skill。

5) Commands（斜杠命令）

它是什么

-   从官方机制看，自定义 commands 已并入 skills：一个 skill 自然就是一个 /command。
-   仍兼容旧的 .claude/commands/*.md，但推荐迁移成 skills（支持 supporting files / invocation control / fork subagent 等）。

什么时候触发

-   你输入 /xxx（或 Claude 在某些实现里会主动建议你用某个 /xxx 工作流）。

总结（一句话）

everything-claude-code 提供了一套可安装、可迁移、可组合的 Claude Code 工程化工作流组件库：用 agents/skills/commands/rules/hooks 把“规划→实现→评审→测试→验证”的软件工程节奏固化到工具里。
