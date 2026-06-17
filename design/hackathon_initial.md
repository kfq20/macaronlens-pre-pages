# Macaron Lens：从 Chat Agent 到 Living Agent

## Hackathon 项目方案

---

# 一、项目背景

过去两年，大模型已经学会了聊天。

ChatGPT、Claude、Gemini 等产品证明了自然语言交互的价值，但它们仍然存在一个核心问题：

> Agent 只能理解用户描述的世界，而无法理解用户正在经历的世界。

现实生活中的大多数需求并不会以文字形式出现。

例如：

* 用户看到一块牛肉，不知道如何处理；
* 用户面对一桌食物，想知道热量是否超标；
* 用户看到空水杯，却忘记自己已经多久没喝水；
* 用户打开冰箱，却不知道哪些食材即将过期；
* 用户深夜还在工作，却没有意识到自己已经连续工作数小时。

这些需求天然具有：

* 多模态（Multimodal）
* 情境化（Contextual）
* 实时性（Real-time）
* 个性化（Personalized）

特点。

而当前 Agent 的交互方式仍然是：

用户提问 → Agent回答

我们认为：

> 下一代 Personal Agent 不应该等待用户描述世界，而应该直接理解世界。

---

# 二、项目愿景

## Living Agent

我们提出一种新的 Agent 形态：

### Living Agent

Living Agent 不生活在聊天框里。

Living Agent 生活在用户的真实世界中。

它能够：

* 看见环境（See）
* 理解环境（Understand）
* 记住用户（Remember）
* 调用工具（Act）
* 主动交互（Proactive）

最终成为真正融入用户生活的智能伙伴。

---

# 三、项目概述

## Macaron Lens

一句话介绍：

> 一个基于 Camera + AR + GenUI + Memory + Living Tool Use 的现实世界 Personal Agent。

用户不需要输入问题。

只需要举起手机。

Agent 即可理解当前环境，并将对应的信息、建议和交互界面直接生成到现实场景中。

---

# 四、Hackathon 点题

## 条件 A：Macaron 3.0 能力覆盖

### ✅ 随手拍（Camera-first Interaction）

用户举起手机即可触发 Agent。

Camera 不再只是输入设备。

而是新的 Prompt。

例如：

拍摄牛肉：

* 部位识别
* 切割建议
* 烹饪推荐

拍摄菜单：

* 热量分析
* 健康评分
* 菜品推荐

拍摄餐桌：

* 营养统计
* 减脂建议

现实世界本身成为输入。

---

### ✅ Proactive Agent

当前 Agent：

用户发起 → Agent响应

Macaron Lens：

环境触发 → Agent主动介入

例如：

看到空杯子：

> 啊偶～
>
> 杯子里没有水了诶，
>
> 要不要喝一点水呢？

看到高热量午餐：

> 今天脂肪摄入有点高哦。

看到深夜工作：

> 已经连续工作三个小时啦。

交互不再由用户发起。

而是由环境触发。

---

### ✅ 双工前端交互

结合：

* Camera
* AR Overlay
* GenUI

实现实时双向互动。

Agent 持续观察环境。

用户持续获得反馈。

形成真正实时的交互循环。

---

# 五、核心创新

## 创新一：Camera is the New Prompt

过去：

用户需要描述世界。

```text
我现在有一块牛肉
应该怎么切？
```

Agent 才能理解。

---

现在：

用户举起手机。

Agent 自动理解：

* 牛肉部位
* 肉纹方向
* 推荐做法
* 营养信息

无需输入。

无需搜索。

现实世界直接成为 Prompt。

---

## 创新二：Proactive Interaction

目前绝大多数 Agent：

属于被动交互。

必须等待用户提问。

---

Macaron Lens：

属于环境驱动交互。

流程：

环境观察

↓

环境理解

↓

需求预测

↓

主动提醒

↓

用户互动

---

Agent 从 Answer Machine

变成 Life Companion。

---

## 创新三：GenUI Native Experience

传统 Agent 输出：

文字。

---

Macaron Lens 输出：

动态生成的 UI。

例如：

