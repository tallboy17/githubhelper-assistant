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
Header 3: Regular expressions
---
#### Don't capture groups you don't use  
Capturing group must be an indication that it's used somewhere in the code. Any group that is not used must be non capturing.  
##### Example  
Don't capture id attribute name here since you can't use it for anything anyway.  
Correct:  
```python
r'(?:id|ID)=(?P\d+)'
```  
Incorrect:
```python
r'(id|ID)=(?P\d+)'
```  
#### Make regular expressions relaxed and flexible  
When using regular expressions try to write them fuzzy, relaxed and flexible, skipping insignificant parts that are more likely to change, allowing both single and double quotes for quoted values and so on.  
##### Example  
Say you need to extract `title` from the following HTML code:  
```html
some fancy title
```  
The code for that task should look similar to:  
```python
title = self._search_regex(
r']+class="title"[^>]*>([^]+class=(["\'])title\1[^>]*>(?P[^(.*?)',
webpage, 'title', group='title')
```