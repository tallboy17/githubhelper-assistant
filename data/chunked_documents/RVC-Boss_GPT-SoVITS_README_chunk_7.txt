---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: Installation
Header 3: macOS
---
**Note: The models trained with GPUs on Macs result in significantly lower quality compared to those trained on other devices, so we are temporarily using CPUs instead.**  
Install the program by running the following commands:  
```bash
conda create -n GPTSoVits python=3.10
conda activate GPTSoVits
bash install.sh --device  --source  [--download-uvr5]
```