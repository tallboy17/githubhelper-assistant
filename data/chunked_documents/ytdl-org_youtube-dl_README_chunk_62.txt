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
Header 3: Use convenience conversion and parsing functions
---
Wrap all extracted numeric data into safe functions from `youtube_dl/utils.py`: `int_or_none`, `float_or_none`. Use them for string to number conversions as well.  
Use `url_or_none` for safe URL processing.  
Use `traverse_obj` for safe metadata extraction from parsed JSON.  
Use `unified_strdate` for uniform `upload_date` or any `YYYYMMDD` meta field extraction, `unified_timestamp` for uniform `timestamp` extraction, `parse_filesize` for `filesize` extraction, `parse_count` for count meta fields extraction, `parse_resolution`, `parse_duration` for `duration` extraction, `parse_age_limit` for `age_limit` extraction.  
Explore `youtube_dl/utils.py` for more useful convenience functions.  
#### More examples  
##### Safely extract optional description from parsed JSON  
When processing complex JSON, as often returned by site API requests or stashed in web pages for "hydration", you can use the `traverse_obj()` utility function to handle multiple fallback values and to ensure the expected type of metadata items. The function's docstring defines how the function works: also review usage in the codebase for more examples.  
In this example, a text `description`, or `None`, is pulled from the `.result.video[0].summary` member of the parsed JSON `response`, if available.  
```python
description = traverse_obj(response, ('result', 'video', 0, 'summary', T(compat_str)))
```
`T(...)` is a shorthand for a set literal; if you hate people who still run Python 2.6, `T(type_or_transformation)` could be written as a set literal `{type_or_transformation}`.  
Some extractors use the older and less capable `try_get()` function in the same way.  
```python
description = try_get(response, lambda x: x['result']['video'][0]['summary'], compat_str)
```  
##### Safely extract more optional metadata  
In this example, various optional metadata values are extracted from the `.result.video[0]` member of the parsed JSON `response`, which is expected to be a JS object, parsed into a `dict`, with no crash if that isn't so, or if any of the target values are missing or invalid.  
```python
video = traverse_obj(response, ('result', 'video', 0, T(dict))) or {}
# formerly:
# video = try_get(response, lambda x: x['result']['video'][0], dict) or {}
description = video.get('summary')
duration = float_or_none(video.get('durationMs'), scale=1000)
view_count = int_or_none(video.get('views'))
```  
#### Safely extract nested lists  
Suppose you've extracted JSON like this into a Python data structure named `media_json` using, say, the `_download_json()` or `_parse_json()` methods of `InfoExtractor`:
```json
{
"title": "Example video",
"comment": "try extracting this",
"media": [{
"type": "bad",
"size": 320,
"url": "
}, {
"type": "streaming",
"url": "
}, {
"type": "super",
"size": 1280,
"url": "
}],
"moreStuff": "more values",
...
}
```  
Then extractor code like this can collect the various fields of the JSON:
```python
...
from ..utils import (
determine_ext,
int_or_none,
T,
traverse_obj,
txt_or_none,
url_or_none,
)
...
...
info_dict = {}
# extract title and description if valid and not empty
info_dict.update(traverse_obj(media_json, {
'title': ('title', T(txt_or_none)),
'description': ('comment', T(txt_or_none)),
}))

# extract any recognisable media formats
fmts = []
# traverse into "media" list, extract `dict`s with desired keys
for fmt in traverse_obj(media_json, ('media', Ellipsis, {
'format_id': ('type', T(txt_or_none)),
'url': ('url', T(url_or_none)),
'width': ('size', T(int_or_none)), })):
# bad `fmt` values were `None` and removed
if 'url' not in fmt:
continue
fmt_url = fmt['url']  # known to be valid URL
ext = determine_ext(fmt_url)
if ext == 'm3u8':
fmts.extend(self._extract_m3u8_formats(fmt_url, video_id, 'mp4', fatal=False))
else:
fmt['ext'] = ext
fmts.append(fmt)

# sort, raise if no formats
self._sort_formats(fmts)

info_dict['formats'] = fmts
...
```
The extractor raises an exception rather than random crashes if the JSON structure changes so that no formats are found.