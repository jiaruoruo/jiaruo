---
type: gap-report
date: 2026-06-29
graph-excluded: true
---

# Gap Report — 2026-06-29（定时 REFLECT）

_自动化定时任务生成。本轮无新增来源（无 URL 输入、index Unprocessed 为空），故 REFLECT 聚焦存量盲区与单源积压复检。_

## 一、产能平衡指标

| 指标 | 数值 | 阈值 | 状态 |
|---|---|---|---|
| Sources / Synthesis 比 | 143 / 6 ≈ 24:1 | < 30 | ✅ 达标 |
| 单源概念（source_count=1） | 32 | — | ⚠ 偏高 |
| 单源且 >30 天的孤立概念 | 18 | — | ⚠ 待深化 |
| Open Questions | 5 | — | 跟踪中 |

## 二、上轮 P0 盲区复检（2026-06-27 gap 报告）

两项 P0 盲区均已补建概念页，盲区消除：

- `functional-safety`（功能安全）：被 25 个来源提及 → **已建页** ✅
- `gan-power-devices`（GaN 功率器件）：被 12 个来源提及 → **已建页** ✅

## 三、本轮新发现盲区（多来源提及但无独立 concept 页）

| 候选概念 | 被提及来源数 | 优先级 | 说明 |
|---|---|---|---|
| `ota-update`（OTA 空中升级） | 14 | **P0** | 跨「软件定义汽车 / MCULess / EEA」三簇高频出现，是核心桥接概念，缺页造成横向链接断裂 |
| `thermal-management`（散热/热管理） | 9 | P1 | 多见于芯片簇与功率器件，可作为 advanced-packaging / gan-power-devices 的桥接点 |
| `cybersecurity-automotive`（车载信息安全） | 4 | P2 | 与 functional-safety 配对，构成「安全」双支柱；当前覆盖稀薄 |

> 建议：下次摄入相关来源时优先建 `ota-update` 页，并连到 software-defined-vehicle / eea-architecture / mculess。

## 四、单源孤立概念积压（source_count=1 且 >30 天，按年龄排序）

以下概念长期单源，建议后续摄入时优先强化定义或补充矛盾点：

model-context-protocol(77d)、multimodal-api(77d)、text-to-speech(77d)、video-generation(77d)、voice-cloning(77d)、reinforcement-learning-locomotion(75d)、can-eth-protocol-conversion(74d)、eea-architecture(74d)、time-sensitive-networking(74d)、agent-security-governance(65d)、llm-knowledge-management(65d)、robot-software-architecture(65d)、llm-benchmark-evaluation(63d)、autosar-configuration-toolchain(46d)、claude-code-workflow(46d)、automotive-sensor(43d)、humanoid-robot-supply-chain(43d)。

特别注意：`eea-architecture` 作为顶层框架概念却仅单源支撑（上轮已标记失衡），仍待补充佐证来源。

## 五、Limitations

> ⚠ 回音室风险：本轮为存量复检，未引入新外部来源，结论基于现有库内交叉计数，可能存在确认偏差。盲区提及计数为关键词匹配（中英混合），存在少量误差。
