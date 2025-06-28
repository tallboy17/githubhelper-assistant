---
repo: binary-husky/gpt_academic
readme_filename: binary-husky_gpt_academic_README.md
stars: 68842
forks: 8356
watchers: 68842
contributors_count: 101
license: GPL-3.0
Header 1: Installation
Header 3: 安装方法II：使用Docker
---
0. 部署项目的全部能力（这个是包含cuda和latex的大型镜像。但如果您网速慢、硬盘小，则不推荐该方法部署完整项目）
![fullcapacity](  
``` sh
# 修改docker-compose.yml，保留方案0并删除其他方案。然后运行：
docker-compose up
```  
1. 仅ChatGPT + GLM4 + 文心一言+spark等在线模型（推荐大多数人选择）
![basic](
![basiclatex](
![basicaudio](  
``` sh
# 修改docker-compose.yml，保留方案1并删除其他方案。然后运行：
docker-compose up
```  
P.S. 如果需要依赖Latex的插件功能，请见Wiki。另外，您也可以直接使用方案4或者方案0获取Latex功能。  
2. ChatGPT + GLM3 + MOSS + LLAMA2 + 通义千问（需要熟悉Nvidia Docker运行时）
![chatglm](  
``` sh
# 修改docker-compose.yml，保留方案2并删除其他方案。然后运行：
docker-compose up
```