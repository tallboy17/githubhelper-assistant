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
Header 3: Others:
---
#### Apple Mac silicon  
You can install ComfyUI in Apple Mac silicon (M1 or M2) with any recent macOS version.  
1. Install pytorch nightly. For instructions, read the Accelerated PyTorch training on Mac Apple Developer guide (make sure to install the latest pytorch nightly).
1. Follow the ComfyUI manual installation instructions for Windows and Linux.
1. Install the ComfyUI dependencies. If you have another Stable Diffusion UI you might be able to reuse the dependencies.
1. Launch ComfyUI by running `python main.py`  
> **Note**: Remember to add your models, VAE, LoRAs etc. to the corresponding Comfy folders, as discussed in ComfyUI manual installation.  
#### DirectML (AMD Cards on Windows)  
This is very badly supported and is not recommended. There are some unofficial builds of pytorch ROCm on windows that exist that will give you a much better experience than this. This readme will be updated once official pytorch ROCm builds for windows come out.  
```pip install torch-directml``` Then you can launch ComfyUI with: ```python main.py --directml```  
#### Ascend NPUs  
For models compatible with Ascend Extension for PyTorch (torch_npu). To get started, ensure your environment meets the prerequisites outlined on the installation page. Here's a step-by-step guide tailored to your platform and installation method:  
1. Begin by installing the recommended or newer kernel version for Linux as specified in the Installation page of torch-npu, if necessary.
2. Proceed with the installation of Ascend Basekit, which includes the driver, firmware, and CANN, following the instructions provided for your specific platform.
3. Next, install the necessary packages for torch-npu by adhering to the platform-specific instructions on the Installation page.
4. Finally, adhere to the ComfyUI manual installation guide for Linux. Once all components are installed, you can run ComfyUI as described earlier.  
#### Cambricon MLUs  
For models compatible with Cambricon Extension for PyTorch (torch_mlu). Here's a step-by-step guide tailored to your platform and installation method:  
1. Install the Cambricon CNToolkit by adhering to the platform-specific instructions on the Installation
2. Next, install the PyTorch(torch_mlu) following the instructions on the Installation
3. Launch ComfyUI by running `python main.py`