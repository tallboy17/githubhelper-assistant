---
repo: xai-org/grok-1
readme_filename: xai-org_grok-1_README.md
stars: 50291
forks: 8354
watchers: 50291
contributors_count: 6
license: Apache-2.0
Header 1: Model Specifications
---
Grok-1 is currently designed with the following specifications:  
- **Parameters:** 314B
- **Architecture:** Mixture of 8 Experts (MoE)
- **Experts Utilization:** 2 experts used per token
- **Layers:** 64
- **Attention Heads:** 48 for queries, 8 for keys/values
- **Embedding Size:** 6,144
- **Tokenization:** SentencePiece tokenizer with 131,072 tokens
- **Additional Features:**
- Rotary embeddings (RoPE)
- Supports activation sharding and 8-bit quantization
- **Maximum Sequence Length (context):** 8,192 tokens