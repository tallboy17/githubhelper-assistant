---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: Installation
Header 3: Install Manually
---
#### Install Dependences  
```bash
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits

pip install -r extra-req.txt --no-deps
pip install -r requirements.txt
```  
#### Install FFmpeg  
##### Conda Users  
```bash
conda activate GPTSoVits
conda install ffmpeg
```  
##### Ubuntu/Debian Users  
```bash
sudo apt install ffmpeg
sudo apt install libsox-dev
```  
##### Windows Users  
Download and place ffmpeg.exe and ffprobe.exe in the GPT-SoVITS root  
Install Visual Studio 2017  
##### MacOS Users  
```bash
brew install ffmpeg
```