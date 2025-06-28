---
repo: pytorch/pytorch
readme_filename: pytorch_pytorch_README.md
stars: 91087
forks: 24541
watchers: 91087
contributors_count: 322
license: NOASSERTION
Header 2: More About PyTorch
Header 3: Dynamic Neural Networks: Tape-Based Autograd
---
PyTorch has a unique way of building neural networks: using and replaying a tape recorder.  
Most frameworks such as TensorFlow, Theano, Caffe, and CNTK have a static view of the world.
One has to build a neural network and reuse the same structure again and again.
Changing the way the network behaves means that one has to start from scratch.  
With PyTorch, we use a technique called reverse-mode auto-differentiation, which allows you to
change the way your network behaves arbitrarily with zero lag or overhead. Our inspiration comes
from several research papers on this topic, as well as current and past work such as
torch-autograd,
autograd,
Chainer, etc.  
While this technique is not unique to PyTorch, it's one of the fastest implementations of it to date.
You get the best of speed and flexibility for your crazy research.  
!Dynamic graph