---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: CONFIGURATION
Header 3: Configuration file encoding
---
The configuration files are decoded according to the UTF BOM if present, and in the encoding from system locale otherwise.  
If you want your file to be decoded differently, add `# coding: ENCODING` to the beginning of the file (e.g. `# coding: shift-jis`). There must be no characters before that, even spaces or BOM.