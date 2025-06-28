---
repo: deepseek-ai/DeepSeek-V3
readme_filename: deepseek-ai_DeepSeek-V3_README.md
stars: 97889
forks: 15924
watchers: 97889
contributors_count: 21
license: MIT
Header 2: 2. Model Summary
---
---  
**Architecture: Innovative Load Balancing Strategy and Training Objective**  
- On top of the efficient architecture of DeepSeek-V2, we pioneer an auxiliary-loss-free strategy for load balancing, which minimizes the performance degradation that arises from encouraging load balancing.
-  We investigate a Multi-Token Prediction (MTP) objective and prove it beneficial to model performance.
It can also be used for speculative decoding for inference acceleration.  
---  
**Pre-Training: Towards Ultimate Training Efficiency**  
- We design an FP8 mixed precision training framework and, for the first time, validate the feasibility and effectiveness of FP8 training on an extremely large-scale model.
- Through co-design of algorithms, frameworks, and hardware, we overcome the communication bottleneck in cross-node MoE training, nearly achieving full computation-communication overlap.
This significantly enhances our training efficiency and reduces the training costs, enabling us to further scale up the model size without additional overhead.
- At an economical cost of only 2.664M H800 GPU hours, we complete the pre-training of DeepSeek-V3 on 14.8T tokens, producing the currently strongest open-source base model. The subsequent training stages after pre-training require only 0.1M GPU hours.  
---  
**Post-Training: Knowledge Distillation from DeepSeek-R1**  
-   We introduce an innovative methodology to distill reasoning capabilities from the long-Chain-of-Thought (CoT) model, specifically from one of the DeepSeek R1 series models, into standard LLMs, particularly DeepSeek-V3. Our pipeline elegantly incorporates the verification and reflection patterns of R1 into DeepSeek-V3 and notably improves its reasoning performance. Meanwhile, we also maintain a control over the output style and length of DeepSeek-V3.  
---