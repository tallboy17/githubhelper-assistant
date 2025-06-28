---
repo: hiyouga/LLaMA-Factory
readme_filename: hiyouga_LLaMA-Factory_README.md
stars: 53088
forks: 6501
watchers: 53088
contributors_count: 192
license: Apache-2.0
Header 2: Provided Datasets
---
Pre-training datasets  
- Wiki Demo (en)
- RefinedWeb (en)
- RedPajama V2 (en)
- Wikipedia (en)
- Wikipedia (zh)
- Pile (en)
- SkyPile (zh)
- FineWeb (en)
- FineWeb-Edu (en)
- The Stack (en)
- StarCoder (en)  
  
Supervised fine-tuning datasets  
- Identity (en&zh)
- Stanford Alpaca (en)
- Stanford Alpaca (zh)
- Alpaca GPT4 (en&zh)
- Glaive Function Calling V2 (en&zh)
- LIMA (en)
- Guanaco Dataset (multilingual)
- BELLE 2M (zh)
- BELLE 1M (zh)
- BELLE 0.5M (zh)
- BELLE Dialogue 0.4M (zh)
- BELLE School Math 0.25M (zh)
- BELLE Multiturn Chat 0.8M (zh)
- UltraChat (en)
- OpenPlatypus (en)
- CodeAlpaca 20k (en)
- Alpaca CoT (multilingual)
- OpenOrca (en)
- SlimOrca (en)
- MathInstruct (en)
- Firefly 1.1M (zh)
- Wiki QA (en)
- Web QA (zh)
- WebNovel (zh)
- Nectar (en)
- deepctrl (en&zh)
- Advertise Generating (zh)
- ShareGPT Hyperfiltered (en)
- ShareGPT4 (en&zh)
- UltraChat 200k (en)
- AgentInstruct (en)
- LMSYS Chat 1M (en)
- Evol Instruct V2 (en)
- Cosmopedia (en)
- STEM (zh)
- Ruozhiba (zh)
- Neo-sft (zh)
- Magpie-Pro-300K-Filtered (en)
- Magpie-ultra-v0.1 (en)
- WebInstructSub (en)
- OpenO1-SFT (en&zh)
- Open-Thoughts (en)
- Open-R1-Math (en)
- Chinese-DeepSeek-R1-Distill (zh)
- LLaVA mixed (en&zh)
- Pokemon-gpt4o-captions (en&zh)
- Open Assistant (de)
- Dolly 15k (de)
- Alpaca GPT4 (de)
- OpenSchnabeltier (de)
- Evol Instruct (de)
- Dolphin (de)
- Booksum (de)
- Airoboros (de)
- Ultrachat (de)  
  
Preference datasets  
- DPO mixed (en&zh)
- UltraFeedback (en)
- COIG-P (zh)
- RLHF-V (en)
- VLFeedback (en)
- RLAIF-V (en)
- Orca DPO Pairs (en)
- HH-RLHF (en)
- Nectar (en)
- Orca DPO (de)
- KTO mixed (en)  
  
Some datasets require confirmation before using them, so we recommend logging in with your Hugging Face account using these commands.  
```bash
pip install --upgrade huggingface_hub
huggingface-cli login
```