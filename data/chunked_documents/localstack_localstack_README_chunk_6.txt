---
repo: localstack/localstack
readme_filename: localstack_localstack_README.md
stars: 59419
forks: 4177
watchers: 59419
contributors_count: 426
license: NOASSERTION
Header 1: Overview
Header 2: Install
Header 3: PyPI (macOS, Linux, Windows)
---
LocalStack is developed using Python. To install the LocalStack CLI using `pip`, run the following command:  
```bash
python3 -m pip install localstack
```  
The `localstack-cli` installation enables you to run the Docker image containing the LocalStack runtime. To interact with the local AWS services, you need to install the `awslocal` CLI separately. For installation guidelines, refer to the `awslocal` documentation.  
> **Important**: Do not use `sudo` or run as `root` user. LocalStack must be installed and started entirely under a local non-root user. If you have problems with permissions in macOS High Sierra, install with `pip install --user localstack`