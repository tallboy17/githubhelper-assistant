---
repo: huggingface/transformers
readme_filename: huggingface_transformers_README.md
stars: 146142
forks: 29471
watchers: 146142
contributors_count: 436
license: Apache-2.0
Header 2: Why shouldn't I use Transformers?
---
- This library is not a modular toolbox of building blocks for neural nets. The code in the model files is not refactored with additional abstractions on purpose, so that researchers can quickly iterate on each of the models without diving into additional abstractions/files.
- The training API is optimized to work with PyTorch models provided by Transformers. For generic machine learning loops, you should use another library like Accelerate.
- The example scripts) are only *examples*. They may not necessarily work out-of-the-box on your specific use case and you'll need to adapt the code for it to work.