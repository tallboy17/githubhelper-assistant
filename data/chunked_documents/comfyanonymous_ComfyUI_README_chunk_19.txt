---
repo: comfyanonymous/ComfyUI
readme_filename: comfyanonymous_ComfyUI_README.md
stars: 80954
forks: 8971
watchers: 80954
contributors_count: 213
license: GPL-3.0
Header 1: Running
Header 3: For AMD cards not officially supported by ROCm
---
Try running it with this command if you have issues:  
For 6700, 6600 and maybe other RDNA2 or older: ```HSA_OVERRIDE_GFX_VERSION=10.3.0 python main.py```  
For AMD 7600 and maybe other RDNA3 cards: ```HSA_OVERRIDE_GFX_VERSION=11.0.0 python main.py```