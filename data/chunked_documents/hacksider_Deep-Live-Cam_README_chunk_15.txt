---
repo: hacksider/Deep-Live-Cam
readme_filename: hacksider_Deep-Live-Cam_README.md
stars: 71366
forks: 10204
watchers: 71366
contributors_count: 50
license: AGPL-3.0
Header 2: Command Line Arguments (Unmaintained)
---
```
options:
-h, --help                                               show this help message and exit
-s SOURCE_PATH, --source SOURCE_PATH                     select a source image
-t TARGET_PATH, --target TARGET_PATH                     select a target image or video
-o OUTPUT_PATH, --output OUTPUT_PATH                     select output file or directory
--frame-processor FRAME_PROCESSOR [FRAME_PROCESSOR ...]  frame processors (choices: face_swapper, face_enhancer, ...)
--keep-fps                                               keep original fps
--keep-audio                                             keep original audio
--keep-frames                                            keep temporary frames
--many-faces                                             process every face
--map-faces                                              map source target faces
--mouth-mask                                             mask the mouth region
--video-encoder {libx264,libx265,libvpx-vp9}             adjust output video encoder
--video-quality [0-51]                                   adjust output video quality
--live-mirror                                            the live camera display as you see it in the front-facing camera frame
--live-resizable                                         the live camera frame is resizable
--max-memory MAX_MEMORY                                  maximum amount of RAM in GB
--execution-provider {cpu} [{cpu} ...]                   available execution provider (choices: cpu, ...)
--execution-threads EXECUTION_THREADS                    number of execution threads
-v, --version                                            show program's version number and exit
```  
Looking for a CLI mode? Using the -s/--source argument will make the run program in cli mode.