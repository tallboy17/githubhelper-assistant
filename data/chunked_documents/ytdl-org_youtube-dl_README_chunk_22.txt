---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: VIDEO SELECTION
---
Videos can be filtered by their upload date using the options `--date`, `--datebefore` or `--dateafter`. They accept dates in two formats:  
- Absolute dates: Dates in the format `YYYYMMDD`.
- Relative dates: Dates in the format `(now|today)[+-]0-9(s)?`  
Examples:  
```bash
# Download only the videos uploaded in the last 6 months
$ youtube-dl --dateafter now-6months

# Download only the videos uploaded on January 1, 1970
$ youtube-dl --date 19700101

$ # Download only the videos uploaded in the 200x decade
$ youtube-dl --dateafter 20000101 --datebefore 20091231
```