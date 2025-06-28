---
repo: soimort/you-get
readme_filename: soimort_you-get_README.md
stars: 55790
forks: 9764
watchers: 55790
contributors_count: 226
license: NOASSERTION
Header 1: You-Get
---
![Build Status](
![PyPI version](
![Gitter](  
**NOTICE (30 May 2022): Support for Python 3.5, 3.6 and 3.7 will eventually be dropped. (see details here))**  
**NOTICE (8 Mar 2019): Read this if you are looking for the conventional "Issues" tab.**  
---  
You-Get is a tiny command-line utility to download media contents (videos, audios, images) from the Web, in case there is no other handy way to do it.  
Here's how you use `you-get` to download a video from YouTube:  
```console
$ you-get '
site:                YouTube
title:               Me at the zoo
stream:
- itag:          43
container:     webm
quality:       medium
size:          0.5 MiB (564215 bytes)
# download-with: you-get --itag=43 [URL]

Downloading Me at the zoo.webm ...
100% (  0.5/  0.5MB) ├██████████████████████████████████┤[1/1]    6 MB/s

Saving Me at the zoo.en.srt ... Done.
```  
And here's why you might want to use it:  
* You enjoyed something on the Internet, and just want to download them for your own pleasure.
* You watch your favorite videos online from your computer, but you are prohibited from saving them. You feel that you have no control over your own computer. (And it's not how an open Web is supposed to work.)
* You want to get rid of any closed-source technology or proprietary JavaScript code, and disallow things like Flash running on your computer.
* You are an adherent of hacker culture and free software.  
What `you-get` can do for you:  
* Download videos / audios from popular websites such as YouTube, Youku, Niconico, and a bunch more. (See the full list of supported sites)
* Stream an online video in your media player. No web browser, no more ads.
* Download images (of interest) by scraping a web page.
* Download arbitrary non-HTML contents, i.e., binary files.  
Interested? Install it now and get started by examples.  
Are you a Python programmer? Then check out the source and fork it!  
![](