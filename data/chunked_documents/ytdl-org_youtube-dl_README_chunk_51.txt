---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: Why do I need to go through that much red tape when filing bugs?
---
Before we had the issue template, despite our extensive bug reporting instructions, about 80% of the issue reports we got were useless, for instance because people used ancient versions hundreds of releases old, because of simple syntactic errors (not in youtube-dl but in general shell usage), because the problem was already reported multiple times before, because people did not actually read an error message, even if it said "please install ffmpeg", because people did not mention the URL they were trying to download and many more simple, easy-to-avoid problems, many of whom were totally unrelated to youtube-dl.  
youtube-dl is an open-source project manned by too few volunteers, so we'd rather spend time fixing bugs where we are certain none of those simple problems apply, and where we can be reasonably confident to be able to reproduce the issue without asking the reporter repeatedly. As such, the output of `youtube-dl -v YOUR_URL_HERE` is really all that's required to file an issue. The issue template also guides you through some basic steps you can do, such as checking that your version of youtube-dl is current.