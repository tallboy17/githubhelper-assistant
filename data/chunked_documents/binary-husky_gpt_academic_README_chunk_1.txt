---
repo: binary-husky/gpt_academic
readme_filename: binary-husky_gpt_academic_README.md
stars: 68842
forks: 8356
watchers: 68842
contributors_count: 101
license: GPL-3.0
---
> [!IMPORTANT]
> `master主分支`最新动态(2025.3.2): 修复大量代码typo / 联网组件支持Jina的api / 增加deepseek-r1支持
> `frontier开发分支`最新动态(2024.12.9): 更新对话时间线功能，优化xelatex论文翻译
> `wiki文档`最新动态(2024.12.5): 更新ollama接入指南
>
> 2025.2.2: 三分钟快速接入最强qwen2.5-max视频
> 2025.2.1: 支持自定义字体
> 2024.10.10: 突发停电，紧急恢复了提供whl包的文件服务器
> 2024.5.1: 加入Doc2x翻译PDF论文的功能，查看详情
> 2024.3.11: 全力支持Qwen、GLM、DeepseekCoder等中文大语言模型！ SoVits语音克隆模块，查看详情
> 2024.1.17: 安装依赖时，请选择`requirements.txt`中**指定的版本**。 安装命令：`pip install -r requirements.txt`。  
  


 GPT 学术优化 (GPT Academic)
  
[![Github][Github-image]][Github-url]
[![License][License-image]][License-url]
[![Releases][Releases-image]][Releases-url]
[![Installation][Installation-image]][Installation-url]
[![Wiki][Wiki-image]][Wiki-url]
[![PR][PRs-image]][PRs-url]  
[Github-image]: 
[License-image]: 
[Releases-image]: 
[Installation-image]: 
[Wiki-image]: 
[PRs-image]:   
[Github-url]: 
[License-url]: 
[Releases-url]: 
[Installation-url]: 
[Wiki-url]: 
[PRs-url]:   

  
**如果喜欢这个项目，请给它一个Star；如果您发明了好用的快捷键或插件，欢迎发pull requests！**  
If you like this project, please give it a Star.
Read this in English | 日本語 | 한국어 | Русский | Français. All translations have been provided by the project itself. To translate this project to arbitrary language with GPT, read and run `multi_language.py` (experimental).
  
> [!NOTE]
> 1.本项目中每个文件的功能都在自译解报告`self_analysis.md`详细说明。随着版本的迭代，您也可以随时自行点击相关函数插件，调用GPT重新生成项目的自我解析报告。常见问题请查阅wiki。
>    ![常规安装方法](#installation)  ![一键安装脚本](  ![配置说明]( ![wiki](
>
> 2.本项目兼容并鼓励尝试国内中文大语言基座模型如通义千问，智谱GLM等。支持多个api-key共存，可在配置文件中填写如`API_KEY="openai-key1,openai-key2,azure-key3,api2d-key4"`。需要临时更换`API_KEY`时，在输入区输入临时的`API_KEY`然后回车键提交即可生效。  
  
  
功能（⭐= 近期新增功能） | 描述
--- | ---
⭐接入新模型 | 百度千帆与文心一言, 通义千问Qwen，上海AI-Lab书生，讯飞星火，LLaMa2，智谱GLM4，DALLE3, DeepseekCoder
⭐支持mermaid图像渲染 | 支持让GPT生成流程图、状态转移图、甘特图、饼状图、GitGraph等等（3.7版本）
⭐Arxiv论文精细翻译 (Docker) | [插件] 一键以超高质量翻译arxiv论文，目前最好的论文翻译工具
⭐实时语音对话输入 | [插件] 异步监听音频，自动断句，自动寻找回答时机
⭐AutoGen多智能体插件 | [插件] 借助微软AutoGen，探索多Agent的智能涌现可能！
⭐虚空终端插件 | [插件] 能够使用自然语言直接调度本项目其他插件
润色、翻译、代码解释 | 一键润色、翻译、查找论文语法错误、解释代码
自定义快捷键 | 支持自定义快捷键
模块化设计 | 支持自定义强大的插件，插件支持热更新
程序剖析 | [插件] 一键剖析Python/C/C++/Java/Lua/...项目树 或 自我剖析
读论文、翻译论文 | [插件] 一键解读latex/pdf论文全文并生成摘要
Latex全文翻译、润色 | [插件] 一键翻译或润色latex论文
批量注释生成 | [插件] 一键批量生成函数注释
Markdown中英互译 | [插件] 看到上面5种语言的README了吗？就是出自他的手笔
PDF论文全文翻译功能 | [插件] PDF论文提取题目&摘要+翻译全文（多线程）
Arxiv小助手 | [插件] 输入arxiv文章url即可一键翻译摘要+下载PDF
Latex论文一键校对 | [插件] 仿Grammarly对Latex文章进行语法、拼写纠错+输出对照PDF
谷歌学术统合小助手 | [插件] 给定任意谷歌学术搜索页面URL，让gpt帮你写relatedworks
互联网信息聚合+GPT | [插件] 一键让GPT从互联网获取信息回答问题，让信息永不过时
公式/图片/表格显示 | 可以同时显示公式的tex形式和渲染形式，支持公式、代码高亮
启动暗色主题 | 在浏览器url后面添加```/?__theme=dark```可以切换dark主题
多LLM模型支持 | 同时被GPT3.5、GPT4、清华ChatGLM2、复旦MOSS伺候的感觉一定会很不错吧？
更多LLM模型接入，支持huggingface部署 | 加入Newbing接口(新必应)，引入清华Jittorllms支持LLaMA和盘古α
⭐void-terminal pip包 | 脱离GUI，在Python中直接调用本项目的所有函数插件（开发中）
更多新功能展示 (图像生成等) …… | 见本文档结尾处 ……
  
- 新界面（修改`config.py`中的LAYOUT选项即可实现“左右布局”和“上下布局”的切换）


  


  
- 所有按钮都通过读取functional.py动态生成，可随意加自定义功能，解放剪贴板


  
- 润色/纠错


  
- 如果输出包含公式，会以tex形式和渲染形式同时显示，方便复制和阅读


  
- 懒得看项目代码？直接把整个工程炫ChatGPT嘴里


  
- 多种大语言模型混合调用（ChatGLM + OpenAI-GPT3.5 + GPT4）


  
