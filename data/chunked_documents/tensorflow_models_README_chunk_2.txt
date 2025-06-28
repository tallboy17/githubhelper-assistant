---
repo: tensorflow/models
readme_filename: tensorflow_models_README.md
stars: 77596
forks: 45569
watchers: 77596
contributors_count: 359
license: NOASSERTION
Header 1: Welcome to the Model Garden for TensorFlow
---
The TensorFlow Model Garden is a repository with a number of different
implementations of state-of-the-art (SOTA) models and modeling solutions for
TensorFlow users. We aim to demonstrate the best practices for modeling so that
TensorFlow users can take full advantage of TensorFlow for their research and
product development.  
To improve the transparency and reproducibility of our models, training logs on
TensorBoard.dev are also provided for models to the
extent possible though not all models are suitable.  
| Directory | Description |
|-----------|-------------|
| official | • A collection of example implementations for SOTA models using the latest TensorFlow 2's high-level APIs• Officially maintained, supported, and kept up to date with the latest TensorFlow 2 APIs by TensorFlow• Reasonably optimized for fast performance while still being easy to read For more details on the capabilities, check the guide on the Model-garden|
| research | • A collection of research model implementations in TensorFlow 1 or 2 by researchers• Maintained and supported by researchers |
| community | • A curated list of the GitHub repositories with machine learning models and implementations powered by TensorFlow 2 |
| orbit | • A flexible and lightweight library that users can easily use or fork when writing customized training loop code in TensorFlow 2.x. It seamlessly integrates with `tf.distribute` and supports running on different device types (CPU, GPU, and TPU). |