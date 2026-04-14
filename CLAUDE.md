# CLAUDE.md — 知识库行为契约

> 本文件是 LLM 操作本知识库的核心行为规范。所有操作必须严格遵守本契约。
> 当本文件规则更新时，必须同步更新 USER_GUIDE.md 对应章节。

---

## 一、系统概述

### 三层架构

```
raw/          ← 原始素材层（人类拥有，LLM 只读）
├── articles/     外部文章
├── clippings/    网页剪藏
├── images/       图片
├── pdfs/         PDF 文件
├── notes/        随手笔记
└── personal/     个人写作

wiki/         ← 知识提炼层（LLM 完全读写）
├── sources/      摄入后的来源页
├── concepts/     概念知识页
├── entities/     实体页（人/工具/机构/论文）
├── synthesis/    综合分析页
├── templates/    页面模板
├── outputs/      输出与报告（graph-excluded）
├── index.md      系统索引（graph-excluded）
├── log.md        操作日志（graph-excluded）
├── overview.md   健康仪表盘（graph-excluded）
└── QUESTIONS.md  问题追踪（graph-excluded）

outputs/      ← 对外输出层（最终产物）
scripts/      ← 工具脚本
```

### 核心原则

- **你完全拥有 `wiki/` 目录的读取和写入权限**，可自由创建、修改、组织其中的文件。
- **`raw/` 目录由人类拥有，你只能读取，绝不修改任何 raw/ 下的文件。**
- 所有操作必须在 `wiki/log.md` 末尾追加日志记录（只追加，不修改已有记录）。
- 所有 wiki/ 下的 .md 文件必须有合法 YAML frontmatter，包含 `type` 和 `date` 字段。

---

## 二、INGEST 操作规范

**触发词**：`ingest`、`摄入`、`处理这个`

### 来源类型判断（优先级由高到低）

1. frontmatter 含 `type: personal-writing` → 走**个人写作**流程
2. 文件路径包含 `raw/personal/` → 走**个人写作**流程
3. frontmatter 含 `type: pdf-reference` → 走 **PDF 参考**流程（同外部来源标准流程，额外标注 PDF 章节来源）
4. 其他 → 走**外部来源标准流程**

### 缺少 frontmatter 时的处理规则

- 从文件第一个 `#` 标题提取 title；若无标题则从文件名推断
- `source_url` 字段留空，在 `wiki/sources/<slug>.md` 中标注「来源未知」
- `date` 使用文件系统修改时间
- 不中断 INGEST，但在 `wiki/log.md` 记录：`警告：来源文件 <filename> 缺少标准 frontmatter`

---

### 外部来源标准流程（11 步）

**Step 1：读取原始来源**
读取 `raw/` 中的目标文件（只读，绝不修改）。

**Step 2：计算 SHA-256 哈希**
使用 Python hashlib 计算原始文件的 SHA-256 哈希值，用于后续完整性验证。

```python
import hashlib
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()
```

**Step 3：与用户确认核心要点**
逐一摄入时，向用户呈现提取到的核心要点，保持参与感，等待确认后再继续。

**Step 4：生成 slug**
规则：英文小写，用连字符，简洁且具辨识度。
示例：`attention-is-all-you-need`、`poor-charlies-almanack`、`value-investing-principles`

**Step 5：创建 wiki/sources/<slug>.md**
使用 `wiki/templates/source-template.md`，frontmatter 必须填写：
- `raw_file`: 相对路径（如 `raw/articles/filename.md`）
- `raw_sha256`: 步骤 2 计算的哈希值
- `last_verified`: 今日日期（YYYY-MM-DD）
- 若来源发表日期超过 2 年前：设置 `possibly_outdated: true`，并在 Summary 末尾添加：
  > ⚠ 此来源发表于 2 年以上前（{date}），部分内容可能已过时。

**Step 6：概念名称对齐检查**（提取概念之前必须执行）

1. 将每个提取到的概念名称统一映射为英文小写连字符 slug
   - 示例：「第一性原理」→ `first-principles-thinking`
   - 示例：「注意力机制」→ `attention-mechanism`
2. 在 `wiki/concepts/` 中查找该 slug 文件是否已存在
3. **同时检查所有已有 concept 页的 `aliases` 字段**：
   - 遍历 `wiki/concepts/*.md`，解析每页 frontmatter 的 `aliases` 列表
   - 检查是否包含当前概念名称（支持中英文别名匹配，大小写不敏感）
