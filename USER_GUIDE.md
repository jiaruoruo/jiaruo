# USER_GUIDE.md — 知识库使用指南

> 本文件是面向用户的操作手册，与 CLAUDE.md 保持同步。
> 当 CLAUDE.md 规则更新时，本文件对应章节必须同步更新。

_最后同步：2026-08-11_

---

## 一、系统概述

本知识库采用三层架构：

```
raw/          ← 你的原始素材（只有你能写入）
  工作/         ← 工作相关素材
    clippings/  ← 网页剪藏（按主题分子目录）
    articles/   ← 外部文章
    pdfs/       ← PDF 文献
    notes/      ← 随手笔记
    personal/   ← 个人写作
  生活/         ← 生活相关素材（同上结构）
wiki/         ← AI 自动维护的知识提炼层
outputs/      ← 最终对外输出产物
```

**你只需要做的事：** 将文章、PDF、网页剪藏放入 `raw/` 对应子目录，然后告诉 AI「ingest」即可。

---

## 二、触发操作的方式

### INGEST — 摄入新来源

**触发词：** `ingest`、`摄入`、`处理这个`，或直接输入一个 URL

| 输入方式 | 示例 |
|---|---|
| 指定文件路径 | `ingest raw/工作/clippings/MyTopic/2026-04-15-xxx.md` |
| 直接输入 URL | `ingest https://example.com/article` |
| 泛指当前文件 | `处理这个` |

**URL 直接输入：** AI 会自动调用 `defuddle` 抓取网页，保存到 `raw/工作/clippings/{topic}/`（topic 根据内容判断），再进入标准摄入流程。若抓取失败，AI 会提示你手动保存。

**摄入流程（12 步）概览：**

1. 读取原始来源（只读 raw/，绝不修改）
2. 计算 SHA-256 哈希（用于完整性验证）
3. 向你展示核心要点，等待确认
4. 生成 slug（英文小写连字符）
5. **来源去重检测**——检查是否已有相同 URL 或同一来源的译文版本
6. 创建 `wiki/sources/<slug>.md`
7. 概念名称对齐检查（aliases 匹配，避免重复建页）
8. 处理提取到的每个概念
9. 处理提取到的每个实体
10. 更新 `wiki/index.md`
11. 检查 `wiki/QUESTIONS.md`，看是否能回答已有问题
12. **收尾自检（强制）**：运行 `python scripts/lint.py --gate`（关键检查失败必须先修）→ 更新索引（qmd 为可选外部引擎，缺席时无需操作）→ 更新 `wiki/overview.md` 仪表盘 → 追加日志

**⚠ 入库前清洗不可见字符：** 从网页 / 微信复制的标题可能带入零宽空格、BOM 等不可见 Unicode 字符，会污染 `raw_file` 路径并触发 lint 误报。AI 在保存 raw 文件与写入 `raw_file` 字段时会自动清洗（见 CLAUDE.md「不可见字符清洗规则」），你无需手动处理；若你手动重命名了 raw 文件，请确保文件名不含这类字符。

**个人写作**（`raw/personal/` 下的文件）：
- 不生成客观摘要，核心论点写入 concept 页的 `My Position` 节
- 不计入 `source_count`（避免自我背书）

---

### QUERY — 查询知识库

**触发词：** 直接提问，或「根据我的知识库……」

AI 会：
1. 用检索获取相关页面：首选 `qmd query`（可选外部语义引擎）；qmd 缺席时（本仓库默认）用 `python scripts/tools/wiki_index.py query "<问题>" --json --top 5`（关键词级）；若皆不可用则读 `wiki/index.md` 手动选取
2. 完整读取最相关的 5 个页面
3. 合成答案，每条结论溯源到具体 `wiki/sources/` 页面
4. 标注各来源的置信度级别
5. 若答案有复用价值，写入 `wiki/outputs/`

**输出格式**根据问题类型自动选择：
- 普通问题 → Markdown 正文
- 比较类（A vs B）→ 表格
- 演示类 → Marp 幻灯片
- 趋势类 → Python matplotlib 代码块
- 清单类 → 结构化列表

---

