---
repo: hiyouga/LLaMA-Factory
readme_filename: hiyouga_LLaMA-Factory_README.md
stars: 53088
forks: 6501
watchers: 53088
contributors_count: 192
license: Apache-2.0
Header 2: Changelog
---
[25/04/28] We supported fine-tuning the **Qwen3** model family.  
[25/04/21] We supported the **Muon** optimizer. See examples for usage. Thank @tianshijing's PR.  
[25/04/16] We supported fine-tuning the **InternVL3** model. See PR #7258 to get started.  
[25/04/14] We supported fine-tuning the **GLM-Z1** and **Kimi-VL** models.  
[25/04/06] We supported fine-tuning the **Llama 4** model. See PR #7611 to get started.  
Full Changelog  
[25/03/31] We supported fine-tuning the **Qwen2.5 Omni** model. See PR #7537 to get started.  
[25/03/15] We supported **SGLang** as inference backend. Try `infer_backend: sglang` to accelerate inference.  
[25/03/12] We supported fine-tuning the **Gemma 3** model.  
[25/02/24] Announcing **EasyR1**, an efficient, scalable and multi-modality RL training framework for efficient GRPO training.  
[25/02/11] We supported saving the **Ollama** modelfile when exporting the model checkpoints. See examples for usage.  
[25/02/05] We supported fine-tuning the **Qwen2-Audio** and **MiniCPM-o-2.6** on audio understanding tasks.  
[25/01/31] We supported fine-tuning the **DeepSeek-R1** and **Qwen2.5-VL** models.  
[25/01/15] We supported **APOLLO** optimizer. See examples for usage.  
[25/01/14] We supported fine-tuning the **MiniCPM-o-2.6** and **MiniCPM-V-2.6** models. Thank @BUAADreamer's PR.  
[25/01/14] We supported fine-tuning the **InternLM 3** models. Thank @hhaAndroid's PR.  
[25/01/10] We supported fine-tuning the **Phi-4** model.  
[24/12/21] We supported using **SwanLab** for experiment tracking and visualization. See this section for details.  
[24/11/27] We supported fine-tuning the **Skywork-o1** model and the **OpenO1** dataset.  
[24/10/09] We supported downloading pre-trained models and datasets from the **Modelers Hub**. See this tutorial for usage.  
[24/09/19] We supported fine-tuning the **Qwen2.5** models.  
[24/08/30] We supported fine-tuning the **Qwen2-VL** models. Thank @simonJJJ's PR.  
[24/08/27] We supported **Liger Kernel**. Try `enable_liger_kernel: true` for efficient training.  
[24/08/09] We supported **Adam-mini** optimizer. See examples for usage. Thank @relic-yuexi's PR.  
[24/07/04] We supported contamination-free packed training. Use `neat_packing: true` to activate it. Thank @chuan298's PR.  
[24/06/16] We supported **PiSSA** algorithm. See examples for usage.  
[24/06/07] We supported fine-tuning the **Qwen2** and **GLM-4** models.  
[24/05/26] We supported **SimPO** algorithm for preference learning. See examples for usage.  
[24/05/20] We supported fine-tuning the **PaliGemma** series models. Note that the PaliGemma models are pre-trained models, you need to fine-tune them with `paligemma` template for chat completion.  
[24/05/18] We supported **KTO** algorithm for preference learning. See examples for usage.  
[24/05/14] We supported training and inference on the Ascend NPU devices. Check installation section for details.  
[24/04/26] We supported fine-tuning the **LLaVA-1.5** multimodal LLMs. See examples for usage.  
[24/04/22] We provided a **Colab notebook** for fine-tuning the Llama-3 model on a free T4 GPU. Two Llama-3-derived models fine-tuned using LLaMA Factory are available at Hugging Face, check Llama3-8B-Chinese-Chat and Llama3-Chinese for details.  
[24/04/21] We supported **Mixture-of-Depths** according to AstraMindAI's implementation. See examples for usage.  
[24/04/16] We supported **BAdam** optimizer. See examples for usage.  
[24/04/16] We supported **unsloth**'s long-sequence training (Llama-2-7B-56k within 24GB). It achieves **117%** speed and **50%** memory compared with FlashAttention-2, more benchmarks can be found in this page.  
[24/03/31] We supported **ORPO**. See examples for usage.  
[24/03/21] Our paper "LlamaFactory: Unified Efficient Fine-Tuning of 100+ Language Models" is available at arXiv!  
[24/03/20] We supported **FSDP+QLoRA** that fine-tunes a 70B model on 2x24GB GPUs. See examples for usage.  
[24/03/13] We supported **LoRA+**. See examples for usage.  
[24/03/07] We supported **GaLore** optimizer. See examples for usage.  
[24/03/07] We integrated **vLLM** for faster and concurrent inference. Try `infer_backend: vllm` to enjoy **270%** inference speed.  
[24/02/28] We supported weight-decomposed LoRA (**DoRA**). Try `use_dora: true` to activate DoRA training.  
[24/02/15] We supported **block expansion** proposed by LLaMA Pro. See examples for usage.  
[24/02/05] Qwen1.5 (Qwen2 beta version) series models are supported in LLaMA-Factory. Check this blog post for details.  
[24/01/18] We supported **agent tuning** for most models, equipping model with tool using abilities by fine-tuning with `dataset: glaive_toolcall_en`.  
[23/12/23] We supported **unsloth**'s implementation to boost LoRA tuning for the LLaMA, Mistral and Yi models. Try `use_unsloth: true` argument to activate unsloth patch. It achieves **170%** speed in our benchmark, check this page for details.  
[23/12/12] We supported fine-tuning the latest MoE model **Mixtral 8x7B** in our framework. See hardware requirement here.  
[23/12/01] We supported downloading pre-trained models and datasets from the **ModelScope Hub**. See this tutorial for usage.  
[23/10/21] We supported **NEFTune** trick for fine-tuning. Try `neftune_noise_alpha: 5` argument to activate NEFTune.  
[23/09/27] We supported **$S^2$-Attn** proposed by LongLoRA for the LLaMA models. Try `shift_attn: true` argument to enable shift short attention.  
[23/09/23] We integrated MMLU, C-Eval and CMMLU benchmarks in this repo. See examples for usage.  
[23/09/10] We supported **FlashAttention-2**. Try `flash_attn: fa2` argument to enable FlashAttention-2 if you are using RTX4090, A100 or H100 GPUs.  
[23/08/12] We supported **RoPE scaling** to extend the context length of the LLaMA models. Try `rope_scaling: linear` argument in training and `rope_scaling: dynamic` argument at inference to extrapolate the position embeddings.  
[23/08/11] We supported **DPO training** for instruction-tuned models. See examples for usage.  
[23/07/31] We supported **dataset streaming**. Try `streaming: true` and `max_steps: 10000` arguments to load your dataset in streaming mode.  
[23/07/29] We released two instruction-tuned 13B models at Hugging Face. See these Hugging Face Repos (LLaMA-2 / Baichuan) for details.  
[23/07/18] We developed an **all-in-one Web UI** for training, evaluation and inference. Try `train_web.py` to fine-tune models in your Web browser. Thank @KanadeSiina and @codemayq for their efforts in the development.  
[23/07/09] We released **FastEdit** ⚡🩹, an easy-to-use package for editing the factual knowledge of large language models efficiently. Please follow FastEdit if you are interested.  
[23/06/29] We provided a **reproducible example** of training a chat model using instruction-following datasets, see Baichuan-7B-sft for details.  
[23/06/22] We aligned the demo API with the OpenAI's format where you can insert the fine-tuned model in **arbitrary ChatGPT-based applications**.  
[23/06/03] We supported quantized training and inference (aka **QLoRA**). See examples for usage.  
  
> [!TIP]
> If you cannot use the latest feature, please pull the latest code and install LLaMA-Factory again.