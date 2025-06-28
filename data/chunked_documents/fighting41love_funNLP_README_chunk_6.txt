---
repo: fighting41love/funNLP
readme_filename: fighting41love_funNLP_README.md
stars: 74401
forks: 14890
watchers: 74401
contributors_count: 11
license: None
Header 1: LLM的训练_推理_低资源_高效训练
---
| 资源名（Name）      | 描述（Description） | 链接     |
| :---        |    :----   |          :--- |
|QLoRA--Guanaco|一种高效的微调方法，可以在单个48GB的GPU上微调一个拥有65B参数的模型，同时保持完整的16位微调任务性能，并通过QLoRA将梯度反向传播通过一个冻结的、4位量化的预训练语言模型到低秩适配器（LoRA）|github|
|Chinese-Guanaco|一个中文低资源的量化训练/部署方案|github|
|   DeepSpeed Chat: 一键式RLHF训练  |       |   github    |
|   LLMTune: 在消费级GPU上微调大型65B+LLM   |   可以在普通消费级GPU上进行4位微调，例如最大的65B LLAMA模型。LLMTune还实现了LoRA算法和GPTQ算法来压缩和量化LLM，并通过数据并行处理大型模型。此外，LLMTune提供了命令行界面和Python库的使用方式    |  github     |
|  基于ChatGLM-6B+LoRA在指令数据集上进行微调    |  基于deepspeed支持多卡微调，速度相比单卡提升8-9倍具体设置可见 微调3 基于DeepSpeed进行Lora微调     |    github   |
|  微软发布RLHF训练工具DeepSpeed Chat    |       |  github     |
|  LlamaChat：Mac上基于LLaMa的聊天机器人    |       |  github     |
|   ChatGPT/GPT4开源“平替”们   |       |   github    |
|训练大型机器学习模型的实用建议和技巧|帮助您训练大型模型（>1B 参数）、避免不稳定性、保存开始失败的实验而不从 0 重新开始|link|
|  Instruction Tuning with GPT-4    |       |   paper    |
|   xturing   |   一个Python软件包，用于高效、快速、简单地微调LLM模型，支持LLaMA、GPT-J、GPT-2等多种模型，可使用单GPU和多GPU训练，使用LoRA等高效微调技术可将硬件成本降低高达90%，并在短时间内完成模型训练   |   github    |
|   GPT4All   |    一个允许在Macbook本地运行GPT的开源项目。基于LLaMa-7B大语言模型打造，包括数据、代码和demo都是开源的，对话风格偏向AI助理   |    github   |
|   用Alpaca-LoRA微调ChatGPT类模型   |       |  link     |
|  LMFlow    |   可扩展、方便有效的工具箱，用于微调大型机器学习模型    |   github    |
|闻达：大型语言模型调用平台|目前支持chatGLM-6B、chatRWKV、chatYuan和chatGLM-6B模型下的chatPDF（自建知识库查找）' |github|
|Micro Agent|小型自主智能体开源项目，由LLM(OpenAI GPT-4)提供动力，可以为你编写软件，只需设置一个“目的”，让它自己工作|github|
|Llama-X|开源的学术研究项目，通过社区共同努力，逐步将LLaMA的性能提高到SOTA LLM水平，节省重复工作，共同创造更多、更快的增量|github|
|Chinese-LLaMA-Alpaca|中文LLaMA&Alpaca大语言模型+本地部署 (Chinese LLaMA & Alpaca LLMs) - 开源了经过中文文本数据预训练的中文LLaMA大模型；开源了进一步经过指令精调的中文Alpaca大模型；快速地使用笔记本电脑（个人PC）本地部署和体验量化版大模型| github |
|Efficient Alpaca|基于LLaMA实现的开源项目，旨在通过微调 LLaMA-7B模型在资源消耗更少、推理速度更快、更适合研究者使用方面提高Stanford Alpaca的性能|github|
|ChatGLM-6B-Slim|裁减掉20K图片Token的ChatGLM-6B，完全一样的性能，占用更小的显存| github |
|Chinese-Vicuna|一个中文低资源的llama+lora方案| github |
|Alpaca-LoRA|用LoRA在消费级硬件上复现斯坦福Alpaca的结果|github|
|LLM Accelerator|让基础大模型更聪明的LLM Accelerator来了！基础大模型正在诸多应用中发挥着日益重要的作用。大多数大语言模型的训练都是采取自回归的方式进行生成，虽然自回归模型生成的文本质量有所保证，但却导致了高昂的推理成本和长时间的延迟。由于大模型的参数量巨大、推理成本高，因此如何在大规模部署大模型的过程中降低成本、减小延迟是一个关键课题。针对此问题，微软亚洲研究院的研究员们提出了一种使用参考文本无损加速大语言模型推理的方法 LLM Accelerator，在大模型典型的应用场景中可以取得两到三倍的加速。|blog|
|大语言模型（LLM）微调技术笔记||github|
|PyLLMs|简洁的 Python 库，用于连接各种 LLM(OpenAI、Anthropic、Google、AI21、Cohere、Aleph Alpha、HuggingfaceHub)，内置模型性能基准。非常适合快速原型设计和评估不同模型，具有以下特点：通过少量代码连接顶级 LLM；响应元数据包括处理的Token、成本和延迟，对各个模型进行标准化；支持多模型：同时从不同模型获取补全；LLM 基准：评估模型的质量、速度和成本|github|
|用混合精度加速大型语言模型|通过使用低精度浮点数运算，可以将训练和推断速度提升多达3倍，同时不影响模型准确性|blog|
|新的LLM训练方法 Federate|杜克大学和微软一起发布了一个新的LLM训练方法 Federated GPT，这个训练方法是将原本中心化的训练方法分散到不同的边缘设备里面（edge device），然后训练完成后，再上传到中心去将各子模型合并。|github|