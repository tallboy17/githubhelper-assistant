---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: INSTALLATION
---
To install it right away for all UNIX users (Linux, macOS, etc.), type:  
sudo curl -L  -o /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl  
If you do not have curl, you can alternatively use a recent wget:  
sudo wget  -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl  
Windows users can download an .exe file and place it in any location on their PATH except for `%SYSTEMROOT%\System32` (e.g. **do not** put in `C:\Windows\System32`).  
You can also use pip:  
sudo -H pip install --upgrade youtube-dl  
This command will update youtube-dl if you have already installed it. See the pypi page for more information.  
macOS users can install youtube-dl with Homebrew:  
brew install youtube-dl  
Or with MacPorts:  
sudo port install youtube-dl  
Alternatively, refer to the developer instructions for how to check out and work with the git repository. For further options, including PGP signatures, see the youtube-dl Download Page.