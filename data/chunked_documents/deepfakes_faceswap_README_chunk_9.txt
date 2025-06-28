---
repo: deepfakes/faceswap
readme_filename: deepfakes_faceswap_README.md
stars: 54171
forks: 13423
watchers: 54171
contributors_count: 81
license: GPL-3.0
Header 1: General notes:
---
- All of the scripts mentioned have `-h`/`--help` options with arguments that they will accept. You're smart, you can figure out how this works, right?!  
NB: there is a conversion tool for video. This can be accessed by running `python tools.py effmpeg -h`. Alternatively, you can use ffmpeg to convert video into photos, process images, and convert images back to the video.  
**Some tips:**  
Reusing existing models will train much faster than starting from nothing.
If there is not enough training data, start with someone who looks similar, then switch the data.