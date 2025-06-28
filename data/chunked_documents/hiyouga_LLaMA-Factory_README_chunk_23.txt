---
repo: hiyouga/LLaMA-Factory
readme_filename: hiyouga_LLaMA-Factory_README.md
stars: 53088
forks: 6501
watchers: 53088
contributors_count: 192
license: Apache-2.0
Header 2: Getting Started
Header 3: Use W&B Logger
---
To use Weights & Biases for logging experimental results, you need to add the following arguments to yaml files.  
```yaml
report_to: wandb
run_name: test_run # optional
```  
Set `WANDB_API_KEY` to your key when launching training tasks to log in with your W&B account.