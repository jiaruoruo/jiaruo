# 分布式网关通信TDT

# 项目说明三页纸（汇报时长建议5min）

| <u>**一、申请审批事项**</u> |
| --- |
| 申请审批通过分布式网关通信预研项目的立项申请，包括：<br>1. 研究问题、目标和研究价值 <br>2. 资源申请<br> a. 全项目生命周期预算：174.9万元，其中业务费用6.9万元，人力成本168万元<br> b. ~~PDCP阶段前释放预算：xx元，其中业务费用xx元，人力成本xx元 （产研科技树可剪裁）~~<br>3. TDT团队成员任命 |
| <u>**二、预评审意见**</u> |
| 1. TSEG 预审意见（补充纪要链接或截图），及待办闭环说明<br>2. 财经意见（群组/部门财经代表：~~，AI委员会财经代表[适用于AI-RD项目]：~~@郭婷）<br>3. 人力意见（人力BP：@赵霞） |
| <u>**三、项目关键信息**</u> |
| 1. **技术路标承接：**为实现2027年OC量产与面向EEA4.0的下一代计算与通信架构，承接自算力平台技术沙盘中通信系统下的 “XoverETH协议转换” 和 “通信故障监控及处理” 技术点<br>2. **问题定义**：伴随整车智能化到来及L4自动驾驶功能，整车驱动与传感器数量增多，计算趋于集中化，主干网由CAN 转换为ETH，主流新势力主机厂，正逐步采用ETH替代CAN作为主干网，并进行功能部署；为支撑驱动、底盘等功能集中部署，ETH的实时性与可靠性需要进一步的提升，开发**高效的CAN与ETH互转协议与相应的冗余策略**成为必须；<br>3. **解题思路：**设计高效的**协议转换标准**与科学的**转发策略**，以减少通信时延，增强通信确定性。开发**动态路由策略**，以使网关具备优先级调度、冗余切换等功能，提高通信实时性与可靠性。在此基础上，实现**ZCU驱动能力服务化封装**，验证以太网主干网对业务上移的支撑能力。最后，设计**网关性能验证**试验方案，完成CAN-CAN及CAN-A核的全链路通信性能测试。<br>4. **项目目标：**<br> a. 关键技术指标：<br> i. 协议转换支持多条业务基于优先级的调度策略，多业务混合ECU(CAN) <--> ECU(CAN)之间时延/抖动：<br> 1. 触发式报文：小于1ms<br> 2. 报文周期<20ms：小于±20%<br> 3. 报文周期≥20ms：小于±10%<br> ii. 动态路由表更新响应延迟： 确认故障后小于5ms（确认故障-＞切换成功）<br> iii. ZCU驱动原子服务时延/抖动<br> 1. 执行器类驱动：请求响应的时延（Fire/Forget）小于1ms<br> 2. 传感器类/状态上报/故障类驱动：1ms/10ms类更新频率（Cyclic）抖动小于±20%<br> b. 交付物形式<br> i. 设计报告<br> 1. 协议设计规范<br> 2. 路由转换动态切换策略设计报告<br> 3. ZCU驱动能力原子服务设计报告<br> ii. 测试报告<br> 1. 转换协议测试报告<br> 2. ZCU网关性能测试报告<br> 3. ZCU至CCU端到端性能测试报告<br> iii. 软件<br> 1. 路由转换动态切换软件<br> 2. ZCU驱动能力原子服务（含基于BZCU的Server软件和基于LZCU的Client软件）<br> 3. 测试用软件(含BZCU和LZCU)<br> c. 项目里程碑：PDCP 2025/05/10，如xx完成技术方案；TDCP 20xx/xx/xx，如xx上线发布<br>5. **TDT团队成员（完整信息见下文5.3部分）** |

# 技术路标承接

> 💡 面向EEA4.0下一代计算与通信架构的高通信带宽需求、L4自动驾驶及27年无人驾驶OC项目量产，整车通信骨干网将由CAN转换为以太网，基于算力平台技术沙盘，**X**over**ETH协议转换**为关键技术

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/f54805e5-3ba0-4e6f-baa0-347f63d5a166.png)

# 项目价值

## 问题定义

> 阐述要解决的技术问题，以及解题的挑战点，导出解题的关键技术点

伴随整车**智能化**到来及**L4自动驾驶**功能，整车业务趋向**中央集中部署，**智能汽车主干网由CAN 转换为ETH，届时面临的**CAN-ETH转发协议**及转发**规则制定**；



ETH取代CAN作为骨干网的优势：

- ETH具备与**SOA软件架构**更好的支撑；
- ETH具备**高带宽**使**软件灵活部署**成为了可能，更好的支撑**软件平台化**，**降低开发成本**；
- ETH具备环网能力，实现通信的无缝**冗余**，**实时性**及**抗干扰**能力等优点；
| 序号 | 路由链路 | 网关形态 |
| --- | --- | --- |
| EEA2.0 | CAN—**XCU（中央网关）**—CAN | **XCU 为中央网关**，整车以CAN网络为主干网络，承担功能交互；ETH为局域网络，部署OTA及数据上传功能； |
| EEA3.0 | CAN—**ZCU（区域网关）**—ETH—CCU（FSD） | **ZCU为分布式区域网关**，**CCU为中央网关**，整车以CAN网络为主干网；ETH承担部分功能交互**（实时性及安全性不高的功能）；** |
| **数据流对比图**<br>![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/14693284-edab-4916-aaac-a9738526458a.png) |  |  |

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/14693284-edab-4916-aaac-a9738526458a.png)


| 序号 | 问题点 | 问题描述说明 |  |
| --- | --- | --- | --- |
| 1 | 缺少CAN-ETH 路由通信标准化协议技术 | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/367f90d7-e9e8-40f0-99e1-9c64de9d6542.png) | **问题****描述：**<br>面向ETH作为整车通信主干网，需要探索一种高标准化程度，高准确，低延迟的CAN—ETH互转协议 |
| 2 | 缺少CAN-ETH 节点路由失效的冗余方案 | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/d2306939-93e7-42e9-a9d4-1752f05b21be.png) | **问题描述：**<br>当网关某一网关路由失效，需要一种动态冗余路由方案，保证车辆行驶功能基础安全 |
| 3 | 缺少区域控制驱动服务化，原子数据转换标准化技术 | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/14027f95-b329-487e-b06f-adf1c93b8ed9.png) | **问题描述：**<br>面向中央计算力不断提升，区域控制偏向驱动执行，支撑更灵活的业务功能部署，区域驱动原子服务化功能，从区域控制标准化，模块化，及中央计算全局资源调度，进一步提升成本效率； |
| 4 | 缺少CAN-ETH路由转换性能基线 | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/a51d3395-9f74-41b5-a9ca-fd1862ff8d2b.png) | **问题描述：**<br>单条业务转换性能<br>多业务并发转换性能<br>多业务、多优先级转换调度策略 |
| 5 | 缺少CAN-ETH-CCU（A核）路由链路性能基线 | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/b8f79b99-99e9-42ee-bba8-5541cb2fee68.png) | **问题描述：**<br>单业务端到端（A核<-->ECU、ECU<-->ECU）转发时延、抖动<br>多业务混合端到端（A核<-->ECU、ECU<-->ECU）转发时延、抖动，优先级策略<br>链路稳定性验证(低优先级高背景流、主、备链路切换） |

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/367f90d7-e9e8-40f0-99e1-9c64de9d6542.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/d2306939-93e7-42e9-a9d4-1752f05b21be.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/14027f95-b329-487e-b06f-adf1c93b8ed9.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/a51d3395-9f74-41b5-a9ca-fd1862ff8d2b.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/b8f79b99-99e9-42ee-bba8-5541cb2fee68.png)

