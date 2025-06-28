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
Header 3: Command-Line
---
```bash
markitdown path-to-file.pdf > document.md
```  
Or use `-o` to specify the output file:  
```bash
markitdown path-to-file.pdf -o document.md
```  
You can also pipe content:  
```bash
cat path-to-file.pdf | markitdown
```