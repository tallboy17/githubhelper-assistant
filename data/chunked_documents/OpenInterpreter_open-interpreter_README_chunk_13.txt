---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
Header 3: Customize System Message
---
You can inspect and configure Open Interpreter's system message to extend its functionality, modify permissions, or give it more context.  
```python
interpreter.system_message += """
Run shell commands with -y so the user doesn't have to confirm them.
"""
print(interpreter.system_message)
```