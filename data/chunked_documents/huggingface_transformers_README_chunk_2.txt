---
repo: huggingface/transformers
readme_filename: huggingface_transformers_README.md
stars: 146147
forks: 29471
watchers: 146147
contributors_count: 436
license: Apache-2.0
Header 2: Installation
---
Transformers works with Python 3.9+ PyTorch 2.1+, TensorFlow 2.6+, and Flax 0.4.1+.  
Create and activate a virtual environment with venv or uv, a fast Rust-based Python package and project manager.  
```py
# venv
python -m venv .my-env
source .my-env/bin/activate
# uv
uv venv .my-env
source .my-env/bin/activate
```  
Install Transformers in your virtual environment.  
```py
# pip
pip install "transformers[torch]"

# uv
uv pip install "transformers[torch]"
```  
Install Transformers from source if you want the latest changes in the library or are interested in contributing. However, the *latest* version may not be stable. Feel free to open an issue if you encounter an error.  
```shell
git clone 
cd transformers

# pip
pip install .[torch]

# uv
uv pip install .[torch]
```