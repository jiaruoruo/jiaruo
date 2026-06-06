---
created: 2026-05-23T11:27:54 (UTC +08:00)
tags: []
source: https://mp.weixin.qq.com/s/e1vrUYcGE6RToVkl_HcXZQ
author: 猕猴桃
---

# Karpathy、Claude Code之父Boris，最新访谈，把整个程序员圈炸了！

> ## Excerpt
> 假期的时候，红衫AI Ascent 2026 上有两场值得认真看的演讲。一场是 Boris Cherny 的，Claude Code 之父。一场是 Karpathy 的。两个人从不同角度把同一件事讲清楚了。编程的执行层被解决了。但方向层，反而变得更难了。热度特别高，收假了赶紧补个课！Claude Code之父- Boris，现在是怎么工作的？Boris说，2026 年过去5个月，今年彻底没写过一行

---
假期的时候，红衫AI Ascent 2026 上有两场值得认真看的演讲。一场是 Boris Cherny 的，Claude Code 之父。一场是 Karpathy 的。

两个人从不同角度把同一件事讲清楚了。**编程的执行层被解决了。但方向层，反而变得更难了。**

热度特别高，收假了赶紧补个课！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/durt1819APrYCkTUILsjNibkWdxNp1cnZyN8Sfexnu8iat2tz3UOcCB4USjkt0sKt5rfd5I4fkJp8qvJw5SaJxMb9EkokFU2bzG1YFEibGR1bw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

## Claude Code之父- Boris，现在是怎么工作的？

Boris说，2026 年过去5个月，今年彻底没写过一行代码。

而且，他现在基本不坐在电脑前了。日常操作在手机上的 Claude App 里完成。左边一个 Code 选项卡，同时跑 5 到 10 个会话，每个会话里一堆 Agent，平时几百个在线，晚上可能几千个。

他自己发明了一个工作流叫 Sloop。原理很简单，让 Claude 用 Cron 来预约未来的任务，做成循环。每分钟、每五分钟、或每天跑一次。

他现在有几十个循环在跑。一个盯 PR，自动修 CI 或自动 Rebase。一个维护 CI 健康，测试偶尔挂了自己去修。一个每 30 分钟抓一次 Twitter 反馈，分类总结发给他。

有一天他试着挑战极限，一天处理了 150 个 PR。

在 Anthropic 内部的状态现在也改了，全公司没有手写代码了，所有 SQL、所有基础架构，全部模型生成。他的 Claude 在后台循环跑的时候，会自动在 Slack 上跟同事的 Claude 沟通，互相解决问题。

人在睡觉，AI 在 Slack 上互相 @、互相对齐、互相 debug。

这里有个背景： Boris表示在Claude Code刚内测的时候，自己只有 10% 的代码是用它写的。但是，从去年5月 Opus4 出来之后，Claude Code的增长曲线开始起飞，从 4 到 4.5 到 4.6 到 4.7，每次模型更新，都在用户增长上疯狂体现。 他承认，Claude Code可能是一次违背PMF的赌注，但这也算是一个新的模式：为还不存在的模型提前建好 harness。

