# 📰 每日前沿技术简报 - 2026-07-19

> 采集时间：2026-07-19 12:42 CST | 数据来源：arXiv API + GitHub Trending

---

## 🔬 arXiv 新论文精选（2026-07-16 提交）

### 🤖 机器人 & 具身智能

**1. RoboTTT: Context Scaling for Robot Policies**
- 链接：https://arxiv.org/abs/2607.15275v1
- 作者：Yunfan Jiang, Yevgen Chebotar 等（斯坦福/NVIDIA）
- **亮点**：将机器人视觉运动策略的上下文扩展到 8K 时间步（比现有方案大 3 个数量级），不增加推理延迟。实现了一次性视频模仿学习、在线策略改进、5 分钟 10 阶段装配任务完整完成。提出上下文长度作为机器人基础模型的新扩展轴。
- **与车载/机器人相关**：长上下文策略对复杂多阶段任务（如自动驾驶场景规划）有参考价值

**2. HDR: Hierarchical Denoising For Multi-Step Visual Reasoning**
- 链接：https://arxiv.org/abs/2607.15278v1
- 作者：Zezhong Qian 等
- **亮点**：提出树形层级潜变量框架用于视频多步推理，成功率从 34.22 提升到 60.29（+76.2%），推理速度是双向扩散的 54.2 倍。包含真实机器人实验验证。
- **与车载相关**：视频推理能力对自动驾驶感知决策有直接意义

**3. SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration**
- 链接：https://arxiv.org/abs/2607.15257v1
- 作者：Yuyao Zhang 等（清华大学/蚂蚁）
- **亮点**：多 Agent 信息搜索框架，将搜索进度外部化为显式状态（前沿任务、证据图、覆盖地图、失败记忆），避免重复搜索循环。管道并行调度机制提高吞吐。

### 🧠 大语言模型 & 推理

**4. Partition, Prompt, Aggregate: Statistical Self-Consistency in Language Models**
- 链接：https://arxiv.org/abs/2607.15277v1
- 作者：Patrik Wolf 等（苏黎世联邦理工）
- **亮点**：检验 LLM 是否满足概率自一致性（全概率法则）。发现广泛违反基本一致性性质。提出"宏观谬误"现象：细粒度子群体估计聚合后比直接总体估计更准确。为 LLM 评估提供新的免参考标准。

**5. In-Place Tokenizer Expansion for Pre-trained LLMs**
- 链接：https://arxiv.org/abs/2607.15232v1
- **亮点**：在预训练后扩展 tokenizer 词表的方法，通过 BPE 合并延续 + 均值初始化 + 两阶段微调实现，解决多语言碎片化问题。对端侧模型尤其重要。

### 🖼️ 计算机视觉 & 生成模型

**6. MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators**
- 链接：https://arxiv.org/abs/2607.15273v1
- 作者：Yushi Huang 等
- **亮点**：将 RL 优化引入 MeanFlow 平均速度生成器。4 步 MeanFlowNFT 在 Wan 2.1 上 VBench 84.33，超过 50 步 RL 调优扩散模型。

**7. Online Neural Space Time Memory for Dynamic Novel View Synthesis**
- 链接：https://arxiv.org/abs/2607.15271v1
- 作者：Baback Elmieh 等（Meta）
- **亮点**：动态场景的实时新视角合成，分离记忆更新和应用频率，实现分钟级在线记忆。

**8. ARMOR++: Agentic Orchestration for Transferable Attacks on Deepfake Detectors**
- 链接：https://arxiv.org/abs/2607.15246v1
- 作者：Christos Korgialas 等
- **亮点**：LLM 编排多域攻击原语进行深度伪造检测器的可迁移攻击，揭示当前深度伪造检测的可靠性差距。

### 🚗 自动驾驶相关

**9. teLLMe: Exploratory Causal Analysis of Urban Driving Data**
- 链接：https://arxiv.org/abs/2607.15254v1
- **亮点**：城市驾驶数据的探索性因果分析系统，结合因果结构学习 + LLM 自然语言查询，从行车记录仪数据中分析天气、高峰时段与交通密度的因果关系。

**10. Motion-Conditioned Multi-View Fusion for Myocardial Infarction Localization**
- 链接：https://arxiv.org/abs/2607.15268v1
- **亮点**：运动引导的多视图融合框架用于心梗定位，展示了运动线索 + 基础模型表示的融合范式。

---

## 📦 GitHub Trending（2026-07-19）

| 项目 | 描述 | Stars | 今天增长 |
|------|------|-------|---------|
| [lyogavin/airllm](https://github.com/lyogavin/airllm) | 单卡 4GB GPU 运行 70B 模型推理 | 23,385 ⭐ | +161 |
| [KnockOutEZ/wigolo](https://github.com/KnockOutEZ/wigolo) | 本地优先 AI 编码 Agent 搜索/抓取/研究工具，零 API Key | 1,317 ⭐ | +203 |
| [ibelick/ui-skills](https://github.com/ibelick/ui-skills) | Design Engineers 的设计技能库 | 5,116 ⭐ | +123 |
| [elder-plinius/G0DM0D3](https://github.com/elder-plinius/G0DM0D3) | 解放版 AI 聊天客户端 | 9,556 ⭐ | +69 |
| [MoonshotAI/kimi-cli](https://github.com/MoonshotAI/kimi-cli) | Kimi Code CLI - 你的下一个 CLI Agent | 9,547 ⭐ | +65 |
| [apache/ossie](https://github.com/apache/ossie) | 跨平台语义元数据交换行业标准规范 | 1,308 ⭐ | +47 |
| [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map) | 流式数据 3D 场景重建的前馈基础模型 | - | - |
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 本地优先代码智能图谱，MCP/CLI 代码审查上下文缩减 | - | - |

### 🔥 值得关注
- **airllm**：端侧大模型推理的里程碑项目，单卡 4GB 跑 70B，对车载域控的端侧部署有参考价值
- **kimi-cli**：月之暗面开源的 CLI 编码 Agent，与 Cursor/Claude Code 竞争
- **wigolo**：零成本本地 AI 搜索/抓取工具，适合 Agent 工作流

---

## 📊 大语言模型测评 TOP 10

> ⚠️ 今天的排名数据采集受限：Artificial Analysis、Chatbot Arena、Soreg、OpenCompass 等排名站点均为动态渲染页面，web_search 和 DNS 解析在内网环境下不可用，无法提取最新排名数据。
> 
> 建议贾若手动查看：https://artificialanalysis.ai/models

---

## 📝 总结

**今日关键词**：长上下文机器人策略、视频多步推理、LLM 自一致性、端侧 tokenizer 扩展、深度伪造攻击

**趋势观察**：
1. 机器人基础模型从单步向长上下文扩展（RoboTTT 8K 时间步），上下文长度成为新扩展轴
2. 视频推理模型在具身智能中发挥越来越重要的作用
3. LLM 评估从单纯的准确率转向统计自一致性等更深层次的检验
4. 端侧 AI 工具链持续活跃（airllm、wigolo、kimi-cli）
