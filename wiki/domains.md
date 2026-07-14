---
type: system-domains
graph-excluded: true
---

# 知识库领域导航（Domains）

> 由 `scripts/tools/build_domains.py` 自动生成，按主题域受控词表归类。
> 一个页面可同时属于多个域。无主域标签的页面见文末「待归类」。
> 主域标签定义见 CLAUDE.md「主题域标签（tags）受控词表」。

## 具身智能 / 人形机器人（`embodied-ai`）

- [[concepts/automotive-ai-chip]]（汽车AI芯片）
- [[concepts/behavior-foundation-model]]（行为基础模型）
- [[concepts/embodied-ai]]（具身智能）
- [[concepts/humanoid-robot]]（人形机器人）
- [[concepts/robot-software-architecture]]（机器人软件架构）
- [[concepts/vision-language-action-model]]（视觉-语言-动作模型）
- [[entities/octo-robot-policy]]（Octo）
- [[synthesis/embodied-ai-humanoid-robot-synthesis]]（人形机器人与具身智能：约束已从「会动」下移到「身体层」三大瓶颈）
- [[synthesis/sdv-vla-agent-convergence-synthesis]]（端到端自动驾驶与具身智能的架构收敛综合）

## 汽车 EEA / MCU-less / 车载通信（`automotive-eea`）

_（暂无）_

## 芯片设计 / 制造 / 封装（`chip`）

- [[concepts/analog-chip-design]]（模拟芯片设计）
- [[concepts/automotive-ai-chip]]（汽车AI芯片）
- [[concepts/chip-design]]（芯片设计）
- [[concepts/mobile-soc]]（移动 SoC）

## 端侧推理 / TinyML（`edge-ai`）

- [[concepts/edge-ai]]（边缘AI）
- [[concepts/neuromorphic-computing]]（神经形态计算）
- [[synthesis/edge-ai-on-device-inference-synthesis]]（边缘AI：推理下沉到设备端，重塑 MCU 角色，受困于不可能三角）

## Agent 架构 / MCP / 治理（`agent`）

- [[concepts/agent-architecture]]（智能体系统架构）
- [[concepts/agent-feedback-loop]]（智能体反馈循环）
- [[concepts/agent-harness]]（Agent Harness）
- [[concepts/agent-memory]]（智能体记忆系统）
- [[concepts/agent-planning]]（智能体规划）
- [[concepts/agent-security-governance]]（Agent安全治理）
- [[concepts/human-in-the-loop]]（人在回路）
- [[concepts/tool-use-mcp]]（智能体工具调用）
- [[entities/claude-opus-4]]（Claude Opus 4）
- [[entities/hermes-agent]]（Hermes Agent）
- [[entities/kimi-k2]]（Kimi K2（Moonshot AI））
- [[entities/langgraph]]（LangGraph）
- [[entities/superagent]]（Superagent）
- [[synthesis/agent-theme-synthesis]]（Agent 主题综合：单 Agent 内部分层 × Harness 基础设施 × 生产安全治理）

## 金融数据 / 量化（`finance`）

_（暂无）_

## 待归类（无主域标签）

