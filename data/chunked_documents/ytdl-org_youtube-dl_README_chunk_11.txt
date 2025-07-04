---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: OPTIONS
Header 2: Verbosity / Simulation Options:
---
-q, --quiet                          Activate quiet mode
--no-warnings                        Ignore warnings
-s, --simulate                       Do not download the video and do not
write anything to disk
--skip-download                      Do not download the video
-g, --get-url                        Simulate, quiet but print URL
-e, --get-title                      Simulate, quiet but print title
--get-id                             Simulate, quiet but print id
--get-thumbnail                      Simulate, quiet but print thumbnail URL
--get-description                    Simulate, quiet but print video
description
--get-duration                       Simulate, quiet but print video length
--get-filename                       Simulate, quiet but print output
filename
--get-format                         Simulate, quiet but print output format
-j, --dump-json                      Simulate, quiet but print JSON
information. See the "OUTPUT TEMPLATE"
for a description of available keys.
-J, --dump-single-json               Simulate, quiet but print JSON
information for each command-line
argument. If the URL refers to a
playlist, dump the whole playlist
information in a single line.
--print-json                         Be quiet and print the video
information as JSON (video is still
being downloaded).
--newline                            Output progress bar as new lines
--no-progress                        Do not print progress bar
--console-title                      Display progress in console titlebar
-v, --verbose                        Print various debugging information
--dump-pages                         Print downloaded pages encoded using
base64 to debug problems (very verbose)
--write-pages                        Write downloaded intermediary pages to
files in the current directory to debug
problems
--print-traffic                      Display sent and read HTTP traffic
-C, --call-home                      Contact the youtube-dl server for
debugging
--no-call-home                       Do NOT contact the youtube-dl server
for debugging