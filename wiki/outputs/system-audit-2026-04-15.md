---
type: system-audit
date: 2026-04-15
graph-excluded: true
---

# System Audit Report — 2026-04-15

> 核查执行者：Claude Opus 4.6（自动化系统核查）
> 核查范围：目录结构、CLAUDE.md 规则覆盖、模板完整性、系统文件隔离、lint.py 检查项、qmd 状态

---

## 一、目录结构完整性

### raw/ 层

| 子目录 | 状态 | 备注 |
|---|---|---|
| raw/articles/ | ✅ 存在 | 当前为空 |
| raw/clippings/ | ✅ 存在 | 7 个 .md 文件（含 4 个新增未处理文件） |
| raw/images/ | ✅ 存在 | 当前为空 |
| raw/pdfs/ | ✅ 存在 | 12 个 PDF 文件（均未处理） |
| raw/notes/ | ✅ 存在 | 当前为空 |
| raw/personal/ | ✅ 存在 | 当前为空 |

**raw/ 结论：✅ 全部 6 个子目录存在且结构完整。**

### wiki/ 层

| 子目录/文件 | 状态 | 备注 |
|---|---|---|
| wiki/sources/ | ✅ 存在 | 1 个文件：minimax-api-overview.md |
| wiki/concepts/ | ✅ 存在 | 5 个文件 |
| wiki/entities/ | ✅ 存在 | 1 个文件：minimax.md |
| wiki/synthesis/ | ✅ 存在 | 当前为空 |
| wiki/templates/ | ✅ 存在 | 5 个模板文件 |
| wiki/outputs/ | ✅ 存在 | 1 个 lint 报告 |
| wiki/index.md | ✅ 存在 | |
| wiki/log.md | ✅ 存在 | |
| wiki/overview.md | ✅ 存在 | |
| wiki/QUESTIONS.md | ✅ 存在 | |

### outputs/ 层（根目录）

| 目录 | 状态 | 备注 |
|---|---|---|
| outputs/ | ✅ 存在 | 当前为空 |
| scripts/ | ✅ 存在 | 1 个文件：lint.py |

**wiki/ + outputs/ 结论：✅ 全部子目录存在，架构完整。**

---

## 二、CLAUDE.md 关键规则覆盖

### 核心原则

