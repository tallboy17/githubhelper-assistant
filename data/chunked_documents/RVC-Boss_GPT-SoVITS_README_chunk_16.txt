---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: V3 Release Notes
---
New Features:  
1. The timbre similarity is higher, requiring less training data to approximate the target speaker (the timbre similarity is significantly improved using the base model directly without fine-tuning).  
2. GPT model is more stable, with fewer repetitions and omissions, and it is easier to generate speech with richer emotional expression.  
[more details]()  
Use v3 from v2 environment:  
1. `pip install -r requirements.txt` to update some packages  
2. Clone the latest codes from github.  
3. Download v3 pretrained models (s1v3.ckpt, s2Gv3.pth and models--nvidia--bigvgan_v2_24khz_100band_256x folder) from huggingface and put them into `GPT_SoVITS/pretrained_models`.  
additional: for Audio Super Resolution model, you can read how to download