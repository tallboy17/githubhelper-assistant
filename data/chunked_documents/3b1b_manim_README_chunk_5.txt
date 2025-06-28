---
repo: 3b1b/manim
readme_filename: 3b1b_manim_README.md
stars: 78528
forks: 6766
watchers: 78528
contributors_count: 164
license: MIT
Header 2: Installation
Header 3: Mac OSX
---
1. Install FFmpeg, LaTeX in terminal using homebrew.
```sh
brew install ffmpeg mactex
```  
2. If you are using an ARM-based processor, install Cairo.
```sh
arch -arm64 brew install pkg-config cairo
```  
3. Install latest version of manim using these command.
```sh
git clone 
cd manim
pip install -e .
manimgl example_scenes.py OpeningManimExample (make sure to add manimgl to path first.)
```