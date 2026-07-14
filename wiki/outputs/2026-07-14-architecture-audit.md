---
type: output
title: "知识库架构设计审计"
date: 2026-07-14
graph-excluded: true
---

# 知识库架构设计审计（2026-07-14）

> 触发：`QUERY` — 老贾问"我的知识库架构设计有哪些需要优化的吗？"
> 方法：基于 `CLAUDE.md` 契约 + `overview.md` 健康仪表盘 + 概念模板/实际页面样本（mculess-architecture 等）的案头审查，**未做全量脚本统计**。

## 一、已验证的良好设计（建议保持不动）

| 设计 | 现状证据 | 评价 |
|---|---|---|
| 三层分离 + `raw/` 只读铁律 | CLAUDE.md 第 10-43 行 | 边界清晰，人类/LLM 职责分明 |
| Wikilink 英文小写连字符 + 中文走 `aliases` | 模板 + lint Check 9 | 图谱稳定的基石，已固化为门禁 |
| SHA-256 完整性 + pre-commit gate | lint Check 6 + 第十四节 | 最后防线有效（本次 57 误报被拦） |
| `confidence: high` 人工确认卡点 | 第十节 | 防 AI 自嗨，设计正确 |
| REFLECT 产能平衡触发机制 | 第五节（S/R>30 等信号） | 已把比值从 34:1 压回 25:1 |
| 多助手并行约定 | 第 44-53 行 | 冲突面已识别，约定合理 |
| 元数据字段已较完整 | 模板含 `tags/source_count/confidence/domain_volatility/aliases` | `domain_volatility` 已落地（mculess 页=high），Check 7 有字段支撑 |

## 二、优化清单

### P0 — 工程化 / 可复现性（换机器即断的风险）

**1. Python 依赖未版本化**
- 现状：仓库内**无 `requirements.txt`**（已搜索确认 0 命中）。`python-docx / python-pptx / openpyxl / beautifulsoup4` 及 `qmd` 的依赖均未锁定。
- 风险：知微与 Claude Code 在不同机器并行维护，环境漂移会让"摄入二进制文件（pptx/docx/xlsx/vsdx）"直接失败——本次 articles 批次正是靠临时装库才跑通。
- 建议：沉淀 `requirements.txt`（或 `pyproject.toml`），列出 INGEST/LINT 实际 import 的包与版本。

**2. `qmd` 是外部未版本化单点依赖**
- 现状：CLAUDE.md 大量依赖 `qmd`（Step 12.2 `qmd update`、QUERY Q1 `qmd query`、REFLECT `qmd multi-get`、LINT `qmd status`），但 `qmd` 不在仓库内，无安装说明、无版本约束。
- 风险：一旦 `qmd` 不可用，INGEST 收尾 + QUERY 检索全部降级为手扫 `index.md`（契约已写降级路径，但体验断裂、易漏）。
- 建议：在 `README.md`/`CLAUDE.md` 明确 `qmd` 的安装方式与版本；或提供一个仓库内的轻量 fallback 索引脚本，使"qmd 缺席"时不依赖人工扫文件。

### P1 — 元数据治理（影响检索质量与综合覆盖率）

**3. `tags` 有字段但无受控词表**
- 现状：概念模板已有 `tags: []`（mculess 页实际打了 `mculess/automotive/eea/zonal-gateway/bom-cost`）。但契约**未规定主题域受控词表**，tags 是自由文本。
- 风险：无法可靠做"跨主题簇综合覆盖率"统计，也无法生成领域导航；不同助手打的 tag 词形可能不一致（如 `automotive` vs `auto`）。
- 建议：在 CLAUDE.md 定义 6 大主题域受控词表（如 `embodied-ai / automotive-eea / chip / edge-ai / agent / finance`），并在 INGEST Step 7 强制每个 concept 至少打 1 个主域 tag。

**4. `overview.md` 健康计数靠手填**
- 现状：Sources/Concepts/Entities 计数在 Step 12.3 手动更新（本次 228/74/31/9）。lint Check 3 只校验 `index.md` 一致性，**不校验 overview 计数**。
- 风险：计数与真实文件数可能漂移（本次靠人工对齐，无自动校验）。
- 建议：让 `lint.py` 顺带校验 overview 计数段，或由 lint 自动生成 overview 的计数行，消除手填漂移。

### P2 — 索引与并行协作

**5. `index.md` 单文件 + 手动维护，且"权威"关系含糊**
- 现状：`index.md` 把 228 个 source 全列在一个 md，Step 10 要求"将来源从 Unprocessed 移动到 Processed"（手动）。但 `qmd` 另有自己的索引库（用于 `query`）。两者"谁是检索权威"在契约里没说清。
- 风险：大文件 + 双助手并行 append 易冲突；手挪列表易漏（本次靠脚本批量改）。
- 建议：明确"qmd 索引 = 检索权威，index.md = 人类可读导航视图"，并让 index.md 可由脚本从文件树/qmd 生成，减少手填。

**6. `log.md` 并行 append 冲突面**
- 现状：单文件日志，双助手都 append。git 纯追加通常能 auto-merge，但同一行边界会冲突（约定第 6 条已要求"保留双方变更"，属治标）。
- 建议：日志按日期分文件（`log-YYYY-MM-DD.md`），彻底消除冲突面；或保留单文件但约定"每段以日期时间前缀保证行唯一"。

### P3 — 导航体验（非必须）

**7. `synthesis/` vs `outputs/` 边界对使用者略混**
- 现状：`synthesis/` 参与图谱（正式知识），`outputs/` graph-excluded（lint 报告 / gap-report / query 答案）。但 gap-report 既含"过程产物"也含"可复用结论"。
- 建议：在 CLAUDE.md 明确"可复用结论必落 `synthesis/`，过程/报告必落 `outputs/`"，并在导航页区分两类。

**8. 缺"按主题域"导航视图**
- 现状：有 `tags` 但 `index.md` 只按类型（source/concept/entity/synthesis）组织，无领域视图。
- 建议：加 `wiki/domains.md`（graph-excluded），按受控词表汇总各域概念/synthesis；或由 lint 生成。

## 三、落地优先级建议

- **立即做（P0）**：补 `requirements.txt` + 明确 `qmd` 安装方式。这两项零架构改动、纯工程沉淀，却直接决定跨机器可复现性。
- **近期做（P1）**：定义 tags 受控词表 + 让 lint 校验 overview 计数。提升元数据可统计性。
- **观察（P2/P3）**：索引权威澄清、日志分文件、领域导航——可在下次维护痛点出现时再动，不必现在重构。

## ⚠ Confidence Notes

- 本报告为**架构审计**（非知识综合），结论基于契约文本 + 少量样本页推断，**未做全量脚本统计**。
- P0#1 的包清单（python-docx/pptx/openpyxl/beautifulsoup4 + qmd）依据 articles 批次 INGEST 实践经验，落地前需用 `pip freeze` 核实实际 import。
- P1#3 tags 词形不一致、P2#5 index 冲突面等为**推断风险**，建议落地前用脚本量化确认（如统计 tags 去重分布、grep index.md 行数）。
- 已验证项（domain_volatility/tags 字段存在、requirements.txt 缺失）置信度中高。
