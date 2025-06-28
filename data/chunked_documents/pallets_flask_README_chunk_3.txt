---
repo: pallets/flask
readme_filename: pallets_flask_README.md
stars: 69846
forks: 16481
watchers: 69846
contributors_count: 401
license: BSD-3-Clause
Header 1: Flask
Header 2: A Simple Example
---
```python
# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
return "Hello, World!"
```  
```
$ flask run
* Running on  (Press CTRL+C to quit)
```