## 技术洞察

> 五看。分析行业标杆的解决方案的优势和劣势，识别业界遇到什么挑战性的问题，现在的问题为何不好解决，有哪些路线需要验证

### 看行业

> 👉 新形态EEA架构下对整车中央网关&分布式网**关发展趋势**
> 1.**融合网关：**网关由单独的控制器节点→中央计算+区域控制器（集成中央网关+分布式网关）。
> 2.**分布式网关**：网关形态由1个整车中央式网关→多个集成分布式网关形态。
> 3.**高速通信网关：**实现**以太网ETH**与传统总线**（CAN/LIN）**的高效**协议转换**。

#### 车载网关发展阶段：

| **第一阶段:分布式架构下的传统CAN网关** | **第二阶段:域集中架构下的集中式网关** | **第三阶段:中央计算+Zonal架构下的分布式网关** |
| --- | --- | --- |
| 各个功能由单一的ECU实现。动力、底盘、车身、娱乐，网段，通过CAN、LIN等传统总线连接。网段之间的交互通过**CAN网关实现**. | 功能域一般分为动力、底盘、车身、座舱、ADAS。域内使用CAN通信，通过**域网关**与外部交互。而不同域间通讯，由CAN和ETH承担，在这种架构中，域之间交互通过**集中式网关**。 | 在中央计算+区域控制架构中，域网关（Domain Gateway ）将演变为**区域网关**（Zonal Gateway）。集中式网关将演变集成**中央计算；** |
| ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/a6a7451d-445d-496d-9d51-4e06286459f7.png) | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/6146b54a-939b-4853-add5-6d87ff82b21e.png) | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/4884c049-5626-420a-8070-1790e41362e0.png) |
| 1. **架构演进**：从“功能域”到“物理区域”，兼顾集中化与分布式优势。 <br>2. **通信升级**：传统总线 → 高速以太网，支持高带宽、低延迟场景。 <br>3. **功能扩展**：网关从通信路由转向“通信+计算”融合，强化数据安全与实时处理。 <br>4. **成本优化**：通过区域化架构减少线束和硬件冗余，推动规模化落地。 |  |  |

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/a6a7451d-445d-496d-9d51-4e06286459f7.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/6146b54a-939b-4853-add5-6d87ff82b21e.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/4884c049-5626-420a-8070-1790e41362e0.png)

### 看客户

> 💡 1. **ETH部署高实时性功能**：ETH网络**当前**仅为状态显示+车身控制类通信信息，（未部署动力驱动，底盘，高压控制类信息）（未来逐步拓展高实时性底盘&动力功能部署）
> 2. **CAN网络节点增多**：CAN/LIN节点数量增多，以RZCU为例 CANFD节点数量为37个，LIN节点数量为28个（智能化程度提高，驱动控制器&传感器数量增多）
> 3. **CAN总线负载增高**：各CAN网段总线负载高的已经达到70%，已接近CAN总线负载拓展性上限；
> 4. **EEA架构演进以软件部署驱动：**当前EEA3.0 物理架构形态趋于稳定，EEA4.0 功能部署&软件架构迎来进一步优化，ETH为软件架构部署提供可能；

> 伴随**智能化程度提升**，整车驱动与传感器数量增多，**计算**趋于**集中化**，为支撑驱动/底盘等功能集中部署，ETH高实时性可靠性需要进一步的提升，基于ETH功能部署**CAN转ETH路由成为必须**；

#### 理想汽车EEA发展

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/91f4f2cc-eb71-48d5-a60c-6bb64ae93093.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/c6e67498-d25a-46cf-a1df-8b86e2f466e7.png)

#### EEA 3.0整车网络通信&分布式网关路由状态(R-ZCU)

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/59800345-c636-47c2-a8db-b9be5b3f2fb2.jpg)
1. **整车主干网信息**
|  | CCU（中央算力单元） | HU（人机交互主机） | LZCU（左区域控制器） | RZCU（右区域控制器） | BZCU（后区域控制器） |
| --- | --- | --- | --- | --- | --- |
| 网段 | 公共网段：<br>**整车：**ZCAN，ETH1，ETH2，ETH3，CHCAN1,CHCAN2,<br>**HU：**ETH5，ETH6，LVDS1-LVDS4<br>域内网段：<br>LVDS×7，ETH4，RDCAN2 | 公共网段：<br>**整车：**ZCAN<br>**CCU：**ETH5，ETH6，LVDS1-LVDS4<br>域内网段：<br>LVDS×4，BLECAN | 公共网段：<br>**整车：**ZCAN，<br>**CCU：**ETH1<br>域内网段<br>CANFD×8<br>LIN×6 | 公共网段：<br>**整车：**ZCAN，<br>**CCU：**ETH2<br>域内网段：<br>CANFD×4<br>LIN×6 | 公共网段：<br>**整车：**ZCAN，<br>**CCU：**ETH3<br>私有网段：<br>CANFD×7<br>CAN×1<br>LIN×6 |
| 区域功能 | 中央计算功能+自动驾驶控功能模块 | 车载娱乐控制功能模块 | 1.娱乐功放功能模块<br>2.抬头显示HUD&二排屏幕显示功能模块<br>3.整车灯光控制功能模块<br>4.车身数字钥匙功能模块<br>5.车身门功能模块<br>6.车身附件雨刮&传感器等功能模块 | 1.气囊&车门控制功能模块<br>2.动力驱动&高压充电&高压电池管理功能模块<br>3.发动机增程器管理&DCDC管理控制模块<br>4.底盘稳定系统&后轮转向系统控制模块<br>5.空调热管理功能模块； | 1.底盘制动功能模块<br>2.后空调加热功能模块<br>3.后排座椅按摩加热功能模块<br>4.主动悬架系统功能模块 |

