# MCU-LESS技术

# MCU-LESS技术行业现状

|  | RCP（10Base-T1S） |  | GPAN |
| --- | --- | --- | --- |
| 原理 |  |  |  |
| 带宽 | 10M |  | 100M |
| 通讯方式 | 1. 基于IEEE802.3cg<br>2. 物理层特性<br> * 采用单对双绞线（SPE）实现10Mbps半双工通信，支持最长25米传输距离<br> * 支持多点拓扑（Multidrop）结构，无需交换机即可连接至少8个节点<br> * Pt-Pt下支持全双工，最长距离15米<br>3. 冲突避免机制（PLCA），通过物理层冲突避免（PLCA）技术实现确定性传输：<br> * 由Node ID=0的协调器周期性发送信标（BEACON）启动传输周期；<br> * 每个节点按Node ID顺序获得传输机会（TO），在固定时间窗口内发送数据；<br> * 若节点无数据发送，则自动跳过当前机会，避免总线空闲<br>4. 支持TSN 802.1AS/IEEE1588 |  | 1. 物理层<br> a. 单对双绞线，同当前百兆以太线束要求<br> b. 支持百兆全双工<br>2. 协议层<br> a. 支持PTP协议，**精度约80ns**<br> b. 自定义通讯机制<br> c. 支持数据报快速交换和转发，**转发时延约1.4us** |
| 休眠唤醒 | OPEN Alliance TC10/TC14 Version V1.0 |  | 协议：自定义格式，也可支持TC10睡眠 |
| 供应商 | ADI | NXP | 汇顶 |
| 芯片资源 | 1. AD3306 MACPHY：[https://www.analog.com/media/en/technical-documentation/data-sheets/ad3306.pdf](https://www.analog.com/media/en/technical-documentation/data-sheets/ad3306.pdf)<br> a. 24-pin LFCSP 4mm x 4mm<br> b. ASIL-QM compliant<br> c. VBAT Connectivity (5V - 48V)<br>2. AD3301/4/5：[AD3300_1_4_5_DS_RevSpB.pdf](https://li.feishu.cn/file/X8rZbh3QSorHs9x87OZcffwInBB)<br> a. SPI, I2C, PWM, GPIO, LIN, UART, ILAS/ISELED<br> b. FlexibleIO (e.g. Additional UART, SPI interface)<br> c. 24-pin LFCSP 4mm x 4mm<br> d. ASIL-QM compliant<br> e. VBAT Connectivity (5V - 48V) | 1. TJA1415<br> a. 支持IEEE1722 传输协议<br> b. ASIL B<br> c. 接口：ILas，SPI，UART，PWM，LIN，I2C，GPIO，ADC | 1. GE1101 |
| 供应商推荐应用场景 | 1. External Lights (Headlamps/Rear/Grill)<br>2. BMS<br>3. Internal/Ambient Lighting<br>4. Door ECU<br>5. Zonal ECU<br>6. Suspension<br>7. Inverter<br>8. Steering<br>9. Brakes<br>10. Displays<br>11. Power Distribution<br>12. RADAR (short range/internal or synchronization)<br>13. Seat ECU<br>14. Keyless Entry<br>15. LIDAR<br>16. Ultrasonic Sensors<br>17. OBC<br>18. IMU |  | 区域控制器<br>门模块<br>座椅模块等 |
| 总结 | 1. 底层通信基于10M Base-T1S，调度型通信方式，最小调度周期1ms，可用带宽有限，可以应用于实时性和数据量要求同CAN/CANFD通信的场景<br>2. 已有芯片Pin数量较少（大部分都是20~40Pin），IO太少应用范围有限<br>3. ADI、NXP、TI、ON等国外公司下一代产品暂未规划 |  | 1. 底层通信基于100M以太，通信协议类似于EtherCat，可全双工通信，通信时延小，可用于较大数据量的高实时性通信，缺点：通信协议为私有协议，现有软件可工具链基本不能支持；<br>2. 已有48Pin原型芯片，27年规划48/144/196Pin芯片，外设接口类型丰富，可应用场景较多<br>3. 国内仅汇顶科技一家研究，资源单一，注意供应风险 |

# MCU-LESS应用场景设想

1. **顶层 (High-End)：** **超强算力 SoC 集成虚拟 MCU（+高性能多核 MCU）**。
  * A核虚拟MCU，运行实时性、启动时间要求不高的功能；
  * 高性能多核MCU，运行高功能安全要求、高实时性可靠性、启动时间要求高的功能。
2. **中间层 (Zonal)：** **高性能多核 MCU (Zone Controller)或MCU-LESS**。
  * 负责配电、I/O 聚合、唤醒管理。
  * 数量_：_ 全车仅剩 2-4 颗大 MCU。
3. **底层 (Edge)：** **无 MCU (MCU-LESS)**。
  * 执行器变成“哑巴硬件”或“智能驱动”。
  * 传感器变成“原始数据发送者”。
  * 消灭了：门控模块、座椅模块、灯控模块、水泵模块等数十个分布式 MCU。


## **应用目标：**

1、降低BOM成本

2、减少维护软件数量以及OTA节点数量

3、提高软件迭代效率

4、PCB小型化

## 上车节奏



# 前期验证（用于ZCU和DZCU/SCU）：

1. 高实时性控制
  a. 车窗防夹、座椅防夹：防夹效果和当前是否有差异
  b. 底盘高度传感器采集、电磁阀控制：高度采集软件调度1ms 空簧电磁阀控制10ms
2. 专用信号采集方案
  a. SENT信号，是否一定要？
  b. PSI5 SPI转PSI5
3. 休眠唤醒：
  a. 关注休眠下的功耗，唤醒时间；
  b. 唤醒类型：数字量、模拟量、CAN、LIN；
4. GW功能：
  a. CAN（FD）-CAN（FD）
  b. CAN-LIN
  c. ETH-CANFD？
  d. IMU数据
  e. 信号路由
  f. 报文采集
  g. GPAN-CAN/LIN/ETH（不同节点间路由）
5. 帧数据
  a. 专用帧最大数量，包大小？ACK信息验证
  b. 公共帧（最大努力传输）包大小？，无ACK？
  c. 外设优先级验证？
  d. 最短传输距离验证
  e. 最小帧间隔
  f. 最大负载下的可靠性验证，丢包率
6. 功能安全（GPAN芯片ASIL-B）
  a. 高功能安全的如何处理？EPB卡钳驱动ASIL-D，主动悬架 ASIL-C
  b. 主节点MCU重启如何处理？
7. 分布式功放
  a. 适配理想当前铂金、HIFI音响
8. 通信故障
  a. 环切菊花链的时间
9. 主节点资源
  a. RAM
  b. Flash
  c. CPU

## 验证方案

**功能安全：**

- 加速踏板和制动踏板，不能用BZCU采集；
- EPB驻车不能用BZCU控制；
- 主动悬架的PSI5信号采集，如果只做路由的话，可以由BZCU采集


**汇顶MCU-LESS芯片资源与BZCU需求MAP表：**

| 序号 | 类型 | 名称 | 是否支持 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 输入 | IA | Y |  |
| 2 | 输入 | IDL | Y |  |
| 3 | 输入 | ID | Y |  |
| 4 | 输入 | HALL | Y |  |
| 5 | 输入 | PWM | Y |  |
| 6 | 输入 | INT（中断） | Y |  |
| 7 | 输出 | PWM | Y |  |
| 8 | 输出 | OD | Y |  |
| 9 | Bus | SENT | N |  |
| 10 | Bus | SPI | Y |  |
| 11 | Bus | I2C | Y |  |
| 12 | Bus | PSI5 | N | SPI转PSI5 |
| 13 | Bus | RMII | Y |  |
| 14 | Bus | CAN/CANFD | Y |  |
| 15 | Bus | LIN | Y |  |
**验证进展（截止到11.15）**

| 底层功能调试 |  | 问题 |  |
| --- | --- | --- | --- |
| 已完成 | 31 | 已解决 | 22 |
| 调试中 | 8 | 未解决 | 8 |


**成本评估：**

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 变量 | 4851价格 | 2.5 |  | 新的MCU价格 | 80 |  | 单个4851硬件面积 | 64 |
|  | GPAN QFN64价格(T1) | 9 |  | GPAN BGA144价格 | 12 |  |  |  |
|  | GPAN QFN64价格(CAN) | 7 |  | GPAN BGA196价格 | 18 |  |  |  |
|  |  |  |  |  |  |  |  |  |
| 二级网络 | 比对项 | 当前方案 | 个数 | 价格 | GPAN方案 | 价格 | 备注 |  |
| 左前ZCU | MCU | TC389 | 1 | 80 | TC4/其它 | 80 | 相同型号，算力更强，IO更少 |  |
|  | 现有IO扩展芯片(D9+A9) | 4851(8选1) | 16 | 2.5 | 省掉8个+8个 |  | BGA144/196都可支持64个模拟IO(暂定) |  |
|  | GPAN1 | 无 |  |  | BGA144 | 12 | 仅做IO扩展(级联或单独外设接口) |  |
|  | GPAN2 | 无 |  |  | BGA144 | 12 | GPAN网络+做IO扩展 |  |
|  | 4851硬件面积节约 | 1024 |  | 5 |  |  | 硬件成本节约 |  |
|  | 合计 |  |  | 125 |  | 104 |  |  |
|  |  |  |  |  | 节约 | 21 |  |  |
| 右前ZCU | MCU | TC389 | 1 | 80 | TC4/其它 | 80 | 相同型号，算力更强，IO更少 |  |
|  | 现有IO扩展芯片(D0+A11) | 4851(8选1) | 8 | 2.5 | 省掉8个 |  | 有11个模拟扩展IO |  |
|  | GPAN1 | 无 |  |  | BGA144(无) |  | 仅做IO扩展 |  |
|  | GPAN2 | 无 |  |  | BGA144 | 12 | GPAN网络+做IO扩展 |  |
|  | 4851硬件面积节约 | 512 |  | 3 |  |  |  |  |
|  | 合计 |  |  | 103 |  | 92 |  |  |
|  |  |  |  |  | 节约 | 11 |  |  |
| 后ZCU (可规划2个?) | MCU | TC399 | 1 | 120 | 无 |  | 相同型号，算力更强，IO更少 |  |
|  | 现有IO扩展芯片(D8+A10) | 4851(8选1) | 18 | 2.5 | 省掉18个 |  | 共有18个4851 |  |
|  | GPAN1(左) | 无 |  |  | BGA144*2(接口选型待定) | 24 | 仅做IO扩展，联合省掉15个4851 |  |
|  | GPAN2(右) | 无 |  |  | BGA196 | 18 | 150个IO相当于约18个IO扩展芯片 |  |
|  | 4851硬件面积节约 | 1152 |  | 6 |  |  |  |  |
|  | 合计 |  |  | 171 |  | 42 |  |  |
|  |  |  |  |  | 节约 | 129 |  |  |
|  |  |  |  |  | 二级网络总共节约： | 161 |  |  |
项目计划

汇顶MCU-LESS芯片量产计划：

20251224：





# backup：

**整车控制器状态梳理**

| 控制器 | 通信类型 | 是否有主动唤醒整车需求 | 负载类型及端口需求 | 备注 |
| --- | --- | --- | --- | --- |
| ALM | LIN | 否 |  | 负载类型单一，端口需求少 |
| RLS | LIN | 是 |  | 负载类型单一，端口需求少 |
| SWB | LIN | 否 |  | 负载类型单一，端口需求少 |
| EW | LIN | 否 |  | 负载类型单一，端口需求少 |
| RL（阅读灯） | LIN | 否 |  | 负载类型单一，端口需求少 |
| IAQS | LIN | 否 |  | 负载类型单一，端口需求少 |
| BLFM | LIN | 否 |  | 负载类型单一，端口需求少 |
| AF | LIN | 否 |  | 负载类型单一，端口需求少 |
| EXV1 | LIN | 否 |  | 负载类型单一，端口需求少 |
| VFRIDGE | LIN | 是 |  | 负载类型多样，端口需求多 |
| MFAN | LIN | 否 |  | 负载类型单一，端口需求少 |
| AFAN | LIN | 否 |  | 负载类型单一，端口需求少 |
| AGS | LIN | 否 |  | 负载类型单一，端口需求少 |
| ESAM | LIN | 否 |  | 负载类型单一，端口需求少 |
| APTC | LIN | 否 |  | 负载类型单一，端口需求少 |
| FSSCU | LIN | 否 |  | 负载类型单一，端口需求少 |
| RSSCU | LIN | 否 |  | 负载类型单一，端口需求少 |
| RLMS | LIN | 否 |  | 负载类型单一，端口需求少 |
| RRMS | LIN | 否 |  | 负载类型单一，端口需求少 |
| LEMVSR | LIN | 否 |  | 负载类型单一，端口需求少 |
| REMVSR | LIN | 否 |  | 负载类型单一，端口需求少 |
| TLSS | LIN | 否 |  | 负载类型单一，端口需求少 |
| TRSS | LIN | 否 |  | 负载类型单一，端口需求少 |
| EWP | LIN | 否 |  | 负载类型单一，端口需求少 |
| OPF | LIN | 否 |  | 负载类型单一，端口需求少 |
| AMP | CAN | 否 |  | 负载类型单一，端口需求多 |
| HUD | CAN | 否 |  | 负载类型单一，端口需求少 |
| ROOFBAR | CAN | 否 |  | 负载类型单一，端口需求少 |
| SMIRM | CAN | 否 |  | 负载类型单一，端口需求少 |
| LHCM | CAN | 否 |  | 负载类型单一，端口需求多 |
| RHCM | CAN | 否 |  | 负载类型单一，端口需求多 |
| RFR | CAN | 是 |  | 负载类型单一，端口需求少 |
| FKS | CAN | 是 |  | 负载类型单一，端口需求少 |
| APSB | CAN | 否 |  | 负载类型单一，端口需求少 |
| PSD | CAN | 否 |  | 负载类型多样，端口需求多 |
| SCU | CAN | 是 |  | 负载类型多样，端口需求多 |
| SMA | CAN | 否 |  | 负载类型多样，端口需求多 |
| UWB | CAN | 是 |  | 负载类型单一，端口需求少 |
| FLDA | CAN | 否 |  | 负载类型单一，端口需求少 |
| EXNFC | CAN | 是 |  | 负载类型单一，端口需求少 |
| PWLC | CAN | 否 |  | 负载类型单一，端口需求少 |
| APS | CAN | 是 |  | 负载类型单一，端口需求少 |
| DCU | CAN | 是 |  | 负载类型多样，端口需求多 |
| ACU | CAN | 否 |  | 负载类型多样，端口需求多 |
| ODU | CAN | 否 |  | 负载类型多样，端口需求多 |
| PDC | CAN | 是 |  | 负载类型多样，端口需求多 |
| BMS | CAN | 是 |  | 负载类型多样，端口需求多 |
| LDCDC | CAN | 是 |  | 负载类型单一，端口需求少 |
| MCUR | CAN | 否 |  | 负载类型多样，端口需求多 |
| OPR | CAN | 否 |  | 负载类型多样，端口需求多 |
| LBMS | CAN | 是 |  | 负载类型多样，端口需求多 |
| EMS | CAN | 否 |  | 负载类型多样，端口需求多 |
| EVVT | CAN | 否 |  | 负载类型单一，端口需求少 |
| MCUF | CAN | 否 |  | 负载类型多样，端口需求多 |
| OPF | CAN | 否 |  | 负载类型多样，端口需求多 |
| GCU | CAN | 否 |  | 负载类型多样，端口需求多 |
| FDCDC | CAN | 否 |  | 负载类型单一，端口需求少 |
| TCM | CAN | 是 |  | 负载类型多样，端口需求多 |
| EPS | CAN | 否 |  | 负载类型多样，端口需求多 |
| ESP | CAN | 否 |  | 负载类型多样，端口需求多 |
| DPB | CAN | 否 |  | 负载类型多样，端口需求多 |
| RWA | CAN | 否 |  | 负载类型多样，端口需求多 |
| RWS | CAN | 否 |  | 负载类型多样，端口需求多 |
| IPB | CAN | 否 |  | 负载类型多样，端口需求多 |
| RACP | CAN | 否 |  | 负载类型单一，端口需求少 |
| DWLC | CAN | 否 |  | 负载类型单一，端口需求少 |
| CTM | CAN | 否 |  | 负载类型多样，端口需求多 |
| ACCM | CAN | 否 |  | 负载类型多样，端口需求多 |
| WPTC | CAN | 否 |  | 负载类型多样，端口需求多 |
| ETC | CAN | 否 |  | 负载类型单一，端口需求少 |

# OC项目量产验证

MCU-LESS Master：PZCU

MCU-LESS Slaver：SCU or CTM（当前MCU：S32K144）



