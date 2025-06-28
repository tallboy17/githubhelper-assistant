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
Header 3: NVIDIA
---
Nvidia users should install stable pytorch using this command:  
```pip install torch torchvision torchaudio --extra-index-url   
This is the command to install pytorch nightly instead which might have performance improvements.  
```pip install --pre torch torchvision torchaudio --index-url   
#### Troubleshooting  
If you get the "Torch not compiled with CUDA enabled" error, uninstall torch with:  
```pip uninstall torch```  
And install it again with the command above.