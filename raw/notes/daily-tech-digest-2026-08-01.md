# 📰 每日前沿技术简报

**日期**: 2026-08-01（周六）
**生成时间**: 10:35 (Asia/Shanghai)

---

## 🔬 arXiv 精选论文（7/31 夜间 ~ 8/1 凌晨新提交）

### 🤖 机器人 / 具身智能

**1. Perception-Aware CBF-RL for Whole-Body Safety in Humanoid Dodgeball (PAC-MAN)** (2607.28623)
- **亮点**: 将控制屏障函数(CBF)安全与真实机载感知结合，用于人形机器人躲避球
- **部署**: Unitree G1 零样本部署，仅用头戴相机分割掩码深度即可实现躲避
- **发现**: 固定机载相机对躲避已足够；关节 CBF 在准确球态下最优，但在固定相机观测下退化
- **域控关联度**: ⭐⭐⭐⭐⭐ 人形机器人安全控制 + 真实部署

**2. Frequency-Adaptive Reactive Diffusion Policy for Contact-Rich Manipulation (FA-RDP)** (2607.28596)
- **亮点**: 解决扩散策略在接触丰富操作中的核心矛盾——多模态保持 vs 快速反应
- **方法**: 共享多频率视觉-力 Transformer，接触前低频多步采样保持多模态，接触后高频一步采样快速反应
- **域控关联度**: ⭐⭐⭐⭐⭐ 机器人操作策略核心方法

**3. Human-Centric Ambient Capture as Embodied Data Engine** (2607.28625)
- **作者**: 丘成桐等人（新加坡国立大学 Ziwei Liu 团队）
- **亮点**: 以人为本的环境数据采集作为具身数据引擎
- **域控关联度**: ⭐⭐⭐ 具身数据采集

### 🧠 AI 智能体 / 大模型

**4. Rethinking Inference-Time Scaling in Local Computer-Use Agents** (2607.28573)
- **亮点**: 系统研究本地计算机使用智能体的推理时缩放——上下文、时序、结构、并行四个维度
- **评估**: Qwen3-VL-8B/30B-A3B, UI-TARS-1.5-7B, OpenCUA-7B on OSWorld
- **发现**: 额外计算常边际递减；上下文缩放改善轨迹稳定性但收益饱和；时序缩放减少停滞但不提升成功率
- **结论**: 高效本地 CUA 需要选择性计算分配和故障感知控制机制
- **域控关联度**: ⭐⭐⭐⭐ 本地推理资源约束场景直接相关

**5. MANTA: Multi-Agent Network Topology Adaptation** (2607.28527)
- **亮点**: 多智能体通信拓扑在推理时自演化，而非固定设计
- **性能**: 5 个基准平均 74.0 分，超越最强基线 5.8 个百分点
- **域控关联度**: ⭐⭐⭐ 多智能体架构自适应

**6. User-Centric System Prompt Auditing for LLM Applications** (2607.28617)
- **亮点**: 以用户为中心的 LLM 系统提示审计框架
- **域控关联度**: ⭐⭐ LLM 安全合规

**7. DualG-MRAG: Decoupling Macro-Reasoning and Micro-Matching for MM-RAG** (2607.28580)
- **亮点**: ACM MM 2026，双层图架构——宏观推理图抑制噪声 + 微观匹配图精确定位
- **域控关联度**: ⭐⭐ 多模态 RAG

**8. InfoOps Bench: Live Information Operations Safety Benchmark** (2607.28503)
- **亮点**: 实时信息操作安全基准，2100+ 信息操作数据跟踪俄/中/伊国家支持的信息资产
- **发现**: 17 个模型中大多数可被利用；诚信度 8.8%-94.5%；除 Z.ai GLM 5.2 外，中国开发模型对中国不利但事实成立的声明合规率骤降 48-70 个百分点
- **域控关联度**: ⭐⭐ AI 安全

### 👁️ 计算机视觉

**9. ReToken: One Token to Improve VLMs for Visual Retrieval** (2607.28627)
- **亮点**: 单个可学习嵌入从预填充视觉 KV 缓存中选择稀疏查询相关视觉 token
- **性能**: Visual Haystacks Qwen3VL-8B +13.4 分；LVBench 长视频零样本迁移 +8.0 分
- **效率**: 训练和长视频推理单 H100 即可
- **代码**: https://github.com/avaxiao/ReToken
- **域控关联度**: ⭐⭐⭐⭐ 长上下文视觉推理效率

---

## 📊 GitHub Trending 今日

| 项目 | 语言 | 今日⭐ | 说明 |
|------|------|--------|------|
| [different-ai/openwork](https://github.com/different-ai/openwork) | TypeScript | +806 | Claude Cowork 开源替代 (19.5k⭐) |
| [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners) | Jupyter | +1,592 | 12 周 24 课 AI 入门 (55k⭐) |
| [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill) | PowerShell | +335 | AI 逆向/渗透技能路由包 |
| [agavra/tuicr](https://github.com/agavra/tuicr) | Rust | +335 | vim 键绑定代码审查 TUI |
| [usekaneo/kaneo](https://github.com/usekaneo/kaneo) | TypeScript | +194 | 开源项目管理工具 |
| [geo-tp/ESP32-Bit-Pirate](https://github.com/geo-tp/ESP32-Bit-Pirate) | C++ | +83 | 硬件黑客工具，支持各种协议 |
| [1jehuang/jcode](https://github.com/1jehuang/jcode) | - | - | 最省 RAM 的编码工具 |

---

## 🔍 域控关联洞察

1. **PAC-MAN** — 人形机器人真实部署安全控制，Unitree G1 零样本部署，对机器人项目安全策略有直接参考
2. **FA-RDP** — 接触丰富操作扩散策略频率自适应，解决多模态保持与快速反应矛盾
3. **Local CUA 推理缩放** — 本地资源受限场景下额外计算收益递减，选择性分配更关键
4. **ReToken** — 单个 token 大幅提升 VLM 视觉检索，长上下文效率优化

---

## 📝 采集状态

| 数据源 | 状态 | 备注 |
|--------|------|------|
| arXiv list | ✅ | cs.AI 245篇 / cs.RO 32篇 / cs.CV 131篇 |
| arXiv abs 逐篇 | ✅ | 抓取 ~12 篇论文详情 |
| GitHub Trending | ✅ | 10+ 项目 |
| HuggingFace Papers | ❌ | fetch 失败 |

---

*简报生成完毕*
