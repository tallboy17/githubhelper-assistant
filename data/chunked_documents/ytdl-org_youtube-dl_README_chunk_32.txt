---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: I extracted a video URL with `-g`, but it does not play on another machine / in my web browser.
---
It depends a lot on the service. In many cases, requests for the video (to download/play it) must come from the same IP address and with the same cookies and/or HTTP headers. Use the `--cookies` option to write the required cookies into a file, and advise your downloader to read cookies from that file. Some sites also require a common user agent to be used, use `--dump-user-agent` to see the one in use by youtube-dl. You can also get necessary cookies and HTTP headers from JSON output obtained with `--dump-json`.  
It may be beneficial to use IPv6; in some cases, the restrictions are only applied to IPv4. Some services (sometimes only for a subset of videos) do not restrict the video URL by IP address, cookie, or user-agent, but these are the exception rather than the rule.  
Please bear in mind that some URL protocols are **not** supported by browsers out of the box, including RTMP. If you are using `-g`, your own downloader must support these as well.  
If you want to play the video on a machine that is not running youtube-dl, you can relay the video content from the machine that runs youtube-dl. You can use `-o -` to let youtube-dl stream a video to stdout, or simply allow the player to download the files written by youtube-dl in turn.