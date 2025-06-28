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
Header 3: Using an MCP Client
---
However, running a server on its own isn't very useful, and should instead be configured into an MCP client. For example, here's the Claude Desktop configuration to use the above server:  
```json
{
"mcpServers": {
"memory": {
"command": "npx",
"args": ["-y", "@modelcontextprotocol/server-memory"]
}
}
}
```  
Additional examples of using the Claude Desktop as an MCP client might look like:  
```json
{
"mcpServers": {
"filesystem": {
"command": "npx",
"args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/files"]
},
"git": {
"command": "uvx",
"args": ["mcp-server-git", "--repository", "path/to/git/repo"]
},
"github": {
"command": "npx",
"args": ["-y", "@modelcontextprotocol/server-github"],
"env": {
"GITHUB_PERSONAL_ACCESS_TOKEN": ""
}
},
"postgres": {
"command": "npx",
"args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://localhost/mydb"]
}
}
}
```