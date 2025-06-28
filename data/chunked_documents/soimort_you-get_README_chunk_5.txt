---
repo: soimort/you-get
readme_filename: soimort_you-get_README.md
stars: 55790
forks: 9764
watchers: 55790
contributors_count: 226
license: NOASSERTION
Header 1: You-Get
Header 2: Installation
Header 3: Option 3: Download from GitHub
---
You may either download the stable (identical with the latest release on PyPI) or the develop (more hotfixes, unstable features) branch of `you-get`. Unzip it, and put the directory containing the `you-get` script into your `PATH`.  
Alternatively, run  
```
$ cd path/to/you-get
$ [sudo] python -m pip install .
```  
Or  
```
$ cd path/to/you-get
$ python -m pip install . --user
```  
to install `you-get` to a permanent path. (And don't omit the dot `.` representing the current directory)  
You can also use the pipenv to install the `you-get` in the Python virtual environment.  
```
$ pipenv install -e .
$ pipenv run you-get --version
you-get: version 0.4.1555, a tiny downloader that scrapes the web.
```