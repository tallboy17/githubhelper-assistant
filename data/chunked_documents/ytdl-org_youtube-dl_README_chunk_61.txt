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
Header 3: Trailing parentheses
---
Always move trailing parentheses after the last argument.  
#### Example  
Correct:  
```python
lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
list)
```  
Incorrect:  
```python
lambda x: x['ResultSet']['Result'][0]['VideoUrlSet']['VideoUrl'],
list,
)
```