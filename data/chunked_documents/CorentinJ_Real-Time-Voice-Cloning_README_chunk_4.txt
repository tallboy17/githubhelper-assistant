---
repo: CorentinJ/Real-Time-Voice-Cloning
readme_filename: CorentinJ_Real-Time-Voice-Cloning_README.md
stars: 54589
forks: 9018
watchers: 54589
contributors_count: 15
license: NOASSERTION
Header 1: Real-Time Voice Cloning
Header 2: Setup
Header 3: 1. Install Requirements
---
1. Both Windows and Linux are supported. A GPU is recommended for training and for inference speed, but is not mandatory.
2. Python 3.7 is recommended. Python 3.5 or greater should work, but you'll probably have to tweak the dependencies' versions. I recommend setting up a virtual environment using `venv`, but this is optional.
3. Install ffmpeg. This is necessary for reading audio files.
4. Install PyTorch. Pick the latest stable version, your operating system, your package manager (pip by default) and finally pick any of the proposed CUDA versions if you have a GPU, otherwise pick CPU. Run the given command.
5. Install the remaining requirements with `pip install -r requirements.txt`