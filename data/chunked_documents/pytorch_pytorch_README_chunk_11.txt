---
repo: pytorch/pytorch
readme_filename: pytorch_pytorch_README.md
stars: 91087
forks: 24541
watchers: 91087
contributors_count: 322
license: NOASSERTION
Header 2: Installation
Header 3: Docker Image
---
#### Using pre-built images  
You can also pull a pre-built docker image from Docker Hub and run with docker v19.03+  
```bash
docker run --gpus all --rm -ti --ipc=host pytorch/pytorch:latest
```  
Please note that PyTorch uses shared memory to share data between processes, so if torch multiprocessing is used (e.g.
for multithreaded data loaders) the default shared memory segment size that container runs with is not enough, and you
should increase shared memory size either with `--ipc=host` or `--shm-size` command line options to `nvidia-docker run`.  
#### Building the image yourself  
**NOTE:** Must be built with a docker version > 18.06  
The `Dockerfile` is supplied to build images with CUDA 11.1 support and cuDNN v8.
You can pass `PYTHON_VERSION=x.y` make variable to specify which Python version is to be used by Miniconda, or leave it
unset to use the default.  
```bash
make -f docker.Makefile
# images are tagged as docker.io/${your_docker_username}/pytorch
```  
You can also pass the `CMAKE_VARS="..."` environment variable to specify additional CMake variables to be passed to CMake during the build.
See setup.py for the list of available variables.  
```bash
make -f docker.Makefile
```