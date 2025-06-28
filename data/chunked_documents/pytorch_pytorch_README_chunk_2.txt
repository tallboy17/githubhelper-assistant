---
repo: pytorch/pytorch
readme_filename: pytorch_pytorch_README.md
stars: 91087
forks: 24541
watchers: 91087
contributors_count: 322
license: NOASSERTION
Header 2: More About PyTorch
---
Learn the basics of PyTorch  
At a granular level, PyTorch is a library that consists of the following components:  
| Component | Description |
| ---- | --- |
| **torch** | A Tensor library like NumPy, with strong GPU support |
| **torch.autograd** | A tape-based automatic differentiation library that supports all differentiable Tensor operations in torch |
| **torch.jit** | A compilation stack (TorchScript) to create serializable and optimizable models from PyTorch code  |
| **torch.nn** | A neural networks library deeply integrated with autograd designed for maximum flexibility |
| **torch.multiprocessing** | Python multiprocessing, but with magical memory sharing of torch Tensors across processes. Useful for data loading and Hogwild training |
| **torch.utils** | DataLoader and other utility functions for convenience |  
Usually, PyTorch is used either as:  
- A replacement for NumPy to use the power of GPUs.
- A deep learning research platform that provides maximum flexibility and speed.  
Elaborating Further: