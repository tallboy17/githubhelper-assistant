---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: How do I pass cookies to youtube-dl?
---
Use the `--cookies` option, for example `--cookies /path/to/cookies/file.txt`.  
In order to extract cookies from browser use any conforming browser extension for exporting cookies. For example, Get cookies.txt LOCALLY (for Chrome) or cookies.txt (for Firefox).  
Note that the cookies file must be in Mozilla/Netscape format and the first line of the cookies file must be either `# HTTP Cookie File` or `# Netscape HTTP Cookie File`. Make sure you have correct newline format in the cookies file and convert newlines if necessary to correspond with your OS, namely `CRLF` (`\r\n`) for Windows and `LF` (`\n`) for Unix and Unix-like systems (Linux, macOS, etc.). `HTTP Error 400: Bad Request` when using `--cookies` is a good sign of invalid newline format.  
Passing cookies to youtube-dl is a good way to workaround login when a particular extractor does not implement it explicitly. Another use case is working around CAPTCHA some websites require you to solve in particular cases in order to get access (e.g. YouTube, CloudFlare).