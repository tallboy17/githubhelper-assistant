---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: OPTIONS
Header 2: Download Options:
---
-r, --limit-rate RATE                Maximum download rate in bytes per
second (e.g. 50K or 4.2M)
-R, --retries RETRIES                Number of retries (default is 10), or
"infinite".
--fragment-retries RETRIES           Number of retries for a fragment
(default is 10), or "infinite" (DASH,
hlsnative and ISM)
--skip-unavailable-fragments         Skip unavailable fragments (DASH,
hlsnative and ISM)
--abort-on-unavailable-fragment      Abort downloading when some fragment is
not available
--keep-fragments                     Keep downloaded fragments on disk after
downloading is finished; fragments are
erased by default
--buffer-size SIZE                   Size of download buffer (e.g. 1024 or
16K) (default is 1024)
--no-resize-buffer                   Do not automatically adjust the buffer
size. By default, the buffer size is
automatically resized from an initial
value of SIZE.
--http-chunk-size SIZE               Size of a chunk for chunk-based HTTP
downloading (e.g. 10485760 or 10M)
(default is disabled). May be useful
for bypassing bandwidth throttling
imposed by a webserver (experimental)
--playlist-reverse                   Download playlist videos in reverse
order
--playlist-random                    Download playlist videos in random
order
--xattr-set-filesize                 Set file xattribute ytdl.filesize with
expected file size
--hls-prefer-native                  Use the native HLS downloader instead
of ffmpeg
--hls-prefer-ffmpeg                  Use ffmpeg instead of the native HLS
downloader
--hls-use-mpegts                     Use the mpegts container for HLS
videos, allowing to play the video
while downloading (some players may not
be able to play it)
--external-downloader COMMAND        Use the specified external downloader.
Currently supports aria2c,avconv,axel,c
url,ffmpeg,httpie,wget
--external-downloader-args ARGS      Give these arguments to the external
downloader