4. 若通过 slug 匹配**或**通过 aliases 匹配到已有页面：**更新已有页面，不创建新页面**
5. 若找不到任何匹配：才创建新页面，并在 frontmatter 的 `aliases` 中同时填入中文名和英文名

**Step 7：处理每个提取到的概念**

**若 `wiki/concepts/<concept>.md` 已存在**：
- 追加新来源 wikilink 到 Sources 节
- 在 Evolution Log 末尾追加一条记录（见 Evolution Log 追加规则）
- 更新 `source_count`（+1）
- 根据 Confidence 更新规则更新 `confidence`
- 更新 `last_reviewed` 字段为今日日期
- 更新 `updated` 字段为今日日期

**若不存在**：
- 创建新文件，使用 `wiki/templates/concept-template.md`
- `aliases` 字段同时填入该概念的中英文名称（以及常见别名）
- `source_count` 设为 1，`confidence` 设为 `low`

**Evolution Log 追加规则**：
| 情况 | Evolution Log 内容 |
|---|---|
| 新来源与当前 Definition 一致 | `- YYYY-MM-DD（N sources）：强化——[来源标题] 与现有定义一致` |
| 有修正 | `- YYYY-MM-DD（N sources）：修正：[具体变化描述]` |
| 相互矛盾 | `- YYYY-MM-DD（N sources）：新增分歧：[分歧内容概述]，见 Contradictions 节` |

**Step 8：处理每个提取到的实体**
逻辑同 Step 6-7，使用 `wiki/templates/entity-template.md`，存放于 `wiki/entities/<slug>.md`。

**Step 9：更新 wiki/index.md**
将来源从 Unprocessed 移动到 Processed（按日期倒序排列）。

**Step 10：检查 QUESTIONS.md**
读取 `wiki/QUESTIONS.md`，检查本次来源是否能回答任何开放问题：
- 若能：提示用户：「此来源可能回答了开放问题：[问题描述]，是否立即执行 QUERY？」
- 用户确认后，执行 QUERY 并将结果写入 `wiki/synthesis/`
- 将该问题从 Open Questions 移入 Resolved Questions，标注解答日期和 synthesis 链接

**Step 11：追加操作日志**
```
YYYY-MM-DD HH:MM | ingest | [来源标题]（slug: [slug]，提取 N 个概念，M 个实体）
```

---

### 个人写作流程（区别于外部来源标准流程）

- **不生成 Summary 节**，跳过客观摘要
- 核心论点写入相关 concept 页的 `## My Position` 节，标注「个人认知」
- **不参与 confidence 的 source_count 计数**（避免用自己的文章给自己背书）
- 若文章中引用了外部来源，提取这些引用并尝试与已有 `wiki/sources/` 页面建立 wikilinks
- `raw_sha256` 哈希机制同样适用
- Evolution Log 记录格式：
  ```
  - YYYY-MM-DD 个人写作 [[sources/slug]] 确立了对此概念的明确立场
  ```

---

## 三、QUERY 操作规范

**触发词**：直接提问，或「根据我的知识库」

### 执行步骤

**Step Q1：检索相关页面**
执行：`qmd query "<用户问题>" --json`，获取 top 5 相关页面。
若 qmd 报错则降级：读取 `wiki/index.md`，从 Sources/Concepts 列表中手动选取最相关的 5 个页面。

**Step Q2：完整读取文件**
逐一完整读取 top 5 文件内容，不跳过任何节。

**Step Q3：合成答案**
- 每个核心结论必须溯源到具体 `wiki/sources/<slug>.md`（**不允许只引用 concept 页**）
- 注明各来源的 `confidence` 级别
- 来源相互矛盾时，显式标注分歧，不得静默选择其一

**Step Q4：输出与归档**（若答案具有复用价值）
- 写入 `wiki/outputs/YYYY-MM-DD-<topic>.md`
- frontmatter 必须含 `graph-excluded: true`
- 输出末尾必须包含「⚠ Confidence Notes」节
- 更新 `wiki/index.md` 的 Recent Synthesis 列表
- 追加 `wiki/log.md`：`YYYY-MM-DD HH:MM | query | [问题摘要]`

### 输出格式规则

| 问题类型 | 输出格式 |
|---|---|
| 普通问题 | Markdown 正文 |
| 比较类（A vs B） | Markdown 表格 |
| 演示类 | Marp 幻灯片（frontmatter 加 `marp: true`） |
| 趋势类 | Python matplotlib 代码块 |
| 清单类 | 结构化 bullet list |

---

## 四、LINT 操作规范

**触发词**：`lint`、`检查`、`健康检查`

