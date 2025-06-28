---
repo: 3b1b/manim
readme_filename: 3b1b_manim_README.md
stars: 78528
forks: 6766
watchers: 78528
contributors_count: 164
license: MIT
Header 2: Using manim
---
Try running the following:
```sh
manimgl example_scenes.py OpeningManimExample
```
This should pop up a window playing a simple scene.  
Look through the example scenes to see examples of the library's syntax, animation types and object types. In the 3b1b/videos repo, you can see all the code for 3blue1brown videos, though code from older videos may not be compatible with the most recent version of manim. The readme of that repo also outlines some details for how to set up a more interactive workflow, as shown in this manim demo video for example.  
When running in the CLI, some useful flags include:
* `-w` to write the scene to a file
* `-o` to write the scene to a file and open the result
* `-s` to skip to the end and just show the final frame.
* `-so` will save the final frame to an image and show it
* `-n ` to skip ahead to the `n`'th animation of a scene.
* `-f` to make the playback window fullscreen  
Take a look at custom_config.yml for further configuration.  To add your customization, you can either edit this file, or add another file by the same name "custom_config.yml" to whatever directory you are running manim from.  For example this is the one for 3blue1brown videos.  There you can specify where videos should be output to, where manim should look for image files and sounds you want to read in, and other defaults regarding style and video quality.