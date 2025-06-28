---
repo: pytorch/pytorch
readme_filename: pytorch_pytorch_README.md
stars: 91087
forks: 24541
watchers: 91087
contributors_count: 322
license: NOASSERTION
Header 2: Installation
Header 3: From Source
---
#### Prerequisites
If you are installing from source, you will need:
- Python 3.9 or later
- A compiler that fully supports C++17, such as clang or gcc (gcc 9.4.0 or newer is required, on Linux)
- Visual Studio or Visual Studio Build Tool (Windows only)  
\* PyTorch CI uses Visual C++ BuildTools, which come with Visual Studio Enterprise,
Professional, or Community Editions. You can also install the build tools from
 The build tools *do not*
come with Visual Studio Code by default.  
An example of environment setup is shown below:  
* Linux:  
```bash
$ source /bin/activate
$ conda create -y -n 
$ conda activate 
```  
* Windows:  
```bash
$ source \Scripts\activate.bat
$ conda create -y -n 
$ conda activate 
$ call "C:\Program Files\Microsoft Visual Studio\\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
```  
A conda environment is not required.  You can also do a PyTorch build in a
standard virtual environment, e.g., created with tools like `uv`, provided
your system has installed all the necessary dependencies unavailable as pip
packages (e.g., CUDA, MKL.)  
##### NVIDIA CUDA Support
If you want to compile with CUDA support, select a supported version of CUDA from our support matrix, then install the following:
- NVIDIA CUDA
- NVIDIA cuDNN v8.5 or above
- Compiler compatible with CUDA  
Note: You could refer to the cuDNN Support Matrix for cuDNN versions with the various supported CUDA, CUDA driver and NVIDIA hardware  
If you want to disable CUDA support, export the environment variable `USE_CUDA=0`.
Other potentially useful environment variables may be found in `setup.py`.  If
CUDA is installed in a non-standard location, set PATH so that the nvcc you
want to use can be found (e.g., `export PATH=/usr/local/cuda-12.8/bin:$PATH`).  
If you are building for NVIDIA's Jetson platforms (Jetson Nano, TX1, TX2, AGX Xavier), Instructions to install PyTorch for Jetson Nano are available here  
##### AMD ROCm Support
If you want to compile with ROCm support, install
- AMD ROCm 4.0 and above installation
- ROCm is currently supported only for Linux systems.  
By default the build system expects ROCm to be installed in `/opt/rocm`. If ROCm is installed in a different directory, the `ROCM_PATH` environment variable must be set to the ROCm installation directory. The build system automatically detects the AMD GPU architecture. Optionally, the AMD GPU architecture can be explicitly set with the `PYTORCH_ROCM_ARCH` environment variable AMD GPU architecture  
If you want to disable ROCm support, export the environment variable `USE_ROCM=0`.
Other potentially useful environment variables may be found in `setup.py`.  
##### Intel GPU Support
If you want to compile with Intel GPU support, follow these
- PyTorch Prerequisites for Intel GPUs instructions.
- Intel GPU is supported for Linux and Windows.  
If you want to disable Intel GPU support, export the environment variable `USE_XPU=0`.
Other potentially useful environment variables may be found in `setup.py`.  
#### Get the PyTorch Source
```bash
git clone 
cd pytorch
# if you are updating an existing checkout
git submodule sync
git submodule update --init --recursive
```  
#### Install Dependencies  
**Common**  
```bash
conda install cmake ninja
# Run this command from the PyTorch directory after cloning the source code using the “Get the PyTorch Source“ section below
pip install -r requirements.txt
```  
**On Linux**  
```bash
pip install mkl-static mkl-include
# CUDA only: Add LAPACK support for the GPU if needed
# magma installation: run with active conda environment. specify CUDA version to install
.ci/docker/common/install_magma_conda.sh 12.4

# (optional) If using torch.compile with inductor/triton, install the matching version of triton
# Run from the pytorch directory after cloning
# For Intel GPU support, please explicitly `export USE_XPU=1` before running command.
make triton
```  
**On MacOS**  
```bash
# Add this package on intel x86 processor machines only
pip install mkl-static mkl-include
# Add these packages if torch.distributed is needed
conda install pkg-config libuv
```  
**On Windows**  
```bash
pip install mkl-static mkl-include
# Add these packages if torch.distributed is needed.
# Distributed package support on Windows is a prototype feature and is subject to changes.
conda install -c conda-forge libuv=1.39
```  
#### Install PyTorch
**On Linux**  
If you're compiling for AMD ROCm then first run this command:
```bash
# Only run this if you're compiling for ROCm
python tools/amd_build/build_amd.py
```  
Install PyTorch
```bash
export CMAKE_PREFIX_PATH="${CONDA_PREFIX:-'$(dirname $(which conda))/../'}:${CMAKE_PREFIX_PATH}"
python setup.py develop
```  
**On macOS**  
```bash
python3 setup.py develop
```  
**On Windows**  
If you want to build legacy python code, please refer to Building on legacy code and CUDA  
**CPU-only builds**  
In this mode PyTorch computations will run on your CPU, not your GPU.  
```cmd
python setup.py develop
```  
Note on OpenMP: The desired OpenMP implementation is Intel OpenMP (iomp). In order to link against iomp, you'll need to manually download the library and set up the building environment by tweaking `CMAKE_INCLUDE_PATH` and `LIB`. The instruction here is an example for setting up both MKL and Intel OpenMP. Without these configurations for CMake, Microsoft Visual C OpenMP runtime (vcomp) will be used.  
**CUDA based build**  
In this mode PyTorch computations will leverage your GPU via CUDA for faster number crunching  
NVTX is needed to build Pytorch with CUDA.
NVTX is a part of CUDA distributive, where it is called "Nsight Compute". To install it onto an already installed CUDA run CUDA installation once again and check the corresponding checkbox.
Make sure that CUDA with Nsight Compute is installed after Visual Studio.  
Currently, VS 2017 / 2019, and Ninja are supported as the generator of CMake. If `ninja.exe` is detected in `PATH`, then Ninja will be used as the default generator, otherwise, it will use VS 2017 / 2019.
 If Ninja is selected as the generator, the latest MSVC will get selected as the underlying toolchain.  
