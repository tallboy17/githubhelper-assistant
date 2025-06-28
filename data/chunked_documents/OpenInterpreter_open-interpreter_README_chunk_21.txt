---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Safety Notice
---
Since generated code is executed in your local environment, it can interact with your files and system settings, potentially leading to unexpected outcomes like data loss or security risks.  
**⚠️ Open Interpreter will ask for user confirmation before executing code.**  
You can run `interpreter -y` or set `interpreter.auto_run = True` to bypass this confirmation, in which case:  
- Be cautious when requesting commands that modify files or system settings.
- Watch Open Interpreter like a self-driving car, and be prepared to end the process by closing your terminal.
- Consider running Open Interpreter in a restricted environment like Google Colab or Replit. These environments are more isolated, reducing the risks of executing arbitrary code.  
There is **experimental** support for a safe mode to help mitigate some risks.