2. **RZCU分布式网段信息**
| ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/7cf3e70c-db29-48a8-8d25-041606aca262.jpg) |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 网段 | 通信速率 | 网段<br>节点 | 通信信息<br>（快周期报文） | 路由信息<br>（快周期报文） | 总线<br>负载 | 通信&路由信息汇总 |
| ETH | 100M | RZCU/<br>LZCU/<br>BZCU/<br>CCU/<br>HU | ETH服务 ID：2919个 | / |  | **车身控制及状态类**<br>1.数字钥匙控制&状态信息<br>2.整车灯光控制&状态信息<br>3.前后雨刮控制&状态信息<br>4.防盗&喇叭状态信息<br>**动力驱动状态类**<br>1.加速踏板状态<br>2.车速状态<br>3.能量回收等级<br>4.Ready状态信息<br>5.故障类信息<br>6.驾驶模式<br>**高压充放电状态类**<br>1.车内外放电状态<br>2.高压状态<br>3.能量管理模式<br>**底盘状态类**<br>1.制动系统状态类信息<br>**座舱娱乐状态类**<br>1.主驾/后排充电状态<br>2.环视摄像头参数状态 |
| ZCAN | 2M | RZCU/<br>LZCU/<br>BZCU/<br>CCU | BMS：ID 0x140，周期：10ms<br>BMS：ID 0x141，周期：10ms<br>[BZCU: ID 0x138, 周期：10ms](BZCU: ID 0x138, 周期：10ms)<br>[BZCU: ID 0x59B, 周期：10ms](BZCU: ID 0x59B, 周期：10ms)<br>[BZCU: ID 0x29A, 周期：20ms](BZCU: ID 0x29A, 周期：20ms)<br>[BZCU: ID 0x2FB, 周期：10ms<br>BZCU: ID 0x2C9, 周期：10ms<br>FSD：0x156，周期：10ms<br>RZCU: 0x216，周期：20ms<br>](BZCU: ID 0x2FB, 周期：10ms<br>BZCU: ID 0x2C9, 周期：10ms<br>FSD：0x156，周期：10ms<br>RZCU: 0x216，周期：20ms<br>)[LZCU: 0x599，周期：10ms](LZCU: 0x599，周期：10ms)<br>[LZCU: 0x59A，周期：10ms](LZCU: 0x59A，周期：10ms)<br>[LZCU: 0x209，周期：20ms<br>RZCU：0x120，周期：10ms<br>](LZCU: 0x209，周期：20ms<br>RZCU：0x120，周期：10ms<br>)RZCU：0x121，周期：10ms<br>RZCU：0x100，周期：10ms | ACU：ID 0x210，周期：20ms | 66.02% | Z CAN<br>网段节点数量：4个<br>节点块周期报文：15条<br>路由快周期报文：1条<br>高通信负载功能交互<br>1.安全气囊加速度信息；<br>2.高压电池充电状态及电池状态信息；<br>3.主动悬架油泵压力信息；<br>4.智能配电状态信息；<br>5.四门锁状态信息；<br>6.时区状态信息；<br>7.EMB制动状态信息；<br>8.电源模式状态；<br>9.前后电机扭矩状态信息；<br>10.车辆行驶状态信息车速/挡位等 |
| PTCAN | 2M | BMS/<br>BZCU/<br>MCU/<br>ODU/<br>PDC/<br>RZCU | BMS：0x261，周期：20ms<br>BMS：0x140，周期：10ms<br>BMS：0x141，周期：10ms<br>MCUR: 0x2E1, 周期：20ms;<br>MCUR: 0x121, 周期：10ms;<br>[MCUR: 0x131, 周期：10ms;](MCUR: 0x131, 周期：10ms;)<br>[ODU: 0x180, 周期：10ms;](ODU: 0x180, 周期：10ms;)<br>RZCU：0x108，周期：10ms;<br>RZCU：0x150，周期：10ms;<br>RZCU：0x188，周期：10ms;<br>RZCU：0x110，周期：10ms;<br>RZCU：0x227，周期：20ms;<br>RZCU：0x151，周期：10ms;<br>RZCU：0x111，周期：10ms;<br>RZCU：0x186，周期：10ms;<br>RZCU：0x100，周期：10ms; | EMS：ID 0x123，周期10ms<br>EMS：0x260，周期：20ms<br>EMS：0x123，周期：10ms<br>DCDC: 0x187, 周期：10ms<br>DCU：0x2C9，周期：20ms<br>[IPB: 0x228，周期：10ms](IPB: 0x228，周期：10ms)<br>[LZCU: 0x2A9，周期：20ms](LZCU: 0x2A9，周期：20ms)<br>[LZCU: 0x209，周期：20ms](LZCU: 0x209，周期：20ms)<br>[LZCU: 0x120，周期：10ms](LZCU: 0x120，周期：10ms) | 54.67% | PT CAN<br>高通信负载功能交互<br>网段ECU数量：6个<br>节点快周期报文数：16条<br>路由快周期报文数：9条<br>高通信负载功能交互<br>1.BMS动力电池功率信息；<br>2.BMS动力电池充电状态；<br>3.EMS发动机状态信息；<br>4.DCDC输出电压&电流状态；<br>5.MCUF/R前后电机驱动扭矩状态信息；<br>6.DCDC输出电压功率及故障保护状态等;<br>7.车辆行驶状态信息车速/挡位等;<br>8.前/后电机MCUF是扭矩及使能控制； |
| CHCAN1 | 2M | BZCU/<br>DPB/<br>EPS/<br>FSD/<br>HWA/<br>LZCU/<br>RWA/<br>RWS/<br>RZCU/<br>TCM/ | [BZCU: 0x12A，周期10ms<br>BZCU: 0x12B，周期20ms<br>BZCU: 0x12C，周期10ms<br>BZCU: 0x127，周期10ms<br>DPB：0x86，周期10ms<br>BZCU：0x218，周期10ms<br>](BZCU: 0x12A，周期10ms<br>BZCU: 0x12B，周期20ms<br>BZCU: 0x12C，周期10ms<br>BZCU: 0x127，周期10ms<br>DPB：0x86，周期10ms<br>BZCU：0x218，周期10ms<br>)BZCU：0x228，周期10ms<br>DPB：0x87，周期10ms<br>DPB：0x1A6，周期10ms<br>DPB：0x106，周期10ms<br>ESP：0x217，周期10ms<br>ESP：0x136，周期10ms<br>ESP：0x1F8，周期10ms<br>ESP：0x76，周期10ms<br>ESP：0x216，周期20ms<br>ESP：0x198，周期10ms<br>FSD：0x196，周期10ms<br>FSD：0x177，周期10ms<br>LZCU：0x237，周期10ms<br>RWS：0x1C5，周期10ms<br>RWS：0x166，周期10ms<br>RWS：0x257，周期20ms<br>HWA：0x1D4，周期10ms | ACU：ID 0x210，周期：20ms | 64.88% | CHCAN1<br>高通信负载功能交互<br>网段ECU数量：10个<br>节点快周期报文数：23条<br>路由快周期报文数：1条<br>高通信负载功能交互<br>1.安全气囊加速度信息；<br>2.车辆行驶状态信息车速/挡位等;<br>3.底盘制动状态信息<br>4.底盘悬架状态信息<br>5.底盘系统车轮状态转速/加速等信息<br>6.底盘IPB制动状态信息；<br>7.底盘电子转向控制状态信息；<br>8.底盘ESP制动工作状态信息；<br>9.FSD功能状态信息；<br>10.底盘RBU制动系统信息；<br>11.底盘后轮转向系统信息； |
| CHCAN2 | 2M | BZCU/<br>DPB/<br>EMS/<br>EPS/<br>ESP/<br>FDCDC/<br>FSD/<br>HWA/<br>LZCU/<br>RWA/<br>RZCU/ | RWS：0x257，周期20ms<br>DPB：0x228，周期10ms<br>DPB：0xA8，周期10ms<br>DPB：0x96，周期10ms<br>EMS：0x123，周期10ms<br>EMS：0x133，周期10ms<br>EMS：0x260，周期20ms<br>EPS：0x116，周期20ms<br>EPS：0x77，周期20ms<br>EPS：0x226，周期20ms<br>EPS：0x187，周期10ms<br>FSD：0x178，周期10ms<br>FSD：0x197，周期10ms<br>FSD：0x2F4，周期20ms<br>GCU：0x122，周期10ms<br>HWA：0x1D4，周期10ms | ACU：ID 0x210，周期：20ms<br>BMS：0x140，周期：10ms<br>BMS：0x141，周期：10ms<br>BZCU：0x146，周期：10ms<br>EMB :ID 0x139，周期：10ms<br>EMB :ID 0x13A，周期：10ms<br>EMB :ID 0x126，周期：10ms<br>LZCU:ID 0x238，周期：10ms<br>LZCU:ID 0x248，周期：10ms<br>LZCU:ID 0x2E0，周期：10ms<br>MCUF:ID 0x120，周期：10ms<br>MCUF:ID 0x130，周期：10ms<br>MCUR:ID 0x121，周期：10ms | 69.88% | CHCAN2<br>网段ECU数量：11个<br>节点快周期报文数：10条<br>路由快周期报文数：13条<br>高通信负载功能交互<br>1.安全气囊加速度信息<br>2.BMS动力电池系统&充电状态<br>3.DPB制动系统状态信息<br>4.发动机增程器状体信息<br>5.EPS转向机状态信息；<br>6.FSD功能状态信息； |
| BDCAN1 | 2M | ACU/<br>FLDCU/FRDCU/RLDCU/RRDCU/RLDHC/<br>RRDHC | ACU：ID 0x210，周期：20ms<br>[FLDCU: ID 0x2C9,周期：20ms](FLDCU: ID 0x2C9,周期：20ms)<br>[RZCU: 0x108，周期10ms<br>RZCU: 0x258，周期20ms<br>RZCU: 0x100，周期10ms<br>](RZCU: 0x108，周期10ms<br>RZCU: 0x258，周期20ms<br>RZCU: 0x100，周期10ms<br>)[RZCU: 0x207，周期20ms](RZCU: 0x207，周期20ms) | EMS：ID 0x123，周期10ms<br>[EPS: ID 0x106，周期10ms<br>](EPS: ID 0x106，周期10ms<br>)[FSD: ID 0x197, 周期10ms](FSD: ID 0x197, 周期10ms)<br>[FSD: ID 0x156, 周期10ms<br>](FSD: ID 0x156, 周期10ms<br>)[IPB: ID 0x86, 周期10ms](IPB: ID 0x86, 周期10ms)<br>[IPB: ID 0x77, 周期10ms<br>IPB: ID 0x96，周期10ms<br>IPB：ID 0x226，周期20ms<br>IPB：ID 0x216，周期20ms<br>LZCU：ID 0x25A，周期20ms<br>](IPB: ID 0x77, 周期10ms<br>IPB: ID 0x96，周期10ms<br>IPB：ID 0x226，周期20ms<br>IPB：ID 0x216，周期20ms<br>LZCU：ID 0x25A，周期20ms<br>)[LZCU: ID 0x219，周期20ms](LZCU: ID 0x219，周期20ms)<br>[LZCU: ID 0x2A9，周期20ms<br>MCUF: ID 0x120，周期10ms<br>MCUR: ID 0x121，周期10ms<br>](LZCU: ID 0x2A9，周期20ms<br>MCUF: ID 0x120，周期10ms<br>MCUR: ID 0x121，周期10ms<br>)[RZCU: ID 0x259，周期20ms](RZCU: ID 0x259，周期20ms) | 43.86% | BD CAN1 <br>网段ECU数量：7个<br>节点快周期报文数：6条<br>路由快周期报文数：15条<br>高通信负载功能交互<br>1.安全气囊加速度信息；<br>2.EMS发动机状态信息；<br>3.EPS转向机状态信息；<br>4.FSD功能状态信息；<br>5.EMB制动状态信息；<br>6.车门锁状态信息；<br>7.MCUF/R前后电机驱动扭矩状态信息；<br>8.车辆行驶状态信息车速/挡位等<br>9.车辆驱动扭矩请求信息 |

