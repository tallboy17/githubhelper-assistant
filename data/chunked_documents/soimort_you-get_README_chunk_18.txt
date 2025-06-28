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
Header 3: Watch a video
---
Use the `--player`/`-p` option to feed the video into your media player of choice, e.g. `mpv` or `vlc`, instead of downloading it:  
```
$ you-get -p vlc '
```  
Or, if you prefer to watch the video in a browser, just without ads or comment section:  
```
$ you-get -p chromium '
```  
**Tips:**  
* It is possible to use the `-p` option to start another download manager, e.g., `you-get -p uget-gtk ' though they may not play together very well.