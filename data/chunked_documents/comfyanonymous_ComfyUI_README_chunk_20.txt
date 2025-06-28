---
repo: comfyanonymous/ComfyUI
readme_filename: comfyanonymous_ComfyUI_README.md
stars: 80954
forks: 8971
watchers: 80954
contributors_count: 213
license: GPL-3.0
Header 1: Running
Header 3: AMD ROCm Tips
---
You can enable experimental memory efficient attention on recent pytorch in ComfyUI on some AMD GPUs using this command, it should already be enabled by default on RDNA3. If this improves speed for you on latest pytorch on your GPU please report it so that I can enable it by default.  
```TORCH_ROCM_AOTRITON_ENABLE_EXPERIMENTAL=1 python main.py --use-pytorch-cross-attention```  
You can also try setting this env variable `PYTORCH_TUNABLEOP_ENABLED=1` which might speed things up at the cost of a very slow initial run.