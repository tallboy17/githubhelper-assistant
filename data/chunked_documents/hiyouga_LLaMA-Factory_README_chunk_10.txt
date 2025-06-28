---
repo: hiyouga/LLaMA-Factory
readme_filename: hiyouga_LLaMA-Factory_README.md
stars: 53088
forks: 6501
watchers: 53088
contributors_count: 192
license: Apache-2.0
Header 2: Supported Models
---
| Model                                                             | Model size                       | Template            |
| ----------------------------------------------------------------- | -------------------------------- | ------------------- |
| Baichuan 2                 | 7B/13B                           | baichuan2           |
| BLOOM/BLOOMZ                 | 560M/1.1B/1.7B/3B/7.1B/176B      | -                   |
| ChatGLM3                          | 6B                               | chatglm3            |
| Command R                   | 35B/104B                         | cohere              |
| DeepSeek (Code/MoE)         | 7B/16B/67B/236B                  | deepseek            |
| DeepSeek 2.5/3              | 236B/671B                        | deepseek3           |
| DeepSeek R1 (Distill)       | 1.5B/7B/8B/14B/32B/70B/671B      | deepseekr1          |
| Falcon                           | 7B/11B/40B/180B                  | falcon              |
| Falcon-H1                        | 0.5B/1.5B/3B/7B/34B              | falcon_h1           |
| Gemma/Gemma 2/CodeGemma          | 2B/7B/9B/27B                     | gemma/gemma2        |
| Gemma 3                          | 1B/4B/12B/27B                    | gemma3/gemma (1B)   |
| GLM-4/GLM-4-0414/GLM-Z1           | 9B/32B                           | glm4/glmz1          |
| GPT-2                  | 0.1B/0.4B/0.8B/1.5B              | -                   |
| Granite 3.0-3.3             | 1B/2B/3B/8B                      | granite3            |
| Hunyuan                        | 7B                               | hunyuan             |
| Index                         | 1.9B                             | index               |
| InternLM 2-3                   | 7B/8B/20B                        | intern2             |
| InternVL 2.5-3                | 1B/2B/8B/14B/38B/78B             | intern_vl           |
| Kimi-VL                      | 16B                              | kimi_vl             |
| Llama                | 7B/13B/33B/65B                   | -                   |
| Llama 2                      | 7B/13B/70B                       | llama2              |
| Llama 3-3.3                  | 1B/3B/8B/70B                     | llama3              |
| Llama 4                      | 109B/402B                        | llama4              |
| Llama 3.2 Vision             | 11B/90B                          | mllama              |
| LLaVA-1.5                      | 7B/13B                           | llava               |
| LLaVA-NeXT                     | 7B/8B/13B/34B/72B/110B           | llava_next          |
| LLaVA-NeXT-Video               | 7B/34B                           | llava_next_video    |
| MiMo                         | 7B                               | mimo                |
| MiniCPM                         | 0.5B/1B/2B/4B/8B                 | cpm/cpm3/cpm4       |
| MiniCPM-o-2.6/MiniCPM-V-2.6     | 8B                               | minicpm_o/minicpm_v |
| Ministral/Mistral-Nemo        | 8B/12B                           | ministral           |
| Mistral/Mixtral               | 7B/8x7B/8x22B                    | mistral             |
| Mistral Small                 | 24B                              | mistral_small       |
| OLMo                            | 1B/7B                            | -                   |
| PaliGemma/PaliGemma2             | 3B/10B/28B                       | paligemma           |
| Phi-1.5/Phi-2                 | 1.3B/2.7B                        | -                   |
| Phi-3/Phi-3.5                 | 4B/14B                           | phi                 |
| Phi-3-small                   | 7B                               | phi_small           |
| Phi-4                         | 14B                              | phi4                |
| Pixtral                       | 12B                              | pixtral             |
| Qwen (1-2.5) (Code/Math/MoE/QwQ)   | 0.5B/1.5B/3B/7B/14B/32B/72B/110B | qwen                |
| Qwen3 (MoE)                        | 0.6B/1.7B/4B/8B/14B/32B/235B     | qwen3               |
| Qwen2-Audio                        | 7B                               | qwen2_audio         |
| Qwen2.5-Omni                       | 3B/7B                            | qwen2_omni          |
| Qwen2-VL/Qwen2.5-VL/QVQ            | 2B/3B/7B/32B/72B                 | qwen2_vl            |
| Seed Coder               | 8B                               | seed_coder          |
| Skywork o1                      | 8B                               | skywork_o1          |
| StarCoder 2                     | 3B/7B/15B                        | -                   |
| TeleChat2                       | 3B/7B/35B/115B                   | telechat2           |
| XVERSE                           | 7B/13B/65B                       | xverse              |
| Yi/Yi-1.5 (Code)                  | 1.5B/6B/9B/34B                   | yi                  |
| Yi-VL                             | 6B/34B                           | yi_vl               |
| Yuan 2                         | 2B/51B/102B                      | yuan                |  
> [!NOTE]
> For the "base" models, the `template` argument can be chosen from `default`, `alpaca`, `vicuna` etc. But make sure to use the **corresponding template** for the "instruct/chat" models.
>
> Remember to use the **SAME** template in training and inference.
>
> \*: You should install the `transformers` from main branch and use `DISABLE_VERSION_CHECK=1` to skip version check.
>
> \*\*: You need to install a specific version of `transformers` to use the corresponding model.  
Please refer to constants.py for a full list of models we supported.  
You also can add a custom chat template to template.py.