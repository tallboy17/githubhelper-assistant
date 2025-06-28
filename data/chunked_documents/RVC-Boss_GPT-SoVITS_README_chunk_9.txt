---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: Installation
Header 3: Running GPT-SoVITS with Docker
---
#### Docker Image Selection  
Due to rapid development in the codebase and a slower Docker image release cycle, please:  
- Check Docker Hub for the latest available image tags
- Choose an appropriate image tag for your environment
- `Lite` means the Docker image **does not include** ASR models and UVR5 models. You can manually download the UVR5 models, while the program will automatically download the ASR models as needed
- The appropriate architecture image (amd64/arm64) will be automatically pulled during Docker Compose
- Docker Compose will mount **all files** in the current directory. Please switch to the project root directory and **pull the latest code** before using the Docker image
- Optionally, build the image locally using the provided Dockerfile for the most up-to-date changes  
#### Environment Variables  
- `is_half`: Controls whether half-precision (fp16) is enabled. Set to `true` if your GPU supports it to reduce memory usage.  
#### Shared Memory Configuration  
On Windows (Docker Desktop), the default shared memory size is small and may cause unexpected behavior. Increase `shm_size` (e.g., to `16g`) in your Docker Compose file based on your available system memory.  
#### Choosing a Service  
The `docker-compose.yaml` defines two services:  
- `GPT-SoVITS-CU126` & `GPT-SoVITS-CU128`: Full version with all features.
- `GPT-SoVITS-CU126-Lite` & `GPT-SoVITS-CU128-Lite`: Lightweight version with reduced dependencies and functionality.  
To run a specific service with Docker Compose, use:  
```bash
docker compose run --service-ports 
```  
#### Building the Docker Image Locally  
If you want to build the image yourself, use:  
```bash
bash docker_build.sh --cuda  [--lite]
```  
#### Accessing the Running Container (Bash Shell)  
Once the container is running in the background, you can access it using:  
```bash
docker exec -it  bash
```