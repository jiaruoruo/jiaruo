---
type: output
title: "SGS AFSP 培训练习题完整解题答案（结合 ISO 26262 / GB-T 34590）"
date: 2026-07-21
graph-excluded: true
tags:
  - automotive-eea
  - functional-safety
  - iso-26262
  - gbt-34590
  - sgs-afsp
  - exam-prep
  - asil
  - hardware-metrics
  - hara
  - fsc
  - tsc
confidence: medium
source_count: 34
---

# SGS AFSP 培训练习题完整解题答案（结合 ISO 26262 / GB-T 34590）

> **用法说明**：本文件是 SGS TÜV Saar ISO 26262 AFSP 培训 36 份练习题扫描件（Day 1–Day 3 + SN 29500 查表）的**解题答案与推导**。所有结论均溯源到具体 `wiki/sources/<slug>.md` 源页，并以 ISO 26262:2018 / GB-T 34590 标准条款为判定依据。
>
> **重要前提**：Day 1 的 HARA 矩阵（p3–p7）与 Day 3 的度量计算表（p6–p7）在扫描件中**为空白练习模板**，并未预填数值。因此本答案对 HARA 给出**方法论 + 完整推导示例**（锚定培训给定的 SG1=ASIL B），对 Day 3 计算直接采用培训给定的结果数值并补充推导逻辑。凡推导示例均标注 `【推导示例】`，凡培训给定值标注 `【培训给定】`。

---

## 0. 解题方法论总览

AFSP 考试的核心能力不是背诵条文，而是 **"在给定 item、给定故障模式、给定元器件 FIT 的条件下，正确选择安全机制、计算度量指标、判断 ASIL 达标性"**。三天的练习题对应 ISO 26262 安全生命周期的三段输出：

| 阶段 | 培训日 | 标准依据 | 输入 | 输出 |
|---|---|---|---|---|
| 概念阶段 | Day 1 | Part 3 | Item Definition | HARA → ASIL → Safety Goal |
| 系统层面 | Day 2 | Part 4 | FSC（FSR） | TSC（SYSR/SYSELR）→ HW/SW 分配 |
| 硬件层面 | Day 3 | Part 5 | HSR | SPFM / LFM / PMHF 计算与达标判定 |

---

## 1. Day 1 题解：HARA 与 ASIL 定级

### 1.1 Item Definition（起点）【培训给定】

- **Item**：电动汽车的 **Torque Demand（转矩需求）** 功能（[[sources/sgs-afsp-day1-item-definition-purpose-function]]）。
- **功能描述**：驾驶员踩加速踏板 → 系统按请求由 E-motor 输出对应转矩；用于全球量产乘用车；能量来自 **400 V 电池**；需向驾驶员提示运行状态与故障。
- **功能框图**：`Driver torque request → Logic → Power Unit → E-motor`，辅助交互：`400V Battery → Power Unit`、`Indication (to other item)`。
- **环境与外部措施**（[[sources/sgs-afsp-day1-item-definition-context]]）：公共道路交通；法规含 **ECE-R100** 与 ISO 26262；外部风险降低措施 = 驾照、主动/被动安全（气囊/安全带）、独立机械驻车装置。**外部措施不属于 ISO 26262 内部安全机制，但影响可控性 C 的评估。**

> 解题要点：Item Definition 是 HARA 的输入，假设必须前后一致；框图里每个功能块（Logic / Power Unit / E-motor）后续都会在 FSC/TSC 中被拆成安全机制。

### 1.2 失效模式识别（Malfunction）【培训给定】

HARA 第 1 步识别 item 的 malfunction（[[sources/sgs-afsp-day1-hara-exercise-p1]]）：

- **M1 — Torque demand without driver request**：无驾驶员请求时的转矩需求 → 非预期车辆移动 / 非预期加速。
- **M2 — No torque demand at driver request**：驾驶员请求时无转矩需求 → 失速 / 无响应。

> 解题要点：malfunction 是"功能违背"，不是危害本身。每个 malfunction 要在不同运行场景下分别评 S/E/C。

### 1.3 情景库（Scenarios under examination）【培训给定】

（[[sources/sgs-afsp-day1-hara-exercise-p2]]）

| 编号 | 运行场景 | 驾驶情景 |
|---|---|---|
| S1 | Parking | 停车场/车库，车内无人 |
| S2 | Parking | 停车场/车库，车内有人（如熟睡儿童） |
| S3 | Standing | 路口/红灯前静止 |
| S4 | Driving | 乡村道路超车 |

