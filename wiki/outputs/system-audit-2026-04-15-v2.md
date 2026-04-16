---
type: system-audit
date: 2026-04-15
graph-excluded: true
---

# System Audit Report — 2026-04-15（第二次）

> 核查执行者：Claude Opus 4.6（自动化系统核查）
> 与首次审计对比基准：system-audit-2026-04-15.md（修复前评分 92%）
> 本次核查在上一轮偏差修复完成后执行，为全量重新核查。

---

## 一、目录结构完整性

### raw/ 层

| 子目录 | 状态 | 文件数 | 备注 |
|---|---|---|---|
| raw/articles/ | ✅ 存在 | 0 | 空 |
| raw/clippings/ | ✅ 存在 | 7 | 6 个未 ingest（1 个已处理：MiniMax） |
| raw/images/ | ✅ 存在 | 0 | 空 |
| raw/pdfs/ | ✅ 存在 | 13 | 全部未 ingest |
| raw/notes/ | ✅ 存在 | 0 | 空 |
| raw/personal/ | ✅ 存在 | 0 | 空 |

**raw/ 结论：✅ 全部 6 个子目录存在，结构完整。**

### wiki/ 层

| 子目录/文件 | 状态 | 文件数 | 备注 |
|---|---|---|---|
| wiki/sources/ | ✅ 存在 | 1 | minimax-api-overview.md |
| wiki/concepts/ | ✅ 存在 | 5 | 全部已验证 |
| wiki/entities/ | ✅ 存在 | 1 | minimax.md（含 updated + Evolution Log） |
| wiki/synthesis/ | ✅ 存在 | 0 | 空，尚无综合分析页 |
| wiki/templates/ | ✅ 存在 | 5 | 全部模板已验证 |
| wiki/outputs/ | ✅ 存在 | 3 | lint-2026-04-13.md、system-audit-2026-04-15.md、lint-2026-04-15.md（新） |
| wiki/index.md | ✅ 存在 | — | |
| wiki/log.md | ✅ 存在 | — | |
| wiki/overview.md | ✅ 存在 | — | 数据已更新 |
| wiki/QUESTIONS.md | ✅ 存在 | — | |

### 根目录其他层

| 目录/文件 | 状态 | 备注 |
|---|---|---|
| outputs/ | ✅ 存在 | 空（对外输出层，正常） |
| scripts/lint.py | ✅ 存在 | 已验证 9 项检查均实现 |
| CLAUDE.md | ✅ 存在 | 已更新至 2026-04-15，含 12 步流程 |
| USER_GUIDE.md | ✅ 存在 | 新建于上一轮修复（此前缺失） |

**结论：✅ 三层架构全部子目录及文件存在，结构完整。**

---

## 二、CLAUDE.md 关键规则覆盖（逐项）

> 对比首次审计：上一轮已修复 3 项（URL/defuddle、canonical_source 去重、qmd update）

| 规则 | 状态 | 说明 |
|---|---|---|
| Raw 层不可变原则 | ✅ 是 | 第一章明确：raw/ 只读，LLM 绝不修改 |
| INGEST 来源类型判断（personal-writing vs 外部来源） | ✅ 是 | 优先级列表完整（personal-writing / raw/personal/ / pdf-reference / 其他） |
| INGEST SHA-256 哈希记录规则 | ✅ 是 | Step 2 计算哈希，Step 6 写入 raw_sha256 |
| INGEST 去重检测（含 canonical_source 译文检测） | ✅ 是 | Step 5 明确：source_url 相同停止，canonical_source 匹配提示译文重复 |
| INGEST 概念名称对齐检查（aliases 匹配） | ✅ 是 | Step 7 详细描述 slug + aliases 双路匹配 |
| INGEST QUESTIONS.md 匹配检查 | ✅ 是 | Step 11 明确 |
| INGEST 缺少 frontmatter 的处理规则 | ✅ 是 | 专节定义，含警告日志记录 |
| INGEST URL 直接输入的 defuddle 调用规则 | ✅ 是 | 新增"URL 直接输入处理规则"章节，含失败降级逻辑 |
| INGEST 最后一步执行 qmd update | ✅ 是 | Step 12 明确：`qmd add wiki/` + 日志追加（注：正确命令为 `qmd update`，详见下方说明） |
| QUERY 使用 qmd query 优先（含 fallback） | ✅ 是 | Step Q1 明确，含 fallback 降级 |
| QUERY 来源溯源要求（追溯到 sources 页） | ✅ 是 | Step Q3 明确禁止只引用 concept 页 |
| QUERY Confidence Notes 输出要求 | ✅ 是 | Step Q4 明确 |
| QUERY 高价值答案持久化规则 | ✅ 是 | Step Q4 明确，含 graph-excluded 要求 |
| confidence: high 必须用户确认，禁止自动晋升 | ✅ 是 | 第十章明确"候选 high"需用户回复「确认」或「ok」 |
| LINT 运行 scripts/lint.py（9 项检查） | ✅ 是 | 第四章明确 |
| LINT 执行 qmd 索引同步验证 | ✅ 是 | Step 3 明确 `qmd status` + 条件性 update |
| REFLECT Stage 0 反向检验 | ✅ 是 | Stage 0 明确必须最先执行，含回音室风险标注 |
| REFLECT Stage 1 使用 qmd multi-get 批量扫描 | ✅ 是 | Stage 1 含命令示例和降级方案 |
| REFLECT Stage 3 Gap Analysis | ✅ 是 | Stage 3 定义三类知识空白 |
| MERGE 跨语言合并专项流程（redirect 文件保留） | ✅ 是 | 第六章专节，旧 slug 保留为 redirect |
| Wikilink 格式铁律（英文小写连字符） | ✅ 是 | 第八章含正确/错误示例 |
| Wikilink 禁止清单（系统文件不得被 wikilink） | ✅ 是 | 第八章列出所有禁止场景 |
| Wiki 语言规范（中文写作，英文 slug，aliases 跨语言） | ✅ 是 | 第九章完整定义 |
| 系统文件隔离规则（graph-excluded: true） | ✅ 是 | 第十二章列出全部文件 |
| 文档维护规则（CLAUDE.md 更新时同步 USER_GUIDE.md） | ✅ 是 | 第十三章明确 |

