# 📰 每日前沿技术简报 — 2026-07-17（周五）

---

## 🤖 机器人 / 具身智能

### 1. RoboTTT: Context Scaling for Robot Policies ⭐⭐⭐
- **来源**: NVIDIA / Stanford, 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.15275v1
- **项目页**: https://research.nvidia.com/labs/gear/robottt/
- **摘要**: 将机器人策略的视觉-运动上下文扩展到 **8K 时间步**（比现有方法大 3 个数量级），推理延迟不变。核心创新：Test-Time Training (TTT) 整合到 VLA 模型中，用 fast weights 压缩历史信息。在真实机器人操作任务上比单步上下文基线提升 87%，完整完成了 5 分钟 10 阶段的装配任务（基线从未完成）。
- **亮点**: 首次观察到闭环性能随预训练上下文长度稳定增长。8K 上下文比 1K 上下文提升 62%，证明上下文长度是机器人基础模型的新缩放维度。
- **关联**: 与贾若正在关注的机器人项目直接相关（关节模组、VLA 策略）

### 2. HDR: Hierarchical Denoising for Multi-Step Visual Reasoning ⭐⭐⭐
- **来源**: 清华大学 / 上海AI Lab, 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.15278v1
- **项目页**: https://hierarchical-diffusion-reasoning.github.io/
- **摘要**: 将视频潜变量组织为树状层次结构，实现从粗到细的多步视觉推理。粗层保留不确定假设用于全局规划，细层逐步精炼为具体视觉状态。在 6 项长推理任务（迷宫、汉诺塔、一笔画、滑动拼图、推箱子、倒水）上，成功率从 34.22 提升到 60.29（相对提升 76.2%）。
- **亮点**: 流式延迟仅 0.70s/latent，比双向扩散快 54.2 倍。仅用 2% 训练数据即保留 82.9% 性能（双向扩散仅 52%）。已在真实机器人迷宫实验中验证。
- **关联**: 视频世界模型 + 多步推理，对具身智能有重要启发

### 3. DriftWorld: Fast World Modeling through Drifting ⭐⭐
- **来源**: MIT, 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.15065v1
- **项目页**: https://susie-lu.github.io/driftworld/
- **摘要**: 基于漂移生成模型的动作条件世界模型，推理时只需一次前向传播即可生成分支（30+ fps，比扩散基线快 17 倍）。在 Bridge-V2、RT-1 等基准上达到 SOTA。
- **亮点**: 可用作离线模拟器来排名真实机器人策略，rollout 评分与真实表现相关度高达 0.99。
- **关联**: 世界模型对机器人规划至关重要，对自动驾驶仿真也有参考价值

### 4. VQ-Touch: 触觉生成框架 ⭐⭐
- **来源**: 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.14728v1
- **摘要**: 跨传感器、跨场景的触觉图像生成框架，减少对昂贵传感器的依赖。DM-VQGAN 提取形变和纹理特征，离散扩散解码器支持多模态生成。

### 5. Image-to-Point Cloud Registration (LiDAR Upsampling) ⭐⭐
- **来源**: 东京大学, 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.14639v1
- **摘要**: 将 LiDAR 视为成像传感器，用 Conditional Rectified Flow 从稀疏扫描生成密集 LiDAR 强度图像，再用预训练特征匹配器与相机图像对齐。R3LIVE 数据集上平均误差 4.89°/1.63m，单次注册 0.68s。
- **关联**: 车规级 LiDAR-相机融合方案的直接参考

---

## 🧠 大语言模型 / AI

### 6. Partition, Prompt, Aggregate: LLM 统计自洽性评估 ⭐⭐
- **来源**: ETH Zurich / Stanford, 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.15277v1
- **摘要**: 用全概率定律评估 LLM 估计的统计自洽性。发现前沿模型广泛违反基本一致性属性——从细粒度子群体重建的估计往往比直接的全局估计更接近人类参考数据（"宏观谬误"）。
- **亮点**: 建立了一个无需参考数据的 LLM 评估新标准。

### 7. SciDiagramEdit: 论文图表自动编辑 ⭐
- **来源**: 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.15272v1
- **摘要**: 从 arXiv 版本历史中挖掘论文修改前后的图表对，学习指令驱动的科学图表编辑。基于 skill evolution 的 agentic 学习方法。

### 8. MeanFlowNFT: 前向过程 RL 加速少步生成 ⭐
- **来源**: 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.15273v1
- **摘要**: 将 DiffusionNFT 框架扩展到 MeanFlow 生成器。Wan 2.1 上 4 步 MeanFlowNFT 达到 VBench 84.33，超过 50 步基线（82.57）。

### 9. Action QFormer: VLA 模型中的结构化表示 ⭐
- **来源**: 2026-07-16
- **arXiv**: https://arxiv.org/abs/2607.14635v1
- **摘要**: 研究动作监督如何塑造 VLA 模型的多模态表示。提出 query-based 动作接口，避免直接动作监督破坏语言和对象接地能力。

---

## 📊 大语言模型测评 TOP 10

> ⚠️ 今天 Artificial Analysis、OpenCompass 和 LMSYS 的排行榜页面均为动态渲染，web_fetch 无法提取实际排名数据。web_search 也不可用。以下为基于已掌握信息的说明：

| 排名 | 模型 | 综合分数 | 提供商 | 备注 |
|------|------|----------|--------|------|
| — | 数据获取失败 | — | — | 各评测网站均为 JS 动态渲染，无法通过静态抓取获取 |

**建议**: 下次尝试用 `openclaw gateway` 中的浏览器自动化工具，或手动查看以下网站：
- [Artificial Analysis Intelligence Index](https://artificialanalysis.ai/models)
- [OpenCompass 司南](https://opencompass.org.cn/leaderboard)
- [LMSYS Chatbot Arena](https://chat.lmsys.org/?arena)

---

## 🔍 今日要点

| 领域 | 关键发现 | 与理想汽车的关联度 |
|------|----------|-------------------|
| 机器人策略 | RoboTTT: 8K 上下文 VLA 策略，性能提升 87% | ⭐⭐⭐ 直接相关 |
| 视觉推理 | HDR: 层次化去噪实现多步推理，76% 成功率提升 | ⭐⭐ 世界模型参考 |
| 世界模型 | DriftWorld: 30fps 快速rollout，离线策略评估 | ⭐⭐ 仿真/规划 |
| 感知融合 | LiDAR-相机注册 0.68s/次 | ⭐⭐ 车规感知 |
| 触觉感知 | VQ-Touch 跨传感器触觉生成 | ⭐ 间接参考 |

---

*采集时间: 2026-07-17 13:23 CST | 数据源: arXiv API (cs.AI/cs.CL/cs.CV/cs.RO)*
