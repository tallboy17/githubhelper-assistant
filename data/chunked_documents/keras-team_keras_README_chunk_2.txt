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
Header 3: Install with pip
---
Keras 3 is available on PyPI as `keras`. Note that Keras 2 remains available as the `tf-keras` package.  
1. Install `keras`:  
```
pip install keras --upgrade
```  
2. Install backend package(s).  
To use `keras`, you should also install the backend of choice: `tensorflow`, `jax`, or `torch`.
Note that `tensorflow` is required for using certain Keras 3 features: certain preprocessing layers
as well as `tf.data` pipelines.