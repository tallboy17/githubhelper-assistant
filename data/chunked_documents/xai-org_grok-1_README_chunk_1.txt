---
repo: xai-org/grok-1
readme_filename: xai-org_grok-1_README.md
stars: 50291
forks: 8354
watchers: 50291
contributors_count: 6
license: Apache-2.0
Header 1: Grok-1
---
This repository contains JAX example code for loading and running the Grok-1 open-weights model.  
Make sure to download the checkpoint and place the `ckpt-0` directory in `checkpoints` - see Downloading the weights  
Then, run  
```shell
pip install -r requirements.txt
python run.py
```  
to test the code.  
The script loads the checkpoint and samples from the model on a test input.  
Due to the large size of the model (314B parameters), a machine with enough GPU memory is required to test the model with the example code.
The implementation of the MoE layer in this repository is not efficient. The implementation was chosen to avoid the need for custom kernels to validate the correctness of the model.