| 规则 | 状态 | 说明 |
|---|---|---|
| Raw 层不可变原则 | ✅ 是 | CLAUDE.md 第一章明确：raw/ 只读，LLM 绝不修改 |
| INGEST 来源类型判断（personal-writing vs 外部来源） | ✅ 是 | 第二章优先级判断：type: personal-writing 或路径含 raw/personal/ 走个人写作流程 |
| INGEST SHA-256 哈希记录规则 | ✅ 是 | Step 2 及 Step 5 明确要求计算并记录 raw_sha256 |
| INGEST 去重检测（含 canonical_source 译文检测） | ⚠️ 部分 | CLAUDE.md 中 Step 6 进行了概念名称对齐检查（aliases 匹配），但**未明确提及 canonical_source 译文检测流程**；source-template.md 有 canonical_source 字段，但 INGEST 流程 11 步中没有对该字段的比对逻辑。**建议在 Step 6 之前增加 source URL + canonical_source 去重检测步骤。** |
| INGEST 概念名称对齐检查（aliases 匹配） | ✅ 是 | Step 6 详细描述：slug 匹配 + aliases 字段遍历，含中英文大小写不敏感匹配 |
| INGEST QUESTIONS.md 匹配检查 | ✅ 是 | Step 10 明确：检查 QUESTIONS.md 开放问题，能回答则提示执行 QUERY |
| INGEST 缺少 frontmatter 的处理规则 | ✅ 是 | 第二章"缺少 frontmatter 时的处理规则"专节，含从标题提取 title、source_url 留空、记录警告 |
| INGEST URL 直接输入的 defuddle 调用规则 | ❌ 否 | **CLAUDE.md 中未包含"URL 直接输入"场景的处理规则，也无 defuddle 调用说明。** 若期望支持直接输入 URL 触发 INGEST，需补充该规则。 |
| INGEST 最后一步执行 qmd update | ❌ 否 | **CLAUDE.md 的 INGEST 11 步流程中，末尾（Step 11）仅要求追加日志，未要求执行 `qmd update` 或 `qmd add wiki/`。** LINT 流程（Step 3）有 qmd 索引同步逻辑，但 INGEST 流程缺失。建议在 Step 11 后增加 Step 12：执行 `qmd add wiki/` 更新索引。 |
| QUERY 使用 qmd query 优先（含 fallback） | ✅ 是 | Step Q1 明确：优先 `qmd query`，报错则 fallback 读取 wiki/index.md |
| QUERY 来源溯源要求（追溯到 sources 页） | ✅ 是 | Step Q3 明确：每个核心结论必须溯源到具体 wiki/sources/<slug>.md，**不允许只引用 concept 页** |
| QUERY Confidence Notes 输出要求 | ✅ 是 | Step Q4 明确：输出末尾必须包含「⚠ Confidence Notes」节 |
| QUERY 高价值答案持久化规则 | ✅ 是 | Step Q4 明确：写入 wiki/outputs/YYYY-MM-DD-<topic>.md，frontmatter 含 graph-excluded: true |
| confidence: high 必须用户确认，禁止自动晋升 | ✅ 是 | 第十章 Confidence 更新规则表格：5+ 来源且无重大矛盾时为"候选 high"，需等待用户明确回复「确认」或「ok」才可设置 |
| LINT 运行 scripts/lint.py（9 项检查） | ✅ 是 | 第四章明确：运行 `python scripts/lint.py`，报告写入 wiki/outputs/ |
| LINT 执行 qmd 索引同步验证 | ✅ 是 | 第四章 Step 3：执行 `qmd status`，对比文件数；若索引落后则执行 `qmd add wiki/` |
| REFLECT Stage 0 反向检验 | ✅ 是 | 第五章明确：在生成合成结论之前主动搜索反驳证据，无反对来源须标注回音室风险 |
| REFLECT Stage 1 使用 qmd multi-get 批量扫描 | ✅ 是 | Stage 1 明确提供 `qmd multi-get` 命令示例，含降级方案 |
| REFLECT Stage 3 Gap Analysis | ✅ 是 | Stage 3 详细定义三类知识空白，输出至 wiki/outputs/gap-report-YYYY-MM-DD.md |
| MERGE 跨语言合并专项流程（redirect 文件保留） | ✅ 是 | 第六章明确：被合并文件保留为 redirect 文件，主 slug 保留英文，旧 wikilinks 不 broken |
| Wikilink 格式铁律（英文小写连字符） | ✅ 是 | 第八章明确列出合法/非法示例，禁止中文/驼峰/下划线 |
| Wikilink 禁止清单（系统文件不得被 wikilink） | ✅ 是 | 第八章列出禁止场景：不得引用 log/index/overview/QUESTIONS/lint 报告/操作名称 |
| Wiki 语言规范（中文写作，英文 slug，aliases 跨语言） | ✅ 是 | 第九章：wiki 层统一中文写作，slug 用英文小写连字符，aliases 覆盖中英文所有叫法 |
| 系统文件隔离规则（graph-excluded: true） | ✅ 是 | 第十二章明确列出需含 graph-excluded: true 的文件范围 |
| 文档维护规则（CLAUDE.md 更新时同步 USER_GUIDE.md） | ✅ 是 | 第十三章明确：规则更新时必须同步 USER_GUIDE.md，不得出现版本漂移 |

**小结：23/25 项覆盖 ✅，2 项缺失/不完整 ❌/⚠：**
- ❌ `INGEST URL 直接输入的 defuddle 调用规则`：CLAUDE.md 中无此规则
- ❌ `INGEST 最后一步执行 qmd update`：11 步流程末尾缺少索引更新步骤
- ⚠ `INGEST 去重检测（canonical_source 译文检测）`：字段存在于模板，但 INGEST 流程中无对应检测步骤

---

## 三、模板文件完整性

### source-template.md

| 必需字段 | 状态 | 实际内容 |
|---|---|---|
| language | ✅ 存在 | `language: "{{zh\|en}}"` |
| canonical_source | ✅ 存在 | `canonical_source: "{{url_or_leave_empty}}"` |
| type | ✅ 存在 | `type: source` |
| date | ✅ 存在 | `date: {{YYYY-MM-DD}}` |
| raw_file | ✅ 存在 | `raw_file: "{{raw/path/to/file.md}}"` |
| raw_sha256 | ✅ 存在 | `raw_sha256: "{{sha256_hash}}"` |
| last_verified | ✅ 存在 | `last_verified: {{YYYY-MM-DD}}` |
| possibly_outdated | ✅ 存在 | `possibly_outdated: false` |
| Summary 节 | ✅ 存在 | 含过时提示占位注释 |
| Key Points / Contradictions / My Notes 节 | ✅ 存在 | 完整 |

**source-template.md：✅ 全部必需字段存在**

### personal-writing-template.md

