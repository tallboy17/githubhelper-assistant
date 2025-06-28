---
repo: nvbn/thefuck
readme_filename: nvbn_thefuck_README.md
stars: 92574
forks: 3717
watchers: 92574
contributors_count: 166
license: MIT
Header 1: The Fuck [![Version][version-badge]][version-link] [![Build Status][workflow-badge]][workflow-link] [![Coverage][coverage-badge]][coverage-link] [![MIT License][license-badge]](LICENSE.md)
Header 2: Installation
---
On macOS or Linux, you can install *The Fuck* via [Homebrew][homebrew]:  
```bash
brew install thefuck
```  
On Ubuntu / Mint, install *The Fuck* with the following commands:
```bash
sudo apt update
sudo apt install python3-dev python3-pip python3-setuptools
pip3 install thefuck --user
```  
On FreeBSD, install *The Fuck* with the following commands:
```bash
pkg install thefuck
```  
On ChromeOS, install *The Fuck* using chromebrew with the following command:
```bash
crew install thefuck
```  
On Arch based systems, install *The Fuck* with the following command:
```
sudo pacman -S thefuck
```  
On other systems, install *The Fuck*  by using `pip`:  
```bash
pip install thefuck
```  
Alternatively, you may use an OS package manager (OS X, Ubuntu, Arch).  
#
It is recommended that you place this command in your `.bash_profile`,
`.bashrc`, `.zshrc` or other startup script:  
```bash
eval $(thefuck --alias)
# You can use whatever you want as an alias, like for Mondays:
eval $(thefuck --alias FUCK)
```  
Or in your shell config (Bash, Zsh, Fish, Powershell, tcsh).  
Changes are only available in a new shell session. To make changes immediately
available, run `source ~/.bashrc` (or your shell config file like `.zshrc`).  
To run fixed commands without confirmation, use the `--yeah` option (or just `-y` for short, or `--hard` if you're especially frustrated):  
```bash
fuck --yeah
```  
To fix commands recursively until succeeding, use the `-r` option:  
```bash
fuck -r
```  
##### Back to Contents