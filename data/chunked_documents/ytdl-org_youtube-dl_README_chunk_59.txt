---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: DEVELOPER INSTRUCTIONS
Header 2: youtube-dl coding conventions
Header 3: Inline values
---
Extracting variables is acceptable for reducing code duplication and improving readability of complex expressions. However, you should avoid extracting variables used only once and moving them to opposite parts of the extractor file, which makes reading the linear flow difficult.  
#### Example  
Correct:  
```python
title = self._html_search_regex(r'([^', webpage, 'title')
```  
Incorrect:  
```python
TITLE_RE = r'([^'
# ...some lines of code...
title = self._html_search_regex(TITLE_RE, webpage, 'title')
```