### 看竞争

> 💡 1. **特斯拉**在最新的整车架构中均部署了**ETH** 且为**环网结构**。整体拓扑分析，ETH为整车**主干网**；
> 2. **华为**在**2021**年已经**实现ETH**的功能部署，并实现**CAN-ETH路由转发**功能；
> 3. **小米**在下一代电子电器架构中采取"快速跟随"策略，规划采用**ETH**作为主干网；
> **主流新势力主机厂，正逐步采用ETH替代CAN作为主干网，并进行功能部署，CAN到ETH的路由转换为必备功能；**

#### 特斯拉

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/74823b0d-16de-4115-ae3e-af87c062b179.png)

#### **小米**

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/36dc2908-198b-4c6c-97db-87decb0c2507.png)

#### 华为

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/c1777609-ee12-4b03-b43c-374ad2185b05.png)

### 看自己

> 💡 - EEA3.0 中主干网逐步由CAN转向ETH，且ETH开始部署车身控制等低实时性要求功能，未来逐步拓展，未来部署底盘/动力/高实时性要求功能；
> - 未来ETH将部署多种不同实时性要求功能数据类型。基于不同类型数据转发要求，构建多级数据转发路径方案；

#### 车载网络通信功能部署

| **架构** | **整车网络架构** | **网关形态** | **网关功能** |
| --- | --- | --- | --- |
| **EEA 1.0** | 分布式 | 中央式网关<br>（CGW） | 多网段CAN通信路由<br>以太网路由 |
| **EEA 2.0** | 域集中式 | 域控制+区域网关<br>（XCU，FBCM，RBCM） | 多网段LIN/CAN/CANFD/<br>以太网通信、路由（**以太网无功能部署**） |
| **EEA 3.0** | 中央计算+区域控制 | 中央网关+区域网关<br>（CCU、L-ZCU，R-ZCU，B-ZCU） | 多网段LIN/CAN/CANFD/<br>以太网通信、路由（**以太网仅部署车身控制****等****低实时性要求功能**） |
| **EEA 4.0**<br>（未来） | 中央计算+区域控制 | 中央网关+区域网关<br>（CCU、L-ZCU，R-ZCU，B-ZCU） | 多网段LIN/CAN/CANFD/<br>以太网通信、路由（**未来部署底盘/动力/高实时性要求功能**） |

#### 当前状态感知

