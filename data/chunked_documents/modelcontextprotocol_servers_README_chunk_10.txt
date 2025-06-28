---
repo: modelcontextprotocol/servers
readme_filename: modelcontextprotocol_servers_README.md
stars: 56456
forks: 6503
watchers: 56456
contributors_count: 423
license: MIT
Header 1: Model Context Protocol servers
Header 2: 🚀 Getting Started
Header 3: Using MCP Servers in this Repository
---
Typescript-based servers in this repository can be used directly with `npx`.  
For example, this will start the Memory server:
```sh
npx -y @modelcontextprotocol/server-memory
```  
Python-based servers in this repository can be used directly with `uvx` or `pip`. `uvx` is recommended for ease of use and setup.  
For example, this will start the Git server:
```sh
# With uvx
uvx mcp-server-git

# With pip
pip install mcp-server-git
python -m mcp_server_git
```  
Follow these instructions to install `uv` / `uvx` and these to install `pip`.