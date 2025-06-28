---
repo: binary-husky/gpt_academic
readme_filename: binary-husky_gpt_academic_README.md
stars: 68842
forks: 8356
watchers: 68842
contributors_count: 101
license: GPL-3.0
Header 1: Updates
Header 3: II：版本:
---
- version 3.80(TODO): 优化AutoGen插件主题并设计一系列衍生插件
- version 3.70: 引入Mermaid绘图，实现GPT画脑图等功能
- version 3.60: 引入AutoGen作为新一代插件的基石
- version 3.57: 支持GLM3，星火v3，文心一言v4，修复本地模型的并发BUG
- version 3.56: 支持动态追加基础功能按钮，新汇报PDF汇总页面
- version 3.55: 重构前端界面，引入悬浮窗口与菜单栏
- version 3.54: 新增动态代码解释器（Code Interpreter）（待完善）
- version 3.53: 支持动态选择不同界面主题，提高稳定性&解决多用户冲突问题
- version 3.50: 使用自然语言调用本项目的所有函数插件（虚空终端），支持插件分类，改进UI，设计新主题
- version 3.49: 支持百度千帆平台和文心一言
- version 3.48: 支持阿里达摩院通义千问，上海AI-Lab书生，讯飞星火
- version 3.46: 支持完全脱手操作的实时语音对话
- version 3.45: 支持自定义ChatGLM2微调模型
- version 3.44: 正式支持Azure，优化界面易用性
- version 3.4: +arxiv论文翻译、latex论文批改功能
- version 3.3: +互联网信息综合功能
- version 3.2: 函数插件支持更多参数接口 (保存对话功能, 解读任意语言代码+同时询问任意的LLM组合)
- version 3.1: 支持同时问询多个gpt模型！支持api2d，支持多个apikey负载均衡
- version 3.0: 对chatglm和其他小型llm的支持
- version 2.6: 重构了插件结构，提高了交互性，加入更多插件
- version 2.5: 自更新，解决总结大工程源代码时文本过长、token溢出的问题
- version 2.4: 新增PDF全文翻译功能; 新增输入区切换位置的功能
- version 2.3: 增强多线程交互性
- version 2.2: 函数插件支持热重载
- version 2.1: 可折叠式布局
- version 2.0: 引入模块化函数插件
- version 1.0: 基础功能  
GPT Academic开发者QQ群：`610599535`  
- 已知问题
- 某些浏览器翻译插件干扰此软件前端的运行
- 官方Gradio目前有很多兼容性问题，请**务必使用`requirement.txt`安装Gradio**  
```mermaid
timeline LR
title GPT-Academic项目发展历程
section 2.x
1.0~2.2: 基础功能: 引入模块化函数插件: 可折叠式布局: 函数插件支持热重载
2.3~2.5: 增强多线程交互性: 新增PDF全文翻译功能: 新增输入区切换位置的功能: 自更新
2.6: 重构了插件结构: 提高了交互性: 加入更多插件
section 3.x
3.0~3.1: 对chatglm支持: 对其他小型llm支持: 支持同时问询多个gpt模型: 支持多个apikey负载均衡
3.2~3.3: 函数插件支持更多参数接口: 保存对话功能: 解读任意语言代码: 同时询问任意的LLM组合: 互联网信息综合功能
3.4: 加入arxiv论文翻译: 加入latex论文批改功能
3.44: 正式支持Azure: 优化界面易用性
3.46: 自定义ChatGLM2微调模型: 实时语音对话
3.49: 支持阿里达摩院通义千问: 上海AI-Lab书生: 讯飞星火: 支持百度千帆平台 & 文心一言
3.50: 虚空终端: 支持插件分类: 改进UI: 设计新主题
3.53: 动态选择不同界面主题: 提高稳定性: 解决多用户冲突问题
3.55: 动态代码解释器: 重构前端界面: 引入悬浮窗口与菜单栏
3.56: 动态追加基础功能按钮: 新汇报PDF汇总页面
3.57: GLM3, 星火v3: 支持文心一言v4: 修复本地模型的并发BUG
3.60: 引入AutoGen
3.70: 引入Mermaid绘图: 实现GPT画脑图等功能
3.80(TODO): 优化AutoGen插件主题: 设计衍生插件

```