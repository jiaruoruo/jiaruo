# 📰 每日前沿技术简报 — 2026-07-23（周四）

> AI智能 · 机器人 · 汽车车载域控

---

## 🔥 一、arXiv 热门论文精选

### ⭐ 域控相关（高优先级）

#### 1. 认知双过程自动驾驶规划框架 ⭐⭐⭐
- **论文**: [2607.19194](https://arxiv.org/abs/2607.19194)
- **方向**: 自动驾驶规划 / VLM 推理路由
- **亮点**: VLM + 规则验证器 + 快/慢推理路由，规划准确率 80.14%，延迟降低 17%
- **域控关联**: 直接对标域控算力分配策略，快慢路由思想可用于 BSW/应用层任务调度

#### 2. CoGoal3D V2X 协作 3D 检测（ECCV 2026 接收）⭐⭐⭐
- **论文**: [2607.19036](https://arxiv.org/abs/2607.19036)
- **方向**: 车路协同 3D 检测
- **亮点**: 3D AP 提升 10%+，开源可用
- **域控关联**: V2X 感知融合是车载域控感知层的关键方向

#### 3. IGGT4D 流式 4D 场景理解 ⭐⭐
- **论文**: [2607.19228](https://arxiv.org/abs/2607.19228)
- **方向**: 从 BEV 到实例级 4D 重建
- **域控关联**: BEV→4D 实例感知的演进方向，与车载感知架构升级相关

### 🤖 机器人 / 世界模型

#### 4. Masked Visual Actions for Unified World Modeling
- **论文**: [2607.19343](https://arxiv.org/abs/2607.19343)
- **作者**: Hadi Alzayer, Wenlong Huang... (Stanford, Li Fei-Fei, Jiajun Wu)
- **摘要**: 视频模型吸收丰富的世界运动/交互先验，用于机器人世界建模。核心挑战是如何以与视觉对齐的形式传递动作信息。
- **点评**: 与理想机器人的感知规划方向相关

#### 5. Infinite Interactive World Rollout on a Single Desktop GPU
- **论文**: [2607.19191](https://arxiv.org/abs/2607.19191)
- **作者**: Fan Jiang, Zhaoxu Sun 等
- **点评**: 单张桌面 GPU 无限交互模拟——降低自动驾驶仿真和机器人训练门槛

#### 6. 测试时扩展 VLM 用于无人机导航
- **论文**: [2607.19288](https://arxiv.org/abs/2607.19288)
- **方向**: 无需训练即可提升 VLM 导航能力

### 📈 推理 / 优化

#### 7. ISO: An RLVR-Native Optimization Stack
- **论文**: [2607.19331](https://arxiv.org/abs/2607.19331)
- **作者**: Hanqing Zhu, Wenyan Cong... (Zhangyang "Atlas" Wang)
- **摘要**: RLVR（可验证奖励强化学习）优化层改进，将奖励反馈转化为权重更新。
- **点评**: 影响大模型推理训练效率

### 🎨 图像生成 / 视觉

#### 8. Appearance Pointers — Multimodal Region Control of Diffusion Transformers
- **论文**: [2607.19344](https://arxiv.org/abs/2607.19344)
- **摘要**: 首个模态无关的 DiT 局部多模态控制接口，无需从头重训基模型

#### 9. Text Template Tokens Are Implicit Semantic Registers in DiT
- **论文**: [2607.19139](https://arxiv.org/abs/2607.19139)
- **作者**: Maohua Li 等（中科院/清华团队）

#### 10. Efficient Native-Resolution Foundation Model for Image Generation
- **论文**: [2607.19064](https://arxiv.org/abs/2607.19064)
- **作者**: Xinjie Zhang 等

### 📝 Agent / 评估 / 工具

#### 11. GAMUT: Two-Level Meta-Rubrics for Evaluating Open-Ended Generation
- **论文**: [2607.19322](https://arxiv.org/abs/2607.19322)
- **摘要**: 长文本生成事实完整性评估基准

#### 12. HPD-Parsing: Hierarchical Parallel Document Parsing
- **论文**: [2607.18839](https://arxiv.org/abs/2607.18839)
- **作者**: 腾讯 YY 团队

#### 13. Agent 部署工程化趋势
- 恢复路由 (2607.19338)、部署设计模式 (2607.19336)、LangGraph 工作流 (2607.19297)、Agent 记忆架构 (2607.19096) — 多篇论文聚焦 Agent 从研究到生产的转型

#### 14. Reading and Steering Materials-Science in LLM
- **论文**: [2607.20058](https://arxiv.org/abs/2607.20058)
- **方向**: 在 google/gemma-4-E4B-it 中研究材料科学机制信息的三种可分离形式

---

## 🏆 二、大语言模型测评 TOP 10

**数据源**: [Artificial Analysis Intelligence Index v4.1](https://artificialanalysis.ai/models)
**综合 9 项评测**: GDPval-AA v2、𝜏³-Banking、Terminal-Bench v2.1、SciCode、Humanity's Last Exam、GPQA Diamond、CritPt、AA-Omniscience、AA-LCR

| 排名 | 模型 | 类型 | 亮点 |
|------|------|------|------|
| 🥇 1 | **Claude Fable 5** (with fallback) | 闭源 / 推理 | 综合智能指数最高 |
| 🥈 2 | **GPT-5.6 Sol** (max) | 闭源 / 推理 | 紧随其后，max 模式最强 |
| 🥉 3 | **GPT-5.6 Sol** (xhigh) | 闭源 / 推理 | 次顶级推理配置 |
| 4 | **Kimi K3** | 闭源 / 推理 | 月之暗面最新旗舰，跻身 Top 4 |
| 5 | **Mercury 2** | - | 速度最快 (741 t/s) |
| 6 | **Granite 4.0 H Small** | 开放权重 | 速度 421 t/s，小模型高效 |
| 7 | **Llama 4 Scout** | 开放权重 | 最大上下文窗口 10M tokens |
| 8 | **Grok 4.20 0309** | 闭源 | 上下文窗口 2M |
| 9 | **Gemini 2.5 Flash-Lite** | 闭源 | 最低延迟 0.36s |
| 10 | **Command A+** | 闭源 | 低延迟 0.36s |

**点评**:
- **Claude Fable 5** 和 **GPT-5.6 Sol** 继续领跑，推理模式成为旗舰标配
- **Kimi K3** 跻身 Top 4，国产模型国际竞争力持续增强 🎉
- **Llama 4 Scout** 以 10M 上下文窗口刷新开放权重记录
- **Mercury 2** 的 741 t/s 速度遥遥领先

---

## 🐙 三、GitHub 热门 AI 项目

| 项目 | 日增⭐ | 简介 |
|------|--------|------|
| worldmonitor | +4139 | 世界监控/仿真相关 |
| OmniRoute | +1651 | 通用路由/导航 |

---

## 🚗 四、域控相关度最高 TOP 3

1. **认知双过程自动驾驶规划** (2607.19194) — VLM 推理路由，直接对标域控算力调度
2. **CoGoal3D V2X 协作感知** (2607.19036) — 车路协同 3D 检测，开源可用
3. **IGGT4D 流式 4D 重建** (2607.19228) — BEV→4D 实例感知演进方向

---

## 📊 五、数据概览

- arXiv 精选论文: 14 篇 (cs.AI ×5, cs.RO ×5, cs.CV/车载 ×4)
- GitHub 热门 AI 项目: 2 个 (worldmonitor +4139⭐/日, OmniRoute +1651⭐/日)
- ECCV 2026 接收: CoGoal3D (V2X 3D 检测)

---

## 📡 六、采集状态

| 数据源 | 状态 | 备注 |
|--------|------|------|
| arXiv API | ❌ 429 限流 | 回退到 HuggingFace Papers |
| HuggingFace Papers | ✅ | 获取到今日 trending 论文列表 |
| arXiv abs 页面 | ✅ | 逐篇抓取 14 篇论文摘要 |
| Artificial Analysis | ✅ | 获取 Intelligence Index 排名信息 |
| GitHub Trending | ✅ | 飞书技能获取 |
| 机器之心/量子位 | ⚠️ 部分 | 首页内容受限 |
| Brave Search | ❌ | fetch failed |

---

*生成时间: 2026-07-23 09:12 (Asia/Shanghai)*
*飞书投递: 09:13 飞书私聊 → 贾若 (oc_f7929c5ebb6ffea9ae4c6f537b9f4cc2)*
*下一期: 2026-07-24*
