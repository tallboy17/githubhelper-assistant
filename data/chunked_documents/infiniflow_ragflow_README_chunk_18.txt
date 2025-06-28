---
repo: infiniflow/ragflow
readme_filename: infiniflow_ragflow_README.md
stars: 58402
forks: 5774
watchers: 58402
contributors_count: 284
license: Apache-2.0
Header 1: 
Header 2: 🔧 Build a Docker image including embedding models
---
This image is approximately 9 GB in size. As it includes embedding models, it relies on external LLM services only.  
```bash
git clone 
cd ragflow/
docker build --platform linux/amd64 -f Dockerfile -t infiniflow/ragflow:nightly .
```