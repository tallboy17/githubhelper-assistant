---
repo: hiyouga/LLaMA-Factory
readme_filename: hiyouga_LLaMA-Factory_README.md
stars: 53088
forks: 6501
watchers: 53088
contributors_count: 192
license: Apache-2.0
Header 2: Getting Started
Header 3: Installation
---
> [!IMPORTANT]
> Installation is mandatory.  
#### Install from Source  
```bash
git clone --depth 1 
cd LLaMA-Factory
pip install -e ".[torch,metrics]" --no-build-isolation
```  
Extra dependencies available: torch, torch-npu, metrics, deepspeed, liger-kernel, bitsandbytes, hqq, eetq, gptq, aqlm, vllm, sglang, galore, apollo, badam, adam-mini, qwen, minicpm_v, modelscope, openmind, swanlab, dev  
#### Install from Docker Image  
```bash
docker run -it --rm --gpus=all --ipc=host hiyouga/llamafactory:latest
```  
This image is built on Ubuntu 22.04 (x86\_64), CUDA 12.4, Python 3.11, PyTorch 2.6.0, and Flash-attn 2.7.4.  
Find the pre-built images:   
Please refer to build docker to build the image yourself.  
Setting up a virtual environment with uv  
Create an isolated Python environment with uv:  
```bash
uv sync --extra torch --extra metrics --prerelease=allow
```  
Run LLaMA-Factory in the isolated environment:  
```bash
uv run --prerelease=allow llamafactory-cli train examples/train_lora/llama3_lora_pretrain.yaml
```  
  
For Windows users  
#### Install PyTorch  
You need to manually install the GPU version of PyTorch on the Windows platform. Please refer to the official website and the following command to install PyTorch with CUDA support:  
```bash
pip uninstall torch torchvision torchaudio
pip install torch torchvision torchaudio --index-url 
python -c "import torch; print(torch.cuda.is_available())"
```  
If you see `True` then you have successfully installed PyTorch with CUDA support.  
Try `dataloader_num_workers: 0` if you encounter `Can't pickle local object` error.  
#### Install BitsAndBytes  
If you want to enable the quantized LoRA (QLoRA) on the Windows platform, you need to install a pre-built version of `bitsandbytes` library, which supports CUDA 11.1 to 12.2, please select the appropriate release version based on your CUDA version.  
```bash
pip install 
```  
#### Install Flash Attention-2  
To enable FlashAttention-2 on the Windows platform, please use the script from flash-attention-windows-wheel to compile and install it by yourself.  
  
For Ascend NPU users  
To install LLaMA Factory on Ascend NPU devices, please upgrade Python to version 3.10 or higher and specify extra dependencies: `pip install -e ".[torch-npu,metrics]"`. Additionally, you need to install the **Ascend CANN Toolkit and Kernels**. Please follow the installation tutorial or use the following commands:  
```bash
# replace the url according to your CANN version and devices
# install CANN Toolkit
wget  -i)".run
bash Ascend-cann-toolkit_8.0.0.alpha002_linux-"$(uname -i)".run --install

# install CANN Kernels
wget  -i)".run
bash Ascend-cann-kernels-910b_8.0.0.alpha002_linux-"$(uname -i)".run --install

# set env variables
source /usr/local/Ascend/ascend-toolkit/set_env.sh
```  
| Requirement  | Minimum | Recommend      |
| ------------ | ------- | -------------- |
| CANN         | 8.0.RC1 | 8.0.0.alpha002 |
| torch        | 2.1.0   | 2.4.0          |
| torch-npu    | 2.1.0   | 2.4.0.post2    |
| deepspeed    | 0.13.2  | 0.13.2         |
| vllm-ascend  | -       | 0.7.3          |  
Remember to use `ASCEND_RT_VISIBLE_DEVICES` instead of `CUDA_VISIBLE_DEVICES` to specify the device to use.  
If you cannot infer model on NPU devices, try setting `do_sample: false` in the configurations.  
Download the pre-built Docker images: 32GB | 64GB  
#### Install BitsAndBytes  
To use QLoRA based on bitsandbytes on Ascend NPU, please follow these 3 steps:  
1. Manually compile bitsandbytes: Refer to the installation documentation for the NPU version of bitsandbytes to complete the compilation and installation. The compilation requires a cmake version of at least 3.22.1 and a g++ version of at least 12.x.  
```bash
# Install bitsandbytes from source
# Clone bitsandbytes repo, Ascend NPU backend is currently enabled on multi-backend-refactor branch
git clone -b multi-backend-refactor 
cd bitsandbytes/

# Install dependencies
pip install -r requirements-dev.txt

# Install the dependencies for the compilation tools. Note that the commands for this step may vary depending on the operating system. The following are provided for reference
apt-get install -y build-essential cmake

# Compile & install
cmake -DCOMPUTE_BACKEND=npu -S .
make
pip install .
```  
2. Install transformers from the main branch.  
```bash
git clone -b main 
cd transformers
pip install .
```  
3. Set `double_quantization: false` in the configuration. You can refer to the example.  
