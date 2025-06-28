---
repo: comfyanonymous/ComfyUI
readme_filename: comfyanonymous_ComfyUI_README.md
stars: 80954
forks: 8971
watchers: 80954
contributors_count: 213
license: GPL-3.0
Header 1: Installing
Header 2: Manual Install (Windows, Linux)
Header 3: AMD GPUs (Linux only)
---
AMD users can install rocm and pytorch with pip if you don't have it already installed, this is the command to install the stable version:  
```pip install torch torchvision torchaudio --index-url   
This is the command to install the nightly with ROCm 6.4 which might have some performance improvements:  
```pip install --pre torch torchvision torchaudio --index-url 