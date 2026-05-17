# Automotive Claude Code Agents — 使用教程手册

> **版本**: v1.0.0 | **语言**: 中文 | **更新**: 2026-05-11  
> **适用人群**: 汽车软件工程师、ECU 开发人员、功能安全专家  
> **配套文档**: [详细说明书](AUTOMOTIVE_AGENTS_REFERENCE.md)

---

## 目录

- [第一章：快速开始（10分钟上手）](#第一章快速开始10分钟上手)
- [第二章：安装与环境配置](#第二章安装与环境配置)
- [第三章：基础使用方法](#第三章基础使用方法)
- [第四章：功能安全开发教程（ISO 26262）](#第四章功能安全开发教程iso-26262)
- [第五章：网络安全工程教程（ISO 21434）](#第五章网络安全工程教程iso-21434)
- [第六章：AUTOSAR 开发教程](#第六章autosar-开发教程)
- [第七章：车辆诊断开发教程](#第七章车辆诊断开发教程)
- [第八章：ADAS 感知开发教程](#第八章adas-感知开发教程)
- [第九章：电池管理系统教程（BMS）](#第九章电池管理系统教程bms)
- [第十章：LLM Council 多模型协作教程](#第十章llm-council-多模型协作教程)
- [第十一章：HIL/SIL 测试教程](#第十一章hilsil-测试教程)
- [第十二章：中国标准合规教程](#第十二章中国标准合规教程)
- [第十三章：开发者扩展指南](#第十三章开发者扩展指南)
- [第十四章：常见问题（FAQ）](#第十四章常见问题faq)

---

## 第一章：快速开始（10分钟上手）

### 1.1 前置要求

| 要求 | 版本 | 说明 |
|------|------|------|
| Claude Code | 最新版 | 必须 |
| Git | 2.30+ | 必须 |
| Python | 3.10+ | 可选（运行示例） |
| Node.js | 18+ | 可选（部分工具） |

### 1.2 一键安装

```bash
# 克隆仓库
git clone https://github.com/sydyg/automotive-claude-code-agents.git
cd automotive-claude-code-agents

# 执行安装（追加模式，不覆盖现有配置）
./install.sh

# 验证安装状态
./install.sh --status
```

安装完成后，所有资产将部署到 `~/.claude/` 目录，以 `automotive-` 为命名前缀。

### 1.3 第一个命令

在 Claude Code 中输入以下命令体验工具包：

```
/automotive-review
```

这将触发汽车软件代码审查 Agent，按照 MISRA C 和 ISO 26262 标准审查当前打开的代码文件。

### 1.4 5分钟场景演示

**场景：我需要检查一段 ABS 控制代码是否符合 ISO 26262**

1. 在 Claude Code 中打开 ABS 控制代码文件
2. 输入命令：
   ```
   /automotive-safety-audit
   ```
3. Agent 自动执行：
   - 识别安全关键函数
   - 检查 ASIL 等级注释
   - 验证 MISRA C 合规性
   - 生成合规报告

**输出示例**：
```
ISO 26262 合规审查报告
====================
文件: abs_control.c
检测到安全关键函数: abs_pressure_control()

⚠ 问题 1 [ASIL-C]: 缺少安全注释
  位置: abs_control.c:47
  要求: ASIL-C 函数须添加 /* @ASIL{C} */ 注释
  
⚠ 问题 2 [MISRA-C 17.2]: 递归调用
  位置: abs_control.c:112
  规则: 禁止递归（MISRA C:2012 Rule 17.2）
  
✅ 通过: 无动态内存分配
✅ 通过: 函数参数数量合规（≤8个参数）

总计: 2 警告, 0 错误
建议: 修复上述问题后重新提交审查
```

---

## 第二章：安装与环境配置

### 2.1 安装选项

#### 完整安装（推荐）

```bash
./install.sh
```

安装内容：
- 所有 Agents（27个领域）
- 所有 Commands（200+命令）
- 所有 Skills（75+技能）
- Knowledge Base（507+文档）
- Rules（37+规则文件）
- Git Hooks（自动化检查）

#### 按领域安装

```bash
# 仅安装功能安全相关资产
./install.sh --domain functional-safety

# 仅安装网络安全相关资产
./install.sh --domain cybersecurity

# 仅安装 ADAS 相关资产
./install.sh --domain adas
```

#### 预览安装（不实际执行）

```bash
./install.sh --dry-run
```

#### 安装到指定项目

```bash
./install.sh --project /path/to/your/automotive/project
```

### 2.2 环境变量配置

复制并编辑环境变量文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件，填入必要配置：

```bash
# ===== 必填：AI 模型 =====
ANTHROPIC_API_KEY=sk-ant-api03-xxxxx    # 从 console.anthropic.com 获取

# ===== 可选：LLM Council 多模型功能 =====
AZURE_OPENAI_API_KEY=xxxxx              # Azure OpenAI 密钥
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# ===== 可选：汽车工具路径 =====
CANOE_LICENSE_SERVER=192.168.1.100      # Vector CANoe 授权
MATLAB_LICENSE_FILE=/opt/matlab/lic.dat  # MATLAB 授权
```

### 2.3 配置 CLAUDE.md

在项目根目录创建或编辑 `CLAUDE.md`，定义 Claude 工作规范：

```markdown
# 项目配置：智能座舱 ECU 开发

## 安全等级
- 项目 ASIL 等级: ASIL-B
- 需要遵循: ISO 26262 Part 6

## 编码规范
- C 代码: MISRA C:2012（强制规则全部遵守）
- C++ 代码: AUTOSAR C++14
- 禁止: 动态内存分配、递归、goto 语句

## 通信协议
- 内部总线: AUTOSAR COM
- 诊断: UDS over CAN (ISO 14229)

## 测试要求  
- 单元测试覆盖率: ≥ 80%
- 安全关键函数: MC/DC 覆盖率 100%
```

### 2.4 验证安装

```bash
# 检查所有组件状态
./install.sh --status

# 输出示例
Automotive Claude Code Agents Status
=====================================
[✓] Agents:        42/42 installed
[✓] Commands:      213/213 installed  
[✓] Skills:        78/78 installed
[✓] Knowledge:     507/507 documents
[✓] Rules:         37/37 rules
[✓] Git Hooks:     5/5 hooks active
[✓] API Key:       Claude API configured
[~] LLM Council:   Azure API not configured (optional)
```

### 2.5 卸载

```bash
# 完整卸载（仅移除 automotive-* 前缀的资产）
./install.sh --uninstall
```

> ⚠️ 卸载不会影响您现有的 Claude Code 配置

---

## 第三章：基础使用方法

### 3.1 命令调用格式

所有命令在 Claude Code 中以斜线 `/` 开头调用：

```
/<命令名> [参数]
```

### 3.2 最常用命令速查

| 场景 | 命令 | 说明 |
|------|------|------|
| 代码审查 | `/automotive-review` | 按汽车标准审查代码 |
| 生成代码 | `/automotive-generate` | 生成符合标准的代码 |
| 安全分析 | `/automotive-safety-analyze` | ASIL 分析与安全需求 |
| 诊断代码 | `/automotive-diag-uds` | 生成 UDS 诊断服务 |
| AUTOSAR 配置 | `/automotive-autosar-classic` | AUTOSAR Classic 开发 |
| 测试生成 | `/automotive-test-unit` | 生成单元测试 |
| 网络安全 | `/automotive-sec-tara` | TARA 威胁分析 |
| 文档生成 | `/automotive-document` | 技术文档自动生成 |

### 3.3 命令参数传递

```
# 基本调用
/automotive-review

# 带参数调用
/automotive-safety-analyze --asil ASIL-D --component brake_controller

# 带文件路径
/automotive-diag-uds --service 0x22 --file src/diagnostics/data_ids.h
```

### 3.4 与 Agent 对话

除命令调用外，也可直接用自然语言与 Agent 对话：

```
我需要为制动系统 ECU 执行 HARA 分析，
该 ECU 控制前轮制动力分配，
车辆最高速度 200km/h，驾驶员无法直接控制。
请按照 ISO 26262 标准执行分析。
```

Agent 会自动识别任务类型，激活对应的 Skills 和 Rules。

---

## 第四章：功能安全开发教程（ISO 26262）

### 4.1 场景：为新 ECU 执行完整功能安全分析

**目标**：为自适应巡航控制（ACC）ECU 执行 ISO 26262 功能安全分析

#### 步骤 1：执行 HARA

```
/automotive-safety-hara

请为以下系统执行 HARA:
- 系统: 自适应巡航控制（ACC）
- 速度范围: 0-130 km/h
- 传感器: 毫米波雷达 + 摄像头
- 执行器: 发动机扭矩控制 + 制动系统
```

**期望输出**：

```
HARA 分析报告 - 自适应巡航控制（ACC）
======================================

危害场景识别:
H-01: 意外加速（ACC 误触发加速）
  S: S3（重伤）| E: E4（高频）| C: C3（难控制）→ ASIL-D

H-02: 无法制动（ACC 跟车时制动失效）
  S: S3 | E: E3 | C: C2 → ASIL-C

H-03: 错误激活（静止时意外激活）
  S: S2 | E: E2 | C: C1 → ASIL-A

安全目标:
SG-01 [ASIL-D]: 防止 ACC 系统导致意外加速
SG-02 [ASIL-C]: 确保 ACC 跟车场景下制动系统可用
SG-03 [ASIL-A]: 防止 ACC 在静止状态意外激活
```

#### 步骤 2：ASIL 分解与需求派生

```
/automotive-safety-asil

基于 HARA 结果，请为 SG-01 (ASIL-D) 执行 ASIL 分解，
采用独立冗余架构（两个独立通道）
```

**输出**：

```
ASIL 分解: SG-01 [ASIL-D]
=========================
分解策略: ASIL-D → ASIL-B(D) + ASIL-B(D)

通道 A（主通道）[ASIL-B]:
  FSR-01A: ACC 控制算法不得产生 >0.3g 意外加速
  FSR-02A: 加速度监控周期 ≤ 10ms

通道 B（监控通道）[ASIL-B]:  
  FSR-01B: 独立监控 ACC 输出扭矩值
  FSR-02B: 检测到异常时，100ms 内触发安全状态

独立性要求:
  - 两通道使用不同 MCU（硬件独立）
  - 两通道软件独立开发（防止共因失效）
```

#### 步骤 3：生成安全关键代码

```
/automotive-generate

根据 FSR-01A，生成 ACC 加速度监控函数，
要求:
- ASIL-B 等级
- MISRA C:2012 合规
- 最大执行时间: 5ms（WCET 分析）
```

**生成的代码**：

```c
/**
 * @brief ACC acceleration monitoring function
 * @asil ASIL-B
 * @misra MISRA-C:2012 Rule 15.5, 17.2 compliant
 * @req FSR-01A, FSR-02A
 * @wcet 3.2ms (measured on Cortex-M4 @ 180MHz)
 */
/* @ASIL{B} */
static Std_ReturnType Acc_MonitorAcceleration(
    const AccState_Type* const state,
    const float32 requestedAccel_mss)
{
    Std_ReturnType ret = E_OK;
    float32 actualAccel_mss;
    
    /* [FSR-02A] Monitor period check: called every 10ms */
    if (state == NULL_PTR)
    {
        /* MISRA C:2012 Rule 15.5: single exit point with error */
        ret = E_NOT_OK;
    }
    else
    {
        actualAccel_mss = Acc_GetActualAcceleration();
        
        /* [FSR-01A] Max acceleration limit: 0.3g = 2.94 m/s² */
        if (requestedAccel_mss > ACC_MAX_ACCEL_MPS2)
        {
            /* Trigger safety state immediately */
            (void)SafetyManager_TriggerSafeState(
                SAFETY_CAUSE_ACC_OVERACCEL);
            ret = E_NOT_OK;
        }
    }
    
    return ret;
}
```

#### 步骤 4：生成安全测试用例

```
/automotive-test-unit

为 Acc_MonitorAcceleration 函数生成 MC/DC 覆盖率 100% 的测试用例
```

#### 步骤 5：合规审计

```
/automotive-safety-audit

请对 acc_monitor.c 执行 ISO 26262 Part 6 合规审计
```

---

## 第五章：网络安全工程教程（ISO 21434）

### 5.1 场景：为远程诊断接口执行 TARA

**目标**：评估 OBD-II 端口远程访问的网络安全风险

#### 步骤 1：执行 TARA

```
/automotive-sec-tara

分析目标: 远程诊断接口（OBD-II over 4G/5G）
资产: 诊断访问权限、ECU 软件更新能力
威胁模型: STRIDE
```

**输出**：

```
TARA 分析报告 - 远程诊断接口
==============================

资产识别:
A-01: 诊断访问令牌（高价值）
A-02: ECU 固件更新权限（极高价值）
A-03: 车辆识别信息（中价值）

威胁场景（STRIDE）:
T-01: 未授权诊断访问 [Spoofing]
  可行性: HIGH | 影响: HIGH → 风险值: 5（需立即处理）

T-02: 固件篡改 [Tampering]  
  可行性: MEDIUM | 影响: CRITICAL → 风险值: 5

T-03: 诊断数据窃听 [Information Disclosure]
  可行性: MEDIUM | 影响: MEDIUM → 风险值: 3

安全目标:
CS-01: 远程诊断访问必须经过双因素认证
CS-02: 固件更新必须验证密码学签名（RSA-3072 或 ECC-384）
CS-03: 诊断通信必须加密（TLS 1.3）
```

#### 步骤 2：设计安全启动链

```
/automotive-sec-secureboot

目标芯片: NXP S32K344
信任根: eFuse OTP
要求: 支持密钥轮换
```

**输出**：

```c
/* 安全启动配置 - NXP S32K344 */
/* @cybersecurity ISO21434 CS-02 */

#define SECURE_BOOT_KEY_SIZE    256U  /* RSA-3072 or ECC-384 */

typedef struct {
    uint8_t  publicKeyHash[32];   /* SHA-256 of public key */
    uint8_t  imageSignature[64];  /* ECDSA-384 signature */
    uint32_t imageLength;
    uint32_t imageVersion;        /* For rollback protection */
} SecureBoot_ImageHeader_Type;

/**
 * @brief Verify firmware image signature
 * @security ISO21434 [CS-02]
 * @note Called before any firmware execution
 */
Std_ReturnType SecureBoot_VerifyImage(
    const SecureBoot_ImageHeader_Type* header,
    const uint8_t* imageData)
{
    /* Step 1: Verify public key hash against eFuse */
    /* Step 2: Verify image signature with ECDSA-384 */
    /* Step 3: Check version for rollback protection */
    /* ... implementation ... */
}
```

#### 步骤 3：实现 CAN 入侵检测

```
/automotive-sec-ids

总线: CAN FD
基线学习周期: 7天
检测方法: 统计异常 + 时序分析
```

#### 步骤 4：生成合规报告

```
/automotive-sec-tara --report

生成 UN R155 合规性证明文档，
包含 TARA 摘要、风险处理措施、残余风险声明
```

---

## 第六章：AUTOSAR 开发教程

### 6.1 场景：创建 AUTOSAR Classic 软件组件

**目标**：开发一个符合 AUTOSAR 规范的车速传感器软件组件

#### 步骤 1：创建 SWC 定义

```
/automotive-autosar-classic

创建软件组件:
- 名称: VehicleSpeedSensor
- 类型: Sensor SWC
- 接口: 提供 VehicleSpeed (float32, 单位 km/h)
- ASIL: ASIL-B
- 周期: 10ms
```

**生成的 ARXML 片段**：

```xml
<!-- VehicleSpeedSensor.arxml -->
<AUTOSAR>
  <AR-PACKAGES>
    <AR-PACKAGE>
      <SHORT-NAME>ComponentTypes</SHORT-NAME>
      <ELEMENTS>
        <APPLICATION-SW-COMPONENT-TYPE>
          <SHORT-NAME>VehicleSpeedSensor</SHORT-NAME>
          <CATEGORY>APPLICATION</CATEGORY>
          <!-- ASIL-B safety classification -->
          <SW-COMPONENT-DOCUMENTATION>
            <CATEGORY>ASIL_B</CATEGORY>
          </SW-COMPONENT-DOCUMENTATION>
          <PORTS>
            <P-PORT-PROTOTYPE>
              <SHORT-NAME>PPort_VehicleSpeed</SHORT-NAME>
              <PROVIDED-INTERFACE-TREF>
                /Interfaces/VehicleSpeedInterface
              </PROVIDED-INTERFACE-TREF>
            </P-PORT-PROTOTYPE>
          </PORTS>
          <INTERNAL-BEHAVIORS>
            <SWC-INTERNAL-BEHAVIOR>
              <SHORT-NAME>VehicleSpeedSensor_IB</SHORT-NAME>
              <RUNNABLES>
                <RUNNABLE-ENTITY>
                  <SHORT-NAME>VehicleSpeedSensor_Run</SHORT-NAME>
                  <MINIMUM-START-INTERVAL>0.01</MINIMUM-START-INTERVAL>
                </RUNNABLE-ENTITY>
              </RUNNABLES>
            </SWC-INTERNAL-BEHAVIOR>
          </INTERNAL-BEHAVIORS>
        </APPLICATION-SW-COMPONENT-TYPE>
      </ELEMENTS>
    </AR-PACKAGE>
  </AR-PACKAGES>
</AUTOSAR>
```

#### 步骤 2：生成实现代码

```
/automotive-autosar-classic --generate-impl

基于 VehicleSpeedSensor.arxml 生成 C 实现代码
包括 Rte 接口调用
```

**生成的 C 代码**：

```c
/* VehicleSpeedSensor.c - AUTOSAR SWC Implementation */
/* @ASIL{B} */
/* Generated by automotive-claude-code-agents */

#include "Rte_VehicleSpeedSensor.h"

/* MISRA C:2012 Rule 8.4: Function declarations */
FUNC(void, VehicleSpeedSensor_CODE) VehicleSpeedSensor_Run(void);

/**
 * @brief 10ms periodic runnable - Read and publish vehicle speed
 * @asil ASIL-B  
 * @req VehicleSpeedSensor-SRS-001
 */
/* @ASIL{B} */
FUNC(void, VehicleSpeedSensor_CODE) VehicleSpeedSensor_Run(void)
{
    float32 speedRaw_kmh;
    float32 speedFiltered_kmh;
    Std_ReturnType readStatus;
    
    /* Read raw speed from hardware abstraction layer */
    readStatus = Rte_Call_RPPort_SpeedHW_ReadSpeed(&speedRaw_kmh);
    
    if (E_OK == readStatus)
    {
        /* Apply low-pass filter (IIR, alpha=0.1) */
        speedFiltered_kmh = VehicleSpeed_ApplyFilter(speedRaw_kmh);
        
        /* Validate range: 0 to 300 km/h */
        if ((speedFiltered_kmh >= 0.0F) && 
            (speedFiltered_kmh <= VEHICLE_SPEED_MAX_KMH))
        {
            (void)Rte_Write_PPort_VehicleSpeed_Speed(speedFiltered_kmh);
        }
        else
        {
            /* Out of range: report DEM event */
            (void)Dem_ReportErrorStatus(
                DemConf_DemEventParameter_E_SPEED_RANGE_VIOLATION,
                DEM_EVENT_STATUS_FAILED);
        }
    }
}
```

#### 步骤 3：配置通信矩阵

```
/automotive-autosar-com

为 VehicleSpeed 信号配置 CAN 通信:
- 帧 ID: 0x3A0
- 周期: 10ms
- 字节序: Little Endian
- 范围: 0-300 km/h (精度 0.01 km/h)
```

---

## 第七章：车辆诊断开发教程

### 7.1 场景：实现完整 UDS 诊断服务

**目标**：为 EV 电池管理 ECU 实现 UDS 诊断服务

#### 步骤 1：生成 UDS 服务框架

```
/automotive-diag-uds

ECU 名称: BatteryManagementUnit
支持服务:
- 0x10 (DiagnosticSessionControl)
- 0x22 (ReadDataByIdentifier): 
    - 0xF190: VIN
    - 0x2001: 电池 SOC
    - 0x2002: 电池温度（4个传感器）
    - 0x2003: 电池电压
- 0x27 (SecurityAccess): Level 0x01/0x02
- 0x14 (ClearDTC)
- 0x19 (ReadDTC)
语言: C
协议: UDS over CAN (ISO 15765-2 TP)
```

**生成代码示例**（ReadDataByIdentifier 0x2001）：

```c
/* BMS_DiagReadData.c */
/* UDS Service 0x22 - ReadDataByIdentifier */

#include "Dcm.h"
#include "Bms_Interface.h"

/**
 * @brief Read Battery SOC (DID 0x2001)
 * @req BMS-DIAG-002
 * @uds 0x22 0x2001
 */
Std_ReturnType BmsDiag_ReadSoc(
    uint8* data,
    Dcm_OpStatusType opStatus,
    uint16* dataLength,
    Dcm_NegativeResponseCodeType* errorCode)
{
    Std_ReturnType ret = E_OK;
    float32 socValue;
    
    (void)opStatus;  /* MISRA: unused parameter */
    
    /* Read SOC from BMS core module */
    if (Bms_GetStateOfCharge(&socValue) == E_OK)
    {
        /* Encode: SOC% * 100 → uint16 (0-10000 = 0.00%-100.00%) */
        uint16 socEncoded = (uint16)(socValue * 100.0F);
        
        data[0] = (uint8)((socEncoded >> 8U) & 0xFFU);
        data[1] = (uint8)(socEncoded & 0xFFU);
        *dataLength = 2U;
    }
    else
    {
        *errorCode = DCM_E_CONDITIONSNOTCORRECT;
        ret = E_NOT_OK;
    }
    
    return ret;
}
```

#### 步骤 2：生成 DTC 定义

```
/automotive-diag-dtc

为 BMS ECU 生成 DTC 定义，包含:
- P0A1B: 电池 SOC 传感器故障
- P0AC0: 电池电压过高
- P0AC1: 电池电压过低
- P0AFF: 电池热管理系统故障
格式: SAE J2012 / ISO 15031-6
```

#### 步骤 3：ECU 刷写流程

```
/automotive-diag-flash

目标 ECU: BatteryManagementUnit v2.1.0 → v2.2.0
传输协议: UDS ISO 15765-2
加密: 不加密（内网环境）
完整性验证: CRC-32
```

**生成的刷写序列**：

```python
# ECU Flash Programming - BMS v2.1.0 → v2.2.0
# Generated by automotive-diag-flash

import udsoncan

async def flash_bms_ecu(client: udsoncan.Client, firmware_path: str):
    """7-step UDS flash programming procedure"""
    
    # Step 1: Switch to Extended Diagnostic Session
    await client.change_session(
        udsoncan.services.DiagnosticSessionControl.Session.extendedDiagnosticSession)
    
    # Step 2: Security Access (Level 0x01)
    seed = await client.request_seed(0x01)
    key = calculate_security_key(seed.seed)  # OEM algorithm
    await client.send_key(0x01, key)
    
    # Step 3: Enable Programming Session
    await client.change_session(
        udsoncan.services.DiagnosticSessionControl.Session.programmingSession)
    
    # Step 4: Erase Memory (Routine 0xFF00)
    await client.start_routine(0xFF00, b'\x00\x00\x00\x00\xFF\xFF\xFF\xFF')
    
    # Step 5: Request Download
    firmware = open(firmware_path, 'rb').read()
    await client.request_download(
        memory_address=0x00000000,
        memory_size=len(firmware),
        compression=0x00,
        encrypting=0x00)
    
    # Step 6: Transfer Data (4KB blocks)
    BLOCK_SIZE = 4096
    for i in range(0, len(firmware), BLOCK_SIZE):
        block = firmware[i:i+BLOCK_SIZE]
        await client.transfer_data(
            block_sequence_counter=(i // BLOCK_SIZE + 1) % 256,
            data=block)
    
    # Step 7: Request Transfer Exit + Verify CRC
    await client.request_transfer_exit()
    crc = calculate_crc32(firmware)
    result = await client.start_routine(0x0202, crc.to_bytes(4, 'big'))
    
    print(f"Flash complete: {result}")
```

---

## 第八章：ADAS 感知开发教程

### 8.1 场景：实现多传感器融合感知

**目标**：开发前向感知模块（摄像头 + 毫米波雷达融合）

#### 步骤 1：设计感知架构

```
/automotive-adas-perception

设计前向感知模块:
传感器:
- 1x 前置摄像头（1920x1080, 30fps）
- 1x 77GHz 毫米波雷达（±18°, 200m）
输出:
- 障碍物列表（位置、速度、类别）
- 车道线检测结果
框架: ROS 2 (Humble)
安全等级: ASIL-B（SOTIF 适用）
```

**输出架构**：

```python
# perception_node.py - ROS 2 Perception Node
# @asil ASIL-B
# @sotif Performance limitation analysis required

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, PointCloud2
from autoware_auto_perception_msgs.msg import DetectedObjects

class FusionPerceptionNode(Node):
    """
    Multi-sensor fusion perception node
    Fuses camera + radar for obstacle detection
    
    @safety ASIL-B
    @sotif_limitation:
      - Camera degraded in fog (visibility < 50m)
      - Radar false positive on metal bridges
    """
    
    def __init__(self):
        super().__init__('fusion_perception')
        
        # Camera subscriber
        self.camera_sub = self.create_subscription(
            Image, '/camera/front/image_raw',
            self.camera_callback, 10)
        
        # Radar subscriber  
        self.radar_sub = self.create_subscription(
            PointCloud2, '/radar/front/points',
            self.radar_callback, 10)
        
        # Output publisher
        self.objects_pub = self.create_publisher(
            DetectedObjects, '/perception/objects', 10)
        
        # Initialize fusion algorithm (EKF)
        self.ekf_tracker = ExtendedKalmanFilter(dt=0.033)
    
    def fuse_detections(self, camera_dets, radar_dets):
        """Sensor fusion using Extended Kalman Filter"""
        # ... fusion logic ...
        pass
```

#### 步骤 2：SOTIF 分析

```
/automotive-adas-perception --sotif

对前向感知模块执行 SOTIF 性能限制分析:
- 列出已知性能限制（KPL）
- 列出未知性能限制（UKPL）
- 评估触发条件
```

#### 步骤 3：生成感知测试场景

```
/automotive-test-sil

为前向感知模块生成 SIL 测试场景集:
- 基础场景: 晴天直道、弯道跟车
- 边界场景: 大雨、强逆光、隧道出口
- 安全相关: 行人横穿、切入车辆
使用 CARLA 仿真格式
```

---

## 第九章：电池管理系统教程（BMS）

### 9.1 场景：实现 SOC 估算算法

**目标**：开发基于扩展卡尔曼滤波的 SOC 估算算法

#### 步骤 1：生成 SOC 估算代码

```
/automotive-battery-bms

实现 SOC 估算算法:
- 方法: 扩展卡尔曼滤波（EKF）
- 电池模型: RC等效电路（2阶RC）
- 输入: 电流、电压、温度
- 输出: SOC（0-100%），估算精度 ±2%
- 语言: C（嵌入式，无浮点运算库）
安全等级: ASIL-B
```

**生成代码**：

```c
/* bms_soc_ekf.c - SOC Estimation using Extended Kalman Filter */
/* @ASIL{B} */
/* @req BMS-SOC-001, BMS-SOC-002 */

#include "bms_soc_ekf.h"
#include "battery_model.h"

/* EKF state vector: [SOC, V_RC1, V_RC2] */
#define EKF_STATE_DIM  3U
#define EKF_MEAS_DIM   1U

typedef struct {
    float32 x[EKF_STATE_DIM];           /* State vector */
    float32 P[EKF_STATE_DIM][EKF_STATE_DIM]; /* Covariance matrix */
    float32 Q[EKF_STATE_DIM][EKF_STATE_DIM]; /* Process noise */
    float32 R[EKF_MEAS_DIM][EKF_MEAS_DIM];  /* Measurement noise */
} Ekf_State_Type;

static Ekf_State_Type g_ekfState;

/**
 * @brief Initialize EKF with initial SOC estimate
 * @param initialSoc Initial SOC value (0.0 - 1.0)
 */
void BmsSoc_EkfInit(float32 initialSoc)
{
    /* Initialize state */
    g_ekfState.x[0] = initialSoc;   /* SOC */
    g_ekfState.x[1] = 0.0F;         /* V_RC1 */
    g_ekfState.x[2] = 0.0F;         /* V_RC2 */
    
    /* Initialize covariance (high uncertainty) */
    g_ekfState.P[0][0] = 0.01F;     /* SOC uncertainty */
    g_ekfState.P[1][1] = 0.001F;    /* V_RC1 uncertainty */
    g_ekfState.P[2][2] = 0.001F;    /* V_RC2 uncertainty */
    
    /* Process noise (tuned from experimental data) */
    g_ekfState.Q[0][0] = 1e-6F;
    g_ekfState.Q[1][1] = 1e-5F;
    g_ekfState.Q[2][2] = 1e-5F;
    
    /* Measurement noise */
    g_ekfState.R[0][0] = 1e-4F;     /* Voltage measurement noise */
}

/**
 * @brief EKF prediction step (called at 100Hz)
 * @param current_A Battery current in Amperes (positive = discharge)
 * @param dt_s      Time step in seconds
 */
void BmsSoc_EkfPredict(float32 current_A, float32 dt_s)
{
    /* State propagation */
    float32 coulombEff = (current_A > 0.0F) ? 0.98F : 1.0F;
    
    /* SOC update via Coulomb counting */
    g_ekfState.x[0] -= (coulombEff * current_A * dt_s) / BATTERY_CAPACITY_AS;
    
    /* RC voltage update */
    float32 tau1 = Battery_GetRC1TimeConst(g_ekfState.x[0]);
    g_ekfState.x[1] = g_ekfState.x[1] * expf(-dt_s / tau1) +
                       current_A * Battery_GetRC1Resistance(g_ekfState.x[0]) *
                       (1.0F - expf(-dt_s / tau1));
    
    /* SOC boundary check */
    g_ekfState.x[0] = CLAMP(g_ekfState.x[0], 0.0F, 1.0F);
}
```

#### 步骤 2：热管理仿真

```
/automotive-battery-bms --thermal

生成电池热管理仿真模型:
电池组: 96S1P (磷酸铁锂, 75Ah)
冷却方式: 液冷（水冷板）
目标温度范围: 15-40°C
```

---

## 第十章：LLM Council 多模型协作教程

### 10.1 场景：架构决策辩论

**目标**：通过 Claude + GPT 辩论确定 SDV 中间件选型

#### 步骤 1：发起辩论

在终端执行：

```bash
./commands/llm-council/council-debate.sh \
  --topic "SDV 中间件选型：SOME/IP vs DDS vs Zenoh" \
  --context "新一代智能汽车域控制器，需要支持50个节点，延迟要求<1ms，支持AUTOSAR Adaptive" \
  --rounds 3
```

**辩论过程**：

```
=== LLM Council 辩论会议 ===
议题: SDV 中间件选型
参与者: Claude Opus 4.6 (A) | GPT-5.4 (B)

--- Round 1: 初始立场 ---

[Claude-A]: 推荐 SOME/IP
理由:
1. AUTOSAR Adaptive 原生支持，与目标平台完全契合
2. 成熟的汽车行业实施（宝马、奔驰大规模部署）
3. 静态配置，可预测延迟，适合 ASIL-B 以下场景

[GPT-B]: 推荐 DDS (Data Distribution Service)
理由:
1. 动态发现机制，50节点扩展性更优
2. QoS 策略更精细（可靠性、持久性、截止时间）
3. ROS 2 原生使用，生态完善

--- Round 2: 反驳与深化 ---

[Claude-A 反驳]: DDS 的动态发现在安全关键场景
引入不确定性，ASIL 认证困难...

[GPT-B 反驳]: SOME/IP 在高频小消息场景吞吐量
不及 DDS iceoryx 零拷贝实现...

--- Round 3: 综合共识 ---

[共识结论]: 混合架构
- 安全关键通信（底盘控制）→ SOME/IP
- 大数据流（传感器数据）→ DDS iceoryx
- 云端/跨域通信 → Zenoh（统一适配）
```

#### 步骤 2：生成架构决策记录（ADR）

```bash
./commands/llm-council/council-decide.sh \
  --debate-id "SDV-MIDDLEWARE-2026" \
  --format ADR
```

**生成的 ADR**：

```markdown
# ADR-2026-001: SDV 中间件架构选型

## 状态: 已接受

## 背景
新一代 SDV 域控制器需要支持 50 节点通信，
延迟要求 <1ms（安全关键），<10ms（数据流）。

## 决策
采用混合中间件架构：
1. SOME/IP（安全关键通信，AUTOSAR AP 集成）
2. DDS iceoryx（传感器数据流，零拷贝）
3. Zenoh（云端/跨域通信）

## 共识程度: 85% (Claude-A: 90%, GPT-B: 80%)

## 少数意见 [GPT-B]:
建议考虑 Eclipse Cyclone DDS 统一架构，降低维护复杂度。

## 影响
- 正面: 最优性能，标准合规
- 负面: 三套中间件维护成本增加

## 审阅者
LLM Council (Claude Opus 4.6 + GPT-5.4)
日期: 2026-05-11
```

#### 步骤 3：多模型代码审查

```bash
# 审查指定文件
./commands/llm-council/council-review.sh \
  --file src/middleware/some_ip_adapter.cpp \
  --focus "安全性,性能,MISRA合规"

# 审查 PR
./commands/llm-council/council-review.sh \
  --pr 142 \
  --repo github.com/myorg/sdv-platform
```

---

## 第十一章：HIL/SIL 测试教程

### 11.1 场景：搭建 ABS ECU 的 HIL 测试环境

#### 步骤 1：生成 HIL 测试配置

```
/automotive-hilsil-setup

测试目标: ABS ECU (Bosch 9.3)
HIL 平台: dSPACE MicroAutoBox III
被测信号:
- 输入: 4个轮速传感器（0-200 km/h）
- 输入: 制动踏板压力（0-200 bar）
- 输出: 4个液压阀控制信号
- 输出: 泵电机 PWM
测试场景: 紧急制动、冰面制动、弯道制动
```

**生成测试配置**：

```python
# hil_test_abs.py - ABS HIL Test Configuration
# Platform: dSPACE MicroAutoBox III

import dspace.mlapi.rtplatform as rt
from dspace.mlapi import RealTimePlatform

class AbsHilTest:
    """ABS ECU HIL Test Suite"""
    
    WHEEL_SPEED_CHANNELS = ['WS_FL', 'WS_FR', 'WS_RL', 'WS_RR']
    MAX_WHEEL_SPEED_KMH = 200.0
    
    def __init__(self, platform_name: str):
        self.platform = RealTimePlatform(platform_name)
        
    def test_emergency_brake_dry_road(self):
        """
        TC-ABS-001: Emergency braking on dry road (μ=0.9)
        Requirement: Stopping distance ≤ 40m from 100 km/h
        ASIL-C safety test
        """
        # Initial conditions
        self._set_vehicle_speed(100.0)  # km/h
        self._set_road_friction(0.9)    # dry road
        
        # Apply emergency brake
        self._apply_brake_pressure(200.0)  # bar
        
        # Monitor ABS activation
        result = self._monitor_abs_activation(timeout_s=5.0)
        
        # Assertions
        assert result.abs_activated == True, "ABS should activate"
        assert result.stopping_distance_m <= 40.0, \
            f"Stopping distance {result.stopping_distance_m}m > 40m"
        assert result.wheel_lock_duration_s < 0.1, \
            "Wheel lock duration should be minimal"
            
    def test_brake_ice_road(self):
        """TC-ABS-002: Braking on ice (μ=0.1)"""
        self._set_vehicle_speed(80.0)
        self._set_road_friction(0.1)
        self._apply_brake_pressure(150.0)
        result = self._monitor_abs_activation(timeout_s=8.0)
        assert result.vehicle_stability == True
```

#### 步骤 2：生成 SIL 测试（无硬件）

```
/automotive-test-sil

基于步骤1的测试脚本，生成 SIL 版本:
使用 CarMaker 虚拟车辆模型替代真实硬件
支持批量运行 1000+ 场景
```

#### 步骤 3：MC/DC 覆盖率分析

```
/automotive-test-coverage

分析 ABS 控制算法的 MC/DC 覆盖率:
目标: 100%（ASIL-C 要求）
工具: LDRA Testbed
报告格式: HTML + PDF
```

---

## 第十二章：中国标准合规教程

### 12.1 场景：L2 辅助驾驶系统中国法规合规审查

#### 步骤 1：激活中国合规 Agent

```
/automotive-china-l2-compliance

系统: 车道保持辅助（LKA）
标准:
- GB/T 26773-2023（车道保持辅助系统）
- GB/T 40429-2021（汽车驾驶自动化分级）
执行: 完整合规性差距分析
```

**输出**：

```
L2 中国法规合规分析报告
=========================
标准: GB/T 26773-2023 车道保持辅助系统

检查项 1: 系统激活条件
  要求: 车速 60-150 km/h 方可激活
  当前实现: 车速 > 60 km/h 激活（缺少上限）
  ⚠ 不符合 - 需添加上限 150 km/h

检查项 2: 驾驶员脱手报警
  要求: 连续脱手 > 15s 必须发出报警
  当前实现: 20s 后报警
  ⚠ 不符合 - 需缩短至 15s

检查项 3: 系统退出响应
  要求: 驾驶员转向时，< 0.5s 退出辅助
  当前实现: < 0.3s
  ✅ 符合

合规得分: 67% (4/6 项通过)
建议优先修复: 项目1、项目2
```

#### 步骤 2：生成 CATARC 认证材料

```
/automotive-china-compliance --report

生成以下认证材料:
1. 技术规格书（中文版）
2. 系统功能说明
3. 测试报告摘要
4. 偏差说明（如有）
格式: Word + PDF
```

---

## 第十三章：开发者扩展指南

### 13.1 创建自定义 Agent

#### 1. 创建 Agent 定义文件

```bash
# 在对应领域目录下创建
touch agents/my-domain/my-custom-agent.yaml
```

#### 2. 填写 Agent YAML 模板

```yaml
# agents/my-domain/my-custom-agent.yaml
name: my-custom-agent
version: "1.0.0"
namespace: automotive  # 必须使用 automotive 前缀

description: |
  描述此 Agent 的专业能力和适用场景。
  
role: "Senior Automotive Software Engineer - [专业领域]"

expertise:
  - "[专业技术1]"
  - "[专业技术2]"
  - "[相关标准]"

skills_used:
  - "automotive-cybersecurity/iso-21434-tara"  # 引用已有 Skill
  - "my-domain/my-custom-skill"               # 引用自定义 Skill

standards:
  - "ISO 26262:2018"
  - "AUTOSAR 4.4"

context_loading:
  # 任务开始时自动加载的知识
  - path: "knowledge-base/standards/iso26262"
  - path: "rules/safety-standards"

workflows:
  - name: "主要工作流"
    description: "处理主要任务类型"
    trigger: "当用户请求[任务类型]时"
    steps:
      - "步骤1：分析需求"
      - "步骤2：执行[专业分析]"
      - "步骤3：生成[输出物]"
      - "步骤4：验证合规性"

output_formats:
  - "结构化报告（Markdown）"
  - "代码（附标准合规注释）"

quality_gates:
  - "所有代码通过 MISRA 检查"
  - "安全函数含 ASIL 注释"
```

#### 3. 安装自定义 Agent

```bash
./install.sh --include-custom agents/my-domain/
```

### 13.2 创建自定义 Skill

```bash
# 创建 Skill 目录
mkdir -p skills/my-automotive-skill
```

```markdown
<!-- skills/my-automotive-skill/core-knowledge.md -->
# My Automotive Skill

## 概述
此 Skill 提供[专业领域]的专业知识。

## 核心知识点

### 1. [知识点1]
详细描述...

### 2. [知识点2]
代码示例：
```c
// 示例代码
```

## 最佳实践
- 实践1
- 实践2

## 常见错误
- 错误1及解决方案
```

### 13.3 添加自定义 Command

```bash
# 创建 Command 文件
mkdir -p commands/my-domain
cat > commands/my-domain/my-command.md << 'EOF'
# /automotive-my-command

## 功能描述
执行[特定任务]。

## 参数
- `--target <文件>`: 目标文件路径
- `--level <级别>`: 分析级别 (basic/full)

## 使用示例
```
/automotive-my-command --target src/my_module.c --level full
```

## Agent 行为
激活后，执行以下步骤：
1. 读取目标文件
2. 应用[专业分析]
3. 生成报告
EOF
```

### 13.4 使用代码生成脚本

```bash
# 批量生成 Skills（覆盖 37 个汽车领域）
python scripts/generate_skills.py --domains all

# 生成编排 Agents（40 种模式）
python scripts/generate_orchestration_agents.py

# 生成领域视角 Agents（27 个领域）
python scripts/generate_domain_agents.py --domain battery

# 一键生成所有资产
python scripts/generate_all.py
```

### 13.5 贡献代码规范

提交 Pull Request 前，请确保：

```bash
# 1. 运行格式化
make format

# 2. 运行 Lint 检查
make lint

# 3. 运行测试
make test

# 4. 检查测试覆盖率（需 ≥ 80%）
make coverage

# 5. 验证 YAML Schema
python scripts/validate-schema.py agents/my-domain/my-agent.yaml
```

提交信息规范（Conventional Commits）：

```
feat(agents): 添加新的电池热管理 Agent
fix(skills): 修复 UDS 诊断代码生成错误
docs(tutorial): 更新 AUTOSAR 配置教程
test(safety): 添加 HARA 分析单元测试
```

---

## 第十四章：常见问题（FAQ）

### Q1: 安装后命令无法识别，Claude Code 提示"命令不存在"

**原因**: Claude Code 未加载 `~/.claude/` 目录中的命令。

**解决方案**:
```bash
# 检查安装状态
./install.sh --status

# 确认文件已安装到正确路径
ls ~/.claude/commands/ | grep automotive

# 重启 Claude Code
```

### Q2: LLM Council 功能无法使用，提示 Azure API 错误

**原因**: 未配置 Azure OpenAI 密钥。

**解决方案**:
```bash
# 在 .env 文件中添加
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/

# 验证连接
curl -H "api-key: $AZURE_OPENAI_API_KEY" \
  "$AZURE_OPENAI_ENDPOINT/openai/models?api-version=2024-02-01"
```

### Q3: MISRA C 检查总是报告大量错误，如何调整严格程度？

**原因**: 默认启用全部 MISRA C:2012 强制规则。

**解决方案**:

编辑 `rules/coding-standards/misra-c-2012.md`，注释掉不适用的规则：

```markdown
<!-- 对于原型阶段，可临时关闭部分规则 -->
<!-- Rule 15.5: 允许多个 return 语句 (PROTOTYPE ONLY) -->
```

或在代码中使用偏差注释：
```c
/* DEVIATION: MISRA C:2012 Rule 11.3
   Reason: Hardware register access requires pointer cast
   Approval: Safety Team, 2026-05-11 */
```

### Q4: 如何查看某个 Agent 支持哪些具体功能？

```
# 在 Claude Code 中查询
/automotive-help --agent functional-safety

# 或查看 Agent 定义文件
cat agents/functional-safety/*.yaml
```

### Q5: 执行 HARA 分析时如何指定系统边界？

```
/automotive-safety-hara

分析系统: [系统名称]
系统边界（包含）:
- ECU 软件
- 传感器接口

系统边界（排除）:
- 传感器硬件本身
- 执行器机械部分

运行工况:
- 正常行驶 (0-200 km/h)
- 停车场低速 (0-20 km/h)
```

### Q6: 安装后如何更新到最新版本？

```bash
# 拉取最新代码
git pull origin main

# 重新安装（追加模式，安全更新）
./install.sh

# 验证更新结果
./install.sh --status
```

### Q7: 如何在 CI/CD 流水线中集成此工具包？

在 `.github/workflows/automotive-ci.yml` 中：

```yaml
name: Automotive Software CI

on: [push, pull_request]

jobs:
  automotive-checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Install Automotive Agents
        run: |
          git clone https://github.com/sydyg/automotive-claude-code-agents
          cd automotive-claude-code-agents
          ./install.sh --ci-mode
          
      - name: MISRA C Check
        run: make lint
        
      - name: Safety Annotation Check
        run: python scripts/check-safety-annotations.py src/
        
      - name: Run Tests with Coverage
        run: make coverage
```

### Q8: 工具包会覆盖我已有的 Claude 配置吗？

**不会**。工具包采用追加安装（Append-Only）策略：
- 所有资产使用 `automotive-` 前缀，不与现有资产冲突
- 绝不修改已有配置文件
- 可随时通过 `./install.sh --uninstall` 完整卸载

### Q9: 如何报告 Bug 或请求新功能？

1. 在 [GitHub Issues](https://github.com/sydyg/automotive-claude-code-agents/issues) 提交问题
2. 使用对应模板：
   - Bug Report: 说明复现步骤、期望行为、实际行为
   - Feature Request: 说明使用场景、提议实现方案
3. 安全漏洞：请通过 [SECURITY.md](../SECURITY.md) 私下报告

### Q10: 工具包支持哪些 Claude Code 版本？

| Claude Code 版本 | 支持状态 |
|----------------|---------|
| Claude Code 最新版 | ✅ 完全支持 |
| Claude Code v1.x | ✅ 支持（部分功能受限） |
| 其他 AI 编码工具 | ❌ 不支持 |

---

## 学习路径推荐

### 嵌入式 ECU 工程师（8周）

| 周 | 学习目标 | 实践任务 |
|----|---------|---------|
| 1-2 | 安装 + 基础命令 | 审查现有代码，生成 MISRA 报告 |
| 3-4 | AUTOSAR Classic | 创建第一个 SWC 组件 |
| 5-6 | 功能安全入门 | 执行 HARA，生成安全需求 |
| 7-8 | 诊断开发 | 实现完整 UDS 服务 |

### 自动驾驶算法工程师（6周）

| 周 | 学习目标 | 实践任务 |
|----|---------|---------|
| 1-2 | ADAS Agent 入门 | 生成感知算法框架 |
| 3-4 | SOTIF 分析 | 执行性能限制分析 |
| 5-6 | 测试自动化 | 搭建 SIL 仿真测试 |

### 电池/新能源工程师（4周）

| 周 | 学习目标 | 实践任务 |
|----|---------|---------|
| 1-2 | BMS 算法开发 | 实现 SOC 估算 |
| 3-4 | 安全合规 | UN 38.3 合规分析 |

---

*本教程手册配套 [详细说明书](AUTOMOTIVE_AGENTS_REFERENCE.md) 使用*  
*项目主页: [GitHub](https://github.com/sydyg/automotive-claude-code-agents)*  
*版本: v1.0.0 | 更新: 2026-05-11*
