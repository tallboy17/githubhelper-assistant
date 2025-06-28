---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: How do I stream directly to media player?
---
You will first need to tell youtube-dl to stream media to stdout with `-o -`, and also tell your media player to read from stdin (it must be capable of this for streaming) and then pipe former to latter. For example, streaming to vlc can be achieved with:  
youtube-dl -o - " | vlc -