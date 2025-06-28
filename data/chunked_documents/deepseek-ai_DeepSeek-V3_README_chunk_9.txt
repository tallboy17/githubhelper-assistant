---
repo: deepseek-ai/DeepSeek-V3
readme_filename: deepseek-ai_DeepSeek-V3_README.md
stars: 97889
forks: 15924
watchers: 97889
contributors_count: 21
license: MIT
Header 2: 6. How to Run Locally
---
DeepSeek-V3 can be deployed locally using the following hardware and open-source community software:  
1. **DeepSeek-Infer Demo**: We provide a simple and lightweight demo for FP8 and BF16 inference.
2. **SGLang**: Fully support the DeepSeek-V3 model in both BF16 and FP8 inference modes, with Multi-Token Prediction coming soon.
3. **LMDeploy**: Enables efficient FP8 and BF16 inference for local and cloud deployment.
4. **TensorRT-LLM**: Currently supports BF16 inference and INT4/8 quantization, with FP8 support coming soon.
5. **vLLM**: Support DeepSeek-V3 model with FP8 and BF16 modes for tensor parallelism and pipeline parallelism.
6. **LightLLM**: Supports efficient single-node or multi-node deployment for FP8 and BF16.
7. **AMD GPU**: Enables running the DeepSeek-V3 model on AMD GPUs via SGLang in both BF16 and FP8 modes.
8. **Huawei Ascend NPU**: Supports running DeepSeek-V3 on Huawei Ascend devices in both INT8 and BF16.  
Since FP8 training is natively adopted in our framework, we only provide FP8 weights. If you require BF16 weights for experimentation, you can use the provided conversion script to perform the transformation.  
Here is an example of converting FP8 weights to BF16:  
```shell
cd inference
python fp8_cast_bf16.py --input-fp8-hf-path /path/to/fp8_weights --output-bf16-hf-path /path/to/bf16_weights
```  
> [!NOTE]
> Hugging Face's Transformers has not been directly supported yet.