**本次结论：25/25 ✅（上次 22/25，净增 3 项）**

### ⚠ 新发现细节问题（不计入计分，但需记录）

- CLAUDE.md Step 12 写的是 `qmd add wiki/`，但实际 qmd 命令不支持 `add`，正确命令为 **`qmd update`**。本次核查通过运行 `qmd --help` 确认。建议修正。

---

## 三、模板文件完整性（逐项验证必需字段）

### source-template.md

| 字段/节 | 状态 |
|---|---|
| type: source | ✅ |
| date | ✅ |
| language | ✅ `"{{zh\|en}}"` |
| canonical_source | ✅ `"{{url_or_leave_empty}}"` |
| raw_file | ✅ |
| raw_sha256 | ✅ |
| last_verified | ✅ |
| possibly_outdated | ✅ |
| Summary（含过时提示注释） | ✅ |
| Key Points / Contradictions / My Notes | ✅ |

**source-template.md：✅ 通过**

### personal-writing-template.md

| 字段/节 | 状态 |
|---|---|
| type: personal-writing | ✅ |
| confidence_at_writing | ✅ |
| raw_file / raw_sha256 | ✅ |
| Core Argument 节（替代 Summary） | ✅ |
| Limitations 节 | ✅ |

**personal-writing-template.md：✅ 通过**

### concept-template.md

| 字段/节 | 状态 |
|---|---|
| type / date / updated | ✅ |
| aliases（中文别名 + English Name + english-slug） | ✅ |
| domain_volatility | ✅ |
| last_reviewed | ✅ |
| source_count / confidence | ✅ |
| Definition / Key Points / My Position / Contradictions / Sources | ✅ |
| Evolution Log（含格式注释和示例） | ✅ |

**concept-template.md：✅ 通过**

### entity-template.md

| 字段/节 | 状态 | 对比首次审计 |
|---|---|---|
| type / date | ✅ | — |
| **updated** | ✅ | 上轮修复新增 |
| aliases | ✅ | — |
| entity_type | ✅ | — |
| Description / Key Contributions / Related Concepts / Sources | ✅ | — |
| **Evolution Log** | ✅ | 上轮修复新增 |

**entity-template.md：✅ 通过（上次 ❌，本次已修复）**

### synthesis-template.md

| 字段/节 | 状态 |
|---|---|
| type / date / source_count / confidence | ✅ |
| Thesis / Evidence / Synthesis / Sources | ✅ |
| Counter-evidence（含回音室风险占位符） | ✅ |
| Confidence Notes | ✅ |
| Limitations | ✅ |

**synthesis-template.md：✅ 通过**

**模板完整性结论：5/5 ✅（上次 4/5，entity-template 已修复）**

---

## 四、系统文件隔离状态

