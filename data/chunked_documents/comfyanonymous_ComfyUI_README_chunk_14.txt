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
Header 3: Intel GPUs (Windows and Linux)
---
(Option 1) Intel Arc GPU users can install native PyTorch with torch.xpu support using pip (currently available in PyTorch nightly builds). More information can be found here  
1. To install PyTorch nightly, use the following command:  
```pip install --pre torch torchvision torchaudio --index-url   
2. Launch ComfyUI by running `python main.py`  
(Option 2) Alternatively, Intel GPUs supported by Intel Extension for PyTorch (IPEX) can leverage IPEX for improved performance.  
1. For Intel® Arc™ A-Series Graphics utilizing IPEX, create a conda environment and use the commands below:  
```
conda install libuv
pip install torch==2.3.1.post0+cxx11.abi torchvision==0.18.1.post0+cxx11.abi torchaudio==2.3.1.post0+cxx11.abi intel-extension-for-pytorch==2.3.110.post0+xpu --extra-index-url  --extra-index-url 
```  
For other supported Intel GPUs with IPEX, visit Installation for more information.  
Additional discussion and help can be found here.