---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: INSTALLATION
Header 2: DEPENDENCIES
Header 3: Strongly recommended
---
* **ffmpeg** and **ffprobe** - Required for merging separate video and audio files, as well as for various post-processing tasks. License depends on the build  
There are bugs in ffmpeg that cause various issues when used alongside yt-dlp. Since ffmpeg is such an important dependency, we provide custom builds with patches for some of these issues at yt-dlp/FFmpeg-Builds. See the readme for details on the specific issues solved by these builds  
**Important**: What you need is ffmpeg *binary*, **NOT** the Python package of the same name