| 类型 | CAN-ETH转发数据状态描述 | 示意 |
| --- | --- | --- |
| 当前现状 | - 当前EEA 3.0架构中ETH部署车身电子控制及车辆状态信息上报功能，并无标准报文CAN-ETH路由转换协议。<br>- 当前所有CAN-ETH数据均上行到ASW，链路单一，数据转发不能分级部署，时效性欠佳及资源消耗较高； | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/dda2dd42-9a63-4916-a604-3bef94f34525.png) |
| 理想状态 | 未来ETH将部署多种不同实时性要求功能数据类型。基于不同类型数据转发要求，构建多级数据转发路径方案；<br>- 基于功能业务类型数据：采用通道①<br>- 基于报文转发类型数据：采用通道②<br>- 基于高时效转发类型数据：采用通道③ | ![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/6d6b3eaf-e76e-44e2-8f19-044b3b5b83d5.png) |

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/dda2dd42-9a63-4916-a604-3bef94f34525.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/6d6b3eaf-e76e-44e2-8f19-044b3b5b83d5.png)

### 技术机会点

> 💡 车载网络中**ETH变为主干网**成为必然趋势，车载高实时性功能逐步在ETH部署，优化“中央计算+区域控制”架构下的网关时延与吞吐量，提升架构灵活性。据此识别出以下三个机会点：

> 1. **CAN-ETH双向转换协议****：**制定双向转换协议解决我司此领域空白，构建多级数据转发路径方案；
> 2. **路由转换动态切换策略****：**考虑高实时性业务功能通信鲁棒性，在单链路出现故障时保证通信；
> 3. **ZCU驱动能力原子服务功能****：**支撑业务上移和整车业务灵活部署；

## 价值阐述

> 由技术洞察导出技术机会点，论述技术机会点的价值
> 必要性：从无到有
> 竞争力/技术领先性/效率提升: 从有到优（比如：成本、效率、质量、能力）

| 序号  | **技术创新点**      | **价值描述**                                                                                     |
| --- | -------------- | -------------------------------------------------------------------------------------------- |
| 1   | CAN-ETH双向转换协议  | - 解决CAN-ETH双向转换协议从无到有的问题；<br>- 建立高标准化，高可靠，低延迟的CAN—ETH互转协议，满足智驾、车控等业务对通信性能的严苛需求，保证智驾表现与安全性能。  |
| 2   | 路由转换动态切换策略     | - 解决以太网通讯的可靠性与实时性问题；<br>- 满足智能驾驶、车控等业务对高可靠性通信的需求，在单链路出现故障时保证通信。                              |
| 3   | ZCU驱动能力原子服务功能  | - 将ZCU驱动能力虚拟化为服务功能，向上提供服务接口，支撑CCU与ZCU功能架构分层解耦、独立迭代；<br>- 支撑业务上移和整车业务灵活部署，降低ZCU硬件成本与车型适配开发成本； |
| 4   | ZCU网关性能验证      | - 建立ZCU网关的多维度性能基线：量化时延、吞吐量、故障恢复时间等关键指标；<br>- 通过极限测试明确ZCU芯片的网关性能边界，指导芯片选型。                    |
| 5   | ZCU至CCU端到端性能验证 | - 量化全链路性能基线：量化时延、抖动、吞吐量、优先级、带宽利用率等关键指标；<br>- 识别端到端通信的性能瓶颈，量化动态路由策略收益。                        |



# 解题思路（关键技术点和验证点）

> 基于技术洞察识别到行业问题进而导出研究的机会点，**对机会点进一步分析解题思路**
> 从第一性原理出发，阐述解决问题的**创新方法/思路方向**
> 说明**开发模式**，如联合开发（高校合作等）、自研自制、委外等

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/0f6db9c2-afdd-46ab-967e-42fd3d48f6b3.png)

## CAN（LIN）-ETH双向转换协议设计

> 👉 关键技术点1：CAN(LIN)-ETH-CAN(LIN)，CAN(LIN)-ETH双向转换协议设计
> 牵头人：> @潘欢
> 负责人：> @刘兴涛> @张敏> @库海鹏

### 方案概述

为适配集中高性能计算和分布式通信的软件框架，骨干ETH网和分布式CAN网络的互联互通，制定高效的协议转换标准，最大化降低协议转换时间，减少通信时延，增强通信确定性，满足CAN-ETH-CAN, CAN-ETH各场景下的功能和性能要求。

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/db42a374-241c-41d4-855b-c3632fe58950.png)

### 关键指标

**协议设计**

1. **路由转发时间**
1）协议对延迟性能要求的支撑和优化，单条报文（以以太网帧计，长度小于512字节）处理时间小于30us；
     2）支持多条业务基于优先级的调度策略，支撑触发式报文时延小于1ms；

2. **路由转发资源：**
     1）当CPU占用率小于5%，内存占用率小于5%时，支持容量大于等于100条CAN frames/100ms

3. **路由转发功能：**
     1）支持报文一对多协议转换冗余



**转发策略**

1. 转发策略

### 方案框架设计

协议设计框架

_1）__协议对确定性及安全性的支撑和优化_

2）针对不同的功能场景和性能要求，制定灵活的转换协议及交互机制。

3）CAN-ETH-CAN 利用精简协议定义，达到快速转发的目的。跳过复杂的TCP/IP协议栈，直接基于以太网底层协议的路由，减少封装/解封装时间。同时利用TSN协议及数据优先级队列机制，保障高优先级、低延时的CAN报文能够得到确定性转发。

4）CAN-ETH复用MVBS-DDS协议的特性，承担服务网关的功能。将CAN信号转化为DDS服务进行发布，并将以太网DDS服务的请求和状态转化为CAN报文进行发送。

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/55fca6f5-bcd6-4173-94f5-83451738e19e.png)


| 目的MAC（6字节） | 源MAC（6字节） | TPID（16b）0x8100 | 优先级PRI（3b） | CFI（1b） | VLAN ID（12b） | Type（16b）0x0801 | IP数据报（46~1500字节） | FCS（4字节） |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |


| 版本(4)IPV4:0100 | 首部长度（4） | 服务类型（8） | 总长度（16） |  |
| --- | --- | --- | --- | --- |
| 标志字段（16） |  |  | 标志位字段（3） | 段偏移（13） |
| 生存期TTL（8） |  | 协议（8）UDP | 首部校验和（16） |  |
| 源IP地址（32） |  |  |  |  |
| 目的IP地址（32） |  |  |  |  |
| 源端口（16） |  |  | 目的端口（16） |  |
| 长度（16） |  |  | 校验和（16） |  |
| PduHeader ID（32） |  |  |  |  |
| Length（32） |  |  |  |  |
| PayLoad |  |  |  |  |
| PduHeader ID（32） |  |  |  |  |
| Length（32） |  |  |  |  |
| PayLoad |  |  |  |  |
| ... |  |  |  |  |
针对ETH 驱动buffer 

### 验证方案（可选）

> 采用何种方式验证前述的关键指标。包含测试环境、测试流程等

### 交付物

协议设计规范、测试报告



## 路由转换动态切换策略

