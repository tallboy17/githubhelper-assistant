---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Sample FastAPI Server
---
The generator update enables Open Interpreter to be controlled via HTTP REST endpoints:  
```python
# server.py

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from interpreter import interpreter

app = FastAPI()

@app.get("/chat")
def chat_endpoint(message: str):
def event_stream():
for result in interpreter.chat(message, stream=True):
yield f"data: {result}\n\n"

return StreamingResponse(event_stream(), media_type="text/event-stream")

@app.get("/history")
def history_endpoint():
return interpreter.messages
```  
```shell
pip install fastapi uvicorn
uvicorn server:app --reload
```  
You can also start a server identical to the one above by simply running `interpreter.server()`.