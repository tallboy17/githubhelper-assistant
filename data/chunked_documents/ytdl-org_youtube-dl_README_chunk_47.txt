---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: Should I add `--hls-prefer-native` into my config?
---
When youtube-dl detects an HLS video, it can download it either with the built-in downloader or ffmpeg. Since many HLS streams are slightly invalid and ffmpeg/youtube-dl each handle some invalid cases better than the other, there is an option to switch the downloader if needed.  
When youtube-dl knows that one particular downloader works better for a given website, that downloader will be picked. Otherwise, youtube-dl will pick the best downloader for general compatibility, which at the moment happens to be ffmpeg. This choice may change in future versions of youtube-dl, with improvements of the built-in downloader and/or ffmpeg.  
In particular, the generic extractor (used when your website is not in the list of supported sites by youtube-dl cannot mandate one specific downloader.  
If you put either `--hls-prefer-native` or `--hls-prefer-ffmpeg` into your configuration, a different subset of videos will fail to download correctly. Instead, it is much better to file an issue or a pull request which details why the native or the ffmpeg HLS downloader is a better choice for your use case.