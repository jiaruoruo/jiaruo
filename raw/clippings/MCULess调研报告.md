# MCULess调研报告

# 一、MCU-less 概述

MCU-less（无MCU节点）是一种新兴的电子架构理念，其核心思想是将外围终端（传感器/执行器）设备中的微控制器（MCU）剔除，直接通过硬件接口将其连接到中央或区域控制器，实现“计算中心化、外围简化”的控制模式。该方案可显著减少MCU数量、降低软件复杂性、提高OTA效率、压缩系统成本，并提升整体E/E架构的灵活性与可靠性。

---

# 二、半导体厂商 MCU-less 方案调研

> :unicorn_face: 1. 当前只有ADI/TI有通用MCU-less芯片量产，但IO数量很少，价格较高
> 2. LED驱动领域 ST/Infineon 都有量产芯片
> 3. 国外/国内 各芯片厂都在和OEM一起探讨&布局 MCU-less方案

| 厂商 | 代表方案 / 器件 | 价格 | 有效IO数量 | IO功能配置 | 通讯方式 | Roadmap |
| --- | --- | --- | --- | --- | --- | --- |
| ADI | AD3300/3301/3304/3305（E²B收发器） | 1.3美金 | 12路 | SPI/I²C/UART/PWM/GPIO/LIN | 10BASE-T1S（集成MAC/PHY，支持E²B协议） | 28年计划量产40路IO的产品 |
| TI | PTCAN5102DGQRQ1 https://www.ti.com/lit/ds/symlink/tcan5102-q1.pdf?ts=1761521900716 | 0.487美金 | 13路 | SPI/I²C/PWM/UART/IO 没有ADC | CAN FD Light、10BASE-T1S | 2025年Q3，20路IO的CANFD-Light的产品 2026年Q4, 32路IO的CANFD-Light的产品 |
| NXP | - | - | - | - | - | 还在设计规划 |
| ST | L99LDLH32/L99LDLL16（LED驱动器） |  | 32路LED | 可编程PWM/电流DAC控制 | CAN FD Light（集成收发器+协议控制器） | 2028年计划量产96路（仍是LED驱动） |
| Infineon | TLD7002-16ES（LED驱动器） |  | 16路LED | 可编程PWM/电流DAC控制 | CAN FD Light（主推），10BASE-T1S（研究中） | 2025年前发布首代产品 |
| 汇顶科技 | GE1101 | 预计14RMB | 64 | SPI/I²C/UART/PWM/GPIO/LIN/CAN/TDM | 100BaseT1, 环网/菊花链式组网 | - |
※ SCU MCU S32K144, 14RMB左右

1. **Analog Devices (ADI)** – E²B（Ethernet to Edge Bus）
- **核心芯片系列**：AD3300/3301/3304/3305（E²B 收发器），AD3301价格1.3美金
- **有效IO个数**：12路 SAIF（Sensor/Actuator Interface），支持 SPI/I²C/UART/PWM/GPIO/LIN 等多种配置。
- **通讯方式**：10BASE-T1S（10M以太网），集成MAC/PHY并使用E²B低复杂度协议栈。
- **Roadmap（至2030年）**：
  * 2024年发布首批E²B芯片，支持BMW灯光系统量产；
  * 预计2028年推出40路有效IO的产品
---
2. **Texas Instruments (TI) **– MCU-less 通信PHY架构
- **代表方案**：SPI传感器 + 集成PHY（CAN或10BASE-T1S），实现通信协议硬件桥接。
- **有效IO个数/配置**：未发布具体器件，方案支持SPI/I²C/模拟等传感器输入。
- **通讯方式**：CAN FD Light、10BASE-T1S（以太网MACPHY）
- **Roadmap**：
  * 2025年前推出初步样片（预计20路有效IO，CANFD），26年推出32路有效IO，10BaseT1S的芯片；


