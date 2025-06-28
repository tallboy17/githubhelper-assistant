---
repo: huggingface/transformers
readme_filename: huggingface_transformers_README.md
stars: 146147
forks: 29471
watchers: 146147
contributors_count: 436
license: Apache-2.0
Header 2: Quickstart
---
Get started with Transformers right away with the Pipeline API. The `Pipeline` is a high-level inference class that supports text, audio, vision, and multimodal tasks. It handles preprocessing the input and returns the appropriate output.  
Instantiate a pipeline and specify model to use for text generation. The model is downloaded and cached so you can easily reuse it again. Finally, pass some text to prompt the model.  
```py
from transformers import pipeline

pipeline = pipeline(task="text-generation", model="Qwen/Qwen2.5-1.5B")
pipeline("the secret to baking a really good cake is ")
[{'generated_text': 'the secret to baking a really good cake is 1) to use the right ingredients and 2) to follow the recipe exactly. the recipe for the cake is as follows: 1 cup of sugar, 1 cup of flour, 1 cup of milk, 1 cup of butter, 1 cup of eggs, 1 cup of chocolate chips. if you want to make 2 cakes, how much sugar do you need? To make 2 cakes, you will need 2 cups of sugar.'}]
```  
To chat with a model, the usage pattern is the same. The only difference is you need to construct a chat history (the input to `Pipeline`) between you and the system.  
> [!TIP]
> You can also chat with a model directly from the command line.
> ```shell
> transformers chat Qwen/Qwen2.5-0.5B-Instruct
> ```  
```py
import torch
from transformers import pipeline

chat = [
{"role": "system", "content": "You are a sassy, wise-cracking robot as imagined by Hollywood circa 1986."},
{"role": "user", "content": "Hey, can you tell me any fun things to do in New York?"}
]

pipeline = pipeline(task="text-generation", model="meta-llama/Meta-Llama-3-8B-Instruct", torch_dtype=torch.bfloat16, device_map="auto")
response = pipeline(chat, max_new_tokens=512)
print(response[0]["generated_text"][-1]["content"])
```  
Expand the examples below to see how `Pipeline` works for different modalities and tasks.  

Automatic speech recognition  
```py
from transformers import pipeline

pipeline = pipeline(task="automatic-speech-recognition", model="openai/whisper-large-v3")
pipeline("
{'text': ' I have a dream that one day this nation will rise up and live out the true meaning of its creed.'}
```  
  

Image classification  


  
```py
from transformers import pipeline

pipeline = pipeline(task="image-classification", model="facebook/dinov2-small-imagenet1k-1-layer")
pipeline("
[{'label': 'macaw', 'score': 0.997848391532898},
{'label': 'sulphur-crested cockatoo, Kakatoe galerita, Cacatua galerita',
'score': 0.0016551691805943847},
{'label': 'lorikeet', 'score': 0.00018523589824326336},
{'label': 'African grey, African gray, Psittacus erithacus',
'score': 7.85409429227002e-05},
{'label': 'quail', 'score': 5.502637941390276e-05}]
```  
  

Visual question answering  


  
```py
from transformers import pipeline

pipeline = pipeline(task="visual-question-answering", model="Salesforce/blip-vqa-base")
pipeline(
image="
question="What is in the image?",
)
[{'answer': 'statue of liberty'}]
```  
