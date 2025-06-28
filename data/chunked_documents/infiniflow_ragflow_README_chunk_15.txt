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
---
When it comes to system configurations, you will need to manage the following files:  
- .env: Keeps the fundamental setups for the system, such as `SVR_HTTP_PORT`, `MYSQL_PASSWORD`, and
`MINIO_PASSWORD`.
- service_conf.yaml.template: Configures the back-end services. The environment variables in this file will be automatically populated when the Docker container starts. Any environment variables set within the Docker container will be available for use, allowing you to customize service behavior based on the deployment environment.
- docker-compose.yml: The system relies on docker-compose.yml to start up.  
> The ./docker/README file provides a detailed description of the environment settings and service
> configurations which can be used as `${ENV_VARS}` in the service_conf.yaml.template file.  
To update the default HTTP serving port (80), go to docker-compose.yml and change `80:80`
to `:80`.  
Updates to the above configurations require a reboot of all containers to take effect:  
> ```bash
> $ docker compose -f docker-compose.yml up -d
> ```