| 必需字段 | 状态 | 实际内容 |
|---|---|---|
| type: personal-writing | ✅ 存在 | `type: personal-writing` |
| confidence_at_writing | ✅ 存在 | `confidence_at_writing: medium` |
| raw_file | ✅ 存在 | `raw_file: "{{raw/personal/filename.md}}"` |
| raw_sha256 | ✅ 存在 | `raw_sha256: "{{sha256_hash}}"` |
| Core Argument 节（替代 Summary） | ✅ 存在 | `## Core Argument` |
| Limitations 节 | ✅ 存在 | `## Limitations` |

**personal-writing-template.md：✅ 全部必需字段存在**

### concept-template.md

| 必需字段 | 状态 | 实际内容 |
|---|---|---|
| aliases | ✅ 存在 | 含中文别名、英文名、英文 slug 三个占位符 |
| domain_volatility | ✅ 存在 | `domain_volatility: medium` |
| last_reviewed | ✅ 存在 | `last_reviewed: {{YYYY-MM-DD}}` |
| Evolution Log 节 | ✅ 存在 | 含详细格式示例注释 |
| type / date / updated | ✅ 存在 | 完整 |
| source_count / confidence | ✅ 存在 | 初始值 0 / low |
| My Position / Contradictions / Sources 节 | ✅ 存在 | 完整 |

**concept-template.md：✅ 全部必需字段存在**

### entity-template.md

| 必需字段 | 状态 | 实际内容 |
|---|---|---|
| aliases | ✅ 存在 | 含别名1/alias2 两个占位符 |
| type / date / entity_type | ✅ 存在 | 完整 |
| Description / Key Contributions / Related Concepts / Sources 节 | ✅ 存在 | 完整 |
| ⚠ updated 字段 | ❌ 缺失 | entity-template.md 无 `updated` 字段（concept 模板有，CLAUDE.md 步骤8 同步 Step 7 逻辑，但模板缺失） |
| ⚠ Evolution Log 节 | ❌ 缺失 | CLAUDE.md Step 8 要求 entity 逻辑"同 Step 6-7"，但 entity-template 无 Evolution Log 节 |

**entity-template.md：⚠ 2 项可能缺失（`updated` 字段、`Evolution Log` 节）**

### synthesis-template.md

| 必需字段 | 状态 | 实际内容 |
|---|---|---|
| Counter-evidence 节 | ✅ 存在 | `## Counter-evidence`，含回音室风险标注占位符 |
| Confidence Notes 节 | ✅ 存在 | `## Confidence Notes`，含 ⚠ 标注模板 |
| Limitations 节 | ✅ 存在 | `## Limitations` |
| type / date / confidence / source_count | ✅ 存在 | 完整 |
| Thesis / Evidence / Synthesis / Sources 节 | ✅ 存在 | 完整 |

**synthesis-template.md：✅ 全部必需字段存在**

---

## 四、系统文件隔离状态

| 文件 | graph-excluded: true | 实际 frontmatter type |
|---|---|---|
| wiki/log.md | ✅ 有 | `type: system-log` |
| wiki/index.md | ✅ 有 | `type: system-index` |
| wiki/overview.md | ✅ 有 | `type: system-overview` |
| wiki/QUESTIONS.md | ✅ 有 | `type: system-questions` |

**系统文件隔离：✅ 全部 4 个系统文件均含 `graph-excluded: true`**

---

## 五、scripts/lint.py 检查项验证

验证 scripts/lint.py 是否实现全部 9 项检查：

| # | 检查项 | 状态 | 函数名 |
|---|---|---|---|
| 1 | YAML Frontmatter 合法性 | ✅ 实现 | `check_frontmatter()` L168 |
| 2 | Broken Wikilinks | ✅ 实现 | `check_broken_wikilinks()` L196 |
| 3 | Index 一致性 | ✅ 实现 | `check_index_consistency()` L233 |
| 4 | Stub 页面（正文 < 100 字符） | ✅ 实现 | `check_stub_pages()` L256 |
| 5 | 近重复概念名称（Jaccard > 0.7） | ✅ 实现 | `check_near_duplicate_concepts()` L282 |
| 6 | SHA-256 完整性 | ✅ 实现 | `check_sha256_integrity()` L318 |
| 7 | Stale 页面（domain_volatility 阈值） | ✅ 实现 | `check_stale_pages()` L361 |
| 8 | 跨语言重复（URL + aliases 重叠） | ✅ 实现 | `check_cross_language_duplicates()` L406 |
| 9 | Wikilink 格式规范（CJK/驼峰/下划线） | ✅ 实现 | `check_wikilink_format()` L466 |

