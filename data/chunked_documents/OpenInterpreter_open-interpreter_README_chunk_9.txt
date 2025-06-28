---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
Header 3: Interactive Chat
---
To start an interactive chat in your terminal, either run `interpreter` from the command line:  
```shell
interpreter
```  
Or `interpreter.chat()` from a .py file:  
```python
interpreter.chat()
```  
**You can also stream each chunk:**  
```python
message = "What operating system are we on?"

for chunk in interpreter.chat(message, display=False, stream=True):
print(chunk)
```