> 👉 关键技术点2：路由转换动态切换策略基于负载、工况选择不同的路由策略
> 牵头人：> @贾若
> 负责人：> @库海鹏> @张敏> @刘兴涛> @张八旺

### 方案概述

> 技术概述，简要解释该技术点

动态路由策略可以使网关具备优先级调度、冗余切换等功能，提高通讯实时性与可靠性。

冗余切换指的是支持ETH与CAN双通道热备份，当原配置的路由路径出现问题时，可以检测到故障并通过修改路由表保证原有报文可以正确路由到目标网段，比如：

原路由路径：BMS->CAN1->RZCU->ETH->CCU

切换路由：BMS->CAN1->RZCU->CAN->CCU或者BMS->CAN1->RZCU->CAN->LZCU->ETH->CCU

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/53da196d-e120-41ac-88c8-83d14440b6a3.png)
优先级调度指的是路由报文的优先级可以根据运行场景动态更新优先级，比如在发生故障时，临时提升log报文路由的优先级保证云端日志的

### 关键指标

> 可被验证的性能指标，需包含关键指标的导出过程

- 路由表初始化构建时间：＜200ms（＜CCU启动时间）
- 路由表动态更新响应延迟： 确认故障后小于5ms（确认故障-＞切换成功）
- 非法ID拦截成功率100%

### 方案框架设计

> 将技术点进一步分解，以展示该技术点的设计方案框架。

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/bb933d5a-39bf-464f-b14e-2ac370175f69.png)
1. **初始化与路由表构建**
  a. 广播发现（可行性待进一步确定）
     控制器启动后，向连接的CAN/CANFD网络广播请求报文，触发各ECU节点应答信息，各ECU节点应答报文应包含以下字段：

CAN节点应答示例：  ID=0x7E0, Data=0x03 62 F1 00 [发送报文ID] [接收报文ID]  

  b. 应答处理与初始路由表构建
     通过校验并提取节点发送的报文ID（发送/接收）信息，生成初始路由表，并支持后续动态更新。

2. **动态路由表优化**
     网络监测：实时监控网络节点状态（如新增ECU、节点离线）、通信负载及延迟情况

路由表优化：

  * 若检测到某网段负载超过阈值（如ETH总线负载率>70%），触发负载均衡算法，将部分报文分流至低负载通道
  * 针对不同驾驶场景的实际功能运行状态，为不同业务分配优先级路由路径，确保低延迟传输
  * 新增或删除ECU节点后，主动发现节点并更新到路由表
  * 当原配置的路由路径出现问题时，可以检测到故障并通过修改路由表保证原有报文可以正确路由到目标网段
     安全防护：

  * 非法节点拦截：检测未经验证的报文ID（如ID=0x7E0~0x7EF为诊断保留范围），自动屏蔽并记录日志
  * 网络攻击响应：若检测到异常流量（如每秒>1000次诊断请求），冻结对应网段并启用冗余路由通道


### 验证方案（可选）

> 采用何种方式验证前述的关键指标。包含测试环境、测试流程等



### 交付物

> 如：设计报告、测试报告、开发工具、软件模块等



![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/7f9d5707-22c1-46f5-8e5e-48513e92b399.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/1189cb4a-a018-4fa7-8fdb-93397bc43e11.png)
![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/00f98eb0-f69e-4db4-b7d4-18be0ab03008.png)
静态代码

- 指针访问常量和变量
- 变量显性赋值
常量数据

- 固定首地址
变量数据

- 变量空间预分配


## ZCU驱动能力原子服务功能

> 👉 关键技术点3：ZCU硬件抽象向上提供服务，支撑业务上移
> 牵头人：> @张敏
> 负责人：> @田子豪

### 方案概述

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/e7914378-a29f-4095-8dfc-fa028cab101d.png)
驱动服务主要是在分布式骨干以太网架构下，将ZCU驱动功能通过定义良好的设备抽象接口，封装为可复用的远程调用服务，支持跨平台交互。

原子服务是指提供的驱动服务是独立的、自治的最小功能单元，遵循单一职责原则，确保高内聚、低耦合。

### 关键指标

> 可被验证的性能指标，需包含关键指标的导出过程

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/769ff5d9-1b28-4f94-ac0a-b709cce6c0ad.png)
部署ZBP2.2驱动能力到CCU上后，关注：

1. 执行器类驱动：请求响应的延时（F/F - Fire/Forget）小于1ms
2. 传感器类/状态上报/故障类驱动：1ms/10ms类更新频率（Cyclic）抖动±20%
3. ZBP2.2驱动能力服务CPU负载占用小于15%
4. ZBP2.2驱动能力服务RAM占用小于15%

### 方案框架设计

> 将技术点进一步分解，以展示该技术点的设计方案框架。

1. 真实驱动在zcu接入
2. 设备抽象server-》zcu mvbs-》eth-》ccu mvbs
3. ccu上部署设备抽象client，并向上提供RTE接口，供应用层像本地一样无感调用

### 验证方案（可选）

> 采用何种方式验证前述的关键指标。包含测试环境、测试流程等

关键指标：驱动原子服务方案实时性及传输延迟应至少与原有方案保持一致（通过tester记录的相对延迟时间对比，即T1/T1（原方案）与T3/T4（现方案））

**测试环境：**

| 设备名称 | 用途 |
| --- | --- |
| 主控MCU节点（CCU） | 用于发起调用远端服务运行，驱动、数据采集、故障诊断 |
| 驱动MCU节点（BZCU） | 用于响应远端服务运行，驱动、数据采集、故障诊断 |
| Tester节点（VN5640） | 用于记录主控及驱动节点信息，计算端到端执行延迟 |

**测试流程：**

单服务功能测试：

输入：在CCU环境中模拟Topic数据发起对驱动输出、数据采集、故障诊断逻辑服务请求。

输出：BZCU上及时响应服务，负载可通过示波器测量电磁阀驱动信号是否符合预期，并可观测相关数据。

性能：Tester抓包分析DDS Topic的端到端延迟和丢包率（对比T1/T2/T3/T4）

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/ec00f864-143d-4827-9bf8-7e2391ad7bb2.png)

### 交付物

> 如：设计报告、测试报告、开发工具、软件模块等

设计报告、测试报告、BZCU（驱动server）软件、LZCU（驱动client）软件

## ZCU网关性能验证

> 👉 关键验证点1：分布式网关ZCU 在不同网络负载情况下，CPU负载率资源消耗/
> CANFD-ETH，ETH-CANFD，多场景下的验证
> 牵头人：> @张敏
> 负责人：> @张八旺> @张伟> @潘欢> @库海鹏

### 方案概述

> 技术概述，简要解释该技术点

为适配集中高性能计算和分布式通信的软件框架，需要骨干ETH网的通信，仍然满足集中式网关CAN通信的性能要求。

- 对于触发式/报文周期＜10ms报文的CAN2UDP路由，ZCU会将立即发送。
- 对于报文周期≥10ms报文的CAN2UDP路由，ZCU会将报文缓存，超时1ms发送或缓存>640字节时发送。
- UDP2CAN报文在中断中直接路由