### 执行步骤

1. 运行 `python scripts/lint.py`（包含 9 项检查，见下方说明）
2. 报告自动写入 `wiki/outputs/lint-YYYY-MM-DD.md`（frontmatter 含 `graph-excluded: true`）
3. 执行 `qmd status`，对比索引文件数与 `wiki/` 实际 `.md` 文件数（排除系统文件）
   - 若索引落后：执行 `qmd add wiki/`，在报告中记录「索引已更新」
4. 向用户展示摘要，询问是否立即修复发现的问题

### 9 项检查说明

| # | 检查项 | 说明 |
|---|---|---|
| 1 | YAML Frontmatter 合法性 | 所有 wiki/ 下 .md 文件是否有合法 YAML frontmatter（含 type 和 date） |
| 2 | Broken Wikilinks | [[xxx]] 引用了不存在的页面 |
| 3 | Index 一致性 | wiki/index.md 中标记的文件是否都实际存在 |
| 4 | Stub 页面 | 正文少于 100 字符的空壳页面 |
| 5 | 近重复概念名称 | slug 名称 Jaccard 相似度 > 0.7 的 concept 页对 |
| 6 | SHA-256 完整性 | raw 文件哈希与 source 页 raw_sha256 字段比对（⚠ SOURCE MODIFIED） |
| 7 | Stale 页面 | 超过 domain_volatility 时效阈值（high=90天, medium=180天, low=365天） |
| 8 | 跨语言重复 | source URL 相似度检测 + 不同 concept 页的 aliases 字段重叠检测 |
| 9 | Wikilink 格式规范 | 检测非英文小写连字符格式的 wikilink（如中文词汇、驼峰、下划线）及别名断链 |

---

## 五、REFLECT 操作规范

**触发词**：`reflect`、`综合分析`、`发现规律`

### 四阶段执行

**Stage 0：反向检验（必须最先执行）**
在生成任何合成结论之前，主动搜索反驳证据。
- 若无反对来源，在 synthesis 页的 Limitations 节标注：
  > ⚠ 回音室风险：未找到反驳来源，结论可能存在确认偏差。

**Stage 1：模式扫描**
使用 qmd 批量扫描（若 qmd 不可用则逐一读取）：
```bash
qmd multi-get "wiki/concepts/*.md" -l 40
qmd multi-get "wiki/entities/*.md" -l 40
qmd multi-get "wiki/synthesis/*.md" -l 60
```
识别：
- 跨来源的重复模式
- 隐性关联（多处提及但未建立链接的概念对）
- 内容空白（重要主题缺乏覆盖）
- 矛盾对（相互冲突的结论）

**Stage 2：深度合成**
对有证据支撑的候选项，完整读取相关页面，写入 `wiki/synthesis/<topic>-synthesis.md`（使用 `wiki/templates/synthesis-template.md`）。

**Stage 3：Gap Analysis**
识别并输出以下类型的知识空白：
- `source_count = 1` 且创建超过 30 天的孤立概念
- 多处提及但无独立页面的概念/实体（隐性盲区）
- 覆盖明显稀薄的主题领域

输出到 `wiki/outputs/gap-report-YYYY-MM-DD.md`（frontmatter 含 `graph-excluded: true`）。

**完成后**：
- 更新 `wiki/overview.md` 的 Health Dashboard 数据
- 更新 `wiki/index.md` 的 Recent Synthesis 列表
- 追加 `wiki/log.md`：`YYYY-MM-DD HH:MM | reflect | [本次综合主题]`

---

## 六、MERGE 操作规范

**触发词**：`merge`、`去重`

### 同语言合并流程

1. 与用户确认合并方案（**绝不自动合并，必须等待用户明确确认**）
2. 主 slug 保留，被合并页面的所有 wikilinks 全部更新为主 slug
3. 被合并文件替换为重定向文件：
   ```markdown
   ---
   type: redirect
   redirect: "[[concepts/主slug]]"
   date: YYYY-MM-DD
   ---
   ```
4. 追加 `wiki/log.md`：`YYYY-MM-DD HH:MM | merge | [旧slug] → [主slug]`

### 跨语言合并专项流程

1. 主 slug 保留英文
2. `aliases` 字段取两个页面的并集（去重）
3. Key Points、Sources、Evolution Log 按并集合并（去重）
4. `My Position` 节：若两页都有内容，先向用户展示对比，等待确认后再合并
5. 被合并的旧 slug 文件保留为 redirect 文件（确保旧 wikilinks 不 broken）
6. 追加 `wiki/log.md`：`YYYY-MM-DD HH:MM | merge | [旧slug] → [主slug]（跨语言合并）`

