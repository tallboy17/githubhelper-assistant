---
repo: tensorflow/models
readme_filename: tensorflow_models_README.md
stars: 77596
forks: 45569
watchers: 77596
contributors_count: 359
license: NOASSERTION
Header 1: Welcome to the Model Garden for TensorFlow
Header 2: Installation
---
To install the current release of tensorflow-models, please follow any one of the methods described below.  
#### Method 1: Install the TensorFlow Model Garden pip package  
  
**tf-models-official** is the stable Model Garden package. Please check out the releases to see what are available modules.  
pip3 will install all models and dependencies automatically.  
```shell
pip3 install tf-models-official
```  
Please check out our examples:
- basic library import
- nlp model building
to learn how to use a PIP package.  
Note that **tf-models-official** may not include the latest changes in the master branch of this
github repo. To include latest changes, you may install **tf-models-nightly**,
which is the nightly Model Garden package created daily automatically.  
```shell
pip3 install tf-models-nightly
```  
  
#### Method 2: Clone the source  
  
1. Clone the GitHub repository:  
```shell
git clone 
```  
2. Add the top-level ***/models*** folder to the Python path.  
```shell
export PYTHONPATH=$PYTHONPATH:/path/to/models
```  
If you are using in a Windows environment, you may need to use the following command with PowerShell:
```shell
$env:PYTHONPATH += ":\path\to\models"
```  
If you are using a Colab notebook, please set the Python path with os.environ.  
```python
import os
os.environ['PYTHONPATH'] += ":/path/to/models"
```  
3. Install other dependencies  
```shell
pip3 install --user -r models/official/requirements.txt
```  
Finally, if you are using nlp packages, please also install
**tensorflow-text-nightly**:  
```shell
pip3 install tensorflow-text-nightly
```  
