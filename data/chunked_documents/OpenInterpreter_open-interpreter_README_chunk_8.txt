---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
---
**Update:** The Generator Update (0.1.5) introduced streaming:  
```python
message = "What operating system are we on?"

for chunk in interpreter.chat(message, display=False, stream=True):
print(chunk)
```