---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
Header 3: Running Open Interpreter locally
---
#### Terminal  
Open Interpreter can use OpenAI-compatible server to run models locally. (LM Studio, jan.ai, ollama etc)  
Simply run `interpreter` with the api_base URL of your inference server (for LM studio it is ` by default):  
```shell
interpreter --api_base " --api_key "fake_key"
```  
Alternatively you can use Llamafile without installing any third party software just by running  
```shell
interpreter --local
```  
for a more detailed guide check out this video by Mike Bird  
**How to run LM Studio in the background.**  
1. Download  then start it.
2. Select a model then click **↓ Download**.
3. Click the **↔️** button on the left (below 💬).
4. Select your model at the top, then click **Start Server**.  
Once the server is running, you can begin your conversation with Open Interpreter.  
> **Note:** Local mode sets your `context_window` to 3000, and your `max_tokens` to 1000. If your model has different requirements, set these parameters manually (see below).  
#### Python  
Our Python package gives you more control over each setting. To replicate and connect to LM Studio, use these settings:  
```python
from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "openai/x" # Tells OI to send messages in OpenAI's format
interpreter.llm.api_key = "fake_key" # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.api_base = " # Point this at any OpenAI compatible server

interpreter.chat()
```  
#### Context Window, Max Tokens  
You can modify the `max_tokens` and `context_window` (in tokens) of locally running models.  
For local mode, smaller context windows will use less RAM, so we recommend trying a much shorter window (~1000) if it's failing / if it's slow. Make sure `max_tokens` is less than `context_window`.  
```shell
interpreter --local --max_tokens 1000 --context_window 3000
```