> 解题要点：场景越具体，ASIL 越可辩护。S2（车内有人）通常会抬高严重度或可控性。

### 1.4 ASIL 判定方法（S/E/C 三维查表）

依据 ISO 26262-3:2018（对应 GB-T 34590-3），ASIL 由三维组合确定（[[concepts/asil]]）：

- **S（严重度）**：S0 无伤；S1 轻/中伤；S2 严重（可能存活）；S3 危及生命/致命。
- **E（暴露度）**：E0 不可信；E1 极低；E2 低；E3 中；E4 高。
- **C（可控性）**：C0 可控；C1 易控；C2 通常可控；C3 难控/仅靠运气可控。

**标准 ASIL 判定表（C3 最难控情形为基准，C 等级降低可使 ASIL 下调）**：

| S \ E | E1 | E2 | E3 | E4 |
|---|---|---|---|---|
| **S1** | QM | QM | A | A |
| **S2** | QM | QM | A | B |
| **S3** | A | B | C | D |

- 上表为 **C3**（最难控）基准列；当可控性为 C2/C1/C0 时，对应格的 ASIL 依次下调（例如 S3·E4·C3=D，S3·E4·C2=C，S3·E4·C1=B，S3·E4·C0=QM）。
- 任意组合中 S0 → QM。

### 1.5 完整解题示例（推导 SG1 = ASIL B、SG2 = ASIL C）【推导示例】

