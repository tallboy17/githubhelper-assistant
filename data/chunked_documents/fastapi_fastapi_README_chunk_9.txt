---
repo: fastapi/fastapi
readme_filename: fastapi_fastapi_README.md
stars: 86699
forks: 7531
watchers: 86699
contributors_count: 459
license: MIT
Header 2: Example
Header 3: Check it
---
Open your browser at   
You will see the JSON response as:  
```JSON
{"item_id": 5, "q": "somequery"}
```  
You already created an API that:  
* Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
* Both _paths_ take `GET` operations (also known as HTTP _methods_).
* The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
* The _path_ `/items/{item_id}` has an optional `str` _query parameter_ `q`.