![](https://mmbiz.qpic.cn/mmbiz_png/durt1819APqpo22LcZ7dwbc5gYFhBupV2a9qrsqDzPP5HHNhFa2I8cSc17pa50RXDULZBoulMiaVMib3TjXicIVDoxSmDUTUOOYMp7U5QGMJ20/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

**对他个人而言，编程的时代已经结束了。**

## Karpathy： Software 3.0

Karpathy 的切入点很有意思。

他讲他之前做了一个叫  Menu Gen 的项目。

功能很简单，拍菜单照片，AI 帮你生成每道菜大概长什么样。他用 vibe coding 搭了一个完整应用，部署到 Vercel，OCR 识别菜名，调图像生成模型。

但是很快他发现，有人做了一个更直接的版本。把照片丢给 Google Gemini，让 Nanobanana 在像素层面直接把菜品图渲染到原始菜单上。输入一张图，输出一张图，中间不需要任何传统应用逻辑。

Karpathy 看完意识到，自己做的整个 Menu Gen 其实已经过时了。那个 App 理论上不该存在。

他把这个现象拉到一个更大的框架。LLM 就是一种新的计算机。传统代码是 Software 1.0，训练神经网络得到的权重是 Software 2.0，Prompting 是 Software 3.0。你往上下文窗口里塞什么，就等于你在编程。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/durt1819APoKiay2MQeFiarKMcLdEvj6dM1LN0BXkNLbqK8KaPZ61rHAJtziaBVu4GbCZEfGViau5liaicN3KB1ZBjia4909ib9ZkbNG2GSLJIkn3Ac/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

另一个很具体的例子是 OpenClaw 的安装方式。以前的工具安装，可能是shell脚本，但是OpenClaw是一段文字说明。把文档扔给你的Agent，Agent 自己读环境，自己判断，自己在循环里 debug，最后自己就装好了。

现在我们要思考的是该给 agent 哪一段文字。

大家不要只关注「编程更快了」。更关键的变化是，更广义的信息处理正在变得可自动化。以前代码处理的是结构化数据，但现在你可以把一批文档丢进去，让模型重新编译这些信息，产出全新的知识结构。这些是以前根本不可能做的事。

## 锯齿状智能

模型的能力非常不均匀，像锯齿。在代码、数学这些高度可验证的领域，几乎比所有人类都厉害。但是一旦脱离这个范围，就可能看起来很蠢。

原因有两层。一是训练方法，最先进的大模型用强化学习调出来的，答案对了就加分，代码恰好是最容易验证对不对的东西。二是实验室自己关注什么，哪些任务经济价值高就往分布里猛塞，代码是最典型的例子。

![](https://mmbiz.qpic.cn/mmbiz_png/durt1819APrMTjedJMibbjCV1NPRAoPb2JYt4tutBpu1ZaGI65jBqZia6IJSGfpPa5J4T19vwia7GfJqel7ww3ZHCOufoOA92HfeDWShkPeLIQ/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

Karpathy还举了一个说明问题的细节，GPT-3.5 到 GPT-4，模型下国际象棋突然变强，当时很多人以为是智能整体提升的副作用。但更可能的原因是预训练数据里被额外加了大量棋谱。实验室决定放什么进去，你就得到什么样的能力分布。

Karpathy说模型不是动物，是幽灵。动物有内在动机、好奇心、自我驱动。模型只是由数据和奖励函数塑形出来的锯齿状实体。你冲它发火不会让它更努力，鼓励它也不会让它更有斗志。它就是统计模拟电路。

而只有理解了这一点，用起来才会更准。

## 人在这个体系里干什么

Boris说，他的角色变成了调度。他关心的是循环怎么跑起来，Agent 之间的依赖怎么自动解决，CI 怎么自己维护。执行全部交出去了。

Karpathy说，人必须负责 specification，必须负责 plan。他说自己其实不太喜欢那些所谓的 plan mode。因为他觉得更关键的是你得和 agent 一起把一份非常细的 spec 设计出来，然后让 agent 填充实现。人负责大框架和约束条件，agent 负责填空。

他给了一个很具体的例子。Menu Gen 里，agent 用 Stripe 支付邮箱去匹配 Google 登录邮箱来分配 credits。但一个人完全可能两边用不同邮箱。这种「邮箱不是用户 ID」的设计判断，agent 做不了。

但是具体的执行细节可以交出去了。比如 PyTorch 里是 keepdims 还是 keepdim，是 dim 还是 axis，这些不需要记了。

但人对底层原理的理解不能丢，tensor 的 storage 和 view 是怎么回事，什么时候在无意义地拷贝内存，这些得自己知道。

Karpathy还引用了一句让他隔两天就想起一次的话，**你可以外包思考，但你不能外包理解。**

## 面试、护城河、创业机会

两人都提到了面试方式要变。

如果还在让候选人刷算法题、解 puzzle，筛选的是上一代工程能力。Karpathy给了一个具体的case，比如 让候选人做一个 Twitter clone，功能完整、安全性高，然后用十个 Codex 或 Claude 实例去攻击他部署的网站，看能不能打穿。谁在这种环境下撑住了，谁才是这个时代的工程师。。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/durt1819APohicUTLhwgicqRKNI4EOtqYow1hPW5UoBCic8TnSgByaIUT6Z0Ru3zyFlCpic4C7DxBGyoPmusq92D4Hpmoz1rDZ0x4VicMKibtk0G0/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

Boris 从团队角度说了一个已经在发生的变化。Claude Code 团队里，工程经理、产品经理、设计师、数据科学家、财务、用户研究员，所有人都在写代码。不是因为他们都是程序员，是因为写代码不再需要专业程序员了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/durt1819APq8mYV0AHzTf89Voel1auiaqxSlAFUiaMr8xf70qe1dr947DzQGC8BpQH07eD2SaNq0r7iccLGRXbF72YcVZws3CDQTLhcEzsa52I/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

当写代码成本降 100 倍，切换成本在 AI 面前不堪一击，模型可以轻松把数据从一个平台迁到另一个。流程效力也在贬值，模型擅长理顺工作流。但网络效应、规模经济、垄断资源依然有效。他的判断，未来 10 年能颠覆现有市场的初创公司会增加 10 倍。

![](https://mmbiz.qpic.cn/mmbiz_png/durt1819APqzQ07iaHzOYKcMcR5nA0nByqicAsrh5jWwCh8l100iapsRCl1tg3krn9sdatYpAr7jBkjOAAicZC2oocXpAKrvVvMpwM2BnDic3icKo/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

Karpathy 给创业者的建议更具体。别追大模型的逃逸速度，去造你自己的 RL 环境。可验证性决定了哪些领域会被率先攻破，很多价值极高的 RL 环境还没被开发出来。如果你能在某个垂直领域构建出足够好的强化学习环境和数据集，就能吃到巨大的杠杆红利。

但是他说这话时笑了一下，「我不方便把答案直接讲透。」

## 写在最后

Boris 引用了一个历史。在 1400 年代欧洲只有 10% 的人识字。印刷机发明后 50 年，出版的文献超过之前一千年的总和。书的成本降了 100 倍。最终全球识字率升到 70%。但作家这个职业依然存在。

编程正在经历同样的事。未来每个人都会编程，就像现在每个人都能读写。但这不是说工程师消失了。是说这个角色的核心能力从「写代码」变成了「知道该让 AI 写什么、以及什么条件绝对不能省」。

执行层的天花板已经被模型捅穿了。 但是又因为模型的锯齿状智能。人在很多地方还不能松手。

这就是 2026 年编程这件事的完整地图。

执行交给模型。方向留给人。

Boris 原始视频：https://www.youtube.com/watch?v=SlGRN8jh2RI

Karpahty原始视频：https://www.youtube.com/watch?v=96jN2OCOfLs

## Claude Code之父- Boris，现在是怎么工作的？
