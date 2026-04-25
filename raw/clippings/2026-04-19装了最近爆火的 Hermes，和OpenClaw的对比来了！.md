---
created: 2026-04-19T08:57:04 (UTC +08:00)
tags: []
source: https://mp.weixin.qq.com/s/KrZ26wvMvOusJRKtEeFekw
author: Shubham Saboo
---

# 装了最近爆火的 Hermes，和OpenClaw的对比来了！

> ## Excerpt
> Datawhale干货

---
## 

 Datawhale干货 

******作者：**Saboo，谷歌高级AI产品经理********

Google Cloud 高级 AI 产品经理 Shubham Saboo **最新实战干货又来了。**

[上一篇，他公开了自己用 OpenClaw 搭建一支 24小时无休的 AI Agent 团队完整方案。](https://mp.weixin.qq.com/s?__biz=MzIyNjM2MzQyNg==&mid=2247720171&idx=1&sn=36047261489a31e84513556494d432fb&scene=21#wechat_redirect)

但他自己发现了一个问题：**Agent 在跑，但没在进化。然后，他在同一台机器上加了最近爆火的 Hermes，做了一个对照实验，发现了一件和上篇完全不同的事：**

Agent 开始自己写技能文件，自己总结故障手册，完成的工作开始留下可复用的痕迹。想知道AI Agent 怎么从"替你干活"进化到"自己变好"，这篇值得认真读。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/zW6S9vt0cS8oX1JwMdqgvib410VhSlPIPiclpblEJCkUCWfOshxZB7VsPktYbibKlJNvsRicgAqK3aeFPL3CG3fOX10p9SXP86rhzVEA4IuQTx0/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

在不改变原意的情况下，我们进行了如下整理：

OpenClaw跑了好几个月，我称为“纠正式提示词工程阶段”

我用OpenClaw跑了6个Agent好几个月了。它们确实在工作——研究、写内容、审代码、发通讯，按计划时间自动运行，我早上打开Telegram就能看到结果。

但越跑越发现一件事：**我维护这套系统花的时间，比系统自己进化的时间更多。**

我不停地更新SOUL.md文件，清理过期记忆，在不同Agent上重复同样的纠错。Agent没有变好——是我越来越擅长管理它们。这两件事看起来像，但本质上完全不同。

我把这套方法叫"纠正式提示词工程"。

流程是这样的：观察Agent输出，发现问题，解释如何修正，更新记忆或指令，等待行为固定下来。Kelly（我的Agent团队的一员）早期的草稿全是emoji，我告诉她不要emoji、也别用标签、句子要短要有力，一周后她学会了。Dwight（Agent团队的另一员）抓取了太多无关信息，我让他把注意力放在有效信息上，他也做了调整。

这套循环有效。但它有一个隐含的前提：你是一个学习系统。

每一次进步都依赖你发现问题、诊断问题、把修正写下来。Agent不会在你睡着的时候变好——它们只在你关注并修正它们的时候变好。

对照实验：给OpenClaw加了爆火的Hermes Agent

我继续让OpenClaw小队正常运作，但在Hermes Agent上又部署了一个叫 Monica 的实例。任务、使用的Mac Mini和访问Dwight情报文件的权限都一样。不是替换，是加了一个对照组。

Hermes Agent是Nous Research的开源项目。安装只需一条命令：

```
<span leaf="">curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash</span>
```

然后运行“`hermes setup”`。它检测到Mac Mini上的OpenClaw，主动提出导入设置、记忆和API密钥。设置 Telegram 时，它一步步引导我通过 BotFather，发完token就接通了。

有一个建议：**用前沿模型。因为学习循环需要更强的推理能力才能跑好。**

OpenClaw Vs Hermes 对比来了

第一个不同

第一个让我觉得不一样的时刻，是我去检查`~/.hermes/skills/`目录，发现了一些我没有创建的文件，顿时恍然大悟。

其中一个叫`local-writing-canon-analysis/SKILL.md`。Monica写了一个流程：在起草我风格的内容之前，先读我已发布的文章。不是笼统地声称“我了解你的风格”，而是先读已发布的作品，然后从那些经过编辑最后保留下来的文本中推断出我的写作语气。  

文件里有一个具体的编辑规则：保留复利型论点，不把新话题当作产品对比来呈现，文章应以记忆、重复使用等结果为中心，而不是以功能为主。

这不是我写的，是她写的。她观察了我保留了什么、删除了什么，然后把规律写了下来。

OpenClaw和Hermes的Monica，差别只有一个：**谁在负责改进循环的所有权。**

-   OpenClaw：我发现问题，教她修正的办法，她存起来，下次用。进步依赖我们两个都在场。
    
-   Hermes：复杂任务完成后，她自己评估发生了什么，决定什么值得保留，写进技能文件。我可以检查、编辑、删除——但我不需要主动发起这件事。
    

第二个不同

Hermes还有一件事让我注意到——回溯能力。

我搜索"telegram OR gateway OR restart OR stuck"的时候，它把几周前一次对话的完整排障过程全部浮出来了：轮询冲突的问题、"gateway状态显示正常但不等于真的健康"的教训、实际可行的修复路径。那次对话没有人手动整理进记忆，它就在那里。

工作会留下痕迹——不只是"发生了什么"的记录，而是"下次怎么做"的方法。

让OpenClaw和Hermes，各司其职

两套系统现在同时在跑。

OpenClaw那套处理研究、内容起草、代码审查和邮件通讯，按定时任务跑。Hermes的Monica在同一台Mac Mini上作为首席协调官实验在跑，读的是Dwight在OpenClaw上生成的同一份情报文件。Dwight写DAILY-INTEL.md，Monica读它，并通过磁盘上的一个 Markdown 文件完成交接。

两套都支持agentskills.io标准，技能文件在OpenClaw、Hermes、Claude Code、Cursor之间可以移植。没有任何东西被锁死在一个平台里。

OpenClaw给我手动控制和可预测性，而 Hermes 则为 Monica 带来了一个更能自我维持、持续改进的循环。  

最后总结一下我实践后的经验：把需要完全控制的Agent留在OpenClaw，而需要观察自主进化的Agent，则跑在Hermes上。

![](https://mmbiz.qpic.cn/mmbiz_png/vI9nYe94fsGxu3P5YibTO899okS0X9WaLmQCtia4U8Eu1xWCz9t8Qtq9PH6T1bTcxibiaCIkGzAxpeRkRFYqibVmwSw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=2)

**一起“**点****赞”****三连**↓**
