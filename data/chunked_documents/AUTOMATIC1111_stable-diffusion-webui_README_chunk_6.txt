---
repo: AUTOMATIC1111/stable-diffusion-webui
readme_filename: AUTOMATIC1111_stable-diffusion-webui_README.md
stars: 153963
forks: 28611
watchers: 153963
contributors_count: 429
license: AGPL-3.0
Header 1: Stable Diffusion web UI
Header 2: Installation and Running
Header 3: Automatic Installation on Linux
---
1. Install the dependencies:
```bash
# Debian-based:
sudo apt install wget git python3 python3-venv libgl1 libglib2.0-0
# Red Hat-based:
sudo dnf install wget git python3 gperftools-libs libglvnd-glx
# openSUSE-based:
sudo zypper install wget git python3 libtcmalloc4 libglvnd
# Arch-based:
sudo pacman -S wget git python3
```
If your system is very new, you need to install python3.11 or python3.10:
```bash
# Ubuntu 24.04
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.11

# Manjaro/Arch
sudo pacman -S yay
yay -S python311 # do not confuse with python3.11 package

# Only for 3.11
# Then set up env variable in launch script
export python_cmd="python3.11"
# or in webui-user.sh
python_cmd="python3.11"
```
2. Navigate to the directory you would like the webui to be installed and execute the following command:
```bash
wget -q 
```
Or just clone the repo wherever you want:
```bash
git clone 
```  
3. Run `webui.sh`.
4. Check `webui-user.sh` for options.