**附加特性验证：**
- 报告输出：✅ `write_report()` 写入 `wiki/outputs/lint-YYYY-MM-DD.md`，frontmatter 含 `graph-excluded: true`
- 系统文件排除：✅ `SYSTEM_FILES = {"index.md", "log.md", "overview.md", "QUESTIONS.md"}` 正确排除
- HTML 注释跳过：✅ `extract_wikilinks()` 中 `re.sub(r"<!--.*?-->", "")` 防止模板占位符触发误报
- Stale 阈值：✅ `STALE_DAYS = {"high": 90, "medium": 180, "low": 365}`（与 CLAUDE.md 一致）
- Jaccard 阈值：✅ `JACCARD_THRESHOLD = 0.7`（与 CLAUDE.md 一致）

**scripts/lint.py：✅ 全部 9 项检查均已实现，逻辑与 CLAUDE.md 规范一致**

---

## 六、qmd 状态

### 索引状态

```
Index: C:/Users/jiaruo/.cache/qmd/index.sqlite
Size:  172.0 KB

Documents
  Total:    17 files indexed
  Vectors:  0 embedded
  Pending:  17 need embedding (run 'qmd embed')
  Updated:  1d ago

Collections
  D:\AI\LLM-WIKI\jiaruo\wiki (qmd://D:\AI\LLM-WIKI\jiaruo\wiki/)
    Pattern:  **/*.md
    Files:    17 (updated 1d ago)
```

**索引分析：**
- 当前 wiki/ 目录实际 .md 文件数：17（含模板、系统文件、概念/实体/来源/输出页）
- qmd 已索引文件数：17
- ✅ 索引与实际文件数一致，无需补充 `qmd add wiki/`
- ⚠ **嵌入向量：0/17（全部待嵌入）**——17 个文件均未生成嵌入向量，运行 `qmd query` 将仅依赖关键词匹配，无语义搜索能力。建议执行 `qmd embed` 生成向量。

**注意：** raw/clippings/ 下有 4 个新增文件（2026-04-15 日期的 4 个 .md），以及 raw/pdfs/ 中有大量未处理 PDF，这些均属于 `raw/` 层（未 ingest），不应进入 qmd 索引，当前状态正确。

### 测试查询结果

执行 `qmd search "机器人传感器通信"` → 返回：**No results found.**

原因：嵌入向量均未生成（`Vectors: 0 embedded`），搜索无法匹配。这属于正常状态，执行 `qmd embed` 后即可恢复语义搜索能力。

---

## 七、综合评分与修复优先级

### 问题清单

| 优先级 | 问题 | 建议修复 |
|---|---|---|
| 🔴 高 | qmd 嵌入向量全部缺失（0/17），语义搜索不可用 | 执行 `qmd embed` |
| 🔴 高 | 4 个新增 raw/clippings/ 文件未 ingest（2026-04-15 日期） | 执行 INGEST 处理这 4 个文件 |
| 🟡 中 | CLAUDE.md 缺少 INGEST 末尾 `qmd update` 步骤 | 在 Step 11 后增加 Step 12：`qmd add wiki/` |
| 🟡 中 | CLAUDE.md 缺少 URL 直接输入时的 defuddle 调用规则 | 补充 INGEST 触发词章节：URL 输入 → defuddle 抓取 → 保存至 raw/ → 走标准 INGEST |
| 🟡 中 | CLAUDE.md INGEST 流程中无 canonical_source 译文去重检测步骤 | 在 Step 5 创建 source 页后，增加 canonical_source URL 比对逻辑 |
| 🟡 中 | entity-template.md 缺少 `updated` 字段和 `Evolution Log` 节 | 更新模板，与 concept-template.md 保持一致 |
| 🟢 低 | wiki/overview.md 数据未更新（总来源数显示 0，实际已有 1 个来源，5 个 concept） | 执行 REFLECT 或手动更新 overview.md 数据 |
| 🟢 低 | raw/pdfs/ 下 12 个 PDF 文件全部未 ingest | 按需择优处理 |

### 整体健康评分

| 维度 | 得分 | 说明 |
|---|---|---|
| 目录结构完整性 | 10/10 | 全部子目录存在 |
| CLAUDE.md 规则覆盖 | 22/25 | 2 项缺失，1 项部分缺失 |
| 模板完整性 | 9/10 | entity-template 有 2 个字段缺失 |
| 系统文件隔离 | 10/10 | 全部正确隔离 |
| lint.py 检查项 | 10/10 | 全部 9 项实现 |
| qmd 索引同步 | 8/10 | 文件数一致，但嵌入向量全部缺失 |

**综合得分：69/75（92%）**

---

_审计完成时间：2026-04-15_
_下次建议审计时间：知识库规则重大更新后，或累计 ingest 10+ 新来源后_