---

## 七、ADD-QUESTION 操作规范

**触发词**：`我想搞清楚`、`add question`、`记录一个问题`

### 执行步骤

1. 将问题规范化，提取核心疑问（去除语气词，提炼为一句话）
2. 追加到 `wiki/QUESTIONS.md` 的 Open Questions 节：
   ```markdown
   - [ ] [问题内容]（opened YYYY-MM-DD）
   ```
3. 追加 `wiki/log.md`：`YYYY-MM-DD HH:MM | add-question | [问题摘要]`

---

## 八、Wikilink 使用规范

### 格式铁律（不可违反）

所有 wikilink 目标必须使用**英文小写连字符**格式：

```
✅ [[value-investing]]
✅ [[attention-mechanism]]
✅ [[warren-buffett]]

❌ [[价值投资]]      ← 中文词汇，禁止
❌ [[ValueInvesting]] ← 驼峰，禁止
❌ [[value_investing]] ← 下划线，禁止
```

### 中文名称的正确处理方式

1. 写入 concept 页 frontmatter 的 `aliases` 字段
2. concept 页正文**第一行**使用括号标注：`价值投资（Value Investing）`
3. wikilink **始终**用英文 slug

### 允许使用 wikilinks 的场景

- concept 页引用其他 concept/entity 页
- source 页引用 concept/entity 页
- synthesis 页引用 concept/source/entity 页

### 禁止使用 wikilinks 的场景

- **任何页面**不得引用系统文件：`[[log]]`、`[[index]]`、`[[overview]]`、`[[QUESTIONS]]`
- **任何页面**不得引用 lint 报告：`[[outputs/lint-xxx]]`
- **任何页面**不得以操作名称作为 wikilink：`[[ingest]]`、`[[query]]`、`[[reflect]]`
- `log.md` 内部记录使用**纯文本路径**（如 `wiki/sources/xxx.md`），不使用 wikilinks

---

## 九、Wiki 语言规范

- **Wiki 层**（concept/entity/synthesis 页）统一用**中文**写作
- concept 页 `title` 字段使用中文主名称（Obsidian 图谱节点显示）
- 英文术语在 concept 页**首次出现**时括号标注：`注意力机制（Attention Mechanism）`
- 所有 **slug（文件名）** 统一用英文小写连字符，不使用中文文件名
- `aliases` 字段覆盖中英文所有叫法

---

## 十、Confidence 更新规则

| 来源数量 | Confidence | 处理方式 |
|---|---|---|
| 1 个来源 | `low` | 自动设置，无需确认 |
| 3+ 个来源 | `medium` | 自动设置，无需确认 |
| 5+ 个来源且无重大矛盾 | **候选 high** | 向用户展示 Definition 和 Sources 列表，**等待明确确认** |
| 用户明确回复「确认」或「ok」 | `high` | 才可设置 |

**注意**：`raw/personal/` 下的个人写作**不参与** `source_count` 计数。

---

## 十一、Source Integrity Rules（来源完整性规则）

### Re-ingest 规则
若 lint 报告 `⚠ SOURCE MODIFIED`（SHA-256 不匹配）：
1. 重新摄入该文件（执行完整的外部来源标准流程）
2. 更新所有受影响的 concept/entity 页面
3. Evolution Log 记录：
   ```
   - YYYY-MM-DD（N sources）：来源更新：wiki/sources/[slug].md 哈希变更，内容已重新提取
   ```

### 时效性规则
- 来源发表日期超过 2 年：设置 `possibly_outdated: true`，在 Summary 末尾添加提示

### 矛盾处理规则
- 矛盾来源**必须**在 source 页和 concept 页的 Contradictions 节显式记录
- **不得静默覆盖**：发现矛盾时，不删除旧定义，而是在 Contradictions 节并列呈现分歧

---

## 十二、系统文件隔离规则

以下文件的 frontmatter 必须含 `graph-excluded: true`，不参与 Obsidian 图谱显示：

- `wiki/log.md`
- `wiki/index.md`
- `wiki/overview.md`
- `wiki/QUESTIONS.md`
- `wiki/outputs/` 下**所有**文件

---

## 十三、文档维护规则

- 当本 CLAUDE.md 规则更新时，必须同步更新 `USER_GUIDE.md` 对应章节
- 确保两份文档保持一致，不得出现版本漂移

---

_最后更新：2026-04-13_
