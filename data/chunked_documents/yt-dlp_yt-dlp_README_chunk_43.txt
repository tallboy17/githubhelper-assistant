---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: MODIFYING METADATA
Header 2: Modifying metadata examples
---
```bash
# Interpret the title as "Artist - Title"
$ yt-dlp --parse-metadata "title:%(artist)s - %(title)s"

# Regex example
$ yt-dlp --parse-metadata "description:Artist - (?P.+)"

# Set title as "Series name S01E05"
$ yt-dlp --parse-metadata "%(series)s S%(season_number)02dE%(episode_number)02d:%(title)s"

# Prioritize uploader as the "artist" field in video metadata
$ yt-dlp --parse-metadata "%(uploader|)s:%(meta_artist)s" --embed-metadata

# Set "comment" field in video metadata using description instead of webpage_url,
# handling multiple lines correctly
$ yt-dlp --parse-metadata "description:(?s)(?P.+)" --embed-metadata

# Do not set any "synopsis" in the video metadata
$ yt-dlp --parse-metadata ":(?P)"

# Remove "formats" field from the infojson by setting it to an empty string
$ yt-dlp --parse-metadata "video::(?P)" --write-info-json

# Replace all spaces and "_" in title and uploader with a `-`
$ yt-dlp --replace-in-metadata "title,uploader" "[ _]" "-"

```