- [[concepts/advanced-packaging]]（先进封装）— tags: ['packaging', 'advanced', 'backend']
- [[concepts/arm-architecture]]（ARM 体系结构）— tags: ['arm', 'processor', 'embedded']
- [[concepts/automotive-ethernet-10base-t1s]]（10BASE-T1S 车载以太网）— tags: ['automotive-ethernet', '10base-t1s', 'ieee-802-3cg', 'plca', 'mculess', 'rcp']
- [[concepts/automotive-sensor]]（Automotive Sensor（汽车传感器））— tags: ['sensor', 'automotive', 'lidar', 'radar', 'camera']
- [[concepts/autonomous-driving]]（自动驾驶）— tags: ['automotive', 'adas', 'perception']
- [[concepts/autosar-complex-driver]]（AUTOSAR复杂驱动）— tags: ['autosar', 'bsw', 'cdd', 'automotive-software', 'mcal']
- [[concepts/autosar-configuration-toolchain]]（AUTOSAR配置工具链）— tags: ['autosar', 'toolchain', 'cdd', 'automotive-software', 'devtools']
- [[concepts/can-eth-protocol-conversion]]（CAN-ETH 协议转换）— tags: ['automotive', 'can-bus', 'ethernet', 'protocol', 'gateway']
- [[concepts/claude-code-workflow]]（Claude Code工程工作流）— tags: ['claude-code', 'llm-engineering', 'ai-workflow', 'agents', 'developer-tools']
- [[concepts/dexterous-hand]]（灵巧手技术）— tags: ['dexterous-hand', 'manipulation', 'tactile-sensor', 'robotics']
- [[concepts/eda-tools]]（EDA 工具）— tags: ['eda', 'tool', 'ic-design']
- [[concepts/eea-architecture]]（整车EEA架构）— tags: ['automotive', 'eea', 'electrical-architecture', 'zonal', 'centralized-computing']
- [[concepts/embedded-system]]（嵌入式系统）— tags: ['embedded', 'system']
- [[concepts/ethercat-realtime-communication]]（EtherCAT 实时通信）— tags: ['ethercat', 'real-time-communication', 'robotics', 'fieldbus']
- [[concepts/flexible-electronics]]（柔性电子）— tags: ['flexible', 'manufacturing', 'emerging']
- [[concepts/flip-chip]]（倒装芯片）— tags: ['packaging', 'interconnect', 'flip-chip']
- [[concepts/functional-safety]]（功能安全）— tags: ['functional-safety', 'automotive', 'iso26262', 'asil', 'robotics']
- [[concepts/gan-power-devices]]（氮化镓功率器件）— tags: ['gan', 'power-electronics', 'wide-bandgap', 'robotics', 'datacenter']
- [[concepts/gpan-communication]]（GPAN 通信协议）— tags: ['gpan', 'industrial-network', 'real-time-communication', 'robotics', 'automotive', 'mculess']
- [[concepts/humanoid-robot-supply-chain]]（人形机器人供应链）— tags: ['humanoid-robot', 'supply-chain', 'bom', 'actuator', 'manufacturing']
- [[concepts/ic-packaging]]（集成电路封装）— tags: ['semiconductor', 'packaging', 'backend']
- [[concepts/ic-testing]]（集成电路测试）— tags: ['semiconductor', 'testing', 'backend']
- [[concepts/lidar]]（激光雷达）— tags: ['automotive', 'sensor', 'perception']
- [[concepts/llm-benchmark-evaluation]]（大语言模型基准测试评估）— tags: ['LLM', 'benchmark', '模型评测', 'evaluation']
- [[concepts/llm-knowledge-management]]（LLM驱动知识库管理）— tags: ['knowledge-management', 'llm', 'second-brain', 'obsidian', 'personal-knowledge']
- [[concepts/low-power-design]]（低功耗设计）— tags: ['vlsi', 'power', 'ic-design']
- [[concepts/mculess-architecture]]（MCULess 架构）— tags: ['mculess', 'automotive', 'eea', 'zonal-gateway', 'bom-cost']
- [[concepts/memory-design]]（存储器设计）— tags: ['memory', 'ic-design']
- [[concepts/mems]]（微机电系统）— tags: ['mems', 'sensor', 'manufacturing']
- [[concepts/mixture-of-experts]]（混合专家模型）— tags: ['llm', 'moe', 'sparse-activation', 'transformer', 'efficiency']
- [[concepts/mmwave-radar]]（毫米波雷达）— tags: ['automotive', 'sensor', 'perception']
- [[concepts/model-context-protocol]]（模型上下文协议）— tags: ['mcp', 'protocol', 'llm', 'tooling']
- [[concepts/multimodal-api]]（多模态 API）— tags: ['api', 'multimodal', 'llm']
- [[concepts/power-management-ic]]（电源管理芯片）— tags: ['analog', 'power', 'pmic']
- [[concepts/quasi-direct-drive-motor]]（准直驱电机）— tags: ['motor', 'actuator', 'robotics', 'hardware']
- [[concepts/rcp-remote-control-protocol]]（RCP 远程控制协议）— tags: ['rcp', 'mculess', '10base-t1s', 'automotive', 'eea', 'ieee']
- [[concepts/reinforcement-learning-locomotion]]（强化学习运动控制）— tags: ['reinforcement-learning', 'locomotion', 'robotics', 'ppo']
- [[concepts/rf-chip-design]]（射频芯片设计）— tags: ['rf', 'analog', 'ic-design']
- [[concepts/robot-safety]]（机器人安全）— tags: ['robot-safety', 'functional-safety', 'humanoid-robot', 'safety']
- [[concepts/robot-simulation-framework]]（机器人仿真框架）— tags: ['simulation', 'robotics', 'reinforcement-learning', 'mujoco']
- [[concepts/robotics-roadmap-2025-2035]]（机器人技术路线图 2025–2035）— tags: ['robotics', 'roadmap', 'tess', 'vla', 'humanoid', 'geopolitics']
- [[concepts/semiconductor-manufacturing]]（半导体制造）— tags: ['semiconductor', 'manufacturing', 'wafer']
- [[concepts/sensor-design]]（传感器设计）— tags: ['sensor', 'ic-design']
- [[concepts/sim-to-real-transfer]]（Sim-to-Real 迁移）— tags: ['sim-to-real', 'reinforcement-learning', 'robotics', 'domain-randomization']
- [[concepts/soc-design]]（SoC 设计）— tags: ['soc', 'ic-design']
- [[concepts/soft-robotics]]（软体机器人）— tags: ['soft-robotics', 'materials', 'actuators', 'wearable', 'medical']
- [[concepts/tensor-mathematics]]（张量数学基础）— tags: ['mathematics', 'tensor', 'vector', 'scalar', 'ai-fundamentals']
- [[concepts/text-to-speech]]（文字转语音）— tags: ['tts', 'speech', 'audio', 'ai']
- [[concepts/time-sensitive-networking]]（时间敏感网络）— tags: ['networking', 'tsn', 'real-time', 'automotive', 'ethernet']
- [[concepts/vehicle-domain-controller]]（车载域控制器）— tags: ['vehicle-domain-controller', 'eea-architecture', 'autonomous-driving', 'automotive']
- [[concepts/video-generation]]（AI 视频生成）— tags: ['video', 'generative-ai', 'multimodal']
- [[concepts/vlsi-design]]（超大规模集成电路设计）— tags: ['semiconductor', 'vlsi', 'ic-design']
- [[concepts/voice-cloning]]（音色克隆）— tags: ['tts', 'voice', 'cloning', 'ai']
- [[concepts/wire-bonding]]（引线键合）— tags: ['packaging', 'interconnect']
- [[concepts/zonal-gateway]]（区域网关）— tags: ['automotive', 'eea', 'gateway', 'zcu', 'distributed-control']
- [[entities/automotive-claude-code-agents]]（Automotive Claude Code Agents）— tags: ['automotive-software', 'claude-code', 'agent-orchestration', 'iso26262', 'autosar', 'functional-safety']
- [[entities/broadcom]]（博通（Broadcom））— tags: ['company', 'semiconductor', 'rf']
- [[entities/cadence]]（Cadence（楷登电子））— tags: ['company', 'eda', 'tool']
- [[entities/claude-code]]（Claude Code）— tags: ['llm-tool', 'cli', 'anthropic', 'coding-assistant', 'ai-engineering']
- [[entities/deepseek]]（DeepSeek）— tags: ['llm', 'open-source', 'chinese-ai', 'efficiency', 'moe']
- [[entities/ecc-framework]]（Everything Claude Code (ECC)）— tags: ['ai-agent-framework', 'claude-code', 'agent-orchestration', 'open-source']
- [[entities/flextools]]（FlexTools）— tags: ['autosar', 'toolchain', 'automotive-software', 'devtools']
- [[entities/goodix-technology]]（Goodix Technology（汇顶科技））— tags: ['semiconductor', 'automotive', 'gpan', 'china']
- [[entities/infineon-technologies]]（英飞凌科技）— tags: ['company', 'semiconductor', 'germany', 'motor-control']
- [[entities/isaac-gym]]（Isaac Gym）— tags: ['simulation', 'reinforcement-learning', 'nvidia', 'tool']
- [[entities/kpmg]]（KPMG（毕马威））— tags: ['consulting', 'big-four', 'market-research']
- [[entities/lerobot]]（LeRobot）— tags: ['open-source', 'robotics', 'framework', 'huggingface']
- [[entities/li-auto]]（理想汽车）— tags: ['automotive', 'chinese-oem', 'eea', 'new-energy-vehicle']
- [[entities/mckinsey]]（麦肯锡咨询）— tags: ['consulting', 'strategy', 'research-institution']
- [[entities/mediatek]]（联发科（MediaTek））— tags: ['company', 'semiconductor', 'mobile-soc']
- [[entities/minimax]]（MiniMax）— tags: ['company', 'ai', 'llm', 'multimodal']
- [[entities/openclaw]]（OpenClaw）— tags: ['agent-platform', 'runtime', 'robotics', 'open-source', 'harness', 'multi-agent']
- [[entities/qualcomm]]（高通（Qualcomm））— tags: ['company', 'semiconductor', 'mobile-soc']
- [[entities/renesas-electronics]]（瑞萨电子）— tags: ['company', 'semiconductor', 'mcu', 'japan']
- [[entities/robocasa]]（RoboCasa）— tags: ['simulation', 'imitation-learning', 'open-source', 'kitchen-manipulation']
- [[entities/robosuite]]（robosuite）— tags: ['simulation', 'open-source', 'mujoco', 'reinforcement-learning']
- [[entities/st-microelectronics]]（意法半导体）— tags: ['company', 'semiconductor', 'stm32', 'robotics']
- [[entities/tesla-optimus]]（特斯拉 Optimus）— tags: ['company', 'humanoid-robot', 'end-to-end', 'tesla']
- [[entities/unitree-robotics]]（宇树机器人）— tags: ['company', 'robotics', 'china', 'reinforcement-learning']
- [[entities/zhipu-ai]]（智谱 AI（GLM））— tags: ['llm', 'chinese-ai', 'software-engineering', 'reasoning']
- [[synthesis/agent-architecture-landscape-synthesis]]（Agent 框架三条路线：治理、自进化与安全）— tags: ['agent-harness', 'openclaw', 'hermes-agent', 'superagent', 'agent-architecture']
- [[synthesis/chip-design-manufacturing-flow-synthesis]]（芯片设计制造全流程：一张参考地图，以及它与知识库前沿的割裂）— tags: ['chip-design', 'semiconductor-manufacturing', 'ic-packaging', 'ic-testing', 'knowledge-graph']
- [[synthesis/mculess-eea-architecture-synthesis]]（MCULess 与汽车 EEA 架构演进：硬件路由替代软件路由的过渡范式）— tags: ['mculess', 'automotive', 'eea', 'zonal-gateway', 'gpan', 'rcp']
- [[synthesis/robot-semiconductor-competitive-synthesis]]（机器人半导体竞争格局：三强鼎立与国产追赶）— tags: ['robotics', 'semiconductors', 'competitive-analysis', 'infineon', 'renesas', 'st-microelectronics']
- [[synthesis/vehicle-comms-protocols-synthesis]]（车载实时通信协议演进与 MCU-less 区域架构综合）— tags: ['automotive-ethernet', 'gpan', 'ethercat', '10base-t1s', 'mculess', 'zonal-gateway', 'real-time-communication']
