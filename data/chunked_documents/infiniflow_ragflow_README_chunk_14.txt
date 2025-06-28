---
repo: infiniflow/ragflow
readme_filename: infiniflow_ragflow_README.md
stars: 58402
forks: 5774
watchers: 58402
contributors_count: 284
license: Apache-2.0
Header 1: 
Header 2: 🎬 Get Started
Header 3: 🚀 Start up the server
---
1. Ensure `vm.max_map_count` >= 262144:  
> To check the value of `vm.max_map_count`:
>
> ```bash
> $ sysctl vm.max_map_count
> ```
>
> Reset `vm.max_map_count` to a value at least 262144 if it is not.
>
> ```bash
> # In this case, we set it to 262144:
> $ sudo sysctl -w vm.max_map_count=262144
> ```
>
> This change will be reset after a system reboot. To ensure your change remains permanent, add or update the
> `vm.max_map_count` value in **/etc/sysctl.conf** accordingly:
>
> ```bash
> vm.max_map_count=262144
> ```  
2. Clone the repo:  
```bash
$ git clone 
```  
3. Start up the server using the pre-built Docker images:  
> [!CAUTION]
> All Docker images are built for x86 platforms. We don't currently offer Docker images for ARM64.
> If you are on an ARM64 platform, follow this guide to build a Docker image compatible with your system.  
> The command below downloads the `v0.19.1-slim` edition of the RAGFlow Docker image. See the following table for descriptions of different RAGFlow editions. To download a RAGFlow edition different from `v0.19.1-slim`, update the `RAGFLOW_IMAGE` variable accordingly in **docker/.env** before using `docker compose` to start the server. For example: set `RAGFLOW_IMAGE=infiniflow/ragflow:v0.19.1` for the full edition `v0.19.1`.  
```bash
$ cd ragflow/docker
# Use CPU for embedding and DeepDoc tasks:
$ docker compose -f docker-compose.yml up -d

# To use GPU to accelerate embedding and DeepDoc tasks:
# docker compose -f docker-compose-gpu.yml up -d
```  
| RAGFlow image tag | Image size (GB) | Has embedding models? | Stable?                  |
|-------------------|-----------------|-----------------------|--------------------------|
| v0.19.1           | &approx;9       | :heavy_check_mark:    | Stable release           |
| v0.19.1-slim      | &approx;2       | ❌                   | Stable release            |
| nightly           | &approx;9       | :heavy_check_mark:    | _Unstable_ nightly build |
| nightly-slim      | &approx;2       | ❌                   | _Unstable_ nightly build  |  
4. Check the server status after having the server up and running:  
```bash
$ docker logs -f ragflow-server
```  
_The following output confirms a successful launch of the system:_  
```bash

____   ___    ______ ______ __
/ __ \ /   |  / ____// ____// /____  _      __
/ /_/ // /| | / / __ / /_   / // __ \| | /| / /
/ _, _// ___ |/ /_/ // __/  / // /_/ /| |/ |/ /
/_/ |_|/_/  |_|\____//_/    /_/ \____/ |__/|__/

* Running on all addresses (0.0.0.0)
```  
> If you skip this confirmation step and directly log in to RAGFlow, your browser may prompt a `network anormal`
> error because, at that moment, your RAGFlow may not be fully initialized.  
5. In your web browser, enter the IP address of your server and log in to RAGFlow.
> With the default settings, you only need to enter ` (**sans** port number) as the default
> HTTP serving port `80` can be omitted when using the default configurations.
6. In service_conf.yaml.template, select the desired LLM factory in `user_default_llm` and update
the `API_KEY` field with the corresponding API key.  
> See llm_api_key_setup for more information.  
_The show is on!_