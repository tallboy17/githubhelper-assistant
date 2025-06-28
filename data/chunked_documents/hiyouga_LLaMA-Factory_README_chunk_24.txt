---
repo: hiyouga/LLaMA-Factory
readme_filename: hiyouga_LLaMA-Factory_README.md
stars: 53088
forks: 6501
watchers: 53088
contributors_count: 192
license: Apache-2.0
Header 2: Getting Started
Header 3: Use SwanLab Logger
---
To use SwanLab for logging experimental results, you need to add the following arguments to yaml files.  
```yaml
use_swanlab: true
swanlab_run_name: test_run # optional
```  
When launching training tasks, you can log in to SwanLab in three ways:  
1. Add `swanlab_api_key=` to the yaml file, and set it to your API key.
2. Set the environment variable `SWANLAB_API_KEY` to your API key.
3. Use the `swanlab login` command to complete the login.