---
3. **NXP** – 智能LIN/CAN驱动器方案
- **代表器件**：SJA1124（LIN桥接）、即将推出的多通道LED/CAN驱动器。
- **有效IO个数**：多通道输出（如16/24路LED），具备独立PWM、电流调节能力。
- **通讯方式**：LIN（SPI桥接），CAN FD Light（在研）、10BASE-T1S（TJA1410）
- **Roadmap**：
  * 2024–2025年：推出基于CAN FD Light的LED/电机驱动器；


---
4. **STMicroelectronics (ST) **– CAN FD Light LED驱动器
- **代表器件**：L99LDLH32（32通道LED驱动器）
- **有效IO个数**：32路LED输出，每通道电流1–15mA，可编程PWM；另有L99LDLL16（16通道）
- **通讯方式**：CAN FD Light（集成协议处理器 + 收发器）
- **Roadmap**：
  * 2022年发布首款CAN FD Light驱动器，现已支持量产；
  * 预计2028年推出96路有效IO的产品
---
5. **Infineon** – 融合型功率驱动与通信接口（待发布）
- **潜在方向**：
  * LITIX™ LED驱动系列升级集成CAN FD Light接口；
  * MOTIX™ 电机驱动集成CAN FD Light，实现门窗/座椅等控制器MCU-less化。
- **通讯方式**：CAN FD Light（主推），预研10BASE-T1S。
- **Roadmap**：
  * 2025年前推出第一代LED驱动产品（含通信接口）；
6. **汇顶科技**
- **有效IO个数**：64路 ，支持 SPI/I²C/UART/PWM/GPIO/LIN/CAN 等多种配置。
- **通讯方式**：100BaseT1，环网/菊花链式组网
- **Roadmap**：
  * 计划26年Q2量产
---

# 三、MCU-less 在汽车中的应用场景

1. 区域控制器场景：小MCU + MCU-less组合
  * 小MCU承载如防夹控制等快速闭环逻辑；
  * MCU-less设备执行锁驱动、照明控制、电机控制等中低速任务。
- **收益**：
  * 将区域控制器中软件向CCU中集中，减少区域控制器软件模块数量，实现降本提效
    + 软件上移到成本更低的SoC当中，降低区域控制器中MCU的规格，从而实现降低成本；
    + 减少区域控制器中逻辑控制功能，降低区域控制器需要OTA的必要性，提高OTA效率和成功率
    + 减少区域控制器中逻辑控制功能，实现软件&硬件解耦，提高功能迭代效率


---
2. 终端执行控制器场景：完全MCU-less化
- **可能的应用案例**：
  * 车灯系统：使用ST/NXP的MCU-less驱动器，中央控制器直接发送灯光动画命令，灯具本地无MCU；
  * 电动座椅：中央控制器通过CAN FD Light控制多个集成电机驱动的终端，无需座椅ECU MCU；
  * 传感器网络：温度/压力传感器经硬件桥接直接上报中央ECU，无需本地ADC+MCU。
- **收益**：
  * 彻底取消本地MCU，简化OTA路径与软件维护；
  * 降低硬件成本与复杂度；
  * 提高整车一致性，便于功能集中调优。
---

# 四、成本结构对比：MCU-less vs. MCU方案

| 成本项目 | MCU方案 | MCU-less方案 | 优势分析 |
| --- | --- | --- | --- |
| 芯片 | MCU + Transceiver | 单芯片集成 | 更高集成度，减少PCB面积 |
| Flash/SRAM存储 | MCU需内置Flash（代码）+ SRAM（缓存） | 无需存储，逻辑由中央ECU处理 | 芯片面积更小，成本更低 |


---

# 五、结语

> 🏝 - MCU-less 有利于 实现软硬件解耦，实现整车软件集中化，从而实现降本（MCU成本）增效（功能迭代，OTA）
> - 当前MCU-less芯片还处于起步阶段

  * MCU-less芯片IO数量比较少，不符合区域控制器的应用需求
  * MCU-less单芯片价格比较高，和同等IO数量MCU相比 还没有成本优势


