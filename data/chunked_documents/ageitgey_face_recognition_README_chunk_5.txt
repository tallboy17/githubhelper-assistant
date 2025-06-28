---
repo: ageitgey/face_recognition
readme_filename: ageitgey_face_recognition_README.md
stars: 54971
forks: 13620
watchers: 54971
contributors_count: 49
license: MIT
Header 1: Face Recognition
Header 2: Installation
Header 3: Installation Options:
---
#### Installing on Mac or Linux  
First, make sure you have dlib already installed with Python bindings:  
* How to install dlib from source on macOS or Ubuntu  
Then, make sure you have cmake installed:  
```brew install cmake```  
Finally, install this module from pypi using `pip3` (or `pip2` for Python 2):  
```bash
pip3 install face_recognition
```  
Alternatively, you can try this library with Docker, see this section.  
If you are having trouble with installation, you can also try out a
pre-configured VM.  
#### Installing on an Nvidia Jetson Nano board  
* Jetson Nano installation instructions
* Please follow the instructions in the article carefully. There is current a bug in the CUDA libraries on the Jetson Nano that will cause this library to fail silently if you don't follow the instructions in the article to comment out a line in dlib and recompile it.  
#### Installing on Raspberry Pi 2+  
* Raspberry Pi 2+ installation instructions  
#### Installing on FreeBSD  
```bash
pkg install graphics/py-face_recognition
```  
#### Installing on Windows  
While Windows isn't officially supported, helpful users have posted instructions on how to install this library:  
* @masoudr's Windows 10 installation guide (dlib + face_recognition)  
#### Installing a pre-configured Virtual Machine image  
* Download the pre-configured VM image (for VMware Player or VirtualBox).