---
repo: fastapi/fastapi
readme_filename: fastapi_fastapi_README.md
stars: 86699
forks: 7531
watchers: 86699
contributors_count: 459
license: MIT
Header 2: Example
Header 3: Run it
---
Run the server with:  
  
```console
$ fastapi dev main.py

╭────────── FastAPI CLI - Development mode ───────────╮
│                                                     │
│  Serving at:                   │
│                                                     │
│  API docs:                │
│                                                     │
│  Running in development mode, for production use:   │
│                                                     │
│  fastapi run                                        │
│                                                     │
╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on  (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```  
  

About the command fastapi dev main.py...  
The command `fastapi dev` reads your `main.py` file, detects the **FastAPI** app in it, and starts a server using Uvicorn.  
By default, `fastapi dev` will start with auto-reload enabled for local development.  
You can read more about it in the FastAPI CLI docs.  