### LINT — 知识库健康检查

**触发词：** `lint`、`检查`、`健康检查`

运行 `python scripts/lint.py`，执行 10 项检查：

| # | 检查项 |
|---|---|
| 1 | YAML Frontmatter 合法性 |
| 2 | Broken Wikilinks（断链） |
| 3 | Index 一致性 |
| 4 | Stub 页面（正文 < 100 字符） |
| 5 | 近重复概念名称（Jaccard > 0.7） |
| 6 | SHA-256 完整性（哈希长度 64 位校验 + 原始文件是否被修改） |
| 7 | Stale 页面（超过时效阈值） |
| 8 | 跨语言重复（URL + aliases 重叠） |
| 9 | Wikilink 格式规范（禁止中文/驼峰/下划线） |
| 10 | Overview 计数一致性（仪表盘计数 vs 实际文件数，质量提示） |

报告自动保存至 `wiki/outputs/lint-YYYY-MM-DD.md`。AI 会展示摘要并询问是否立即修复。

**门禁模式 `--gate`：** `python scripts/lint.py --gate` 不写报告，仅当**关键检查**（frontmatter / 孤儿断链 / index 一致性 / SHA）失败时返回非零退出码。它被 pre-commit hook 调用，提交前自动拦截带病改动（见下方「自动化门禁」）。质量提示类问题（stub/近重复/stale 等）不阻断提交。

---

### REFLECT — 综合分析

**触发词：** `reflect`、`综合分析`、`发现规律`

AI 会执行四阶段分析：
- **Stage 0**：主动搜索反驳证据（防确认偏差）
- **Stage 1**：批量扫描所有 concept/entity/synthesis 页，识别模式与关联
- **Stage 2**：深度合成，写入 `wiki/synthesis/`
- **Stage 3**：Gap Analysis，识别知识空白，写入 `wiki/outputs/gap-report-*.md`

**AI 何时会主动建议 REFLECT：** 当摄入远快于综合（如来源/综合 > 30）、孤立单源概念积压（≥10 个超 30 天）、或某主题被 ≥8 个来源提及却无独立概念页时，AI 会主动提示你「该做一轮 reflect 了」，避免知识库「广而不深」。

---

### MERGE — 合并重复页面

**触发词：** `merge`、`去重`

AI **绝不自动合并**，必须等你明确确认合并方案后才执行。

跨语言合并（如中文页 + 英文页）：
- 保留英文 slug 为主页
- `aliases` 取两页并集
- 旧 slug 保留为 redirect 文件（不破坏已有链接）

---

### ADD-QUESTION — 记录待探索问题

**触发词：** `我想搞清楚`、`add question`、`记录一个问题`

AI 将问题规范化后写入 `wiki/QUESTIONS.md`，后续 INGEST 时会自动检查是否能回答。

---

## 三、置信度机制

| 来源数 | Confidence | 处理方式 |
|---|---|---|
| 1 个 | `low` | 自动设置 |
| 3+ 个 | `medium` | 自动设置 |
| 5+ 个且无重大矛盾 | 候选 `high` | AI 展示证据，**需要你回复「确认」或「ok」才生效** |

> 个人写作（`raw/personal/`）不计入 source_count。

---

## 四、Wikilink 规范（给你写笔记时参考）

`raw/` 目录下的笔记无需遵守 wikilink 规范，AI 在 INGEST 时会自动处理。

若你在 `raw/` 文件中手写了 wikilinks，请使用**英文小写连字符**格式：
```
✅ [[value-investing]]
❌ [[价值投资]]
❌ [[ValueInvesting]]
```

---

### 主题域标签（concept 页）

每个概念页的 `tags` 字段由 AI 在 INGEST 时自动打上**主域标签**，取自 6 大受控词表：`embodied-ai` / `automotive-eea` / `chip` / `edge-ai` / `agent` / `finance`。你无需手动维护；这是 AI 做跨主题综合与导航的依据。完整定义见 CLAUDE.md「主题域标签（tags）受控词表」。

---

## 五、索引与检索

