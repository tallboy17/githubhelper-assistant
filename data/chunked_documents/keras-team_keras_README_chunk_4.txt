---
repo: keras-team/keras
readme_filename: keras-team_keras_README.md
stars: 63162
forks: 19583
watchers: 63162
contributors_count: 406
license: Apache-2.0
Header 1: Keras 3: Deep Learning for Humans
Header 2: Configuring your backend
---
You can export the environment variable `KERAS_BACKEND` or you can edit your local config file at `~/.keras/keras.json`
to configure your backend. Available backend options are: `"tensorflow"`, `"jax"`, `"torch"`, `"openvino"`. Example:  
```
export KERAS_BACKEND="jax"
```  
In Colab, you can do:  
```python
import os
os.environ["KERAS_BACKEND"] = "jax"

import keras
```  
**Note:** The backend must be configured before importing `keras`, and the backend cannot be changed after
the package has been imported.  
**Note:** The OpenVINO backend is an inference-only backend, meaning it is designed only for running model
predictions using `model.predict()` method.