---
repo: nvbn/thefuck
readme_filename: nvbn_thefuck_README.md
stars: 92574
forks: 3717
watchers: 92574
contributors_count: 166
license: MIT
Header 1: The Fuck [![Version][version-badge]][version-link] [![Build Status][workflow-badge]][workflow-link] [![Coverage][coverage-badge]][coverage-link] [![MIT License][license-badge]](LICENSE.md)
Header 2: Third-party packages with rules
---
If you'd like to make a specific set of non-public rules, but would still like
to share them with others, create a package named `thefuck_contrib_*` with
the following structure:  
```
thefuck_contrib_foo
thefuck_contrib_foo
rules
__init__.py
*third-party rules*
__init__.py
*third-party-utils*
setup.py
```  
*The Fuck* will find rules located in the `rules` module.  
##### Back to Contents