---
repo: infiniflow/ragflow
readme_filename: infiniflow_ragflow_README.md
stars: 58402
forks: 5774
watchers: 58402
contributors_count: 284
license: Apache-2.0
Header 1: 
Header 2: 🔨 Launch service from source for development
---
1. Install uv, or skip this step if it is already installed:  
```bash
pipx install uv pre-commit
```  
2. Clone the source code and install Python dependencies:  
```bash
git clone 
cd ragflow/
uv sync --python 3.10 --all-extras # install RAGFlow dependent python modules
uv run download_deps.py
pre-commit install
```  
3. Launch the dependent services (MinIO, Elasticsearch, Redis, and MySQL) using Docker Compose:  
```bash
docker compose -f docker/docker-compose-base.yml up -d
```  
Add the following line to `/etc/hosts` to resolve all hosts specified in **docker/.env** to `127.0.0.1`:  
```
127.0.0.1       es01 infinity mysql minio redis sandbox-executor-manager
```  
4. If you cannot access HuggingFace, set the `HF_ENDPOINT` environment variable to use a mirror site:  
```bash
export HF_ENDPOINT=
```  
5. If your operating system does not have jemalloc, please install it as follows:  
```bash
# ubuntu
sudo apt-get install libjemalloc-dev
# centos
sudo yum install jemalloc
```  
6. Launch backend service:  
```bash
source .venv/bin/activate
export PYTHONPATH=$(pwd)
bash docker/launch_backend_service.sh
```  
7. Install frontend dependencies:  
```bash
cd web
npm install
```  
8. Launch frontend service:  
```bash
npm run dev
```  
_The following output confirms a successful launch of the system:_  
![](  
9. Stop RAGFlow front-end and back-end service after development is complete:  
```bash
pkill -f "ragflow_server.py|task_executor.py"
```