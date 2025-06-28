---
repo: nvbn/thefuck
readme_filename: nvbn_thefuck_README.md
stars: 92574
forks: 3717
watchers: 92574
contributors_count: 166
license: MIT
Header 1: The Fuck [![Version][version-badge]][version-link] [![Build Status][workflow-badge]][workflow-link] [![Coverage][coverage-badge]][coverage-link] [![MIT License][license-badge]](LICENSE.md)
Header 2: Experimental instant mode
---
The default behavior of *The Fuck* requires time to re-run previous commands.
When in instant mode, *The Fuck* saves time by logging output with script),
then reading the log.  
[![gif with instant mode][instant-mode-gif-link]][instant-mode-gif-link]  
Currently, instant mode only supports Python 3 with bash or zsh. zsh's autocorrect function also needs to be disabled in order for thefuck to work properly.  
To enable instant mode, add `--enable-experimental-instant-mode`
to the alias initialization in `.bashrc`, `.bash_profile` or `.zshrc`.  
For example:  
```bash
eval $(thefuck --alias --enable-experimental-instant-mode)
```  
##### Back to Contents