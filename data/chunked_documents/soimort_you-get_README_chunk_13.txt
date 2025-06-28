---
repo: soimort/you-get
readme_filename: soimort_you-get_README.md
stars: 55790
forks: 9764
watchers: 55790
contributors_count: 226
license: NOASSERTION
Header 1: You-Get
Header 2: Getting Started
Header 3: Download anything else
---
If you already have the URL of the exact resource you want, you can download it directly with:  
```
$ you-get 
Site:       stallman.org
Title:      rms
Type:       JPEG Image (image/jpeg)
Size:       0.06 MiB (66482 Bytes)

Downloading rms.jpg ...
100% (  0.1/  0.1MB) ├████████████████████████████████████████┤[1/1]  127 kB/s
```  
Otherwise, `you-get` will scrape the web page and try to figure out if there's anything interesting to you:  
```
$ you-get 
Site:       Tumblr.com
Title:      [tumblr] tumblr_mxhg13jx4n1sftq6do1_640
Type:       Portable Network Graphics (image/png)
Size:       0.11 MiB (118484 Bytes)

Downloading [tumblr] tumblr_mxhg13jx4n1sftq6do1_640.png ...
100% (  0.1/  0.1MB) ├████████████████████████████████████████┤[1/1]   22 MB/s
```  
**Note:**  
* This feature is an experimental one and far from perfect. It works best on scraping large-sized images from popular websites like Tumblr and Blogger, but there is really no universal pattern that can apply to any site on the Internet.