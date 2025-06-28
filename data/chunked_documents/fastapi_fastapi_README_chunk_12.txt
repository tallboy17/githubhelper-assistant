---
repo: fastapi/fastapi
readme_filename: fastapi_fastapi_README.md
stars: 86699
forks: 7531
watchers: 86699
contributors_count: 459
license: MIT
Header 2: Example upgrade
---
Now modify the file `main.py` to receive a body from a `PUT` request.  
Declare the body using standard Python types, thanks to Pydantic.  
```Python hl_lines="4  9-12  25-27"
from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
name: str
price: float
is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
return {"item_name": item.name, "item_id": item_id}
```  
The `fastapi dev` server should reload automatically.