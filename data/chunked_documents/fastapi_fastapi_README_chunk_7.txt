---
repo: fastapi/fastapi
readme_filename: fastapi_fastapi_README.md
stars: 86699
forks: 7531
watchers: 86699
contributors_count: 459
license: MIT
Header 2: Example
Header 3: Create it
---
Create a file `main.py` with:  
```Python
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
return {"item_id": item_id, "q": q}
```  

Or use async def...  
If your code uses `async` / `await`, use `async def`:  
```Python hl_lines="9  14"
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
return {"item_id": item_id, "q": q}
```  
**Note**:  
If you don't know, check the _"In a hurry?"_ section about `async` and `await` in the docs.  
