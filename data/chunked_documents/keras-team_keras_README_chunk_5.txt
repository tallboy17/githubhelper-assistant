---
repo: keras-team/keras
readme_filename: keras-team_keras_README.md
stars: 63162
forks: 19583
watchers: 63162
contributors_count: 406
license: Apache-2.0
Header 1: Keras 3: Deep Learning for Humans
Header 2: Backwards compatibility
---
Keras 3 is intended to work as a drop-in replacement for `tf.keras` (when using the TensorFlow backend). Just take your
existing `tf.keras` code, make sure that your calls to `model.save()` are using the up-to-date `.keras` format, and you're
done.  
If your `tf.keras` model does not include custom components, you can start running it on top of JAX or PyTorch immediately.  
If it does include custom components (e.g. custom layers or a custom `train_step()`), it is usually possible to convert it
to a backend-agnostic implementation in just a few minutes.  
In addition, Keras models can consume datasets in any format, regardless of the backend you're using:
you can train your models with your existing `tf.data.Dataset` pipelines or PyTorch `DataLoaders`.