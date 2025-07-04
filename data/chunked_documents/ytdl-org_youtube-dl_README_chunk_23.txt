---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: How do I update youtube-dl?
---
If you've followed our manual installation instructions, you can simply run `youtube-dl -U` (or, on Linux, `sudo youtube-dl -U`).  
If you have used pip, a simple `sudo pip install -U youtube-dl` is sufficient to update.  
If you have installed youtube-dl using a package manager like *apt-get* or *yum*, use the standard system update mechanism to update. Note that distribution packages are often outdated. As a rule of thumb, youtube-dl releases at least once a month, and often weekly or even daily. Simply go to  to find out the current version. Unfortunately, there is nothing we youtube-dl developers can do if your distribution serves a really outdated version. You can (and should) complain to your distribution in their bugtracker or support forum.  
As a last resort, you can also uninstall the version installed by your package manager and follow our manual installation instructions. For that, remove the distribution's package, with a line like  
sudo apt-get remove -y youtube-dl  
Afterwards, simply follow our manual installation instructions:  
```
sudo wget  -O /usr/local/bin/youtube-dl
sudo chmod a+rx /usr/local/bin/youtube-dl
hash -r
```  
Again, from then on you'll be able to update with `sudo youtube-dl -U`.