---
repo: deepseek-ai/DeepSeek-V3
readme_filename: deepseek-ai_DeepSeek-V3_README.md
stars: 97889
forks: 15924
watchers: 97889
contributors_count: 21
license: MIT
Header 2: 6. How to Run Locally
Header 3: 6.2 Inference with SGLang (recommended)
---
SGLang currently supports MLA optimizations, DP Attention, FP8 (W8A8), FP8 KV Cache, and Torch Compile, delivering state-of-the-art latency and throughput performance among open-source frameworks.  
Notably, SGLang v0.4.1 fully supports running DeepSeek-V3 on both **NVIDIA and AMD GPUs**, making it a highly versatile and robust solution.  
SGLang also supports multi-node tensor parallelism, enabling you to run this model on multiple network-connected machines.  
Multi-Token Prediction (MTP) is in development, and progress can be tracked in the optimization plan.  
Here are the launch instructions from the SGLang team: 