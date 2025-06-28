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
Header 3: Collapse fallbacks
---
Multiple fallback values can quickly become unwieldy. Collapse multiple fallback values into a single expression via a list of patterns.  
#### Example  
Good:  
```python
description = self._html_search_meta(
['og:description', 'description', 'twitter:description'],
webpage, 'description', default=None)
```  
Unwieldy:  
```python
description = (
self._og_search_description(webpage, default=None)
or self._html_search_meta('description', webpage, default=None)
or self._html_search_meta('twitter:description', webpage, default=None))
```  
Methods supporting list of patterns are: `_search_regex`, `_html_search_regex`, `_og_search_property`, `_html_search_meta`.