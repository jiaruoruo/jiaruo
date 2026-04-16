# USER_GUIDE.md — 知识库使用指南

> 本文件是面向用户的操作手册，与 CLAUDE.md 保持同步。
> 当 CLAUDE.md 规则更新时，本文件对应章节必须同步更新。

_最后同步：2026-04-15_

---

## 一、系统概述

本知识库采用三层架构：

```
raw/          ← 你的原始素材（只有你能写入）
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
| 指定文件路径 | `ingest raw/clippings/2026-04-15-xxx.md` |
| 直接输入 URL | `ingest https://example.com/article` |
| 泛指当前文件 | `处理这个` |

**URL 直接输入：** AI 会自动调用 `defuddle` 抓取网页，保存到 `raw/clippings/`，再进入标准摄入流程。若抓取失败，AI 会提示你手动保存。

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
12. 更新 qmd 索引并追加日志

**个人写作**（`raw/personal/` 下的文件）：
- 不生成客观摘要，核心论点写入 concept 页的 `My Position` 节
- 不计入 `source_count`（避免自我背书）

---

### QUERY — 查询知识库

**触发词：** 直接提问，或「根据我的知识库……」

AI 会：
1. 用 `qmd query` 语义搜索（若不可用则降级为手动索引匹配）
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

运行 `python scripts/lint.py`，执行 9 项检查：

| # | 检查项 |
|---|---|
| 1 | YAML Frontmatter 合法性 |
| 2 | Broken Wikilinks（断链） |
| 3 | Index 一致性 |
| 4 | Stub 页面（正文 < 100 字符） |
| 5 | 近重复概念名称（Jaccard > 0.7） |
| 6 | SHA-256 完整性（原始文件是否被修改） |
| 7 | Stale 页面（超过时效阈值） |
| 8 | 跨语言重复（URL + aliases 重叠） |
| 9 | Wikilink 格式规范（禁止中文/驼峰/下划线） |

报告自动保存至 `wiki/outputs/lint-YYYY-MM-DD.md`。AI 会展示摘要并询问是否立即修复。

---

### REFLECT — 综合分析

**触发词：** `reflect`、`综合分析`、`发现规律`

AI 会执行四阶段分析：
- **Stage 0**：主动搜索反驳证据（防确认偏差）
- **Stage 1**：批量扫描所有 concept/entity/synthesis 页，识别模式与关联
- **Stage 2**：深度合成，写入 `wiki/synthesis/`
- **Stage 3**：Gap Analysis，识别知识空白，写入 `wiki/outputs/gap-report-*.md`

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

## 五、qmd 索引维护

qmd 提供语义搜索能力。若搜索结果为空或质量差，执行：

```bash
qmd embed        # 生成嵌入向量（首次使用或新增文件后需执行）
qmd update       # 更新索引（INGEST 后 AI 会自动执行）
qmd status       # 查看索引状态
```

---

## 六、文件放置指南

| 内容类型 | 放入目录 |
|---|---|
| 网页剪藏 | `raw/clippings/` |
| 外部文章（Markdown） | `raw/articles/` |
| PDF 文献 | `raw/pdfs/` |
| 随手笔记 | `raw/notes/` |
| 个人写作/观点文章 | `raw/personal/` |
| 图片 | `raw/images/` |

**命名建议：** `YYYY-MM-DD-标题简写.md`（便于排序）

---

## 七、常见问题

**Q：INGEST 时发现重复来源怎么办？**
A：AI 会提示你，询问是否继续。若是同一来源的译文版本，你可选择摄入为独立页面（使用 `canonical_source` 字段关联原文）或跳过。

**Q：SHA-256 不匹配（SOURCE MODIFIED）怎么处理？**
A：说明 raw/ 下的原始文件被修改过。执行 `ingest` 重新处理该文件，AI 会自动更新所有相关 concept/entity 页面。

**Q：qmd query 返回 No results？**
A：执行 `qmd embed` 生成嵌入向量后重试。

**Q：concept 页的 confidence 何时能升到 high？**
A：需要 5+ 个来源且无重大矛盾，AI 会展示证据请你确认，你回复「确认」或「ok」后才升级。AI 不会自动升级。

---

_本文档与 CLAUDE.md 保持同步，最后更新：2026-04-15_