检索依赖 `qmd`（可选外部语义检索引擎，本仓库不分发）。**当前环境未安装 qmd**，自动降级到仓库自带的 `scripts/tools/wiki_index.py`（关键词级，非语义）：

```bash
python scripts/tools/wiki_index.py query "问题" --json --top 5   # 检索相关页面
python scripts/tools/wiki_index.py multi-get "wiki/concepts/*.md" --lines 40  # REFLECT 扫描
python scripts/tools/wiki_index.py status                        # 统计各类型文件数
```

若需恢复语义检索（嵌入向量），须在原始安装环境确认 `qmd` 来源后安装，并同步 `requirements.txt` 注释。详见 CLAUDE.md「工具链依赖与降级路径」。

---

## 六、自动化门禁（pre-commit）

仓库挂了一道 git 提交前门禁，帮你兜底——避免「摄入完没建概念」「哈希写错」等问题被提交进仓库。

- 每次 `git commit` 前自动运行 `python scripts/lint.py --gate`。
- **关键问题会阻断提交**：frontmatter 非法、引用了不存在的概念页（孤儿断链）、index 不一致、SHA 截断或不匹配。
- 质量提示（stub、近重复等）不阻断，只在常规 `lint` 里提示。

**新克隆仓库后需执行一次安装：**
```bash
git config core.hooksPath scripts/githooks
```

**确需绕过门禁时**（谨慎使用）：
```bash
git commit --no-verify
```

---

## 七、文件放置指南

| 内容类型 | 放入目录 |
|---|---|
| 网页剪藏（工作） | `raw/工作/clippings/{topic}/` |
| 外部文章（工作） | `raw/工作/articles/{topic}/` |
| PDF 文献（工作） | `raw/工作/pdfs/{topic}/` |
| 随手笔记（工作） | `raw/工作/notes/{topic}/` |
| 个人写作/观点文章 | `raw/工作/personal/{topic}/` |
| 网页剪藏（生活） | `raw/生活/clippings/{topic}/` |
| 生活类笔记/文章 | `raw/生活/{type}/{topic}/` |

**命名建议：** `YYYY-MM-DD-标题简写.md`（便于排序）

**目录选择原则：**
- **工作/生活**：按内容是否与职业相关区分
- **{topic}**：内容所属主题，如 `MCULess`、`ISO26262`、`健身`（同类文件应归入同一 topic 子目录）

---

## 八、常见问题

**Q：INGEST 时发现重复来源怎么办？**
A：AI 会提示你，询问是否继续。若是同一来源的译文版本，你可选择摄入为独立页面（使用 `canonical_source` 字段关联原文）或跳过。

**Q：SHA-256 不匹配（SOURCE MODIFIED）怎么处理？**
A：先区分真假。①若是 raw 文件确实改了内容，执行 `ingest` 重新处理，AI 会更新相关 concept/entity 页面。②若只是行尾（CRLF/LF）变动或早期写入了截断哈希（非 64 位），属误报，AI 会重算全量 64 位哈希回填——仓库已用 `.gitattributes` 固定 raw 行尾、并由 lint Check 6 校验哈希长度来防这类误报。③若是 `raw_file` 路径被零宽空格 / BOM 等不可见字符污染（多见于从网页复制的标题），属误报，AI 会清洗文件名与字段值后重算哈希——见 CLAUDE.md「不可见字符清洗规则」。

**Q：为什么我 commit 被拦下来了？**
A：pre-commit 门禁发现了关键问题（多半是引用了不存在的概念页，即孤儿断链）。按提示修复后重新提交；确需绕过用 `git commit --no-verify`（见第六节）。

**Q：检索返回 No results / 质量差？**
A：当前默认用 `wiki_index.py` 关键词检索。若结果不佳，可换更精确的关键词，或安装可选外部 `qmd` 获得语义检索（需先 `qmd embed` 生成嵌入向量）。

**Q：concept 页的 confidence 何时能升到 high？**
A：需要 5+ 个来源且无重大矛盾，AI 会展示证据请你确认，你回复「确认」或「ok」后才升级。AI 不会自动升级。

---

_本文档与 CLAUDE.md 保持同步，最后更新：2026-08-11_
