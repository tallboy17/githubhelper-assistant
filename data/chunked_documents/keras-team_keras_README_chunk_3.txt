---
repo: keras-team/keras
readme_filename: keras-team_keras_README.md
stars: 63162
forks: 19583
watchers: 63162
contributors_count: 406
license: Apache-2.0
Header 1: Keras 3: Deep Learning for Humans
Header 2: Installation
Header 3: Local installation
---
#### Minimal installation  
Keras 3 is compatible with Linux and MacOS systems. For Windows users, we recommend using WSL2 to run Keras.
To install a local development version:  
1. Install dependencies:  
```
pip install -r requirements.txt
```  
2. Run installation command from the root directory.  
```
python pip_build.py --install
```  
3. Run API generation script when creating PRs that update `keras_export` public APIs:  
```
./shell/api_gen.sh
```  
#### Adding GPU support  
The `requirements.txt` file will install a CPU-only version of TensorFlow, JAX, and PyTorch. For GPU support, we also
provide a separate `requirements-{backend}-cuda.txt` for TensorFlow, JAX, and PyTorch. These install all CUDA
dependencies via `pip` and expect a NVIDIA driver to be pre-installed. We recommend a clean python environment for each
backend to avoid CUDA version mismatches. As an example, here is how to create a Jax GPU environment with `conda`:  
```shell
conda create -y -n keras-jax python=3.10
conda activate keras-jax
pip install -r requirements-jax-cuda.txt
python pip_build.py --install
```