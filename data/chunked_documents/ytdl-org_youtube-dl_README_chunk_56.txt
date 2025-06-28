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
Header 3: Provide fallbacks
---
When extracting metadata try to do so from multiple sources. For example if `title` is present in several places, try extracting from at least some of them. This makes it more future-proof in case some of the sources become unavailable.  
#### Example  
Say `meta` from the previous example has a `title` and you are about to extract it. Since `title` is a mandatory meta field you should end up with something like:  
```python
title = meta['title']
```  
If `title` disappears from `meta` in future due to some changes on the hoster's side the extraction would fail since `title` is mandatory. That's expected.  
Assume that you have some another source you can extract `title` from, for example `og:title` HTML meta of a `webpage`. In this case you can provide a fallback scenario:  
```python
title = meta.get('title') or self._og_search_title(webpage)
```  
This code will try to extract from `meta` first and if it fails it will try extracting `og:title` from a `webpage`.