---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: How can I detect whether a given URL is supported by youtube-dl?
---
For one, have a look at the list of supported sites. Note that it can sometimes happen that the site changes its URL scheme (say, from  to  ) and youtube-dl reports an URL of a service in that list as unsupported. In that case, simply report a bug.  
It is *not* possible to detect whether a URL is supported or not. That's because youtube-dl contains a generic extractor which matches **all** URLs. You may be tempted to disable, exclude, or remove the generic extractor, but the generic extractor not only allows users to extract videos from lots of websites that embed a video from another service, but may also be used to extract video from a service that it's hosting itself. Therefore, we neither recommend nor support disabling, excluding, or removing the generic extractor.  
If you want to find out whether a given URL is supported, simply call youtube-dl with it. If you get no videos back, chances are the URL is either not referring to a video or unsupported. You can find out which by examining the output (if you run youtube-dl on the console) or catching an `UnsupportedError` exception if you run it from a Python program.