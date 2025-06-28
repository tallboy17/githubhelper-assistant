---
repo: binary-husky/gpt_academic
readme_filename: binary-husky_gpt_academic_README.md
stars: 68842
forks: 8356
watchers: 68842
contributors_count: 101
license: GPL-3.0
Header 1: Installation
---
```mermaid
flowchart TD
A{"安装方法"} --> W1("I 🔑直接运行 (Windows, Linux or MacOS)")
W1 --> W11["1 Python pip包管理依赖"]
W1 --> W12["2 Anaconda包管理依赖（推荐⭐）"]

A --> W2["II 🐳使用Docker (Windows, Linux or MacOS)"]

W2 --> k1["1 部署项目全部能力的大镜像（推荐⭐）"]
W2 --> k2["2 仅在线模型（GPT, GLM4等）镜像"]
W2 --> k3["3 在线模型 + Latex的大镜像"]

A --> W4["IV 🚀其他部署方法"]
W4 --> C1["1 Windows/MacOS 一键安装运行脚本（推荐⭐）"]
W4 --> C2["2 Huggingface, Sealos远程部署"]
W4 --> C4["3 其他 ..."]
```