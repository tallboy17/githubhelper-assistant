---
repo: fighting41love/funNLP
readme_filename: fighting41love_funNLP_README.md
stars: 74401
forks: 14890
watchers: 74401
contributors_count: 11
license: None
Header 1: 类ChatGPT的开源框架
---
| 资源名（Name）      | 描述（Description） | 链接     |
| :---        |    :----   |          :--- |
|   LLM-As-Chatbot   |   这个项目把市面上有的LLM全部做成了Chatbot，直接可以在google colab运行，不需要自己搭建，非常适用于想体验LLM的朋友们。我刚试了，真的超简单。有些LLM需要的显存比较多，所以最好是要有colab pro订阅。    |  github     |
|   OpenBuddy    |    一款强大的开源多语言聊天机器人模型，目标是全球用户，重点是对话AI和流畅的多语言支持，包括英文、中文等多种语言。基于Facebook的LLAMA模型，进行了微调，包括扩展词汇表、增加常用字符和增强的token embeddings。通过这些改进和多轮对话数据集，OpenBuddy提供了一个强大的模型，能回答问题并在各种语言之间进行翻译任务。OpenBuddy的使命是提供一个免费、开放且可离线使用的AI模型，该模型可以在用户的设备上运行，无论他们的语言或文化背景如何。目前，OpenBuddy-13B的演示版本可以在Discord服务器上找到。其关键功能包括多语言对话AI(包括中文、英文、日文、韩文、法文等)、增强的词汇表和对常见CJK字符的支持，以及两种模型版本：7B和13B   |  github-OpenBuddy  |
|   Panda: 海外中文开源大语言模型   |    基于 Llama-7B, -13B, -33B, -65B 进行中文领域上的持续预训练，使用了接近15M条数据，并针对推理能力在中文benchmark上进行了评测   |   github-PandaLM     |
|  Dromedary：一个开源的自对齐语言模型，只需少量人工监督即可进行训练    |       |    github-Dromedary   |
|   LaMini-LM 蒸馏的小型、高效的语言模型集合  |   从 ChatGPT 蒸馏的小型、高效的语言模型集合，在2.58 M 指令大规模数据集上进行训练    |   github    |
|   LLaMA-Adapter V2    |   上海人工智能实验室 LLaMA-Adapter V2，仅注入14M参数，1小时时间即可完成训练，对比较果确实很惊艳，且具有多模态功能（对图像进行解释和问答）    |    github   |
|   HuggingChat   |   Hugging Face 推出第一个 ChatGPT 开源替代品：HuggingChat。基于 Open Assistant  大模型搭建，支持中文对话与编写代码，但暂不支持中文回复。应用已上线，无需代理，打开即可访问    |   link    |
| Open-Chinese-LLaMA     |   基于 LLaMA-7B 经过 中文数据集增量预训练 产生的 中文大语言模型基座    |   github    |
|   OpenLLaMA   |   LLaMA模型的开源复现，在RedPajama数据集上训练，使用了与LLaMA相同的预处理步骤和超参数，模型结构，上下文长度，训练步骤，学习率调度和优化器。OpenLLaMA的PyTorch和Jax权重可以在Huggingface Hub上获得。OpenLLaMA在各种任务中展现出与LLaMA和GPT-J相似的表现，部分任务表现优异    |  github     |
|  replit-code-v1-3b    |   BY-SA 4.0授权发布，这意味着允许商业使用    |  link    |
|   MOSS   |  MOSS是一个支持中英双语和多种插件的开源对话语言模型，moss-moon系列模型具有160亿参数，在FP16精度下可在单张A100/A800或两张3090显卡运行，在INT4/8精度下可在单张3090显卡运行。MOSS基座语言模型在约七千亿中英文以及代码单词上预训练得到，后续经过对话指令微调、插件增强学习和人类偏好训练具备多轮对话能力及使用多种插件的能力。     |   github   |
|   RedPajama   |   1.2 万亿tokens数据集    |  link     |
|  chinese_llama_alpaca_lora 抽取框架  |       |   github    |
|   Scaling Transformer to 1M tokens and beyond with RMT   |  该论文提出一种名为 RMT 的新技术，或许可将 Transform 的 Token 上限扩展至 100 万，甚至更多。     |     github  |
|   Open Assistant   |   包含大量AI生成的、人工标注的语料库和包括基于LLaMA和基于Pythia的多种模型可选。发布的数据集包括超过161K较高质量的，多达35种语言的人工助手型交互对话语料库    |   data model    |
|   ChatGLM Efficient Tuning   |  基于 PEFT 的高效 ChatGLM 微调     |   github    |
|  Dolly介绍    |       |   news    |
|  Baize：一种对自聊天数据进行参数高效调优的开源聊天模型    |   Baize是一个开源的聊天模型，可以进行多轮对话。它是通过使用ChatGPT自我对话生成高质量的多轮聊天语料库，并使用参数高效调整来增强LLaMA（一个开源的大型语言模型）而创建的。Baize模型在具有最小潜在风险的情况下表现出良好的多轮对话性能。它可以在单个GPU上运行，使更广泛的研究人员可以使用它。Baize模型和数据仅用于研究目的。    |    论文地址源码地址   |
|   GPTrillion--未找到开源代码   |  包含1.5万亿（1.5T）参数的大模型GPTrillion开源了，号称是目前世界上最大的开源LLM    |    google_doc   |
|Cerebras-GPT-13B(可商用)||hugging_face|
|Chinese-ChatLLaMA|中文ChatLLaMA对话模型；预训练/指令微调数据集，基于 TencentPretrain 多模态预训练框架构建，支持简繁体中文、英文、日文等多语言|github|
|Lit-LLaMA|基于Apache 2.0许可证完全开源的LLaMA独立实现，建立在nanoGPT之上，旨在解决原始LLaMA代码采用GPL许可证的限制，以实现更广泛的学术和商业应用|github|
|MosaicML|MPT-7B-StoryWriter，65K tokens，可以把《了不起的盖茨比》都一次性扔进去。|huggingface|
|Langchain|大型语言模型（LLMs）正在成为一项具有变革性的技术，使开发者能够构建以前无法实现的应用程序。然而，仅仅使用这些独立的LLMs通常不足以创建一个真正强大的应用程序 - 真正的力量来自于能够将它们与其他计算或知识来源相结合。|github|
|Guidance|引导能够比传统的提示或链接更有效地控制现代语言模型，并且更高效。引导程序允许您将生成、提示和逻辑控制交错到单一连续流中，与语言模型实际处理文本的方式相匹配。像"Chain of Thought"及其许多变体（例如ART、Auto-CoT等）这样的简单输出结构已被证明能改善语言模型的性能。更强大的语言模型（如GPT-4）的出现使得更丰富的结构成为可能，而引导则使得构建这种结构变得更加容易和经济。|github|
|WizardLM|赋予大型预训练语言模型遵循复杂指令的能力，使用完整进化指令（约300k）训练的WizardLM-7B模型|github|