培训给定的锚点是 **SG1 = "Unintended acceleration has to be avoided"，ASIL B**（[[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]）。下面演示如何由 HARA 推导出这一等级。

**对 M1（非预期加速）在 S4（乡村道路超车，驾驶）下评估：**

- **S**：超车中发生非预期加速，可能追尾/对撞 → 取 **S3**（危及生命）。
- **E**：驾驶工况在公共道路高频出现 → 取 **E4**（高暴露）。
- **C**：需论证可控性。培训将 SG1 定为 ASIL B，逆推要求 C 取 **C1**（S3·E4·C1 → B）。论证逻辑：车辆具备机械驻车制动之外的常规制动能力、且外部措施（安全带/气囊）存在，驾驶员通过制动+松加速可"易控"（C1）。若学员判定为 C2，则得 C；C3 则得 D——这正是 HARA 可辩护性的考点。

**对 M1 在其他场景（节选）：**

- M1 @ S1（停车无人）：S 显著下降（无乘员伤亡风险）→ 通常 QM 或 A，不影响 SG 最高等级。
- M1 @ S2（停车有人）：S 抬升（熟睡儿童），但 E 低（停车）→ 约 A/B。

**对 M2（失速/无响应）在 S4（超车）下评估：**

- 失速在高速超车中同样危险 → S3；E4；但驾驶员可惯性滑行/靠边，可控性通常 C2 → 得 **C**。**C 高于 M1 的 B**（ASIL 等级排序 QM < A < B < C < D），故该 item 的 **worst-case（最高）ASIL 应取 M2 产生的 ASIL C**（即派生安全目标 SG2），即本题整体最高安全等级为 **ASIL C**。

> 解题结论：**HARA 输出两个 Safety Goal——SG1 = "Unintended acceleration has to be avoided"（来自 M1，ASIL B），SG2 = 派生安全目标（来自 M2，ASIL C）**。本 item 的 **worst-case（最高）ASIL 为 ASIL C**（M2 在 S4 下 S3·E4·C2 组合，高于 SG1 的 B）。考试时务必逐场景写 rationale（后果 + 理由），不能只给字母（见 1.6）。
>
> ⚠️ **衔接说明**：培训后续的 FSC/TSC/HWSR 主线围绕 SG1（ASIL B）展开（见第 2、3 章）；但若严格按 HARA 的 worst-case 原则，整个 item 的最高安全要求等级为 **ASIL C**，相关安全要素至少应满足 C。考试中常考"何时取 B、何时取 C"的辨析。



> **完整 HARA 矩阵（全部 8 个 malfunction × scenario 组合）【推导示例】**
>
> 以下按 ISO 26262-3 的 S/E/C 三维评估法逐格填写。模板（p4–p7）原为空，理由为基于安全工程判断 + 培训锚点（SG1=ASIL B 来自 M1@S4，SG2=ASIL C 来自 M2@S4）反推，**非扫描件原值**，仅供方法演示。

| Malfunction | Scenario | Consequence of fault（worst-case 伤害） | S（值 + 理由） | E（值 + 理由） | C（值 + 理由） | ASIL |
|---|---|---|---|---|---|---|
| **M1** 非预期加速 | S1 停车·无人 | 车辆突前冲，撞设施/他车/行人（车内无人） | **S1**：车内无人、车速极低，最坏仅财产/轻微外伤 | **E2**：停车为低频工况 | **C1**：可立即断电停住，易控 | **QM** |
| **M1** 非预期加速 | S2 停车·有人 | 熟睡儿童随车突移撞内饰受伤 | **S2**：乘员受撞击伤、可存活；若判撞墙高速可升 S3 | **E2**：停车低频 | **C2**：车内人无意识需车外干预，通常可控 | **QM**（S2·E2 基准即 QM） |
| **M1** 非预期加速 | S3 路口静止 | 红灯前突前冲追尾前车 | **S2**：追尾致乘员轻伤 | **E3**：路口等待常见（红绿灯频繁） | **C1**：松加速+制动即停，易控 | **QM**（S2·E3·C1 由基准 A 下调） |
| **M1** 非预期加速 | S4 超车 | 超车中非预期加速，追尾/失控 | **S3**：危及生命 | **E4**：驾驶高频 | **C1**：常规制动+松加速可“易控” | **B** ← SG1 |
| **M2** 失速 | S1 停车·无人 | 停车时无法加速（本就停着，几乎无后果） | **S1** | **E2** | **C1** | **QM** |
| **M2** 失速 | S2 停车·有人 | 车内人想驶离但车不动，无直接伤害 | **S1** | **E2** | **C1** | **QM** |
| **M2** 失速 | S3 路口静止 | 起步失败致堵塞/被后车追尾 | **S1**：静止失控风险低 | **E3** | **C1**：可重启/靠边 | **QM** |
| **M2** 失速 | S4 超车 | 超车中失速，无法完成超车，对向车临近→正面碰撞 | **S3**：高速对撞危及生命 | **E4**：驾驶高频 | **C2**：可惯性滑行/靠边，但超车时间窗窄，通常可控非易控 | **C** ← SG2（worst case） |

**worst-case 汇总**：
- SG1（来自 M1）= **ASIL B**（M1 各场景中最高为 M1@S4 = B）；
- SG2（来自 M2）= **ASIL C**（M2 各场景中最高为 M2@S4 = C）；
- **整个 item 的最高安全要求等级 = ASIL C**（取所有组合最高，即 M2@S4），与 §1.5 结论一致。


### 1.6 Analysis of Results（HARA 输出形式）【培训给定】

（[[sources/sgs-afsp-day1-hara-exercise-p8]]）汇总表模板格式：

```
Malfunction (event)        →  Safety Goal            →  Rating: ASIL
Torque demand w/o request  →  SG1 Avoid unintended accel.  →  ASIL B
No torque demand @ request →  SG2 (派生)             →  ASIL C (示例)
```

每一格（p4–p7 模板）需填四栏：**Consequence of fault（worst-case 伤害）+ Reason for S + Reason for E + Reason for C**。ASIL 不是先验给定，而是对每个（malfunction × scenario）组合评出，再取 worst case 定为 SG 的 ASIL。

---

## 2. Day 2 题解：FSC 与 TSC 需求链

### 2.1 Safety Goal 的安全相关特征（FSC 起点）【培训给定】

SG1 = "Unintended acceleration has to be avoided"，**ASIL B**（[[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]）。需填写 5 项安全相关特征：

| 特征 | 含义 | 本案例示例 |
|---|---|---|
| Integrity | ASIL 等级 | ASIL B |
| Safe State | 故障后车辆应进入的安全状态 | 转矩=0 / 电机断电，车辆安全停车 |
| FTTI | 从故障到危险状态的最大允许时间 | 视设计定（典型百毫秒级，需记录） |
| Warning Concept | 警告策略 | 故障检测后通过 Display 提示驾驶员 |
| Degradation Concept | 降级策略 | 检测故障后过渡进入 safe state |

### 2.2 FSR 分解（FSC → FSR）【培训给定 + 推导填充】

SG1 = "Unintended acceleration has to be avoided"（ASIL B）被细化为 **FSR1–FSR6**，分配到初步安全架构的 6 个元素（[[sources/sgs-afsp-day2-fsc-requirements-architecture]]）。

**E/E 初步安全架构框图：**

```
Driver torque request ──▶ Logic ──▶ Actuator ──▶ E-motor
        │                    │           │            │
   400V Supply         fault detect   safe state   motor monitoring
                                   │
                             Indication ──▶ other item (Display, QM)
```

**FSR1–FSR6 分配表：**

| ID | Functional Safety Requirement（功能安全要求文本） | ASIL | 架构元素 |
|---|---|---|---|
| FSR1 | The driver torque request shall be acquired and plausibility-checked (e.g., pedal position corroborated by redundant signals) so an unintended/implausible acceleration demand is detected. | B | Driver torque request |
| FSR2 | The logic element shall evaluate the torque request against safety limits and detect an unintended-acceleration condition within the FTTI; on detection it shall command the safe state. | B | Logic |
| FSR3 | The actuator shall execute only a plausibilized torque command and, on fault detection, transition the powertrain to the safe state (torque = 0 / motor de-energized). | B | Actuator |
| FSR4 | The E-motor shall follow the commanded torque; its actual torque/output shall be monitored so any deviation beyond tolerance is detected and reported to the logic. | B | E-motor |
| FSR5 | The 400V supply shall be monitored and, on fault or on transition to safe state, be safely de-energized/isolated so unintended torque cannot be maintained. | B | 400V Supply |
| FSR6 | On detection of a safety-relevant fault, a warning shall be issued to the driver via the indication interface within the FTTI. | B* | Indication to other item |

**FSR1–FSR6 分配表（中文版）：**

| ID | 功能安全要求文本（中文） | ASIL | 架构元素 |
|---|---|---|---|
| FSR1 | 应获取驾驶员扭矩请求并进行合理性校验（如踏板位置由冗余信号佐证），以便检测到非预期/不合理的加速需求。 | B | Driver torque request（驾驶员扭矩请求） |
| FSR2 | 逻辑单元应将扭矩请求与安全限值比对，并在 FTTI 内检测非预期加速工况；检测后须指令系统进入安全状态。 | B | Logic（逻辑单元） |
| FSR3 | 执行器仅应执行经过合理性校验的扭矩命令，并在故障检测时将动力系统转入安全状态（扭矩=0 / 电机断电）。 | B | Actuator（执行器） |
| FSR4 | 电机应跟随指令扭矩；其实际扭矩/输出应被监测，以使超出容差的偏差被检测并上报逻辑单元。 | B | E-motor（电机） |
| FSR5 | 应监测 400V 供电，并在故障或转入安全状态时安全断电/隔离，使非预期扭矩无法维持。 | B | 400V Supply（400V 供电） |
| FSR6 | 检测到安全相关故障时，应在 FTTI 内通过指示接口向驾驶员发出警告。 | B* | Indication to other item（向其他 item 指示） |

> **溯源与诚实标注**：源页左侧 FSR 表格文本为扫描件、未逐字转录，上表为**基于 SG1（避免非预期加速，ASIL B）+ 6 个架构元素 + §2.1 五项安全特征（Safe State / FTTI / Warning / Degradation）的推导填充**，供考试答题框架使用，非原稿逐字内容。
>
> **ASIL 继承规则**：FSR 必须继承或调整 SG 的 ASIL。本案例 SG1 = ASIL B 且未标注 ASIL 分解，故 **FSR1–FSR5 全部继承 ASIL B**。
>
> **FSR6 的 QM 边界（\*）**：Indication 要求本身按 ASIL B 提出（由 Logic 元素生成警告），但**承接该指示的物理 Display 是 §2.3 所述的 QM other item**——这正体现"要求定 ASIL、承接的 HMI 硬件可定 QM（freedom from interference）"的边界。考试答题时建议显式写出此区分。
>
> **可追溯性**：每条 FSR 都能回溯到 SG1（"avoid unintended acceleration"）且绑定到一个架构元素——这是 FSC 阶段答题的硬性要求（ISO 26262-3 / Part 4 可追溯性）。

### 2.3 TSC 系统草案（System Draft）【培训给定】

（[[sources/sgs-afsp-day2-tsc-system-draft]]）将 FSC 功能元素替换为技术组件：

```
Pedal Sensor → Motor-ECU → Power Unit w/ Motor Monitoring → E-Motor   ← 主线（ASIL B）
    │              │ (HMI 输出)            │
 CAN-Bus(ABS)   Display(QM, other item)  400V Battery │ Hardwire Torque off
```

> **图注**：
> - **Motor-ECU = 电机控制器（ASIL B）**，是承载安全相关扭矩控制/电机监测功能的核心元素，**不是 Display**。
> - 竖线 `│` 表示"外部接口/信号流向"：**Display(QM) 是挂在 Motor-ECU 外的独立 HMI（人机界面）**——源页明确标注 "Display（other item, QM）"，即它属于**另一个 item（仪表/中控等）**，仅接收 Motor-ECU 发来的扭矩需求/警告信息，**自身不参与扭矩控制**。
> - **为什么 Display 可以定 QM**：依据 ISO 26262 要素共存/独立性（freedom from interference）原则——只要能论证 Display 失效（如黑屏）**不会违背安全目标**（Motor-ECU 仍照常控扭矩、硬线 torque off 仍可控断），Display 就无需定 ASIL，按 QM 开发即可。这正是考试考点：**ASIL 只给"失效会直接影响安全目标"的元素，纯信息显示类 HMI 通常定 QM**。
> - 同理，E-Motor、400V Battery 在 §2.5 分配表中也定 QM，因其失效由 Power Unit 的安全机制（电机监测 + 硬线 torque off）所容忍。

> 解题要点：**FSC 关注功能行为，TSC 关注技术实现**。这是 AFSP 高频考点。

### 2.4 系统级安全要求 SYSR【培训给定】

（[[sources/sgs-afsp-day2-tsc-system-level-requirements]]）FSR1–FSR6 导出 **SYSR1–SYSR8**，并引入硬件指标：

**FSR1–FSR6 → SYSR1–SYSR8 完整导出表：**

| SYSR | 来源 FSR | 系统级安全要求文本（中文） | ASIL |
|---|---|---|---|
| SYSR1 | FSR1, FSR4 | 电机状态应以 **< 0.25 s** 周期持续监测，以检测偏离/失效。 | B |
| SYSR2 | FSR1, FSR4 | 电机电流应与期望值以 **< 0.25 s** 周期比较；偏差超阈即判定故障。 | B |
| SYSR3 | FSR1 | 驾驶员扭矩请求应进行合理性校验（如踏板信号与 ABS 车速信号交叉验证），以识别非预期加速需求。 | B |
| SYSR4 | FSR2 | 逻辑单元应在 FTTI 内检测非预期加速工况，并指令系统进入安全状态。 | B |
| SYSR5 | FSR3 | 故障检测时，执行器（Power Unit）应切除扭矩 / 电机断电，并保持于安全状态。 | B |
| SYSR6 | FSR5 | 400V 供电应被监测；故障或转入安全态时应安全隔离，使非预期扭矩无法维持。 | B |
| SYSR7 | FSR6 | ABS 车速信号应对逻辑可用且合理；信号丢失 / 不合理应被检测。 | B |
| SYSR8 | FSR6 | 检测到安全相关故障时，应在 FTTI 内通过指示接口向驾驶员发出警告。 | B |

> **分配（据 §2.5 模板约定）**：SYSR1–SYSR8 统一落到 **Motor-ECU**（逻辑/控制）；其中 SYSR1、SYSR6 同时落到 **Power Unit w/ Motor Monitoring**；SYSR7 落到 **ABS Speed signal**；SYSR5 在 §2.5 模板中记于 **Pedal Sensor**。
>
> **溯源与诚实标注**：**SYSR1、SYSR2 为培训给定示例**（源页已填）；**SYSR3–SYSR8 为基于 FSR1–FSR6 + E/E 架构 + §2.5 分配的推导填充**（源页对应行为空白模板），重点体现 FSR→SYSR 的功能可追溯性，非原稿逐字内容。
>
> **硬件指标（系统级 HW 要求）**：**SYSR10–SYSR11** = 单点/潜伏故障度量（SPFM/LFM，HW 架构指标）；**SYSR20** = PMHF（随机硬件失效概率指标）。三者对应 Day 3 的 SPFM/LFM/PMHF 计算（见 §4）。

### 2.5 分配与 SYSELR【培训给定】

（[[sources/sgs-afsp-day2-tsc-system-design-allocation]]、[[sources/sgs-afsp-day2-tsc-system-element-requirements]]）

| 系统元素 | 分配要求 | ASIL |
|---|---|---|
| Pedal Sensor | SYSR5 | — |
| Motor-ECU | SYSR1–SYSR8 | B |
| Power Unit w/ Motor Monitoring | SYSR1、SYSR6 | B |
| E-Motor | — | **QM** |
| 400V Battery | — | **QM** |
| ABS Speed signal | SYSR7 | — |

Power Unit 元素级要求 **SYSELR1–SYSELR7**：SYSELR1 分流电阻持续测电流（ASIL B）、SYSELR2 以 0.1–10V 标准化信号送 ECU（ASIL B）、SYSELR5–6 为 HW 架构指标、SYSELR7 为 PMHF 预算。

> 解题要点：QM 元素不执行安全功能但可能提供输入；ASIL 可随分配继承或经分解下调（ISO 26262-9）。

### 2.6 组件设计与 HW/SW 分配【培训给定】

（[[sources/sgs-afsp-day2-tsc-component-design-hw-sw-allocation]]）Power Unit 内部：`Analog Input → Power Electronics → Output to motor`，安全相关元素含 Motor Current (SYSELR1)、Analog Output (SYSELR2)、Power Switch (SYSELR3)、Switch Input (SYSELR4)、400V Input。**本示例全部安全要求分配到硬件实现**。下一步即在硬件层细化 HSR（见 Day 3）。

---

## 3. Day 3 题解：硬件度量计算（SPFM / LFM / PMHF）

### 3.1 硬件安全要求 HWSR【培训给定】

（[[sources/sgs-afsp-day3-hw-safety-requirements-design-example]]）组件 "Power Unit and Motor Monitoring"，**HWSR_01–06，均 ASIL B**：

- HWSR_01：分流电阻持续测电机电流
- HWSR_02：以 0.1–10V 标准化信号持续送电机 ECU
- HWSR_03：功率继电器切断电源
- HWSR_04：继电器 **0.5 s 内**切断电机供电
- HWSR_05/06：开关关断=0V、导通=5V 电平定义

### 3.2 BOM 与基准 FIT【培训给定 + SN 29500】

电路（[[sources/sgs-afsp-day3-hw-analysis-circuit-diagram]]）：+60V、电机 M、续流二极管 D1、采样电阻 R1/R2、MOSFET T1、继电器 K1、双运放 IC1（AD8200）、+12V。

（[[sources/sgs-afsp-day3-hw-analysis-bom-fault-rates]]）BOM FIT 表（多数修正因子取 1，功率元件平均工作温度 70°C）：

| 器件 | 类型 | 基准 FIT | 来源 |
|---|---|---|---|
| R1 | 分流电阻 | 0.2 FIT | SN 29500（金属膜） |
| T1 | 晶体管 MOSFET | 60 FIT | SN 29500 |
| K1 | 功率继电器 | 30 FIT | SN 29500 |
| IC1 | AD8200 运放 | 3 FIT | SN 29500 |
| M | 电机 | 50 FIT | Supplier |
| R2 / D1 | 电阻/二极管 | 依 SN 29500 | SN 29500 |

**SN 29500 查表基准**（[[sources/sgs-afsp-sn29500-transistor-fit-rates]]、[[sources/sgs-afsp-sn29500-resistor-inductor-passive-fit-rates]]、[[sources/sgs-afsp-sn29500-capacitor-fit-rates]]）：
- MOS power (SIPMOS)：60 FIT（θ=100°C）；金属膜电阻：0.2 FIT；功率继电器：依类型。
- 1 FIT = 10⁻⁹/h。
- 温度修正：λ_actual = λ_ref × π_T(θ_actual)/π_T(θ_ref)（[[sources/sgs-afsp-sn29500-temperature-correction-factors]]）；θ_ref=55°C、θ_actual=70°C 时 π_T≈1.5–2。

### 3.3 故障模式分布（Birolini）【培训给定】

（[[sources/sgs-afsp-day3-hw-analysis-fault-distribution-components]]、[[sources/sgs-afsp-day3-hw-analysis-fault-distribution-amp-motor]]）

- 电阻（金属膜 R-M）：Open 40%、Short 0%、Drift 等
- 功率继电器（K-P）：Open 20%、**Short（熔焊）80%**
- 二极管（V-S）：Open / Short / 限值变化
- 双运放（AMP）：引脚间 short 多数 2%，功能性故障 9%
- 电机（Motor）：Break(开路) 25%、线圈 Short 25%、高过渡电阻 25%、间歇 25%

> 解题要点：把器件总 FIT 按故障模式拆分，是后续单点/残余/潜伏分类与 DC 计算的基础。继电器熔焊→Short 是典型单点危险模式。

### 3.4 安全机制与诊断覆盖率 DC【培训给定】

（[[sources/sgs-afsp-day3-hw-analysis-safety-mechanisms-dc]]）

- **SM1 — Monitoring of motor current**：在线监测电机电流，参考 **ISO 26262-5 Table 3（电气元件在线监测）**。
- **DC 等级**（ISO 26262-5 定义）：Low / Medium / High 对应约 60% / 90% / 99%（依故障模式覆盖比例）。在线监测电气元件通常可达 Medium–High。
- 解题要点：DC 直接决定多少故障从"单点/残余"转为"被覆盖"，是 SPFM/LFM 计算的杠杆。

### 3.5 SPFM / LFM / PMHF 计算与结果【培训给定】

（[[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p6]]、[[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p7]]、[[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]）

**公式（ISO 26262-5:2018）：**

```
SPFM = 1 − Σ(λ_SP + λ_RF) / Σλ
LFM  = 1 − Σλ_LF / (Σλ_LF + Σλ_MP)
PMHF = Σλ_SP + Σλ_RF + Σ(λ_LF · λ_MP · T_lifetime)
```

其中 λ_SP=单点故障率、λ_RF=残余故障率、λ_LF=潜伏故障率、λ_MP=多点（双点）故障率、T_lifetime=车辆寿命（≈15 年 ≈ 1.314×10⁵ h）。

**培训给定结果（针对 SG1）：**

| 指标 | 结果 | 培训给定 |
|---|---|---|
| SPFM | **0.87（87%）** | [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]] |
| LFM | **0.74（74%）** | 同上 |
| PMHF | **≈ 29.29 FIT** | 同上（分解：Σλ_SP 0.74 + Σλ_RF 0.13 + 双点贡献 29.01×T_lifetime） |

> 推导说明：PMHF 的主导项是双点故障贡献 λ_LF·λ_MP·T_lifetime（≈29 FIT），远大于单点/残余之和（<1 FIT），这与硬件随机失效的物理规律一致。源页写 PMHF=0.74+0.13+29.01×T_lifetime，最终给出 29.29 FIT（训练示例四舍五入）。

### 3.6 达标判定（对照 ASIL B 阈值）【标准判定】

依据 ISO 26262-5:2018 Table 4/5/6（ASIL B 目标；GB-T 34590-5 同源）：

| 指标 | ASIL B 目标 | 培训结果 | 判定 |
|---|---|---|---|
| **SPFM** | ≥ 90%（或 ≥ 80% 带合理性论证） | 87% | ⚠️ **未达 90% 严格线**；达 80% 论证线 |
| **LFM** | ≥ 60%（或 ≥ 40% 带论证） | 74% | ✅ 达标 |
| **PMHF** | ≤ 100 FIT | 29.29 FIT | ✅ 达标 |

> **关键教学点（考试常考）**：本训练示例的 **SPFM = 87% 未满足 ASIL B 的 ≥90% 严格要求**。这正是 ISO 26262 设计迭代循环的体现——若严格要求下不达标，需：① 增加/增强安全机制以提高 DC，降低 Σ(λ_SP+λ_RF)；② 采用 ASIL 分解（ISO 26262-9）将要素冗余降为低 ASIL；③ 重新计算直至达标。LFM 与 PMHF 均已达标，说明该设计的主要短板在单点故障覆盖。

---

## 4. 标准依据与阈值速查（ISO 26262-5:2018）

| ASIL | SPFM（Table 4） | LFM（Table 5） | PMHF（Table 6） |
|---|---|---|---|
| A | 无要求 | 无要求 | 无要求（典型 <1000 FIT） |
| **B** | **≥90%（或 ≥80% 带论证）** | **≥60%（或 ≥40% 带论证）** | **≤100 FIT** |
| C | ≥90%（或 ≥80% 带论证） | ≥60%（或 ≥40% 带论证） | ≤100 FIT |
| D | ≥99% | ≥90% | ≤10 FIT |

> 注：GB-T 34590-5（本库为征求意见稿）与 ISO 26262-5 同源同值，引用时需注意版本时效（[[concepts/gbt-34590]]）。阈值具体数值以标准原文 Table 4/5/6 为准——本知识库 ISO 26262-5 源页为概述，未转录完整表格，建议考试前核对标准正文。

---

## 5. Confidence Notes（置信度说明）

- **置信度：medium**。依据：34 个练习题源页 + 12 份 ISO 26262 + 12 份 GB-T 34590 标准源页，数量充足且为官方材料；但（1）**Day 1 HARA 矩阵与 Day 3 计算表为空白模板**，HARA 推导示例与部分 C 取值为知微基于锚点 SG1=ASIL B 反推的"推导示例"，非扫描件原值；（2）SN 29500 的 FIT/πT/πU/πQ 数值从扫描件转录，密集表格存在行/列错位风险；（3）全部培训案例来自 SGS TÜV Saar 单一机构，缺少 OEM/其他认证机构对照。
- 按 CLAUDE.md §十，未达 high 所需的"多独立来源交叉验证"，维持 medium。

## 6. Limitations（局限性）

- **同源性**：案例集中于 SGS 单一培训课程，机构特有简化假设可能存在。
- **扫描转录**：FIT、πT、πU、πQ 数值需以 SN 29500 标准原文或元器件手册为准。
- **覆盖盲区**：未涉及 Part 6 软件安全、Part 8 支持过程、Part 9 ASIL 分解细则、Part 11 半导体指南。
- **案例单一**：仅 Torque Demand 一个 item，不足以代表制动/转向/高压电池管理等复杂安全关键系统。

---

## Sources

**Day 1（HARA / ASIL）**
- [[sources/sgs-afsp-day1-item-definition-purpose-function]]
- [[sources/sgs-afsp-day1-item-definition-context]]
- [[sources/sgs-afsp-day1-hara-exercise-p1]] ~ [[sources/sgs-afsp-day1-hara-exercise-p8]]

**Day 2（FSC / TSC）**
- [[sources/sgs-afsp-day2-fsc-safety-goal-characteristics]]
- [[sources/sgs-afsp-day2-fsc-requirements-architecture]]
- [[sources/sgs-afsp-day2-tsc-system-draft]]
- [[sources/sgs-afsp-day2-tsc-system-level-requirements]]
- [[sources/sgs-afsp-day2-tsc-system-design-allocation]]
- [[sources/sgs-afsp-day2-tsc-system-element-requirements]]
- [[sources/sgs-afsp-day2-tsc-component-design-hw-sw-allocation]]

**Day 3（硬件度量）**
- [[sources/sgs-afsp-day3-hw-safety-requirements-design-example]]
- [[sources/sgs-afsp-day3-hw-analysis-circuit-diagram]]
- [[sources/sgs-afsp-day3-hw-analysis-bom-fault-rates]]
- [[sources/sgs-afsp-day3-hw-analysis-fault-distribution-components]]
- [[sources/sgs-afsp-day3-hw-analysis-fault-distribution-amp-motor]]
- [[sources/sgs-afsp-day3-hw-analysis-safety-mechanisms-dc]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p6]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-calculation-p7]]
- [[sources/sgs-afsp-day3-hw-analysis-metrics-results-p8]]