### 关键指标

> 可被验证的性能指标，需包含关键指标的导出过程

1. 延时/抖动：
  * 触发式报文：小于1ms
  * 报文周期<20ms：小于±20%
  * 报文周期≥20ms：小于±10%
2. 时序：0乱序
3. 转发丢包率：0%
4. CPU负载：3路CANFD，50%总线平均负载，20%CPU占用

### 方案框架设计

> 将技术点进一步分解，以展示该技术点的设计方案框架。

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/8ded6abe-f40e-4728-84a4-799d59b5057f.png)
1. PduHeader=CanBusId+CanId
2. 触发式/报文周期<10ms报文的CAN2UDP路由，属性设置为TRGGER_ALWAYS
3. 报文周期≥10ms报文的CAN2UDP路由，属性设置为TRGGER_NEVER，SoAdTxUdpTriggerTimeout = 1ms
4. _为了方便验证报文时序，将所有报文的Byte0修改为RollingCounter_

### 验证方案（可选）

> 采用何种方式验证前述的关键指标。包含测试环境、测试流程等

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/d2d3a384-0eb6-4491-a0b8-946cef28ad2f.png)
| **报文节点** | **报文周期（ms）** | **报文数量** | **报文DLC** |
| --- | --- | --- | --- |
| CAN1 | 10 | 5 | 64 |
| CAN2 | 10 | 5 | 64 |
| CAN3 | 10 | 5 | 64 |
| CAN1 | 100 | 10 | 64 |
| CAN2 | 100 | 10 | 64 |
| CAN3 | 100 | 10 | 64 |
| CAN1 | 200 | 10 | 64 |
| CAN2 | 200 | 10 | 64 |
| CAN3 | 200 | 10 | 64 |
| CAN1 | 1000 | 20 | 64 |
| CAN2 | 1000 | 20 | 64 |
| CAN3 | 1000 | 20 | 64 |

路由表规格暂定如上，可根据实际总线负载调整，测试can-eth-can端到端的转发延时，目标触发式报文/1ms周期报文/5ms周期报文满足1ms内路由延时，≥10ms满足2ms内路由延时。

### 交付物

> 如：设计报告、测试报告、开发工具、软件模块等

设计报告、测试报告、BZCU软件、LZCU路由

## ZCU至CCU端到端性能验证

> 👉 关键验证点2：ZCU到CCU，负载、时延、抖动验证
> 牵头人：> @刘兴涛
> 负责人：> @张敏> @库海鹏> @张八旺

### 方案概述

> 技术概述，简要解释该技术点
> 随着多域向中心节点融合后，一些原先布局在各ECU的业务可能会上移到中心节点，这样不仅可以充分利用中心节点高算力、高带宽、端云互联，还能够简化整车架构拓扑，提高产品开发效率。但是从CCU到ECU是一个长长的链路，不仅要跨多个系统（Linux、autosar等），还要跨不同的通信协议（以太网、can、Lin等），要想实现CCU到ECU的端到端实时性通信，通信链路上每一个点都要做最优的设计和极致的优化。

### 关键指标

> 可被验证的性能指标，需包含关键指标的导出过程

1. 单业务端到端（A核<-->ECU、ECU<-->ECU）之间转发延时<1ms，抖动±10%
2. 多业务混合端到端（A核<-->ECU、ECU<-->ECU）之间，高优先级业务转发延时<1ms，抖动±10%，低优先级业务转发延时<2ms，抖动±10%
3. 高负载背景流下，端到端（A核<-->ECU、ECU<-->ECU）之间，高优先级业务转发延时<1ms，抖动±10%

### 方案框架设计

> 将技术点进一步分解，以展示该技术点的设计方案框架。



![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/491c5898-adef-42f5-aefa-2ac07d10dcaf.png)
验证CCU到ECU、ECU到ECU之间通信延迟和抖动。

### 验证方案（可选）

> 采用何种方式验证前述的关键指标。包含测试环境、测试流程等

