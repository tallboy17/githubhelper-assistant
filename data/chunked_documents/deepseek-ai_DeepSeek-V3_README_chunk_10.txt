---
repo: deepseek-ai/DeepSeek-V3
readme_filename: deepseek-ai_DeepSeek-V3_README.md
stars: 97889
forks: 15924
watchers: 97889
contributors_count: 21
license: MIT
Header 2: 6. How to Run Locally
Header 3: 6.1 Inference with DeepSeek-Infer Demo (example only)
---
#### System Requirements  
> [!NOTE]
> Linux with Python 3.10 only. Mac and Windows are not supported.  
Dependencies:
```pip-requirements
torch==2.4.1
triton==3.0.0
transformers==4.46.3
safetensors==0.4.5
```
#### Model Weights & Demo Code Preparation  
First, clone our DeepSeek-V3 GitHub repository:  
```shell
git clone 
```  
Navigate to the `inference` folder and install dependencies listed in `requirements.txt`. Easiest way is to use a package manager like `conda` or `uv` to create a new virtual environment and install the dependencies.  
```shell
cd DeepSeek-V3/inference
pip install -r requirements.txt
```  
Download the model weights from Hugging Face, and put them into `/path/to/DeepSeek-V3` folder.  
#### Model Weights Conversion  
Convert Hugging Face model weights to a specific format:  
```shell
python convert.py --hf-ckpt-path /path/to/DeepSeek-V3 --save-path /path/to/DeepSeek-V3-Demo --n-experts 256 --model-parallel 16
```  
#### Run  
Then you can chat with DeepSeek-V3:  
```shell
torchrun --nnodes 2 --nproc-per-node 8 --node-rank $RANK --master-addr $ADDR generate.py --ckpt-path /path/to/DeepSeek-V3-Demo --config configs/config_671B.json --interactive --temperature 0.7 --max-new-tokens 200
```  
Or batch inference on a given file:  
```shell
torchrun --nnodes 2 --nproc-per-node 8 --node-rank $RANK --master-addr $ADDR generate.py --ckpt-path /path/to/DeepSeek-V3-Demo --config configs/config_671B.json --input-file $FILE
```