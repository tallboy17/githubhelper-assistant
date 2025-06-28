---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
Header 3: Save and Restore Chats
---
`interpreter.chat()` returns a List of messages, which can be used to resume a conversation with `interpreter.messages = messages`:  
```python
messages = interpreter.chat("My name is Killian.") # Save messages to 'messages'
interpreter.messages = [] # Reset interpreter ("Killian" will be forgotten)

interpreter.messages = messages # Resume chat from 'messages' ("Killian" will be remembered)
```