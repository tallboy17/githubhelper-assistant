---
repo: infiniflow/ragflow
readme_filename: infiniflow_ragflow_README.md
stars: 58402
forks: 5774
watchers: 58402
contributors_count: 284
license: Apache-2.0
Header 1: 
Header 2: 🔧 Configurations
Header 3: Switch doc engine from Elasticsearch to Infinity
---
RAGFlow uses Elasticsearch by default for storing full text and vectors. To switch to Infinity, follow these steps:  
1. Stop all running containers:  
```bash
$ docker compose -f docker/docker-compose.yml down -v
```  
> [!WARNING]
> `-v` will delete the docker container volumes, and the existing data will be cleared.  
2. Set `DOC_ENGINE` in **docker/.env** to `infinity`.  
3. Start the containers:  
```bash
$ docker compose -f docker-compose.yml up -d
```  
> [!WARNING]
> Switching to Infinity on a Linux/arm64 machine is not yet officially supported.