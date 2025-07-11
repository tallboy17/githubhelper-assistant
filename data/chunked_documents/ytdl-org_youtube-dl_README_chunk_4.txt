---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: OPTIONS
---
-h, --help                           Print this help text and exit
--version                            Print program version and exit
-U, --update                         Update this program to latest version.
Make sure that you have sufficient
permissions (run with sudo if needed)
-i, --ignore-errors                  Continue on download errors, for
example to skip unavailable videos in a
playlist
--abort-on-error                     Abort downloading of further videos (in
the playlist or the command line) if an
error occurs
--dump-user-agent                    Display the current browser
identification
--list-extractors                    List all supported extractors
--extractor-descriptions             Output descriptions of all supported
extractors
--force-generic-extractor            Force extraction to use the generic
extractor
--default-search PREFIX              Use this prefix for unqualified URLs.
For example "gvsearch2:" downloads two
videos from google videos for youtube-
dl "large apple". Use the value "auto"
to let youtube-dl guess ("auto_warning"
to emit a warning when guessing).
"error" just throws an error. The
default value "fixup_error" repairs
broken URLs, but emits an error if this
is not possible instead of searching.
--ignore-config                      Do not read configuration files. When
given in the global configuration file
/etc/youtube-dl.conf: Do not read the
user configuration in
~/.config/youtube-dl/config
(%APPDATA%/youtube-dl/config.txt on
Windows)
--config-location PATH               Location of the configuration file;
either the path to the config or its
containing directory.
--flat-playlist                      Do not extract the videos of a
playlist, only list them.
--mark-watched                       Mark videos watched (YouTube only)
--no-mark-watched                    Do not mark videos watched (YouTube
only)
--no-color                           Do not emit color codes in output