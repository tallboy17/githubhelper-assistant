---
repo: infiniflow/ragflow
readme_filename: infiniflow_ragflow_README.md
stars: 58402
forks: 5774
watchers: 58402
contributors_count: 284
license: Apache-2.0
Header 1: 
Header 2: 🔧 Build a Docker image without embedding models
---
This image is approximately 2 GB in size and relies on external LLM and embedding services.  
```bash
git clone 
cd ragflow/
docker build --platform linux/amd64 --build-arg LIGHTEN=1 -f Dockerfile -t infiniflow/ragflow:nightly-slim .
```