Additional libraries such as
Magma, oneDNN, a.k.a. MKLDNN or DNNL, and Sccache are often needed. Please refer to the installation-helper to install them.  
You can refer to the build_pytorch.bat script for some other environment variables configurations  
```cmd
cmd

:: Set the environment variables after you have downloaded and unzipped the mkl package,
:: else CMake would throw an error as `Could NOT find OpenMP`.
set CMAKE_INCLUDE_PATH={Your directory}\mkl\include
set LIB={Your directory}\mkl\lib;%LIB%

:: Read the content in the previous section carefully before you proceed.
:: [Optional] If you want to override the underlying toolset used by Ninja and Visual Studio with CUDA, please run the following script block.
:: "Visual Studio 2019 Developer Command Prompt" will be run automatically.
:: Make sure you have CMake >= 3.12 before you do this when you use the Visual Studio generator.
set CMAKE_GENERATOR_TOOLSET_VERSION=14.27
set DISTUTILS_USE_SDK=1
for /f "usebackq tokens=*" %i in (`"%ProgramFiles(x86)%\Microsoft Visual Studio\Installer\vswhere.exe" -version [15^,17^) -products * -latest -property installationPath`) do call "%i\VC\Auxiliary\Build\vcvarsall.bat" x64 -vcvars_ver=%CMAKE_GENERATOR_TOOLSET_VERSION%

:: [Optional] If you want to override the CUDA host compiler
set CUDAHOSTCXX=C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.27.29110\bin\HostX64\x64\cl.exe

python setup.py develop

```  
**Intel GPU builds**  
In this mode PyTorch with Intel GPU support will be built.  
Please make sure the common prerequisites as well as the prerequisites for Intel GPU are properly installed and the environment variables are configured prior to starting the build. For build tool support, `Visual Studio 2022` is required.  
Then PyTorch can be built with the command:  
```cmd
:: CMD Commands:
:: Set the CMAKE_PREFIX_PATH to help find corresponding packages
:: %CONDA_PREFIX% only works after `conda activate custom_env`

if defined CMAKE_PREFIX_PATH (
set "CMAKE_PREFIX_PATH=%CONDA_PREFIX%\Library;%CMAKE_PREFIX_PATH%"
) else (
set "CMAKE_PREFIX_PATH=%CONDA_PREFIX%\Library"
)

python setup.py develop
```  
##### Adjust Build Options (Optional)  
You can adjust the configuration of cmake variables optionally (without building first), by doing
the following. For example, adjusting the pre-detected directories for CuDNN or BLAS can be done
with such a step.  
On Linux
```bash
export CMAKE_PREFIX_PATH="${CONDA_PREFIX:-'$(dirname $(which conda))/../'}:${CMAKE_PREFIX_PATH}"
CMAKE_ONLY=1 python setup.py build
ccmake build  # or cmake-gui build
```  
On macOS
```bash
export CMAKE_PREFIX_PATH="${CONDA_PREFIX:-'$(dirname $(which conda))/../'}:${CMAKE_PREFIX_PATH}"
MACOSX_DEPLOYMENT_TARGET=10.9 CC=clang CXX=clang++ CMAKE_ONLY=1 python setup.py build
ccmake build  # or cmake-gui build
```