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
Header 3: Long lines policy
---
There is a soft limit to keep lines of code under 80 characters long. This means it should be respected if possible and if it does not make readability and code maintenance worse.  
For example, you should **never** split long string literals like URLs or some other often copied entities over multiple lines to fit this limit:  
Correct:  
```python
'
```  
Incorrect:  
```python
'
'PLMYEtVRpaqY00V9W81Cwmzp6N6vZqfUKD4'
```