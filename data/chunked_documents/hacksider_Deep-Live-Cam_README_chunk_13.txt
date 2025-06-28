---
repo: hacksider/Deep-Live-Cam
readme_filename: hacksider_Deep-Live-Cam_README.md
stars: 71366
forks: 10204
watchers: 71366
contributors_count: 50
license: AGPL-3.0
Header 2: Installation (Manual)
Header 3: GPU Acceleration
---
**CUDA Execution Provider (Nvidia)**  
1. Install CUDA Toolkit 12.8.0
2. Install cuDNN v8.9.7 for CUDA 12.x (required for onnxruntime-gpu):
- Download cuDNN v8.9.7 for CUDA 12.x
- Make sure the cuDNN bin directory is in your system PATH
3. Install dependencies:  
```bash
pip install -U torch torchvision torchaudio --index-url 
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu==1.21.0
```  
3. Usage:  
```bash
python run.py --execution-provider cuda
```  
**CoreML Execution Provider (Apple Silicon)**  
Apple Silicon (M1/M2/M3) specific installation:  
1. Make sure you've completed the macOS setup above using Python 3.10.
2. Install dependencies:  
```bash
pip uninstall onnxruntime onnxruntime-silicon
pip install onnxruntime-silicon==1.13.1
```  
3. Usage (important: specify Python 3.10):  
```bash
python3.10 run.py --execution-provider coreml
```  
**Important Notes for macOS:**
- You **must** use Python 3.10, not newer versions like 3.11 or 3.13
- Always run with `python3.10` command not just `python` if you have multiple Python versions installed
- If you get error about `_tkinter` missing, reinstall the tkinter package: `brew reinstall python-tk@3.10`
- If you get model loading errors, check that your models are in the correct folder
- If you encounter conflicts with other Python versions, consider uninstalling them:
```bash
# List all installed Python versions
brew list | grep python

# Uninstall conflicting versions if needed
brew uninstall --ignore-dependencies python@3.11 python@3.13

# Keep only Python 3.10
brew cleanup
```  
**CoreML Execution Provider (Apple Legacy)**  
1. Install dependencies:  
```bash
pip uninstall onnxruntime onnxruntime-coreml
pip install onnxruntime-coreml==1.13.1
```  
2. Usage:  
```bash
python run.py --execution-provider coreml
```  
**DirectML Execution Provider (Windows)**  
1. Install dependencies:  
```bash
pip uninstall onnxruntime onnxruntime-directml
pip install onnxruntime-directml==1.15.1
```  
2. Usage:  
```bash
python run.py --execution-provider directml
```  
**OpenVINO™ Execution Provider (Intel)**  
1. Install dependencies:  
```bash
pip uninstall onnxruntime onnxruntime-openvino
pip install onnxruntime-openvino==1.15.0
```  
2. Usage:  
```bash
python run.py --execution-provider openvino
```
