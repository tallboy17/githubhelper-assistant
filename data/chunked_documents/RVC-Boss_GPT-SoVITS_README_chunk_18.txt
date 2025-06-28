---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: V2Pro Release Notes
---
New Features:  
1. Slightly higher VRAM usage than v2, surpassing v4's performance, with v2's hardware cost and speed.
[more details]()  
2.v1/v2 and the v2Pro series share the same characteristics, while v3/v4 have similar features. For training sets with average audio quality, v1/v2/v2Pro can deliver decent results, but v3/v4 cannot. Additionally, the synthesized tone and timebre of v3/v4 lean more toward the reference audio rather than the overall training set.  
Use v2Pro from v1/v2/v3/v4 environment:  
1. `pip install -r requirements.txt` to update some packages  
2. Clone the latest codes from github.  
3. Download v2Pro pretrained models (v2Pro/s2Dv2Pro.pth, v2Pro/s2Gv2Pro.pth, v2Pro/s2Dv2ProPlus.pth, v2Pro/s2Gv2ProPlus.pth, and sv/pretrained_eres2netv2w24s4ep4.ckpt) from huggingface and put them into `GPT_SoVITS/pretrained_models`.