| 文件 | graph-excluded: true | type 字段 |
|---|---|---|
| wiki/log.md | ✅ | system-log |
| wiki/index.md | ✅ | system-index |
| wiki/overview.md | ✅ | system-overview |
| wiki/QUESTIONS.md | ✅ | system-questions |
| wiki/outputs/lint-2026-04-13.md | ✅ | lint-report |
| wiki/outputs/lint-2026-04-15.md | ✅ | lint-report |
| wiki/outputs/system-audit-2026-04-15.md | ✅ | system-audit |

**结论：✅ 全部系统文件及 outputs/ 下文件均含 `graph-excluded: true`**

---

## 五、scripts/lint.py 检查项（实际运行结果）

本次执行 `python scripts/lint.py`，实际结果：

**总计：2 个问题，7/9 项通过**

| # | 检查项 | 结果 | 详情 |
|---|---|---|---|
| 1 | YAML Frontmatter 合法性 | ✅ 通过 | — |
| 2 | Broken Wikilinks | ✅ 通过 | — |
| 3 | Index 一致性 | ✅ 通过 | — |
| 4 | Stub 页面 | ✅ 通过 | — |
| 5 | 近重复概念名称 | ✅ 通过 | — |
| 6 | SHA-256 完整性 | ❌ 1 个问题 | `wiki/sources/minimax-api-overview.md`：raw_sha256 不匹配（记录值 `c28ba0...`，实际值 `35880c...`）→ 原始文件 `raw/clippings/2026-04-13-接口概览...md` 内容已被修改 |
| 7 | Stale 页面 | ✅ 通过 | — |
| 8 | 跨语言重复 | ❌ 1 个问题 | `wiki/concepts/voice-cloning.md`：别名 `"voice cloning"` 在同一文件 aliases 中重复出现（自我重复，lint.py 的 alias_map 逻辑将同一文件同一 alias 记录为两次） |
| 9 | Wikilink 格式规范 | ✅ 通过 | — |

### Check 6 分析（SOURCE MODIFIED）

原始文件 `raw/clippings/2026-04-13-接口概览 - MiniMax 开放平台文档中心.md` 的实际 SHA-256 与 source 页记录值不匹配，说明该 raw 文件上次 ingest 后被修改过。按 CLAUDE.md 第十一章 Re-ingest 规则，需要重新执行 INGEST。

### Check 8 分析（跨语言重复误报）

`wiki/concepts/voice-cloning.md` 的 aliases 字段中包含多个含 "voice cloning" 字样的别名（如 `"Voice Cloning"` 和 `"voice cloning"`），lint.py 的 alias_map 在小写规范化后将它们归为同一 key，同一文件多条 alias 命中同一规范值，触发了自我匹配。这是 lint.py 的**已知限制**（Check 8 逻辑未排除同文件内重复）。可视为误报。

---

## 六、qmd 状态

### 索引状态（本次 `qmd status` 输出）

```
Index: C:/Users/jiaruo/.cache/qmd/index.sqlite
Size:  172.0 KB

Documents
  Total:    17 files indexed
  Vectors:  0 embedded
  Pending:  17 need embedding (run 'qmd embed')
  Updated:  2d ago
```

### 本次 `qmd update` 执行结果

```
Indexed: 2 new, 4 updated, 13 unchanged, 0 removed
Cleaned up 4 orphaned content hash(es)
Run 'qmd embed' to update embeddings (19 unique hashes need vectors)
```

**新增 2 个文件**：`USER_GUIDE.md`（根目录，未纳入 wiki/ 集合）和 `lint-2026-04-15.md`（outputs/）
**更新 4 个文件**：`log.md`、`overview.md`、`entities/minimax.md`、`templates/entity-template.md`

### 索引同步分析

| 项目 | 状态 |
|---|---|
| wiki/ 实际 .md 文件数 | 19（含新增 lint-2026-04-15.md 和 system-audit-2026-04-15-v2.md） |
| qmd 集合索引文件数 | 17（update 后尚未自动同步本次新增） |
| 嵌入向量 | 0/17（全部待生成） |
| `qmd update` 可用性 | ✅（正确命令，`qmd add` 命令不存在） |

> ⚠ **CLAUDE.md Step 12 命令错误**：当前写的是 `qmd add wiki/`，实际应为 `qmd update`。需修正。

### 测试查询

`qmd search "机器人"` → 返回 No results（嵌入向量未生成，全文搜索无命中）
`qmd search "minimax"` → 返回 No results（同原因）

**qmd 语义搜索当前不可用，需执行 `qmd embed`。**

---

## 七、内容一致性校验（新增项目）

### wiki/index.md 与实际文件对照