**SN 29500 查表**
- [[sources/sgs-afsp-sn29500-transistor-fit-rates]]
- [[sources/sgs-afsp-sn29500-temperature-correction-factors]]
- [[sources/sgs-afsp-sn29500-resistor-inductor-passive-fit-rates]]
- [[sources/sgs-afsp-sn29500-capacitor-fit-rates]]

**标准与概念依据**
- [[sources/iso-26262-3-2018]]、[[sources/iso-26262-4-2018]]、[[sources/iso-26262-5-2018]]
- [[concepts/asil]]、[[concepts/hardware-metrics]]、[[concepts/pmhf]]、[[concepts/sn29500]]、[[concepts/fit-rate]]、[[concepts/fsc]]、[[concepts/tsc]]、[[concepts/hara]]

---

## 7. 修订记录

- **2026-07-22（用户订正）**：修正 §1.5 HARA 推导中 M2 段的逻辑错误。原句“M2 得 C，低于 M1 的 B，故 SG 取 M1 的 ASIL B 为 worst case”方向写反——**ASIL 等级 C > B**，故该 item 的 worst-case（最高）ASIL 应取 **M2 产生的 ASIL C**（派生 SG2）。同步修正 §1.5 结论（SG1=ASIL B 来自 M1；SG2=ASIL C 来自 M2；整体最高 = C），并订正 §4 阈值表 ASIL C 行（SPFM/LFM 目标与 ASIL B 同源：≥90% / ≥60%，原稿 ≥97% / ≥80% 不准）。Day 3 达标判定结论不变：无论按 B 或 C，SPFM=87% 均未达到 ≥90% 严格线（培训示例“不达标→迭代”教学点成立）。
- **2026-07-22（补充）**：应要求补全 §1.5 的 **完整 HARA 矩阵**——对 M1×S1–S4 与 M2×S1–S4 共 8 个组合逐一填写 Consequence / Reason for S / E / C，据 ISO 26262-3 查表得出各组合 ASIL（M1 最高 B=SG1，M2 最高 C=SG2）。结论与用户订正的 worst-case = ASIL C 一致。模板原空白，理由为【推导示例】。

