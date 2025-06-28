---
repo: microsoft/markitdown
readme_filename: microsoft_markitdown_README.md
stars: 59580
forks: 3102
watchers: 59580
contributors_count: 64
license: MIT
Header 1: MarkItDown
Header 2: Usage
Header 3: Plugins
---
MarkItDown also supports 3rd-party plugins. Plugins are disabled by default. To list installed plugins:  
```bash
markitdown --list-plugins
```  
To enable plugins use:  
```bash
markitdown --use-plugins path-to-file.pdf
```  
To find available plugins, search GitHub for the hashtag `#markitdown-plugin`. To develop a plugin, see `packages/markitdown-sample-plugin`.