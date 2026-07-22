---
type: gap-report
date: 2026-07-22
graph-excluded: true
---

# 知识空白报告（Gap Report）— 2026-07-22

> 由 REFLECT 操作 Stage 3 产出。统计基准：293 sources / 85 concepts / 31 entities / 10→11 synthesis。来源/综合比 293:11 ≈ 26.6:1（低于 REFLECT 主动触发线 30:1，但功能安全簇刚完成大规模摄入，综合覆盖率仍偏薄）。

---

## 一、孤儿概念积压（source_count=1 且创建 >30 天）

命中 REFLECT 主动触发条件（≥10 个）。以下 11 个概念仅单来源、且超 30 天未补充，存在「广而不深」风险：

| 概念页 | 创建日期 | 天数 | 主题域线索 |
|---|---|---|---|
| `multimodal-api` | 2026-04-13 | 100 | API（edge-ai/agent 交叉） |
| `text-to-speech` | 2026-04-13 | 100 | TTS |
| `video-generation` | 2026-04-13 | 100 | video |
| `voice-cloning` | 2026-04-13 | 100 | TTS |
| `reinforcement-learning-locomotion` | 2026-04-15 | 98 | reinforcement-learning（embodied-ai） |
| `tensor-mathematics` | 2026-04-28 | 85 | mathematics |
| `agent-security-governance` | 2026-04-25 | 88 | agent |
| `llm-knowledge-management` | 2026-04-25 | 88 | knowledge-management |
| `autosar-configuration-toolchain` | 2026-05-14 | 69 | autosar（automotive-eea） |
| `automotive-sensor` | 2026-05-17 | 66 | sensor（automotive-eea） |
| `claude-code-workflow` | 2026-05-14 | 69 | claude-code |

> 注：其中 `multimodal-api` / `text-to-speech` / `video-generation` / `reinforcement-learning-locomotion` / `robot-simulation-framework` / `sim-to-real-transfer` 同时被 lint Check 7 标记为 Stale（high-volatility，超 90 天阈值），与孤儿清单高度重叠——这些是「既单薄又老化」的高优先回填对象。

**建议**：对 autosar-configuration-toolchain、automotive-sensor、agent-security-governance 等仍具现实价值的单源概念，优先在下次相关摄入时补源；纯兴趣型（如 voice-cloning、video-generation）可保留为 stub 或合并。

---

## 二、隐性盲区（被大量提及却无独立概念页）

按「≥8 个文件提及但无专属 concept 节点」规则扫描全库 concept+source 正文，发现 3 个突出盲区：

| 候选术语 | 提及次数 | 涉及文件数 | 现状 | 建议 |
|---|---|---|---|---|
| **`asil`** | 184 | 62 | 仅在 `functional-safety` 子项 + `iso-26262` 间接承载，**无独立概念页** | **优先创建** `concepts/asil.md`（分级方法论：S×E×C、ASIL 分解、与 AEC-Q 区别） |
| **`spfm`** | 42 | 18 | 由 `hardware-metrics`/`pmhf` 间接承载，无独立页 | 建议创建 `concepts/spfm.md` 或并入 `hardware-metrics` |
| **`lfm`** | 41 | 17 | 同上 | 建议与 SPFM 一并处理 |

> `asil` 被 62/369 个 wiki 文件提及却无节点，是本次扫描最显著的盲区。它是功能安全量化体系的入口，值得独立成页并反链回 `functional-safety` / `iso-26262` / `hardware-metrics`。

---

## 三、覆盖稀薄 / 待强化主题

- **ISO 26262 Part 6（软件层面）、Part 8（支持过程）、Part 9（ASIL 导向分析）**：标准已摄入但尚无针对性综合或概念深挖；AFSP 备考综合亦未覆盖软件安全（见其 Limitations）。建议后续摄入 OEM/Tier1 实际项目文档补足。
- **GB/T 34590 与 ISO 26262 的条文差异**：本批国标为征求意见稿，差异分析待正式发布后做专项对比综合。
- **机器人功能安全落地案例**：`robot-safety` 仍是单源概念（ISO/TS 15066 等），汽车→机器人迁移多为趋势判断，缺已认证反向案例。

---

## 四、标签合规

✅ 全部 85 个概念页均含至少 1 个受控主域标签（embodied-ai / automotive-eea / chip / edge-ai / agent / finance），无缺失。本项无需回填。

---

## 五、本次 REFLECT 已消项

- **新建综合页** `wiki/synthesis/functional-safety-landscape-synthesis.md`（74 源，medium），消解功能安全簇「广而不深」问题，并反链现有 `iso26262-afsp-study-guide` 子综合。
- 综合页已显式标注回音室风险（AFSP 单机构、规范来源非批判性、机器人迁移未验证、国标草稿时效）。

---

## 六、行动清单（供老贾决策）

1. 【高优先】创建 `concepts/asil.md`（184 提及/62 文件盲区）。
2. 【中优先】补齐孤儿概念 autosar-configuration-toolchain / automotive-sensor / agent-security-governance 的二次来源。
3. 【中优先】处理 Stale 6 项（multimodal-api 等），或确认保留为 stub。
4. 【低优先】SPFM/LFM 是否独立成页或并入 hardware-metrics。
5. 【待触发】GB/T 34590 正式版发布后做 ISO↔GBT 差异对比综合。
