---
repo: hacksider/Deep-Live-Cam
readme_filename: hacksider_Deep-Live-Cam_README.md
stars: 71366
forks: 10204
watchers: 71366
contributors_count: 50
license: AGPL-3.0
Header 2: Installation (Manual)
Header 3: Installation
---
This is more likely to work on your computer but will be slower as it utilizes the CPU.  
**1. Set up Your Platform**  
-   Python (3.10 recommended)
-   pip
-   git
-   ffmpeg - ```iex (irm ffmpeg.tc.ht)```
-   Visual Studio 2022 Runtimes (Windows)  
**2. Clone the Repository**  
```bash
git clone 
cd Deep-Live-Cam
```  
**3. Download the Models**  
1. GFPGANv1.4
2. inswapper\_128\_fp16.onnx  
Place these files in the "**models**" folder.  
**4. Install Dependencies**  
We highly recommend using a `venv` to avoid issues.  
For Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
For Linux:
```bash
# Ensure you use the installed Python 3.10
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```  
**For macOS:**  
Apple Silicon (M1/M2/M3) requires specific setup:  
```bash
# Install Python 3.10 (specific version is important)
brew install python@3.10

# Install tkinter package (required for the GUI)
brew install python-tk@3.10

# Create and activate virtual environment with Python 3.10
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```  
** In case something goes wrong and you need to reinstall the virtual environment **  
```bash
# Deactivate the virtual environment
rm -rf venv

# Reinstall the virtual environment
python -m venv venv
source venv/bin/activate

# install the dependencies again
pip install -r requirements.txt
```  
**Run:** If you don't have a GPU, you can run Deep-Live-Cam using `python run.py`. Note that initial execution will download models (~300MB).