---
type: system-log
graph-excluded: true
---

# Operation Log

> 仅追加，禁止修改已有记录。格式：`YYYY-MM-DD HH:MM | 操作类型 | 说明`

<!-- 日志条目从此行之后追加 -->
2026-04-13 00:00 | init | 知识库系统初始化完成
2026-04-13 00:01 | ingest | 接口概览 - MiniMax 开放平台文档中心（slug: minimax-api-overview，提取 5 个概念，1 个实体）
2026-04-15 00:00 | system-audit | 完整系统状态核查，报告写入 wiki/outputs/system-audit-2026-04-15.md（综合得分 92%，发现 8 项问题，2 项高优先级）
2026-04-15 00:01 | fix | 针对审计偏差项批量修复：(1) CLAUDE.md 新增 URL/defuddle 规则、来源去重检测步骤、INGEST 末尾 qmd update，步骤总数 11→12；(2) entity-template.md 补充 updated 字段和 Evolution Log 节；(3) wiki/entities/minimax.md 同步补充 updated 和 Evolution Log；(4) wiki/overview.md 更新为实际数据；(5) USER_GUIDE.md 初始创建（与 CLAUDE.md 同步）
2026-04-15 00:02 | system-audit | 第二次全量系统核查，报告写入 wiki/outputs/system-audit-2026-04-15-v2.md（综合得分 91%，发现 8 项问题，2 项高优先级：SHA-256 不匹配 + qmd 嵌入向量缺失）
2026-04-15 00:03 | fix | 二次审计修复：(1) CLAUDE.md Step 12 命令 qmd add→qmd update；(2) wiki/index.md 补充 Outputs 节登记 4 个输出文件；(3) wiki/overview.md 更新最近 Lint 报告；(4) USER_GUIDE.md 同步修正 qmd 命令
2026-04-15 00:04 | re-ingest | 接口概览 - MiniMax 开放平台文档中心（slug: minimax-api-overview，re-ingest 原因：SHA-256 不匹配，原始文件已更新；变更内容：新增 M2.7/M2.7-highspeed 文本模型、Hailuo-2.3/2.3-Fast 视频模型、music-2.6；更新 raw_sha256→35880ce4，更新 source Key Points 及 multimodal-api / text-to-speech / video-generation concept 页）
2026-04-15 00:05 | ingest | 人形机器人技术研究及快速原型建设（slug: humanoid-robot-research-rapid-prototyping，提取 7 个概念，5 个实体）
2026-04-15 00:06 | ingest | 瑞萨电子在机器人伺服控制与EtherCAT实时通信中的应用（slug: renesas-robot-servo-ethercat-application，PDF 37页，提取 0 个新概念/3个已有概念更新，1 个新实体；修正：EtherCAT 分布式时钟精度 <1μs→<100ns）
2026-04-15 00:07 | ingest | 批量处理 raw/clippings/ 5个文件（slugs: openclaw-simulation-rl-agent / robosuite-quickstart / ethercat-gpan-servo-validation / gpan-mculess-validation / robot-sensor-actuator-communication；新增 2 个概念：robot-simulation-framework / gpan-communication；新增 3 个实体：robocasa / openclaw / robosuite；更新 4 个已有概念页）
2026-04-16 17:15 | warn | 来源文件 raw/clippings/分布式网关通信TDT.md 缺少标准 frontmatter，source_url 留空，date 取摄入日期 2026-04-16
2026-04-16 17:15 | ingest | 分布式网关通信TDT（slug: distributed-gateway-communication-tdt，提取 4 个概念，1 个实体）
2026-04-16 18:36 | query | 分布式网关的价值点（输出写入 wiki/outputs/2026-04-16-distributed-gateway-value.md）
2026-04-18 21:12 | query | 知识库设计优缺点评价（输出写入 wiki/outputs/2026-04-18-kb-design-evaluation.md）
2026-04-19 23:25 | ingest | 批量处理 raw/clippings/ 3个新文件（slugs: agent-harness-revolution-2026 / openclaw-ai-team-practice / hermes-vs-openclaw-comparison；新增 1 个概念：agent-harness；新增 1 个实体：hermes-agent；更新 1 个已有实体：openclaw）
2026-04-19 23:29 | ingest | 个人写作：和 AI 协作的一些实践与思考（slug: ai-collaboration-practices，作者：刘万龙；不计入 source_count；核心立场写入 agent-harness#My Position）
2026-04-19 23:38 | lint | 全量检查，9/9 通过，0 issues；修复内容：YAML 弯引号转义（openclaw-simulation-rl-agent）、4 处断链补全 entities/ 路径前缀、voice-cloning aliases 规范化重复；报告写入 wiki/outputs/lint-2026-04-19.md
2026-04-20 00:01 | ingest | OpenClaw vs Hermes：一文深入理解两大通用 Agent（slug: openclaw-vs-hermes-deep-dive，作者：架构师/JiaGouX；更新 1 个概念：agent-harness source_count 3→4；更新 2 个实体：openclaw/hermes-agent）
2026-04-15 00:08 | ingest | 批量处理 raw/pdfs/ 11个文件（新增 11 个 source 页：embodied-ai-os-whitepaper-2026 / infineon-gc-humanoid-robot-jun2025 / infineon-humanoid-robot-feb2026 / renesas-ra8t2-mcu-introduction / renesas-automotive-ai-audio-detection / renesas-rh850-u2b-introduction / renesas-rzt2h-n2h-introduction / renesas-rzt2n-introduction / renesas-robotic-platform-2025 / st-smart-industry-robotics-v9 / renesas-robot-application-guide-2025；新增 2 个实体：infineon-technologies / st-microelectronics；更新 5 个已有概念页）
2026-04-20 01:30 | ingest | 批量处理 raw/pdfs/ 15个新文件（GPAN 机器人应用介绍 + 英飞凌深圳/北京技术论坛14个演讲）；新增 15 个 source 页：gpan-robot-application-introduction / infineon-sensing-empowers-robotics-shenzhen-2025 / infineon-psoc-gan-motor-drive-shenzhen-2025 / infineon-complete-solution-robotics-shenzhen-2025 / infineon-gan-solution-robotics-shenzhen-2025 / infineon-aiot-sensing-computing-connectivity-shenzhen-2025 / infineon-ai-data-security-protection-shenzhen-2025 / infineon-xensiv-radar-edge-ai-shenzhen-2025 / infineon-airoc-wireless-ai-future-shenzhen-2025 / infineon-wifi-sensing-6g-aiot-beijing-2025 / ai-datacenter-hvdc-bus-evolution-solutions-shenzhen-2025 / infineon-coolgant-ai-datacenter-shenzhen-2025 / infineon-ai-server-power-solution-shenzhen-2025 / infineon-2025-key-products-shenzhen-forum / gan-power-devices-tech-applications-outlook-shenzhen-2025；更新 2 个已有页：gpan-communication（source_count 2→3）/ infineon-technologies（source_count 2→16）；本次因 D: 盘磁盘空间不足（0B），执行 pnpm store prune 释放约 2.4GB 后继续
2026-04-25 16:47 | ingest | OpenClaw、Hermes、Superagent：Agent 时代的三条路线，该怎么选？（slug: agent-route-comparison-2026，提取 2 个概念，3 个实体；新建：agent-security-governance / superagent；更新：agent-harness source_count 4→5 / openclaw / hermes-agent）
2026-04-25 16:47 | ingest | 理想自研芯片马赫M100深度剖析，AI算力数字可以忽略不看（slug: li-auto-mach-m100-deep-dive，提取 1 个新概念 automotive-ai-chip，更新实体 li-auto）
2026-04-25 16:47 | ingest | Karpathy大神的LLM驱动知识库管理方法论（slug: karpathy-llm-knowledge-management，提取 1 个新概念 llm-knowledge-management，0 个实体；Karpathy 背书为本知识库架构提供独立外部验证）
2026-04-25 16:47 | ingest | 机器人软件架构介绍——具身智能研发基础（slug: robot-software-architecture-intro，提取 1 个新概念 robot-software-architecture，更新 2 个概念：ethercat-realtime-communication / humanoid-robot，更新实体 unitree-robotics）
2026-04-25 16:47 | ingest | 理想M100芯片论文全文翻译|也可用于座舱（slug: li-auto-m100-paper-translation，canonical_source: arxiv.org/2604.17862；内容全为图片，实质内容已在 li-auto-mach-m100-deep-dive 覆盖；更新概念 automotive-ai-chip source_count 1→2）
2026-04-25 16:47 | ingest | DeepSeek V4封神了！（slug: deepseek-v4-technical-analysis，提取 1 个新概念 mixture-of-experts（source_count=1），新建实体 deepseek；记录 V4 mHC/混合注意力/Muon/OPD 架构创新）
2026-04-25 16:47 | ingest | 一文看懂混合专家模型 (MoE) 到底是什么？（slug: mixture-of-experts-explained，更新概念 mixture-of-experts source_count 1→2；MoE 基础机制入门教程）
2026-04-25 17:00 | lint | 全量检查，9/9 通过，0 issues；修复内容：(1) lint.py load_frontmatter 改用行首锚定正则替代 naive split，修复文件名含 --- 时 YAML 提前截断的 bug（影响 infineon-airoc-wireless-ai-future-shenzhen-2025）；(2) 3 个 output 文件补充 YAML frontmatter（2026-04-22-infineon-robot-applications / 2026-04-22-robot-mcu-modules-vendors / 2026-04-23-new-business-cocreation-workshop）；(3) openclaw-vs-hermes-deep-dive raw_sha256 更新为实际值（原始文件已修改）；报告写入 wiki/outputs/lint-2026-04-25.md
2026-04-25 17:13 | reflect | 全量综合分析；Stage 1 扫描 24 concepts / 16 entities / 55 sources；Stage 0 反向检验识别 3 处回音室风险；Stage 2 新建 2 个 synthesis 页：robot-semiconductor-competitive-synthesis（confidence: medium，24 来源）/ agent-architecture-landscape-synthesis（confidence: low，7 来源）；Stage 3 识别 4 类知识空白（P1：robot-functional-safety + gan-power-devices 概念页缺失；P2：ros2 + nvidia-jetson 实体缺失）；Gap Report 写入 wiki/outputs/gap-report-2026-04-25.md；新增交叉链接：mixture-of-experts ↔ agent-harness / llm-knowledge-management ↔ agent-harness；更新 wiki/overview.md（Synthesis 0→2）