[分布式网关-ZCU至CCU端到端性能验证方案](https://li.feishu.cn/docx/C2uEdNLlZovH6Tx8P3ZcEHfdnNb)

### 交付物

> 如：设计报告、测试报告、开发工具、软件模块等

详细的测试报告、测试工具。



---
**一、如何将路由延迟降到最低？**

1. **硬件层优化**

**专用通信加速芯片**：
采用集成CAN-Ethernet协议转换的硬件模块（如NXP S32G芯片），通过硬件加速引擎直接解析和封装数据帧，减少CPU干预，实现微秒级延迟。

2. **协议层优化**

**精简协议栈**：
使用定制化协议（如车载SOME/IP协议），去除冗余的IP层头部信息，直接基于MAC层路由，减少封装/解封装时间。

**时间敏感网络（TSN）**：
通过IEEE 802.1Qbv标准预留时隙，确保关键数据（如刹车信号）的确定性传输，避免排队延迟。

3. **软件层优化**

**零拷贝数据传输**：
利用DMA技术直接传输数据，避免内存复制开销4。

**优先级调度与流量整形**：
实施QoS策略，优先处理高优先级数据包（如自动驾驶传感器数据），限制低优先级流量（如OTA更新）。

---
**二、如何实现动态路由？**

1. **路由决策机制**

**集中式控制（SDN架构）**：
中央计算单元作为控制平面，全局监控网络状态（如链路负载、节点健康度），动态下发路由策略。例如，特斯拉HW4.0通过中央网关集成SDN控制器，实时调整Zonal间通信路径。

**分布式决策（服务发现协议）**：
采用AUTOSAR Adaptive中的SOME/IP服务发现机制，自动注册和更新服务实例，动态绑定请求与响应路径。

---
**三、如何利用AI模型推理驱动路由策略优化？**：
在中央计算单元部署AI推理引擎，实时分析网络状态并下发优化策略。

---
**四、典型案例与未来趋势**

**AI与TSN深度融合**：结合时间敏感网络与AI预测，实现纳秒级延迟的确定性通信。

**Chiplet技术普及**：通过异构计算芯片（如CPU+NPU+FPGA）提升路由计算效率。



控制器算力区域中心化与集中化，ZCU趋向于执行功能





# 目标与计划

## 项目目标

### 交付物

1. 设计报告
  a. 协议设计规范
  b. 路由转换动态切换策略设计报告
  c. ZCU驱动能力原子服务设计报告
2. 测试报告
  a. 转换协议测试报告
  b. ZCU网关性能测试报告
  c. ZCU至CCU端到端性能测试报告
3. 软件
  a. 路由转换动态切换软件
  b. ZCU驱动能力原子服务（含基于BZCU的Server软件和基于LZCU的Client软件）
  c. 测试用软件(含BZCU和LZCU)

### 关键技术指标

1. 协议转换对单条报文（以以太网帧计，长度小于512字节）处理时间小于30us；
2. 协议转换在占用CPU小于5%，内存小于5%时，支持容量大于等于100 CAN Frames/100ms；
3. 协议转换支持多条业务基于优先级的调度策略，多业务混合ECU(CAN) <--> ECU(CAN)之间时延/抖动：
  a. 触发式报文：小于1ms
  b. 报文周期<20ms：小于±20%
  c. 报文周期≥20ms：小于±10%
4. 单业务端到端（A核<-->ECU、ECU<-->ECU）之间转发延时小于1ms，抖动±10%
5. 多业务混合端到端（A核<-->ECU、ECU<-->ECU）之间时延/抖动：
  a. 高优先级业务转发延时小于1ms，抖动±10%
  b. 低优先级业务转发延时小于2ms，抖动±10%
6. 动态路由表更新响应延迟： 确认故障后小于5ms（确认故障-＞切换成功）
7. ZCU驱动原子服务时延/抖动
  a. 执行器类驱动：请求响应的时延（Fire/Forget）小于1ms
  b. 传感器类/状态上报/故障类驱动：1ms/10ms类更新频率（Cyclic）抖动小于±20%
8. ZBP2.2驱动能力服务CPU负载占用小于15%，RAM占用小于15%
---


## 项目计划

> 本页需要展示项目一级计划，遵循> [IPD-2.28.3-PS-0001 RD项目节点评审管理办法](https://li.feishu.cn/docx/IAMsdp2dioM9TZxEjbccMmrrnWe)
> 产研科技树项目里程碑计划参照 > [【科技树项目】运营方案-下发版](https://li.feishu.cn/docx/CxTHdR6yWoWjDOx7wlAcdR9WnQh?source_type=message&from=message)
> 如有锚定的目标迁移产品/平台，计划中体现迁移的对象，具体见管理办法中RD/PD互锁迁移章节

![](https://cfe-doc-backend.inner.chj.cloud/api/v1/analysis/file?file_key=feishu-service/1b614c52-78ba-4929-a27d-01996cbe59a5.png)


## 项目预算（包含在总TDT中）

> 建议由**财务BP/项目财经代表（系研财务BP **> @郭婷**；****产研财务BP **> @许舸航> @沈彤**）**协助业务填写。
> 1. 资源预估的维度可以根据自身业务测算维度进行分类预估，例如：根据研发单元、开发模块等；
> 2. 专职投入本产品开发的研发资源，按100%工作量估算；兼职投入人员按照投入占比估算。
> 3. 人力和算力资源如需新增（超出预算包范围），需说明
> 4. ROI 计算（产研不可裁剪；系研和AI-RD按需）
> 算力申请可咨询智能云财务bp > @郭婷

> ✅ 预算结构：
> - 全生命周期预算：xx元

  * 人力费用：xx元（11人），无HC新增
  * 业务费用：材料费用xx元、数据费用xx元等
> - 申请CDCP或PDCP前释放预算：xx元

  * 人力费用：xx元（xx人），有/无HC新增
  * 业务费用：材料费用xx元、数据费用xx元等

### 项目预算汇总

| 费用类别 | 条目 | 预算费用(万元) | 备注 |
| --- | --- | --- | --- |
| 人力费用 | 项目涉及各领域的人员费用 |  | 合计：28人月 预算工时：依据项目定义评估各专业工时投入，不能直接使用标准工时 预算费用：财务依据预算工时输出 人员费用/人月的基线：请与对应部门财务获取，然后*总人月，得出总费用； 涉及工业研究院和海外单列 |
|  | 外协人员费用 |  |  |
| 材料费用 | 耗材（样机/样板/手板） |  | AD Pro *2 M100 *2 RZCU *2 |
|  | 实验材料（仪器/开发工具） |  |  |
|  | 其他（如有，请详细列明，如模具费用） |  |  |
| 算力费用 | 推理算力 |  |  |
|  | 训练算力 |  |  |
| 数据费用 | 数据类型 数据场景 |  |  |
| 认证&测试 | 外发认证 |  |  |
|  | 外发试验 |  |  |
| 专利费用 | 专利费用 |  |  |
| 对外合作 | 技术合作，技术转让等费用 |  |  |
| 预算总额 |  |  | 如果投入不足或超预算，请说明 |

## 风险评估及策略

> ✅ 列举影响项目指标达成，产品成功的关键项目风险、明确严重程度，并给出初步对策和风险应对责任人
> 涉及知识产权、专利保护，需要**法务代表**提供风险排查和出具意见

| 风险类型 | 风险描述 | 风险评估(高/中/低) |  |  | 影响描述 | 风险应对 | 责任人 | 资源需求 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  |  | 发生概率 | 影响程度 | 风险等级 |  |  |  |  |
| 关键技术实现 |  |  |  |  |  |  |  |  |
| 关键技术实现 |  |  |  |  |  |  |  |  |
| 关键技术实现 |  |  |  |  |  |  |  |  |
注：风险等级的设置参见[风险等级说明](https://li.feishu.cn/docx/SIaXddZSGohoxxxj6iGcBYqrndM#doxcnwTLwqCwbhG467kzO4LxRnh)



# 决策申请

> ✅ **主要决策点：**
> - 是否认同技术价值（技术指标、技术创新点）
> - 是否同意项目里程碑和预算

## 至下一DCP节点前释放预算

> 费用类别、条目可实际情况自行增加选项
> 产研科技树申请释放项目全生命周期预算，详见

| 费用类别 | 条目 | 总费用（千元） | 预算属性 | 备注 |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| 本次申请费用 | / |  | / |  |
| 项目总预算 | / |  | / |  |

## TDT团队任命

> **团队成员按需指定，TDT组织运作机制：**> [TDT组织建设与运作机制](https://li.feishu.cn/docx/Oky0dtgeno0mMFxFEDAcwnndn8c)

| **TDT团队** |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **角色** | **工号** | **姓名** | **部门**<br>请具体到二级部门<br>示例：智能云-大数据平台 | **级别**<br>请填写人级 | **过往履历**<br>请说明时间段与对应岗位/学历、院校与专业，并涵盖以下内容：<br>理想汽车工作经历：xxx<br>过往经历<br>工作经历：xxx<br>学业信息：xxx | **备注说明** | **组别** |
| TDT经理 |  |  |  |  |  |  | 核心组 |
| 研发代表 |  |  |  |  |  |  | 核心组 |
| 系统工程师 |  |  |  |  |  |  | 拓展组 |
| 产品代表 |  |  |  |  |  |  | 核心组 |
| 供应代表 |  |  |  |  |  |  | 核心组 |
| 财经代表 |  |  |  |  |  |  | 核心组 |
| 数据代表 |  |  |  |  |  |  | 按需 |
| 硬件代表 |  |  |  |  |  |  | 按需 |
| 软件代表 |  |  |  |  |  |  | 按需 |
| 测试代表 |  |  |  |  |  |  | 按需 |
| 质量代表 |  |  |  |  |  |  | 核心组 |

## 决策意见

> ✅ 1. 评审委员逐一给出评审意见：通过/不通过，及对应原因/要求
> 2. 委员会主任最后给出意见
> 3. 50%人同意立项，即通过；主任有一票否决权

| 评委 | 评审意见 | 备注 |
| --- | --- | --- |








 