牛肉上：

* 切割箭头
* 部位说明

餐桌上：

* 热量标签
* 营养统计

植物旁：

* 浇水提醒

菜单上：

* 推荐指数
* 健康评分

这些 UI 并非预定义。

而是由 Agent 根据环境实时生成。

---

## 创新四：Living Tool Use

传统 Tool Use：

```text
用户提问
↓
调用工具
↓
返回结果
```

---

Macaron Lens：

```text
环境观察
↓
环境推理
↓
规划工具
↓
调用工具
↓
现实反馈
```

例如：

拍摄食物

↓

营养分析工具

↓

热量计算

↓

生成减脂界面

---

拍摄植物

↓

植物识别工具

↓

养护知识库

↓

生成照料建议

---

工具调用首次真正服务于现实场景。

---

## 创新五：Reality-grounded Memory

传统 Memory：

记住聊天。

---

Macaron Lens：

记住生活。

例如：

Agent 记住：

* 用户正在减脂
* 用户喜欢喝咖啡
* 用户经常忘记喝水
* 用户喜欢阅读
* 用户最近在学习英语

---

当再次出现相关场景时：

Agent 可以主动利用长期记忆进行推理。

例如：

看到第三杯咖啡：

> 今天已经喝两杯咖啡啦，
>
> 要不要喝点水呢？

Memory 第一次真正连接现实环境。

---

# 六、Demo 场景

## Demo 1：减脂模式

用户拍摄午餐。

Agent 自动识别：

* 米饭
* 红烧肉
* 蔬菜
* 可乐

生成：

### 今日摄入估算

* 热量：1238 kcal
* 蛋白质：48 g
* 脂肪：67 g
* 碳水：115 g

同时在食物上生成悬浮标签。

提供晚餐建议。

---

## Demo 2：点菜助手

用户拍摄菜单。

Agent 自动分析：

* 热量
* 蛋白质
* 钠含量
* 减脂友好度

生成推荐组合：

### 今日推荐套餐

* 宫保鸡丁
* 清炒时蔬
* 米饭

预计：

550 kcal

---

## Demo 3：牛肉助手

用户拍摄牛肉。

Agent 自动识别：

* 牛腱子（89%）

生成：

* 推荐做法
* 营养分析
* 切割方向

并直接在肉表面显示切割箭头。

---

# 七、Macaron：Living Companion

技术并不会天然产生陪伴感。

因此我们将 Agent 具象化为：

## Macaron

一个生活在现实世界中的小伙伴。

---

它能够：

* 坐在杯子上
* 趴在书本上
* 藏在植物后面
* 出现在餐桌边
* 站在电脑旁

---

看到空杯子：

> 啊偶～
>
> 杯子里没有水了诶。

---

看到用户完成目标：

> 太棒啦！
>
> 今天已经喝够水啦！

---

看到用户学习：

> 又进步了一点点呢～

---

Agent 不再是工具。

而是用户生活中的伙伴。

---

# 八、社交传播设计

我们认为：

AI 最大的传播媒介不是聊天记录。

而是生活。

---

用户不会分享：

“AI 分析了热量。”

但会分享：

“哈哈，它今天又爬到我的杯子上了。”

---

用户不会分享：

“Agent 调用了工具。”

但会分享：

“它说我今天红烧肉吃太多了。”

---

每一次互动都可以生成：

## Living Moments

现实世界

*

AR Overlay

*

Macaron

*

个性化故事

=

天然 UGC 内容

---

# 九、未来方向

Macaron Lens 不仅仅是一个 AR Demo。

它探索的是：

## Personal Agent 的下一种交互范式

从：

Chat Agent

走向：

Living Agent

从：

Text-first

走向：

Camera-first

从：

Passive Assistant

走向：

Proactive Companion

从：

聊天框

走向：

真实世界

---

# 一句话总结

Macaron Lens 通过 Camera、AR、GenUI、Memory 和 Living Tool Use，让 Personal Agent 第一次真正理解用户所处的现实环境，并主动参与用户的日常生活，成为一个持续成长、持续陪伴的 Living Agent。
