---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: DEVELOPER INSTRUCTIONS
---
Most users do not need to build youtube-dl and can download the builds or get them from their distribution.  
To run youtube-dl as a developer, you don't need to build anything either. Simply execute  
python -m youtube_dl  
To run the test, simply invoke your favorite test runner, or execute a test file directly; any of the following work:  
python -m unittest discover
python test/test_download.py
nosetests  
For Python versions 3.6 and later, you can use pynose to implement `nosetests`. The original nose has not been upgraded for 3.10 and later.  
See item 6 of new extractor tutorial for how to run extractor specific test cases.  
If you want to create a build of youtube-dl yourself, you'll need  
* python
* make (only GNU make is supported)
* pandoc
* zip
* nosetests