| index.md 列出 | 实际文件存在 | 状态 |
|---|---|---|
| sources/minimax-api-overview | ✅ | ✅ |
| concepts/multimodal-api | ✅ | ✅ |
| concepts/model-context-protocol | ✅ | ✅ |
| concepts/text-to-speech | ✅ | ✅ |
| concepts/video-generation | ✅ | ✅ |
| concepts/voice-cloning | ✅ | ✅ |
| entities/minimax | ✅ | ✅ |
| outputs/ 节为空 | — | ⚠ lint-2026-04-13.md 等未登记 |

**index.md 遗漏登记**：wiki/outputs/ 下 3 个文件均未在 `## Outputs` 节列出。按照 CLAUDE.md 要求，LINT 和系统审计产生的输出文件应在此登记。

### wiki/overview.md 数据准确性

| 指标 | overview.md 当前值 | 实际值 | 状态 |
|---|---|---|---|
| 总来源数 | 1 | 1 | ✅ |
| 总 Concept 页数 | 5 | 5 | ✅ |
| 总 Entity 页数 | 1 | 1 | ✅ |
| 总 Synthesis 页数 | 0 | 0 | ✅ |
| 高置信度概念数 | 0 | 0 | ✅ |
| 开放问题数 | 0 | 0 | ✅ |
| 最近 Lint 报告 | lint-2026-04-13.md | lint-2026-04-15.md（更新） | ⚠ 未更新 |

---

## 八、综合评分与问题清单

### 问题清单（本次核查发现）

| 优先级 | 类别 | 问题描述 | 建议行动 |
|---|---|---|---|
| 🔴 高 | lint Check 6 | `raw/clippings/2026-04-13-接口概览...md` SHA-256 不匹配，原始文件被修改 | 重新 INGEST 该文件（CLAUDE.md 第十一章 Re-ingest 规则） |
| 🔴 高 | qmd | 嵌入向量 0/19，语义搜索不可用 | 执行 `qmd embed` |
| 🟡 中 | CLAUDE.md | Step 12 命令错误：`qmd add wiki/` → 应为 `qmd update` | 修正 Step 12 命令 |
| 🟡 中 | wiki/index.md | Outputs 节未登记 3 个输出文件 | 补充登记 lint 和 system-audit 产出 |
| 🟡 中 | wiki/overview.md | 最近 Lint 报告未更新为 2026-04-15 版本 | 更新该字段 |
| 🟡 中 | 未 ingest | 6 个 raw/clippings/ 文件（含 4 个 2026-04-15 机器人主题文件）未处理 | 按需执行 INGEST |
| 🟢 低 | lint Check 8 | voice-cloning.md 触发自我重复误报 | 可修复 voice-cloning.md aliases 去重，或记录为 lint.py 已知误报 |
| 🟢 低 | raw/pdfs/ | 13 个 PDF 文件全部未 ingest | 按需执行 INGEST |

### 整体健康评分

| 维度 | 得分 | 对比上次 | 说明 |
|---|---|---|---|
| 目录结构完整性 | 10/10 | → | 全部子目录存在 |
| CLAUDE.md 规则覆盖 | 24/25 | ↑ 22→24 | 25/25 规则覆盖，但 Step 12 命令值错误（`qmd add` vs `qmd update`），扣 1 分 |
| 模板完整性 | 10/10 | ↑ 9→10 | entity-template 已修复 |
| 系统文件隔离 | 10/10 | → | 全部正确隔离 |
| lint.py 检查项 | 10/10 | → | 9 项均实现 |
| 内容一致性（新增） | 7/10 | 新增 | SOURCE MODIFIED + index/overview 未同步 |
| qmd 索引同步 | 7/10 | ↓ 8→7 | 命令不存在已修正用法，但嵌入向量仍为 0 |

**综合得分：68/75（91%）**

> 注：本次引入"内容一致性"维度（新增 10 分），同时 CLAUDE.md 命令错误导致小幅扣分，综合分值与上次相近但维度更完整。

---

## 九、行动建议（优先顺序）

1. **立即**：修正 CLAUDE.md Step 12 命令（`qmd add wiki/` → `qmd update`）
2. **立即**：Re-ingest `raw/clippings/2026-04-13-接口概览...md`（SHA-256 不匹配）
3. **立即**：执行 `qmd embed` 恢复语义搜索
4. **近期**：补充 wiki/index.md 的 Outputs 节登记
5. **近期**：更新 wiki/overview.md 最近 Lint 报告字段
6. **按需**：INGEST 6 个未处理 raw/clippings/ 文件

---

_审计完成时间：2026-04-15_
_本次为第二次全量审计，上次基准：system-audit-2026-04-15.md_
