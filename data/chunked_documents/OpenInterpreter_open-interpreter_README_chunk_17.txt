---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
Header 3: Interactive Mode Commands
---
In the interactive mode, you can use the below commands to enhance your experience. Here's a list of available commands:  
**Available Commands:**  
- `%verbose [true/false]`: Toggle verbose mode. Without arguments or with `true` it
enters verbose mode. With `false` it exits verbose mode.
- `%reset`: Resets the current session's conversation.
- `%undo`: Removes the previous user message and the AI's response from the message history.
- `%tokens [prompt]`: (_Experimental_) Calculate the tokens that will be sent with the next prompt as context and estimate their cost. Optionally calculate the tokens and estimated cost of a `prompt` if one is provided. Relies on LiteLLM's `cost_per_token()` method for estimated costs.
- `%help`: Show the help message.