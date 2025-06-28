---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: On Windows, how should I set up ffmpeg and youtube-dl? Where should I put the exe files?
---
If you put youtube-dl and ffmpeg in the same directory that you're running the command from, it will work, but that's rather cumbersome.  
To make a different directory work - either for ffmpeg, or for youtube-dl, or for both - simply create the directory (say, `C:\bin`, or `C:\Users\\bin`), put all the executables directly in there, and then set your PATH environment variable to include that directory.  
From then on, after restarting your shell, you will be able to access both youtube-dl and ffmpeg (and youtube-dl will be able to find ffmpeg) by simply typing `youtube-dl` or `ffmpeg`, no matter what directory you're in.