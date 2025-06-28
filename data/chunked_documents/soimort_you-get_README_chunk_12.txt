---
repo: soimort/you-get
readme_filename: soimort_you-get_README.md
stars: 55790
forks: 9764
watchers: 55790
contributors_count: 226
license: NOASSERTION
Header 1: You-Get
Header 2: Getting Started
Header 3: Download a video
---
When you get a video of interest, you might want to use the `--info`/`-i` option to see all available quality and formats:  
```
$ you-get -i '
site:                YouTube
title:               Me at the zoo
streams:             # Available quality and codecs
[ DASH ] ____________________________________
- itag:          242
container:     webm
quality:       320x240
size:          0.6 MiB (618358 bytes)
# download-with: you-get --itag=242 [URL]

- itag:          395
container:     mp4
quality:       320x240
size:          0.5 MiB (550743 bytes)
# download-with: you-get --itag=395 [URL]

- itag:          133
container:     mp4
quality:       320x240
size:          0.5 MiB (498558 bytes)
# download-with: you-get --itag=133 [URL]

- itag:          278
container:     webm
quality:       192x144
size:          0.4 MiB (392857 bytes)
# download-with: you-get --itag=278 [URL]

- itag:          160
container:     mp4
quality:       192x144
size:          0.4 MiB (370882 bytes)
# download-with: you-get --itag=160 [URL]

- itag:          394
container:     mp4
quality:       192x144
size:          0.4 MiB (367261 bytes)
# download-with: you-get --itag=394 [URL]

[ DEFAULT ] _________________________________
- itag:          43
container:     webm
quality:       medium
size:          0.5 MiB (568748 bytes)
# download-with: you-get --itag=43 [URL]

- itag:          18
container:     mp4
quality:       small
# download-with: you-get --itag=18 [URL]

- itag:          36
container:     3gp
quality:       small
# download-with: you-get --itag=36 [URL]

- itag:          17
container:     3gp
quality:       small
# download-with: you-get --itag=17 [URL]
```  
By default, the one on the top is the one you will get. If that looks cool to you, download it:  
```
$ you-get '
site:                YouTube
title:               Me at the zoo
stream:
- itag:          242
container:     webm
quality:       320x240
size:          0.6 MiB (618358 bytes)
# download-with: you-get --itag=242 [URL]

Downloading Me at the zoo.webm ...
100% (  0.6/  0.6MB) ├██████████████████████████████████████████████████████████████████████████████┤[2/2]    2 MB/s
Merging video parts... Merged into Me at the zoo.webm

Saving Me at the zoo.en.srt ... Done.
```  
(If a YouTube video has any closed captions, they will be downloaded together with the video file, in SubRip subtitle format.)  
Or, if you prefer another format (mp4), just use whatever the option `you-get` shows to you:  
```
$ you-get --itag=18 '
```  
**Note:**  
* At this point, format selection has not been generally implemented for most of our supported sites; in that case, the default format to download is the one with the highest quality.
* `ffmpeg` is a required dependency, for downloading and joining videos streamed in multiple parts (e.g. on some sites like Youku), and for YouTube videos of 1080p or high resolution.
* If you don't want `you-get` to join video parts after downloading them, use the `--no-merge`/`-n` option.