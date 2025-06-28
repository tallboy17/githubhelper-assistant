---
repo: fastapi/fastapi
readme_filename: fastapi_fastapi_README.md
stars: 86699
forks: 7531
watchers: 86699
contributors_count: 459
license: MIT
Header 2: Dependencies
Header 3: `standard` Dependencies
---
When you install FastAPI with `pip install "fastapi[standard]"` it comes with the `standard` group of optional dependencies:  
Used by Pydantic:  
* email-validator - for email validation.  
Used by Starlette:  
* httpx - Required if you want to use the `TestClient`.
* jinja2 - Required if you want to use the default template configuration.
* python-multipart - Required if you want to support form "parsing", with `request.form()`.  
Used by FastAPI / Starlette:  
* uvicorn - for the server that loads and serves your application. This includes `uvicorn[standard]`, which includes some dependencies (e.g. `uvloop`) needed for high performance serving.
* `fastapi-cli` - to provide the `fastapi` command.