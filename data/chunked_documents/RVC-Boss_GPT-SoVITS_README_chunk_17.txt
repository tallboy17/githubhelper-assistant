---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: V4 Release Notes
---
New Features:  
1. Version 4 fixes the issue of metallic artifacts in Version 3 caused by non-integer multiple upsampling, and natively outputs 48k audio to prevent muffled sound (whereas Version 3 only natively outputs 24k audio). The author considers Version 4 a direct replacement for Version 3, though further testing is still needed.
[more details]()  
Use v4 from v1/v2/v3 environment:  
1. `pip install -r requirements.txt` to update some packages  
2. Clone the latest codes from github.  
3. Download v4 pretrained models (gsv-v4-pretrained/s2v4.ckpt, and gsv-v4-pretrained/vocoder.pth) from huggingface and put them into `GPT_SoVITS/pretrained_models`.