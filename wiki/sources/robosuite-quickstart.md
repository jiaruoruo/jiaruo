---
type: source
title: "机器人学习模拟框架 robosuite 支持强化学习和模仿学习 (1) 快速入门"
date: 2026-04-15
source_url: "https://github.com/ARISE-Initiative/robosuite"
domain: "github.com"
author: ""
tags:
  - robosuite
  - simulation
  - reinforcement-learning
  - imitation-learning
  - mujoco
processed: true
raw_file: "raw/clippings/2026-04-14机器人学习模拟框架 robosuite 支持强化学习和模仿学习 (1) 快速入门.md"
raw_sha256: "eadd42947606994e4c99b5f1f7ec27309403172eb993d39d230dd8207e4f9948"
last_verified: 2026-04-15
possibly_outdated: false
language: "zh"
canonical_source: ""
---

# 机器人学习模拟框架 robosuite 支持强化学习和模仿学习 (1) 快速入门

## Summary

CSDN 技术教程，介绍 robosuite 机器人学习仿真框架（v1.5）的快速入门。robosuite 由斯坦福 SVL 实验室于2017年开发，现由 SVL、UT RPL 和 NVIDIA GEAR 共同维护。基于 MuJoCo 物理引擎，提供标准化基准测试任务、模块化设计和高质量控制器实现，支持强化学习和模仿学习，兼容 OpenAI Gym API。

## Key Points

- **定位**：机器人学习研究仿真框架，基于 MuJoCo，支持强化学习和模仿学习，Gym 兼容 API
- **维护方**：斯坦福 SVL、UT RPL、NVIDIA GEAR 共同维护；GitHub：`ARISE-Initiative/robosuite`
- **支持任务**（19种）：门、升降机、螺母组装、拾取位置、堆叠、工具悬挂、双臂移交/升降机/钉孔/运输、擦拭等
- **支持机器人**（10种）：Baxter、GR1ArmsOnly（人形）、IIWA、Jaco、Kinova3、Panda、Sawyer、SpotWithArmFloating（机器狗带臂）、Tiago、UR5e
- **v1.5 新增**：人形机器人支持、自定义机器人组合、全身控制器（WBC）、遥操作设备扩展、照片级渲染
- **安装**：`pip install robosuite`（macOS/Linux，Python 3.10，依赖 MuJoCo + numpy）；支持源码安装便于开发
- **API 示例**：`suite.make(env_name, robots, has_renderer, use_camera_obs)` → `env.reset()` → `env.step(action)` → `env.render()`

## Concepts Extracted

- [[robot-simulation-framework]]
- [[reinforcement-learning-locomotion]]
- [[embodied-ai]]

## Entities Extracted

- [[robosuite]]

## Contradictions

## My Notes
