# CLAUDE.md — 知识库行为契约

> 本文件是 LLM 操作本知识库的核心行为规范。所有操作必须严格遵守本契约。
> 当本文件规则更新时，必须同步更新 USER_GUIDE.md 对应章节。

---

## 一、系统概述

### 三层架构

```
raw/          ← 原始素材层（人类拥有，LLM 只读）
├── 工作/         工作相关内容（当前所有内容均在此域下）
│   ├── articles/     外部文章（含主题子目录：AI/、MCULess/、机器人应用/、汽车领域/）
│   ├── clippings/    网页剪藏（含主题子目录：AI/、MCULess/、机器人/、汽车领域/、嵌入式汽车电子/、芯片/）
│   ├── images/       图片（含主题子目录：AI/）
│   ├── notes/        随手笔记（含主题子目录：机器人/）
│   ├── pdfs/         PDF 文件（含主题子目录：AI/、MCULess/、功能安全/、机器人/、汽车领域/、嵌入式汽车电子/、芯片分类/、芯片综合类/）
│   └── personal/     个人写作（含子目录：考试资料/）
└── 生活/         生活相关内容（目录结构已备，暂无内容）
    ├── articles/
    ├── clippings/
    ├── images/
    ├── notes/
    ├── pdfs/
    └── personal/

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
- 并行安全：每段日志以 `YYYY-MM-DD HH:MM` 时间戳前缀起头，保证行唯一；git 纯追加通常能自动合并，若冲突保留双方变更（见多助手约定第 6 条）。
- 所有 wiki/ 下的 .md 文件必须有合法 YAML frontmatter，包含 `type` 和 `date` 字段。

### 多助手并行维护约定

本知识库可能由多个 AI 助手（如 Claude Code、知微）从不同设备并行维护。为降低冲突风险：

1. **开始工作前先 `git pull`**：确保本地仓库是最新状态，避免基于过期数据操作。
2. **INGEST 收尾及时提交推送**：完成一批摄入并过 lint 门禁后，立即 `git add` + `git commit` + `git push`，减少两边同时修改同一批文件的时间窗口。
3. **重复摄入防御**：Step 5 的来源去重检测（`source_url` 匹配）是第一道防线；若用户提示"这个在另一台机器上处理过了"则立即跳过。两个助手各自维护的 `wiki/log.md` 条目也是交叉验证依据。
4. **读取 `wiki/log.md` 最新条目**：开始工作前快速浏览最近的日志，了解另一边已经做了什么。
5. **MERGE 操作全局唯一**：第 6 节规定 MERGE 必须等用户确认，天然避免了双边同时合并的冲突。
6. **遇到 git 冲突时保留双方变更**：不要静默覆盖，向用户呈现差异，等待决策。

### 工具链依赖与降级路径

本知识库的脚本与 `qmd` 检索引擎的依赖关系如下，跨机器维护时必须明确：

- **`scripts/lint.py` / `scripts/fix-sha256.py`（仓库自带，常驻）**：仅依赖 PyYAML（见根目录 `requirements.txt`）。`pip install -r requirements.txt` 即可复现。
- **`scripts/tools/wiki_index.py`（仓库自带，常驻）**：qmd 缺席时的关键词检索引擎，纯 stdlib + PyYAML。提供 `query / multi-get / status`（及 `update / add / embed` 占位）。
- **`qmd`（可选外部工具，本仓库不分发）**：带嵌入向量的语义检索引擎，子命令 `embed / update / query / status / multi-get / add`。**当前维护环境未安装 qmd**，所有依赖 qmd 的步骤自动降级到 `wiki_index.py`（关键词级，非语义）。若需恢复语义检索，须在原始安装环境确认 qmd 来源后安装，并同步 `requirements.txt` 注释。

**降级对照（qmd 缺席 = 本仓库默认状态）：**

| 原 qmd 步骤 | 降级实现 |
|---|---|
| `qmd update` / `qmd add` | 无需操作（文件树即实时索引）；`wiki_index.py status` 可校验 |
| `qmd query "<q>" --json` | `python scripts/tools/wiki_index.py query "<q>" --json --top 5` |
| `qmd multi-get "glob" -l N` | `python scripts/tools/wiki_index.py multi-get "glob" --lines N` |
| `qmd status` | `python scripts/tools/wiki_index.py status` |
| `qmd embed` | 不支持（语义嵌入需 qmd） |

**索引权威说明**：`wiki/index.md` 是「人类可读导航视图」（按类型手动维护，含 Processed/Unprocessed 分区），可由 `wiki_index.py status` 校验但不自动覆盖；`wiki_index.py` / `qmd` 的实时文件树扫描是「检索权威」。两者职责不同，互不替代。lint Check 3 已校验 index.md 引用一致性。

---

## 二、INGEST 操作规范

**触发词**：`ingest`、`摄入`、`处理这个`、URL 直接输入

### URL 直接输入处理规则

当用户直接提供一个 URL（而非 `raw/` 下的文件路径）时：

1. 调用 `defuddle <URL>` 抓取并清洗网页正文
2. 将抓取结果保存为 `raw/工作/clippings/{topic}/YYYY-MM-DD-<标题slug>.md`（**只写入 raw/，不跳过**）
   - `{topic}` 根据内容选择：`AI`、`MCULess`、`机器人`、`汽车领域`、`嵌入式汽车电子`、`芯片`
   - 若主题不明确，直接放到 `raw/工作/clippings/` 根目录
3. 在文件顶部写入标准 frontmatter：
   ```yaml
   ---
   source_url: "<原始 URL>"
   title: "<页面标题>"
   date: YYYY-MM-DD
   ---
   ```
4. 随后按**外部来源标准流程**继续执行（从 Step 1 读取刚保存的文件开始）

若 `defuddle` 不可用或抓取失败：提示用户手动将内容保存到 `raw/clippings/`，不得跳过 raw 层直接写入 wiki/。

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

### 不可见字符清洗规则（防御 lint Check 6 假阳性）

从网页 / 微信 / PDF 复制的标题常带入不可见 Unicode 字符（零宽空格 U+200B、零宽连字 U+200C/U+200D、词连接符 U+2060、字节序标记 U+FEFF 等）。这些字符肉眼不可见，但会污染两处并触发 lint Check 6 误报 `SOURCE MODIFIED`：

- **raw 文件名本身含不可见字符** → lint 按 frontmatter 的 `raw_file` 路径解析 `os.path.exists` 失败 → 找不到文件 → 误报。
- **`raw_file` 字段值含不可见字符或字面量转义**（如把 `\uFEFF` 当字符串写入）→ 路径解析失败 → 同上。

**INGEST 必须遵守的清洗动作：**

1. **保存 raw 文件前清洗文件名**（含 URL 直接输入存 clippings、以及协助用户重命名 PDF 时）：strip 所有 Unicode 类别为 `C`（控制 / 格式字符）的字符，至少覆盖 U+200B / U+200C / U+200D / U+2060 / U+FEFF，再按 slug 化规则生成文件名。
2. **写入 `raw_file` 字段前清洗路径字符串**：确保值与磁盘实际文件名逐字节一致（无任何不可见字符），禁止写入字面量转义序列（如 `\uFEFF`）。
3. **Step 2 计算 SHA-256 之前**：先确认 `raw_file` 路径可被 `os.path.exists` 解析；解析失败则回头执行第 1–2 步清洗，不得带着污染值写入 frontmatter 或继续计算哈希。

> 注：本规则作用于「raw 文件入库时」（URL 输入由 LLM 保存、PDF 重命名由用户或 LLM 协助），与「raw/ 只读、绝不修改已入库文件」原则不冲突——它防止的是入库那一刻就带入污染，而非事后改写内容字节。若发现已入库文件被污染，按第十一节 Re-ingest 规则处理（重命名磁盘文件为干净名 + 同步 `raw_file`）。

---

### 外部来源标准流程（12 步）

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

**Step 5：来源去重检测**（创建 source 页之前必须执行）

1. 读取目标来源的 `source_url`
2. 遍历 `wiki/sources/*.md`，检查已有页面的 `source_url` 和 `canonical_source` 字段：
   - `source_url` 规范化后完全相同 → **重复来源，停止 INGEST，提示用户**
   - `canonical_source` 与当前 `source_url` 相同 → **译文重复**，提示：「已有该来源的译文页 `[[sources/slug]]`，是否仍要摄入当前语言版本？」等待用户确认后继续
3. 若未发现重复：继续创建 source 页

**Step 6：创建 wiki/sources/<slug>.md**
使用 `wiki/templates/source-template.md`，frontmatter 必须填写：
- `raw_file`: 相对路径（如 `raw/articles/filename.md`）。**路径字符串须先经「不可见字符清洗规则」处理，确保不含零宽空格 / BOM 等不可见字符**（见上方同名小节），否则 lint Check 6 会误报 `SOURCE MODIFIED`。
- `raw_sha256`: 步骤 2 计算的哈希值，**必须是完整 64 位十六进制字符串，严禁截断**（截断哈希会与全量哈希前缀匹配，导致 lint 误报 SOURCE MODIFIED；lint Check 6 会校验长度并标记 MALFORMED HASH）
- `last_verified`: 今日日期（YYYY-MM-DD）
- 若来源发表日期超过 2 年前：设置 `possibly_outdated: true`，并在 Summary 末尾添加：
  > ⚠ 此来源发表于 2 年以上前（{date}），部分内容可能已过时。

**Step 7：概念名称对齐检查**（提取概念之前必须执行）

1. 将每个提取到的概念名称统一映射为英文小写连字符 slug
   - 示例：「第一性原理」→ `first-principles-thinking`
   - 示例：「注意力机制」→ `attention-mechanism`
2. 在 `wiki/concepts/` 中查找该 slug 文件是否已存在
3. **同时检查所有已有 concept 页的 `aliases` 字段**：
   - 遍历 `wiki/concepts/*.md`，解析每页 frontmatter 的 `aliases` 列表
   - 检查是否包含当前概念名称（支持中英文别名匹配，大小写不敏感）
4. 若通过 slug 匹配**或**通过 aliases 匹配到已有页面：**更新已有页面，不创建新页面**
5. 若找不到任何匹配：才创建新页面，并在 frontmatter 的 `aliases` 中同时填入中文名和英文名

**Step 8：处理每个提取到的概念**

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

**Step 9：处理每个提取到的实体**
逻辑同 Step 7-8，使用 `wiki/templates/entity-template.md`，存放于 `wiki/entities/<slug>.md`。

**Step 10：更新 wiki/index.md**
将来源从 Unprocessed 移动到 Processed（按日期倒序排列）。

**Step 11：检查 QUESTIONS.md**
读取 `wiki/QUESTIONS.md`，检查本次来源是否能回答任何开放问题：
- 若能：提示用户：「此来源可能回答了开放问题：[问题描述]，是否立即执行 QUERY？」
- 用户确认后，执行 QUERY 并将结果写入 `wiki/synthesis/`
- 将该问题从 Open Questions 移入 Resolved Questions，标注解答日期和 synthesis 链接

**Step 12：收尾自检（强制）——lint 门禁 + 更新索引/仪表盘 + 日志**

INGEST 结束前**必须**按顺序完成以下收尾，不得跳过：

1. **运行 lint 门禁**（防止「摄入完就跑、不建概念」导致孤儿 wikilink）：
   ```bash
   python scripts/lint.py --gate
   ```
   - 关键检查（frontmatter / 孤儿断链 / index 一致性 / SHA）任一失败 → **必须先修复再继续**，不得带病提交。
   - 若 source 页引用了尚未创建的 concept/entity（孤儿 wikilink），说明 Step 7–9 未完成，回头补建对应页面。
2. **更新索引**：
   - 若已安装 `qmd`（可选外部语义引擎）：`qmd update`
   - 若 `qmd` 未安装（本仓库默认状态）：无需操作，文件树即为实时索引；可运行 `python scripts/tools/wiki_index.py status` 校验一致性
3. **更新 `wiki/overview.md`** 的 Health Dashboard 数据（Sources/Concepts/Entities/Synthesis 计数与增长趋势行）。
4. 追加日志：
   ```
   YYYY-MM-DD HH:MM | ingest | [来源标题]（slug: [slug]，提取 N 个概念，M 个实体）
   ```

> 注：仓库已挂 pre-commit 门禁（见第十四节），即使遗漏步骤 1，提交时也会被自动拦截；但应在 INGEST 内主动自检，而非依赖最后一道防线。

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
- 首选：`qmd query "<用户问题>" --json`（需安装可选外部语义引擎 qmd），获取 top 5 相关页面。
- qmd 缺席时（本仓库默认）：`python scripts/tools/wiki_index.py query "<用户问题>" --json --top 5`，基于 frontmatter（title/aliases/tags）+ 正文关键词排名返回 top 5。
- 若两者皆不可用：读取 `wiki/index.md`，从 Sources/Concepts 列表中手动选取最相关的 5 个页面。

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

1. 运行 `python scripts/lint.py`（包含 10 项检查，见下方说明）
2. 报告自动写入 `wiki/outputs/lint-YYYY-MM-DD.md`（frontmatter 含 `graph-excluded: true`）
3. 执行 `python scripts/tools/wiki_index.py status`，统计 `wiki/` 下各类型 `.md` 文件数（排除 graph-excluded 系统文件）
   - 若与 `wiki/index.md` / `wiki/overview.md` 登记数不一致：在报告中记录「索引登记待核对」，并提示用户
   - （若已安装 qmd：`qmd status` 可作补充，但 `wiki_index.py status` 为权威文件树统计）
4. 向用户展示摘要，询问是否立即修复发现的问题

### 门禁模式（`--gate`）

`python scripts/lint.py --gate` 用于 pre-commit hook（见第十四节）：**不写报告**，仅当**关键检查**失败时返回非零退出码以阻断提交。

- **关键检查（阻断提交）**：Check 1 frontmatter、Check 2 孤儿/断链 wikilink、Check 3 index 一致性、Check 6 SHA。
- **质量提示（不阻断）**：Check 4 stub、Check 5 近重复、Check 7 stale、Check 8 跨语言、Check 9 格式。
  - 之所以不把 Check 5 列为阻断项：同族概念（如 `chip-design` ↔ `rf-chip-design`）会触发 Jaccard 误报，若阻断会卡死每次提交。

### 10 项检查说明

| # | 检查项 | 说明 |
|---|---|---|
| 1 | YAML Frontmatter 合法性 | 所有 wiki/ 下 .md 文件是否有合法 YAML frontmatter（含 type 和 date） |
| 2 | Broken Wikilinks | [[xxx]] 引用了不存在的页面 |
| 3 | Index 一致性 | wiki/index.md 中标记的文件是否都实际存在 |
| 4 | Stub 页面 | 正文少于 100 字符的空壳页面 |
| 5 | 近重复概念名称 | slug 名称 Jaccard 相似度 > 0.7 的 concept 页对 |
| 6 | SHA-256 完整性 | ①raw_sha256 长度/格式校验：必须 64 位十六进制，否则标记 `❌ MALFORMED HASH`（防截断 bug）；②raw 文件哈希与 source 页 raw_sha256 字段比对（⚠ SOURCE MODIFIED） |
| 7 | Stale 页面 | 超过 domain_volatility 时效阈值（high=90天, medium=180天, low=365天） |
| 8 | 跨语言重复 | source URL 相似度检测 + 不同 concept 页的 aliases 字段重叠检测 |
| 9 | Wikilink 格式规范 | 检测非英文小写连字符格式的 wikilink（如中文词汇、驼峰、下划线）及别名断链 |
| 10 | Overview 计数一致性 | 比对 `wiki/overview.md` 健康仪表盘的 Sources/Concepts/Entities/Synthesis 计数与 `wiki/` 实际文件数（质量提示，不阻断） |

---

## 五、REFLECT 操作规范

**触发词**：`reflect`、`综合分析`、`发现规律`

### 何时应主动触发 REFLECT（产能平衡机制）

摄入速度远快于综合速度时，知识库会「广而不深」——大量孤立、单来源概念堆积，却缺乏跨来源的综合判断。出现以下任一信号时，**应主动提示用户执行 REFLECT**（无需等待触发词）：

- **综合覆盖严重滞后**：`Sources 数 / Synthesis 数 > 30`（例：135 来源仅 2 篇 synthesis）。
- **孤立概念积压**：`source_count = 1` 且创建超过 30 天的概念 ≥ 10 个。
- **隐性盲区**：某主题被 ≥ 8 个来源提及却无独立 concept 页（如曾出现的 functional-safety / gan-power-devices）。
- **某主题簇已成熟**：单一主题下 concept 的累计 `source_count` 已较高（如机器人半导体、MCUless、Agent 路线、芯片制造流程），具备综合条件。

LINT 报告与 `overview.md` 应据此给出 REFLECT 建议。

### 四阶段执行

**Stage 0：反向检验（必须最先执行）**
在生成任何合成结论之前，主动搜索反驳证据。
- 若无反对来源，在 synthesis 页的 Limitations 节标注：
  > ⚠ 回音室风险：未找到反驳来源，结论可能存在确认偏差。

**Stage 1：模式扫描**
- 首选：`qmd multi-get ...`（需安装可选外部 qmd）
- qmd 缺席时（本仓库默认）：
```bash
python scripts/tools/wiki_index.py multi-get "wiki/concepts/*.md" --lines 40
python scripts/tools/wiki_index.py multi-get "wiki/entities/*.md" --lines 40
python scripts/tools/wiki_index.py multi-get "wiki/synthesis/*.md" --lines 60
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

### 主题域标签（tags）受控词表

每个 concept/entity/synthesis 页的 `tags` 字段**必须至少包含 1 个主域标签**，取自以下受控词表（禁止自由发挥，避免跨簇统计/导航失效）：

| 主域标签 | 覆盖范围 |
|---|---|
| `embodied-ai` | 具身智能、人形机器人、运动控制、灵巧手、机器人半导体 |
| `automotive-eea` | 汽车电子电气架构、MCU-less、区域控制器、车载通信（GPAN/EtherCAT/10BASE-T1S）、功能安全 |
| `chip` | 芯片设计、制造、封装、EDA、功率器件（GaN 等） |
| `edge-ai` | 端侧推理、TinyML、NPU/MCU 趋势、端侧不可能三角 |
| `agent` | Agent 架构、Harness、MCP、规划/记忆/反馈回路、安全治理 |
| `finance` | 金融数据、量化、市场结构（neodata/westock 相关） |

附加标签（非主域，建议复用既有小写连字符词）：如 `gpan`、`ethercat`、`zonal-gateway`、`mculess`、`vla`、`tsn` 等。

INGEST Step 7/8 创建或更新 concept 页时，若 `tags` 缺失主域标签，按来源主题补打；REFLECT 阶段发现 `tags` 为空或仅含非受控词的概念，应在 Evolution Log 记录并补齐。

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

### 哈希格式规则（写入时校验）
- `raw_sha256` **必须是完整 64 位十六进制字符串**，严禁截断或简写。
  - 原因：截断哈希（如只存前 8 位）会与全量哈希前缀匹配，让 lint 把「未修改」的来源误报为 `⚠ SOURCE MODIFIED`，淹没真正的篡改信号。
  - lint Check 6 会校验长度，非 64 位标记 `❌ MALFORMED HASH`，并作为 `--gate` 关键检查阻断提交。
- raw 文件应避免被 git 行尾规范化（仓库已配置 `.gitattributes` 的 `raw/** -text`），否则 CRLF/LF 变动会改变字节、导致哈希漂移误报。

### Re-ingest 规则
若 lint 报告 `⚠ SOURCE MODIFIED`（SHA-256 不匹配）：
1. 先区分**真实修改**与**误报**：用 `--ignore-all-space` 或重算确认是内容变更，还是行尾/截断导致的假阳性。
2. 若为误报：重算全量 64 位哈希回填 `raw_sha256`，更新 `last_verified`。
3. 若为真实修改：重新摄入该文件（执行完整的外部来源标准流程），更新所有受影响的 concept/entity 页面，并在 Evolution Log 记录：
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

### synthesis/ 与 outputs/ 的边界

- `wiki/synthesis/` 存放**可复用的跨来源综合结论**（参与 Obsidian 图谱，可被 QUERY/REFLECT 引用），如各主题簇 synthesis 页。
- `wiki/outputs/` 存放**过程产物与一次性报告**（lint 报告、gap-report、单次 QUERY 答案、架构审计等），`graph-excluded` 不参与图谱。
- 判定原则：**可复用、会被未来查询引用的结论 → `synthesis/`；一次性过程/报告 → `outputs/`**。不得把可复用综合塞进 outputs/ 以免脱离图谱。

---

## 十三、文档维护规则

- 当本 CLAUDE.md 规则更新时，必须同步更新 `USER_GUIDE.md` 对应章节
- 确保两份文档保持一致，不得出现版本漂移

---

## 十四、自动化门禁机制（pre-commit gate）

仓库挂载了 git pre-commit 门禁，作为「摄入完就跑、不建概念」等问题的**最后一道防线**。

### 工作机制
- hook 脚本：`scripts/githooks/pre-commit`（随仓库版本化）。
- 每次 `git commit` 前自动运行 `python scripts/lint.py --gate`。
- **关键检查失败即阻断提交**：frontmatter 非法、孤儿/断链 wikilink、index 不一致、SHA 截断或不匹配（详见第四节门禁模式）。
- 质量提示类问题（stub/近重复/stale/跨语言/格式）**不阻断**。

### 安装（每个新克隆执行一次）
```bash
git config core.hooksPath scripts/githooks
```

### 绕过（仅在确有必要时）
```bash
git commit --no-verify
```

> 门禁是兜底，不是免责。INGEST/REFLECT 等操作仍须在流程内主动自检（见各节），不得依赖门禁兜底而带病推进。

---

_最后更新：2026-08-11_
