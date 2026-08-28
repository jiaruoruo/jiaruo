# CAD 文件解析与导入库
## 技术设计方案 & 项目开发计划

**文档版本**：V1.0  
**日期**：2026-08-13  
**状态**：草稿

---

## 目录

1. [项目概述](#1-项目概述)
2. [需求分析](#2-需求分析)
3. [文件格式深度分析](#3-文件格式深度分析)
4. [总体技术方案](#4-总体技术方案)
5. [系统架构设计](#5-系统架构设计)
6. [模块详细设计](#6-模块详细设计)
7. [C++ 接口设计](#7-c-接口设计)
8. [开发计划](#8-开发计划)
9. [团队与费用](#9-团队与费用)
10. [风险管理](#10-风险管理)
11. [交付物清单与验收标准](#11-交付物清单与验收标准)

---

## 1. 项目概述

### 1.1 背景

某商用仿真软件平台需要支持从主流工业 CAD 软件（Siemens NX）导入三维模型文件，以用于工程仿真分析工作。当前仿真平台仅支持标准格式输入，无法直接读取客户提供的 NX 原生格式（`.prt`）及 Parasolid 中性格式（`.x_t`）文件。

### 1.2 项目目标

开发一套**自研 C++ 动态库**，实现以下功能：

- 解析 Siemens NX 原生零件/装配体文件（`.prt`）
- 解析 Parasolid 中性传输格式文件（`.x_t`）
- 提取几何体、拓扑结构、装配层级及零件属性
- 将以上数据转换输出为 STEP（`.stp`）格式
- 通过 C++ 接口供仿真软件调用，实现无缝集成（用户无需手动二次导入）
- 在麒麟操作系统（x86_64，GCC 7.5+）上稳定运行

### 1.3 交付形式

- C++ 动态库（`.so`）及静态库（`.a`）
- 公开头文件（`.h`）
- 源代码
- 接口文档及集成指南
- 测试报告
- 麒麟系统适配报告

---

## 2. 需求分析

### 2.1 功能需求

| 编号 | 需求描述 | 优先级 |
|------|---------|--------|
| F-01 | 解析 NX .prt 零件文件，提取 B-Rep 几何体 | P0 |
| F-02 | 解析 NX .prt 装配体文件，提取装配层级结构 | P0 |
| F-03 | 解析 Parasolid .x_t 文件，提取几何体数据 | P0 |
| F-04 | 将解析结果输出为 STEP AP203/AP214 格式 | P0 |
| F-05 | 提供 C++ 统一调用接口，支持仿真软件集成 | P0 |
| F-06 | 保留零件属性（名称、材质、重量等） | P1 |
| F-07 | 保留装配体中的坐标变换矩阵 | P1 |
| F-08 | 支持批量转换（多文件同时处理） | P2 |
| F-09 | 提供几何完整性验证接口 | P2 |

### 2.2 非功能需求

| 编号 | 需求描述 | 指标 |
|------|---------|------|
| NF-01 | 运行平台 | 麒麟 OS（基于 Linux），x86_64 |
| NF-02 | 编译器 | GCC 7.5+ |
| NF-03 | 几何精度 | 与原始文件误差 < 1×10⁻⁴ mm |
| NF-04 | 转换性能 | 100MB 以内文件转换时间 < 60s |
| NF-05 | 接口稳定性 | ABI 兼容，不破坏已有集成 |
| NF-06 | 无商业 SDK 依赖 | 不依赖 NX/Creo Toolkit 授权 |
| NF-07 | 线程安全 | 支持多线程并发调用 |

### 2.3 文件规格约束（基于样本文件确认）

| 文件类型 | 来源软件 | 确认版本 | 文件大小范围 |
|---------|---------|---------|------------|
| `.prt` 零件 | Siemens NX 6.x ~ 8.5 | 已确认 | 100KB ~ 数十 MB |
| `.prt` 装配 | Siemens NX 6.x ~ 8.5 | 已确认 | 100KB ~ 数十 MB |
| `.x_t` | Parasolid 25.x | 已确认 | 10KB ~ 数 MB |

---

## 3. 文件格式深度分析

> **基于样本文件实际二进制分析（2026-08-13）**

### 3.1 NX .prt 文件格式

#### 3.1.1 文件头识别

```
偏移  内容
0000: D0 CF 11 E0 A1 B1 1A E1  ← OLE2 复合文档签名（100%确认）
0008: [UUID] 00 00 00 00 00 00
0018: 3E 00 03 00 FE FF 09 00  ← OLE2版本及扇区大小参数
```

**结论**：NX .prt 使用 **OLE2（Microsoft Compound Document）** 作为外层容器格式。

#### 3.1.2 内部结构

OLE2 容器内包含以下关键数据流（通过字符串分析确认）：

| 流名称 | 内容 | 用途 |
|--------|------|------|
| `UgAttributes` (XML) | `<UgAttributes version="3">...` | 零件属性（材质、设计者等） |
| `UGS::OM::RootObject` | NX对象管理器根 | 对象树入口 |
| `UGS::Solid::Body` | **Parasolid 几何体数据** | ★ 核心几何 |
| `UGS::Solid::Topol` | 拓扑关系 | 面/边/顶点引用 |
| `UGS::MATRIX` | 4×4变换矩阵 | 坐标变换 |
| `UGS::Assy::ReferenceSet` | 组件引用列表 | 装配结构 |
| `UGS::Facet::JT::Body` | JT 可视化网格 | 仅用于显示（不含精确几何） |
| `UGS::LAYER/COLOR` | 图层/颜色 | 显示属性 |

#### 3.1.3 关键技术发现

**NX 使用 Parasolid 作为底层几何内核**（Siemens 同时拥有 NX 和 Parasolid）。  
`UGS::Solid::Body` 流中存储的是 **Parasolid 二进制格式（`.x_b`）**的几何数据。

这意味着：**NX .prt 解析 = OLE2 容器拆包 + Parasolid 二进制几何解析**

#### 3.1.4 属性数据（XML，偏移 0x800）

```xml
<UgAttributes version="3">
  <Attribute title="MaterialMissingAssignments" value="TRUE" .../>
  <Attribute title="DESIGNER"    value="" .../>
  <Attribute title="APPROVER"    value="" .../>
  <Attribute title="Material"    value="" .../>
  <Attribute title="WEIGHT"      value="" .../>
  ...
</UgAttributes>
```

---

### 3.2 Parasolid .x_t 文件格式

#### 3.2.1 文件头结构

```
**PART1;
MC=x64/Windows NT;
APPL=unigraphics;          ← 来源：NX
FORMAT=text;               ← 文本格式（可读）
SCH=SCH_2500176_25001;     ← Parasolid Schema 25.x
KEY=zhan;                  ← 模型名称
DATE=13-aug-2026;
**PART2;
SCH=SCH_2500176_25001;
**PART3;
**END_OF_HEADER
T51 : TRANSMIT FILE ...    ← 正文开始
```

#### 3.2.2 数据编码

正文采用**紧凑数值编码**：

```
6189 0 10 255 1 4 0 0 0 ...  ← 实体类型码 + 属性序列
29 0 28 30 0 0 +-.01 0 0 1 0 0 .2 0 0  ← 面法向量 + 坐标
```

Parasolid .x_t 的几何类型包括：
- **拓扑实体**：`body`、`lump`、`shell`、`face`、`loop`、`edge`、`vertex`
- **几何基元**：`plane`、`cylinder`、`cone`、`sphere`、`torus`
- **自由曲面**：`bspline_surface`（B样条）
- **曲线**：`line`、`arc`、`bspline_curve`

---

### 3.3 STEP .stp 文件格式（目标输出）

#### 3.3.1 文件特征（基于 z2_asm1.stp 分析）

```
ISO-10303-21;
HEADER;
  originating_system = 'SIEMENS PLM Software NX 8.5';
  FILE_SCHEMA(('CONFIG_CONTROL_DESIGN'));  ← AP203
ENDSEC;
DATA;
  #296=PRODUCT('z2_asm1','z2_asm1',...);  ← 装配体
  #294=PRODUCT('tuojia_model1',...);       ← 子零件1
  #295=PRODUCT('g2_model1',...);           ← 子零件2
  #309=MANIFOLD_SOLID_BREP(...);           ← B-Rep实体
  #313=CYLINDRICAL_SURFACE('',#621,100.); ← 圆柱面 R=100mm
  ...
END-ISO-10303-21;
```

#### 3.3.2 关键实体类型

| STEP 实体 | 含义 |
|-----------|------|
| `MANIFOLD_SOLID_BREP` | 封闭实体（B-Rep） |
| `ADVANCED_BREP_SHAPE_REPRESENTATION` | 高级BRep表示 |
| `NEXT_ASSEMBLY_USAGE_OCCURRENCE` | 装配使用关系 |
| `CARTESIAN_POINT` | 坐标点 |
| `DIRECTION` | 方向向量 |
| `PLANE` / `CYLINDRICAL_SURFACE` | 几何面 |
| `EDGE_LOOP` / `FACE_OUTER_BOUND` | 拓扑边界 |

单位：mm（`SI_UNIT(.MILLI.,.METRE.)`）

---

## 4. 总体技术方案

### 4.1 核心技术发现与简化

**基于文件格式实际分析，确认所有输入格式底层均使用 Parasolid 几何：**

```
NX .prt  →  OLE2 容器  →  内部 Parasolid 几何（.x_b 二进制）
.x_t     →  Parasolid 文本格式（.x_t）
```

**这一发现使技术方案得到根本性简化：**

```
原方案（误判为Pro/E）：        实际方案（NX共享Parasolid）：
  Pro/E解析器                    OLE2拆包（简单）
    +                    →           +
  Parasolid解析器                统一 Parasolid 解析引擎
= 2套独立引擎                  = 1套引擎覆盖所有格式
```

### 4.2 技术选型

| 组件 | 选择 | 理由 |
|------|------|------|
| 语言标准 | C++17 | GCC 7.5+ 完整支持 |
| 构建系统 | CMake 3.14+ | 跨平台，麒麟适配方便 |
| OLE2 解析 | 自研轻量实现（参考 MS-CFB 规范） | 无额外依赖，代码可控 |
| Parasolid 解析 | 自研解析器（.x_t + .x_b） | 核心能力，完全自主 |
| STEP 输出 | OpenCASCADE Technology（OCCT 7.x，LGPL） | 开源合规，STEP写出最成熟 |
| 单元测试 | Google Test（gtest） | 业界标准 |
| 文档生成 | Doxygen | C++ API 文档自动化 |
| 日志 | spdlog（header-only） | 轻量无依赖 |

### 4.3 数据流全景

```
输入                     处理层                        输出
─────────────────────────────────────────────────────────────
                    ┌─ OLE2拆包 ─────────────┐
NX .prt ───────────▶│  提取 Parasolid .x_b   │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
.x_t ──────────────▶  Parasolid 统一解析引擎  │──▶  内部 BRep 模型
                    │  (.x_t 文本 / .x_b 二进制)│     (几何+拓扑+属性)
                    └─────────────────────────┘
                                 │
                                 ▼
                    ┌─────────────────────────┐
                    │   STEP AP214 输出        │──▶  .stp 文件
                    │   (基于 OCCT)           │     (供仿真软件使用)
                    └─────────────────────────┘
─────────────────────────────────────────────────────────────
```

---

## 5. 系统架构设计

### 5.1 库架构总览

```
libcad2step.so / libcad2step.a
┌────────────────────────────────────────────────────────────┐
│                   Public C++ API 层                        │
│              (cad2step.h — 对外唯一接口)                   │
├────────────────────────────────────────────────────────────┤
│   NX .prt 模块          │   .x_t 模块                     │
│  ┌──────────────────┐   │  ┌──────────────────────────┐   │
│  │ OLE2Reader       │   │  │ XtLexer (词法分析)        │   │
│  │ UgsStreamLocator │   │  │ XtParser (语法分析)       │   │
│  │ XbExtractor      │   │  │ XtGeomHandler             │   │
│  └────────┬─────────┘   │  └────────────┬─────────────┘   │
│           │              │               │                 │
├───────────┴──────────────┴───────────────┘                 │
│                                                            │
│           Parasolid 统一解析引擎                            │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  ParasolidKernel                                    │  │
│  │  ├── BodyParser      (Body / Lump / Shell)          │  │
│  │  ├── TopologyBuilder (Face / Loop / Edge / Vertex)  │  │
│  │  ├── GeometryDecoder (Plane/Cylinder/BSpline...)    │  │
│  │  └── AssemblyResolver (装配实例变换)                 │  │
│  └─────────────────────────────────────────────────────┘  │
│                          │                                  │
│               内部 BRep 数据模型                            │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  BRepModel                                          │  │
│  │  ├── Solid (实体)                                   │  │
│  │  │    ├── Shell / Face / Loop / Edge / Vertex       │  │
│  │  │    └── Surface / Curve / Point (几何)            │  │
│  │  ├── AssemblyTree (装配树)                          │  │
│  │  │    └── Node { 变换矩阵, 子节点引用 }              │  │
│  │  └── AttributeMap (属性: 名称/材质/颜色等)           │  │
│  └─────────────────────────────────────────────────────┘  │
│                          │                                  │
│               STEP AP214 输出层 (基于OCCT)                  │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  StepExporter                                       │  │
│  │  ├── BRepToOcct     (BRep → OCCT TopoDS_Shape)      │  │
│  │  ├── AssemblyMapper (装配树 → STEP产品结构)          │  │
│  │  └── StepWriter     (OCCT STEPControl_Writer)       │  │
│  └─────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

### 5.2 项目目录结构

```
libcad2step/
├── CMakeLists.txt
├── cmake/
│   ├── FindOCCT.cmake
│   └── CompilerFlags.cmake           # GCC 7.5+ 编译选项
├── include/                           # 公开头文件（交付给调用方）
│   └── cad2step/
│       ├── cad2step.h                 # 主入口接口
│       ├── convert_result.h           # 转换结果类型
│       ├── brep_types.h               # 几何数据类型定义
│       └── convert_options.h          # 配置选项
├── src/
│   ├── ole2/                          # OLE2 容器解析
│   │   ├── Ole2Reader.h/cpp           # OLE2文件读取
│   │   ├── Ole2Stream.h/cpp           # 数据流访问
│   │   └── Ole2DirectoryEntry.h/cpp   # 目录项解析
│   ├── nx/                            # NX .prt 专用
│   │   ├── NxPrtParser.h/cpp          # .prt 主解析器
│   │   ├── UgsStreamLocator.h/cpp     # UGS流定位
│   │   ├── NxAttributeReader.h/cpp    # XML属性解析
│   │   └── NxAssemblyReader.h/cpp     # 装配结构解析
│   ├── parasolid/                     # Parasolid 统一引擎
│   │   ├── ParasolidKernel.h/cpp      # 核心调度器
│   │   ├── XtLexer.h/cpp              # .x_t 词法分析器
│   │   ├── XtParser.h/cpp             # .x_t 语法分析器
│   │   ├── XbDecoder.h/cpp            # .x_b 二进制解码
│   │   ├── GeomDecoder.h/cpp          # 几何类型解码
│   │   └── TopoBuilder.h/cpp          # 拓扑结构重建
│   ├── model/                         # 内部数据模型
│   │   ├── BRepModel.h/cpp            # BRep数据模型
│   │   ├── AssemblyTree.h/cpp         # 装配树
│   │   ├── GeomTypes.h                # 基础几何类型
│   │   └── AttributeMap.h/cpp         # 属性容器
│   ├── step/                          # STEP 输出
│   │   ├── StepExporter.h/cpp         # STEP导出主控
│   │   ├── BRepToOcct.h/cpp           # BRep→OCCT转换
│   │   └── AssemblyMapper.h/cpp       # 装配树→STEP产品
│   └── api/
│       └── Cad2StepImpl.cpp           # 公开接口实现
├── tests/
│   ├── unit/
│   │   ├── test_ole2_reader.cpp
│   │   ├── test_xt_lexer.cpp
│   │   ├── test_xt_parser.cpp
│   │   ├── test_xb_decoder.cpp
│   │   ├── test_nx_parser.cpp
│   │   ├── test_step_output.cpp
│   │   └── test_assembly.cpp
│   ├── integration/
│   │   └── test_end_to_end.cpp
│   └── testdata/
│       ├── z2_asm1.prt
│       ├── g2_model1.prt
│       ├── tuojia_model1.prt
│       └── zhan.x_t
└── docs/
    ├── format_research/
    │   ├── nx_prt_format.md           # NX格式分析文档
    │   └── parasolid_xt_format.md     # Parasolid格式文档
    └── api/
        └── API_Reference.md           # 接口参考文档
```

---

## 6. 模块详细设计

### 6.1 OLE2 解析模块

**职责**：读取 NX .prt 文件的 OLE2 容器，定位并提取 Parasolid 几何数据流。

**OLE2 格式核心（MS-CFB 规范）：**

```
文件结构：
├── 头部 (512字节): 签名、FAT表位置、扇区大小(512/4096字节)
├── FAT (File Allocation Table): 扇区链表
├── 目录流: 所有 Stream/Storage 的元数据
└── 数据扇区: 实际数据按扇区存储
```

**关键类设计：**

```cpp
class Ole2Reader {
public:
    bool open(const std::string& path);
    
    // 列出所有流名称
    std::vector<std::string> listStreams() const;
    
    // 读取指定流数据
    std::vector<uint8_t> readStream(const std::string& name) const;
    
    // 快速定位UGS Parasolid流
    std::vector<uint8_t> extractParasolidGeometry() const;
};
```

**定位 Parasolid 流的策略：**
1. 遍历 OLE2 目录条目
2. 查找名称匹配 `UGS::Solid::*` 的流
3. 识别 Parasolid 二进制（`.x_b`）标识头
4. 提取完整二进制几何数据

---

### 6.2 Parasolid 统一解析引擎

**职责**：处理两种 Parasolid 数据来源：
- `.x_t`（文本格式，来自直接文件）
- `.x_b`（二进制格式，从 NX .prt 中提取）

#### 6.2.1 .x_t 词法分析器（XtLexer）

```cpp
// Token 类型（基于zhan.x_t样本分析）
enum class XtToken {
    // 实体类型
    INTEGER, FLOAT, STRING, IDENTIFIER,
    // 控制符
    PLUS, MINUS, QUESTION, NEWLINE,
    // Parasolid 实体码（数字形式）
    ENTITY_CODE
};

class XtLexer {
public:
    // 处理 zhan.x_t 中的紧凑数值编码
    // 示例: "6189 0 10 255 1 4 0 0 0 0 0 0 0 1e3 1e-8"
    XtToken nextToken();
    double  getFloat() const;
    int     getInt() const;
};
```

#### 6.2.2 几何类型解码器

基于 Parasolid .x_t 样本，支持以下几何类型：

| 类型码 | 几何类型 | 参数说明 |
|--------|---------|---------|
| `20` | plane | 法向量(x,y,z) + 点坐标 |
| `17` | cylinder | 轴线方向 + 中心点 + 半径 |
| `14` | cone | 轴线 + 顶点 + 半角 |
| `19` | sphere | 中心点 + 半径 |
| `29` | 参数面 | B样条控制点 |
| `30` | 参数曲线 | B样条定义 |

#### 6.2.3 拓扑重建

基于样本文件，.x_t 拓扑实体关系：

```
body (几何体)
└── lump (连通区域)
    └── shell (壳体)
        └── face (面，关联几何类型)
            └── loop (边界环)
                └── fin → edge (边，关联曲线)
                               └── vertex (顶点)
```

---

### 6.3 内部 BRep 数据模型

```cpp
// 几何基础类型
struct Point3D  { double x, y, z; };
struct Vector3D { double x, y, z; };
struct Matrix4x4 { double m[4][4]; };

// 几何面定义
struct Surface {
    enum class Type { Plane, Cylinder, Cone, Sphere, Torus, BSpline };
    Type type;
    std::vector<double> params;  // 类型相关参数
};

// B-Rep 拓扑层级
struct Vertex { Point3D point; };
struct Edge   { int v0, v1; /* vertex indices */ int curve; };
struct Loop   { std::vector<int> edges; };
struct Face   { std::vector<Loop> loops; int surface; bool orientation; };
struct Shell  { std::vector<Face> faces; };
struct Solid  { std::vector<Shell> shells; std::string name; };

// 装配树节点
struct AssemblyNode {
    std::string partName;
    std::string partFile;  // 引用的子零件文件
    Matrix4x4   transform; // 在父装配中的位置
    std::vector<AssemblyNode> children;
};

// 完整 BRep 模型
struct BRepModel {
    std::vector<Solid>   solids;
    AssemblyNode         assemblyRoot;
    AttributeMap         attributes;  // 名称、材质等
};
```

---

### 6.4 STEP AP214 输出模块

基于 OpenCASCADE Technology（OCCT）实现 STEP 写出：

```cpp
class StepExporter {
public:
    // 主导出接口
    bool exportToStep(const BRepModel& model,
                      const std::string& outputPath,
                      const StepOptions& options = {});

private:
    // BRep → OCCT TopoDS_Shape
    TopoDS_Shape buildOcctShape(const Solid& solid);
    TopoDS_Face  buildOcctFace(const Face& face);
    
    // 装配体产品结构 → STEP NEXT_ASSEMBLY_USAGE_OCCURRENCE
    void buildAssemblyStructure(const AssemblyNode& root,
                                Handle(XCAFDoc_ShapeTool) shapeTool);
    
    // 写出 STEP AP214
    bool writeStepFile(const std::string& path);
};
```

**STEP 输出保留内容：**
- 精确 B-Rep 几何（MANIFOLD_SOLID_BREP）
- 装配层级（NEXT_ASSEMBLY_USAGE_OCCURRENCE）
- 零件坐标变换（ITEM_DEFINED_TRANSFORMATION）
- 零件名称（PRODUCT 实体）
- 单位：mm

---

## 7. C++ 接口设计

### 7.1 主接口头文件

```cpp
// cad2step/cad2step.h
// ================================================================
// CAD 文件解析与导入库 - 公开 C++ 接口
// 版本: 1.0.0
// ================================================================
#pragma once
#include <string>
#include <vector>
#include <memory>
#include "convert_result.h"
#include "convert_options.h"

namespace Cad2Step {

/**
 * @brief 主转换器类
 * 
 * 使用示例：
 *   Cad2Step::Converter conv;
 *   auto result = conv.convert("model.prt", "output.stp");
 *   if (result.success) {
 *       // 加载到仿真软件
 *   }
 */
class CAD2STEP_API Converter {
public:
    Converter();
    ~Converter();

    /**
     * @brief 转换单个文件（.prt 或 .x_t）为 STEP
     * @param inputFile  输入文件路径（.prt 或 .x_t）
     * @param outputFile 输出 .stp 文件路径
     * @param options    转换选项（可选）
     */
    ConvertResult convert(const std::string& inputFile,
                          const std::string& outputFile,
                          const ConvertOptions& options = {});

    /**
     * @brief 内存转换（不写磁盘，直接返回STEP数据）
     * @note  供仿真软件内存直传使用，避免临时文件
     */
    ConvertResult convertToMemory(const std::string& inputFile,
                                  std::vector<uint8_t>& stepData,
                                  const ConvertOptions& options = {});

    /**
     * @brief 批量转换
     */
    std::vector<ConvertResult> batchConvert(
        const std::vector<std::string>& inputFiles,
        const std::string& outputDir,
        const ConvertOptions& options = {});

    /**
     * @brief 查询文件信息（不进行完整转换）
     */
    FileInfo queryFileInfo(const std::string& inputFile);

    // 库版本信息
    static std::string getVersion();
    static std::vector<std::string> getSupportedFormats();
};

} // namespace Cad2Step
```

### 7.2 数据类型定义

```cpp
// cad2step/convert_result.h
namespace Cad2Step {

struct ConvertResult {
    bool        success;
    std::string outputPath;       // 输出文件路径
    std::string errorMessage;     // 错误信息（失败时）
    int         solidCount;       // 转换的实体数量
    int         componentCount;   // 装配组件数量
    double      processingTimeMs; // 耗时（毫秒）
    std::string stepVersion;      // 输出STEP版本（AP203/AP214）
};

struct FileInfo {
    std::string format;       // "NX_PRT" 或 "PARASOLID_XT"
    std::string nxVersion;    // NX版本（如 "NX 8.5"）
    bool        isAssembly;   // 是否为装配体
    int         componentCount;
    std::vector<std::string> referencedFiles;  // 引用的子零件
};

} // namespace Cad2Step
```

### 7.3 转换选项

```cpp
// cad2step/convert_options.h
namespace Cad2Step {

struct ConvertOptions {
    // STEP 输出选项
    std::string stepVersion = "AP214";     // "AP203" 或 "AP214"
    bool preserveAssemblyTree = true;      // 保留装配层级
    bool preserveAttributes   = true;      // 保留零件属性
    bool preserveColors       = true;      // 保留颜色信息
    
    // 几何选项
    double precision = 1e-6;               // 几何精度（mm）
    bool   healGeometry = true;            // 自动修复轻微几何问题
    
    // 性能选项
    bool   parallelProcessing = false;     // 多线程处理
    int    maxThreads = 4;                 // 最大线程数
};

} // namespace Cad2Step
```

### 7.4 仿真软件集成方式（内存直传）

```cpp
// 仿真软件集成示例代码（集成指南中提供）
#include "cad2step/cad2step.h"

void SimSoftware::onImportCADFile(const std::string& cadFilePath) {
    Cad2Step::Converter converter;
    
    // 方式1：内存直传（推荐，无临时文件）
    std::vector<uint8_t> stepData;
    auto result = converter.convertToMemory(cadFilePath, stepData);
    if (result.success) {
        this->loadStepFromMemory(stepData);  // 直接加载，用户无感知
    }
    
    // 方式2：临时文件（降级方案）
    std::string tmpFile = getTempPath() + "/~cad2step_" + uuid() + ".stp";
    auto result2 = converter.convert(cadFilePath, tmpFile);
    if (result2.success) {
        this->loadStepFile(tmpFile);
        std::filesystem::remove(tmpFile);   // 自动清理临时文件
    }
}
```

---

## 8. 开发计划

### 8.1 项目里程碑

| 里程碑 | 时间节点 | 内容 |
|--------|---------|------|
| **M0** | 第2周末 | 技术预研完成，OLE2格式验证，开发环境就绪 |
| **M1** | 第6周末 | .x_t 解析模块完成并通过测试 |
| **M2** | 第10周末 | NX .prt 解析模块完成并通过测试 |
| **M3** | 第11周末 | 统一 C++ 接口封装完成 |
| **M4** | 第12周末 | 麒麟系统适配完成 |
| **M5** | 第13周末 | 全量测试、文档完成 |
| **M6** | 第14周末 | 集成联调、正式交付 |

### 8.2 详细开发计划（14周）

#### 阶段一：技术预研与环境搭建（第1-2周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| 搭建 Linux x86_64 开发环境 | 全员 | 2天 | 开发环境 |
| 搭建麒麟OS测试环境 | 全员 | 1天 | 测试环境 |
| 编译验证 OCCT 在麒麟上可用 | 工程师A | 2天 | OCCT验证报告 |
| OLE2 格式深度研究与原型 | 工程师B | 3天 | OLE2解析原型 |
| Parasolid .x_t 格式规范整理 | 工程师A | 2天 | 格式规范文档 |
| 确认接口设计，评审 | 全员 | 1天 | 接口定义草案 |

#### 阶段二：基础框架搭建（第2-3周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| CMake 项目框架，编译选项 | 工程师B | 2天 | 可编译骨架 |
| BRep 内部数据模型设计实现 | 工程师A | 3天 | BRepModel |
| OLE2 Reader 完整实现 | 工程师B | 3天 | Ole2Reader |
| 基础工具类（日志/错误处理） | 工程师A | 2天 | 基础组件 |

#### 阶段三：.x_t 解析模块（第3-7周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| XtLexer 词法分析器 | 工程师A | 5天 | XtLexer |
| XtParser 语法分析器 | 工程师A | 5天 | XtParser |
| 基础几何类型解码（平面/圆柱）| 工程师B | 4天 | 基础几何 |
| B样条曲面解码 | 工程师A | 5天 | BSpline支持 |
| 拓扑结构重建 | 工程师B | 5天 | TopoBuilder |
| .x_t → STEP 端到端验证 | 工程师A/B | 3天 | M1验收测试 |

**M1 验收标准**：zhan.x_t 样本文件成功转换为 .stp，且 STEP 文件可被标准软件打开验证。

#### 阶段四：NX .prt 解析模块（第7-10周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| UGS 流定位算法 | 工程师B | 3天 | UgsStreamLocator |
| Parasolid .x_b 二进制解码 | 工程师A | 7天 | XbDecoder |
| NX 属性 XML 解析 | 工程师B | 2天 | NxAttributeReader |
| NX 装配体结构解析 | 工程师B | 4天 | NxAssemblyReader |
| .prt → STEP 端到端验证 | 工程师A/B | 4天 | M2验收测试 |

**M2 验收标准**：z2_asm1.prt / g2_model1.prt 成功转换，与参考 z2_asm1.stp 几何一致性 > 99%。

#### 阶段五：接口封装与集成（第10-11周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| 公开 C++ API 实现 | 工程师B | 3天 | libcad2step.so |
| 内存直传接口实现 | 工程师A | 2天 | convertToMemory |
| 批量转换功能 | 工程师B | 2天 | batchConvert |
| 错误码体系完善 | 工程师A | 1天 | 错误处理 |

#### 阶段六：麒麟系统适配（第11-12周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| 麒麟 OS 编译全量测试 | 工程师B | 3天 | 编译通过 |
| 运行时依赖分析（ldd） | 工程师B | 1天 | 依赖清单 |
| 性能基准测试 | 工程师A | 2天 | 性能报告 |
| 多线程安全性验证 | 工程师A | 2天 | 安全验证 |
| **麒麟适配报告**编写 | 工程师B | 2天 | **交付物4** |

#### 阶段七：测试与文档（第12-13周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| 单元测试完善（覆盖率>80%） | 工程师A | 4天 | 测试代码 |
| 边界条件测试（损坏/超大文件）| 工程师B | 2天 | 边界测试 |
| API 参考文档（Doxygen）| 工程师A | 2天 | **交付物3** |
| 集成指南编写 | 工程师B | 2天 | 集成指南 |
| **测试报告**整理 | 工程师A | 2天 | **交付物5** |

#### 阶段八：集成联调与交付（第13-14周）

| 任务 | 负责 | 工时 | 产出 |
|------|------|------|------|
| 配合甲方集成（**交付物6**）| 全员 | 3天 | 集成验证 |
| 问题修复与回归 | 全员 | 2天 | 问题修复记录 |
| 最终打包（源码+库+文档）| 工程师B | 2天 | **全量交付包** |

---

## 9. 团队与费用

### 9.1 团队配置

| 角色 | 人数 | 核心能力要求 |
|------|------|------------|
| 技术负责人（兼架构师） | 1 | C++17、二进制格式解析、CAD几何经验 |
| 高级C++工程师 | 2 | C++17、Linux开发、几何算法 |
| 测试工程师 | 1 | gtest、自动化测试（后8周参与） |

> 注：鉴于项目技术难度高，C++ 工程师需有相关工业软件或几何算法开发背景。

### 9.2 工期与费用估算

**项目总工期：14 周**

| 人员 | 工作天数 | 日费率（元） | 小计（万元） |
|------|---------|------------|------------|
| 技术负责人 | 70天 | 2,500 | 17.5 |
| 高级C++工程师 ×2 | 70天×2 | 1,800 | 25.2 |
| 测试工程师 | 40天 | 1,000 | 4.0 |
| **人力小计** | | | **46.7** |
| 风险储备金（15%） | | | 7.0 |
| 项目管理（10%） | | | 4.7 |
| **合计** | | | **约 58 万元** |

### 9.3 建议付款节点

| 节点 | 比例 | 金额（参考） | 触发条件 |
|------|------|------------|---------|
| 合同签署预付 | 20% | ~11.6万 | 签约后 |
| M1 验收（.x_t模块） | 20% | ~11.6万 | .x_t→STP通过测试 |
| M2 验收（.prt模块） | 30% | ~17.4万 | .prt→STP通过测试 |
| M4 验收（麒麟适配） | 20% | ~11.6万 | 麒麟系统验证通过 |
| M6 最终验收 | 10% | ~5.8万 | 集成联调完成 |

---

## 10. 风险管理

### 10.1 风险矩阵

| 风险ID | 风险描述 | 概率 | 影响 | 级别 | 应对措施 |
|--------|---------|------|------|------|---------|
| R-01 | Parasolid .x_b 二进制格式逆向困难 | 中 | 高 | 🔴 | 预留充足工时；备选：尝试NX批处理导出.x_t |
| R-02 | 不同NX版本(.prt) OLE2结构差异 | 中 | 中 | 🟡 | 明确支持版本范围；版本检测逻辑 |
| R-03 | 麒麟OS上OCCT依赖缺失 | 低 | 中 | 🟡 | 预研阶段提前验证；必要时静态链接 |
| R-04 | 测试样本文件不足导致覆盖不全 | 中 | 中 | 🟡 | 尽早收集多版本NX文件；阶段性提交测试 |
| R-05 | 几何精度损失不满足仿真要求 | 低 | 高 | 🟡 | STEP输出精度参数可调；与甲方确认精度标准 |
| R-06 | 仿真软件集成接口不兼容 | 低 | 中 | 🟢 | 提前获取仿真软件API文档；预留适配工时 |
| R-07 | 工期超预期 | 中 | 中 | 🟡 | 分阶段交付；.x_t模块优先交付保底 |

### 10.2 风险缓解机制

**针对 R-01（最高风险）的详细应对：**

```
主路径: 逆向解析 Parasolid .x_b（NX内部格式）
  │ 如果受阻（超出预设工时25%）
  ▼
备用路径A: 研究 NX 批处理脚本，将 .prt 自动导出为 .x_t
  │ 如果NX不可用
  ▼  
备用路径B: 仅支持 .x_t 输入，.prt 转换需配合NX环境预处理
           （分阶段交付，优先保证 .x_t 功能可用）
```

---

## 11. 交付物清单与验收标准

| 编号 | 交付物 | 格式 | 验收标准 |
|------|--------|------|---------|
| **D-01** | `.prt` 导入模块（源码） | C++源码 | 代码可在麒麟编译，通过单元测试 |
| **D-02** | `.prt` 导入模块（编译库） | `.so` + `.a` | 可动态链接，接口符合规范 |
| **D-03** | `.x_t` 导入模块（源码） | C++源码 | 代码可在麒麟编译，通过单元测试 |
| **D-04** | `.x_t` 导入模块（编译库） | `.so` + `.a` | 可动态链接，接口符合规范 |
| **D-05** | C++ 接口头文件 | `.h` | 完整定义所有公开接口 |
| **D-06** | API 参考文档 | Markdown/HTML | Doxygen自动生成，示例代码可运行 |
| **D-07** | 集成指南 | Markdown/PDF | 含仿真软件集成示例代码 |
| **D-08** | 麒麟系统适配报告 | PDF/Word | 含编译步骤、运行验证、性能数据 |
| **D-09** | 单元测试用例 | gtest源码 | 覆盖率 > 80% |
| **D-10** | 测试报告 | PDF | 全部测试通过，含几何精度验证 |
| **D-11** | 集成联调支持 | 现场/远程 | 甲方仿真软件集成验证通过 |

### 最终验收核心指标

1. ✅ 三种格式（.prt/.x_t）均能成功转换为 .stp
2. ✅ 转换后 .stp 几何与原文件误差 < 1×10⁻⁴ mm
3. ✅ 装配体层级结构完整保留
4. ✅ 在麒麟OS（GCC 7.5+）编译运行无问题
5. ✅ 仿真软件调用后模型自动加载，无需用户手动二次导入
6. ✅ 100MB 文件转换时间 < 60 秒

---

## 附录 A：开发环境配置

```bash
# 麒麟OS开发环境依赖安装
sudo apt-get install build-essential cmake ninja-build
sudo apt-get install libocct-dev  # OpenCASCADE
sudo apt-get install libgtest-dev  # Google Test
sudo apt-get install doxygen      # 文档生成

# 编译命令
cd libcad2step
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release \
         -DCMAKE_CXX_STANDARD=17 \
         -DUSE_KYLIN_OS=ON
cmake --build . -j$(nproc)

# 运行测试
ctest --output-on-failure
```

## 附录 B：Parasolid 版本对照

| SCH版本 | Parasolid版本 | 对应NX版本 |
|--------|--------------|-----------|
| SCH_2500176 | 25.x | NX 8.5~9.0 |
| SCH_2700000 | 27.x | NX 10.x |
| SCH_3000000 | 30.x | NX 12.x |
| SCH_3500000 | 35.x | NX 1926+ |

> 本项目样本文件为 SCH_2500176（Parasolid 25.x / NX 8.5），主要支持此版本范围。

---

*文档结束*  
*如需调整技术方案或补充特定仿真软件集成方案，请联系项目技术负责人。*
