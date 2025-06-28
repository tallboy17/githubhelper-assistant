---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: BUGS
Header 2: Opening a bug report or suggestion
Header 3: Is the description of the issue itself sufficient?
---
We often get issue reports that are hard to understand. To avoid subsequent clarifications, and to assist participants who are not native English speakers, please elaborate on what feature you are requesting, or what bug you want to be fixed.  
Make sure that it's obvious  
- What the problem is
- How it could be fixed
- How your proposed solution would look  
If your report is shorter than two lines, it is almost certainly missing some of these, which makes it hard for us to respond to it. We're often too polite to close the issue outright, but the missing info makes misinterpretation likely. As a committer myself, I often get frustrated by these issues, since the only possible way for me to move forward on them is to ask for clarification over and over.  
For bug reports, this means that your report should contain the *complete* output of youtube-dl when called with the `-v` flag. The error message you get for (most) bugs even says so, but you would not believe how many of our bug reports do not contain this information.  
If your server has multiple IPs or you suspect censorship, adding `--call-home` may be a good idea to get more diagnostics. If the error is `ERROR: Unable to extract ...` and you cannot reproduce it from multiple countries, add `--dump-pages` (warning: this will yield a rather large output, redirect it to the file `log.txt` by adding `>log.txt 2>&1` to your command-line) or upload the `.dump` files you get when you add `--write-pages` somewhere.  
**Site support requests must contain an example URL**. An example URL is a URL you might want to download, like ` There should be an obvious video present. Except under very special circumstances, the main page of a video service (e.g. ` is *not* an example URL.