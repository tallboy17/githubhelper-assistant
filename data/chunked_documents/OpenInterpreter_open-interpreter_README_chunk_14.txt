---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
Header 3: Change your Language Model
---
Open Interpreter uses LiteLLM to connect to hosted language models.  
You can change the model by setting the model parameter:  
```shell
interpreter --model gpt-3.5-turbo
interpreter --model claude-2
interpreter --model command-nightly
```  
In Python, set the model on the object:  
```python
interpreter.llm.model = "gpt-3.5-turbo"
```  
Find the appropriate "model" string for your language model here.