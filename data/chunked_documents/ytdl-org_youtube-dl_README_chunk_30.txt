---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: Do I need any other programs?
---
youtube-dl works fine on its own on most sites. However, if you want to convert video/audio, you'll need avconv or ffmpeg. On some sites - most notably YouTube - videos can be retrieved in a higher quality format without sound. youtube-dl will detect whether avconv/ffmpeg is present and automatically pick the best option.  
Videos or video formats streamed via RTMP protocol can only be downloaded when rtmpdump is installed. Downloading MMS and RTSP videos requires either mplayer or mpv to be installed.