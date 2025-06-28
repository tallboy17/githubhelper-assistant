---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: I'm getting an error when trying to use output template: `error: using output template conflicts with using title, video ID or auto number`
---
Make sure you are not using `-o` with any of these options `-t`, `--title`, `--id`, `-A` or `--auto-number` set in command line or in a configuration file. Remove the latter if any.