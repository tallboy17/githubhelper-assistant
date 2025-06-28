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
Header 3: Deprecated
---
* **avconv** and **avprobe** - Now **deprecated** alternative to ffmpeg. License depends on the build
* **sponskrub** - For using the now **deprecated** sponskrub options. Licensed under GPLv3+
* **rtmpdump** - For downloading `rtmp` streams. ffmpeg can be used instead with `--downloader ffmpeg`. Licensed under GPLv2+
* **mplayer** or **mpv** - For downloading `rstp`/`mms` streams. ffmpeg can be used instead with `--downloader ffmpeg`. Licensed under GPLv2+  
To use or redistribute the dependencies, you must agree to their respective licensing terms.  
The standalone release binaries are built with the Python interpreter and the packages marked with **\*** included.  
If you do not have the necessary dependencies for a task you are attempting, yt-dlp will warn you. All the currently available dependencies are visible at the top of the `--verbose` output