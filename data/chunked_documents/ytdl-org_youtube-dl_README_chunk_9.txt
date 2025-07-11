---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: OPTIONS
Header 2: Filesystem Options:
---
-a, --batch-file FILE                File containing URLs to download ('-'
for stdin), one URL per line. Lines
starting with '#', ';' or ']' are
considered as comments and ignored.
--id                                 Use only video ID in file name
-o, --output TEMPLATE                Output filename template, see the
"OUTPUT TEMPLATE" for all the info
--output-na-placeholder PLACEHOLDER  Placeholder value for unavailable meta
fields in output filename template
(default is "NA")
--autonumber-start NUMBER            Specify the start value for
%(autonumber)s (default is 1)
--restrict-filenames                 Restrict filenames to only ASCII
characters, and avoid "&" and spaces in
filenames
-w, --no-overwrites                  Do not overwrite files
-c, --continue                       Force resume of partially downloaded
files. By default, youtube-dl will
resume downloads if possible.
--no-continue                        Do not resume partially downloaded
files (restart from beginning)
--no-part                            Do not use .part files - write directly
into output file
--no-mtime                           Do not use the Last-modified header to
set the file modification time
--write-description                  Write video description to a
.description file
--write-info-json                    Write video metadata to a .info.json
file
--write-annotations                  Write video annotations to a
.annotations.xml file
--load-info-json FILE                JSON file containing the video
information (created with the "--write-
info-json" option)
--cookies FILE                       File to read cookies from and dump
cookie jar in
--cache-dir DIR                      Location in the filesystem where
youtube-dl can store some downloaded
information permanently. By default
$XDG_CACHE_HOME/youtube-dl or
~/.cache/youtube-dl . At the moment,
only YouTube player files (for videos
with obfuscated signatures) are cached,
but that may change.
--no-cache-dir                       Disable filesystem caching
--rm-cache-dir                       Delete all filesystem cache files