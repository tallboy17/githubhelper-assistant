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
Header 3: Mandatory and optional metafields
---
For extraction to work youtube-dl relies on metadata your extractor extracts and provides to youtube-dl expressed by an information dictionary or simply *info dict*. Only the following meta fields in the *info dict* are considered mandatory for a successful extraction process by youtube-dl:  
- `id` (media identifier)
- `title` (media title)
- `url` (media download URL) or `formats`  
In fact only the last option is technically mandatory (i.e. if you can't figure out the download location of the media the extraction does not make any sense). But by convention youtube-dl also treats `id` and `title` as mandatory. Thus the aforementioned metafields are the critical data that the extraction does not make any sense without and if any of them fail to be extracted then the extractor is considered completely broken.  
Any field apart from the aforementioned ones are considered **optional**. That means that extraction should be **tolerant** to situations when sources for these fields can potentially be unavailable (even if they are always available at the moment) and **future-proof** in order not to break the extraction of general purpose mandatory fields.  
#### Example  
Say you have some source dictionary `meta` that you've fetched as JSON with HTTP request and it has a key `summary`:  
```python
meta = self._download_json(url, video_id)
```  
Assume at this point `meta`'s layout is:  
```python
{
...
"summary": "some fancy summary text",
...
}
```  
Assume you want to extract `summary` and put it into the resulting info dict as `description`. Since `description` is an optional meta field you should be ready that this key may be missing from the `meta` dict, so that you should extract it like:  
```python
description = meta.get('summary')  # correct
```  
and not like:  
```python
description = meta['summary']  # incorrect
```  
The latter will break extraction process with `KeyError` if `summary` disappears from `meta` at some later time but with the former approach extraction will just go ahead with `description` set to `None` which is perfectly fine (remember `None` is equivalent to the absence of data).  
Similarly, you should pass `fatal=False` when extracting optional data from a webpage with `_search_regex`, `_html_search_regex` or similar methods, for instance:  
```python
description = self._search_regex(
r']+id="title"[^>]*>([^`, for example:  
```python
description = self._search_regex(
r']+id="title"[^>]*>([^<]+)<',
webpage, 'description', default=None)
```  
On failure this code will silently continue the extraction with `description` set to `None`. That is useful for metafields that may or may not be present.