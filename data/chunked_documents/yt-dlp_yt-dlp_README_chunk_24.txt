---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: USAGE AND OPTIONS
Header 2: Verbosity and Simulation Options:
---
-q, --quiet                     Activate quiet mode. If used with --verbose,
print the log to stderr
--no-quiet                      Deactivate quiet mode. (Default)
--no-warnings                   Ignore warnings
-s, --simulate                  Do not download the video and do not write
anything to disk
--no-simulate                   Download the video even if printing/listing
options are used
--ignore-no-formats-error       Ignore "No video formats" error. Useful for
extracting metadata even if the videos are
not actually available for download
(experimental)
--no-ignore-no-formats-error    Throw error when no downloadable video
formats are found (default)
--skip-download                 Do not download the video but write all
related files (Alias: --no-download)
-O, --print [WHEN:]TEMPLATE     Field name or output template to print to
screen, optionally prefixed with when to
print it, separated by a ":". Supported
values of "WHEN" are the same as that of
--use-postprocessor (default: video).
Implies --quiet. Implies --simulate unless
--no-simulate or later stages of WHEN are
used. This option can be used multiple times
--print-to-file [WHEN:]TEMPLATE FILE
Append given template to the file. The
values of WHEN and TEMPLATE are the same as
that of --print. FILE uses the same syntax
as the output template. This option can be
used multiple times
-j, --dump-json                 Quiet, but print JSON information for each
video. Simulate unless --no-simulate is
used. See "OUTPUT TEMPLATE" for a
description of available keys
-J, --dump-single-json          Quiet, but print JSON information for each
URL or infojson passed. Simulate unless
--no-simulate is used. If the URL refers to
a playlist, the whole playlist information
is dumped in a single line
--force-write-archive           Force download archive entries to be written
as far as no errors occur, even if -s or
another simulation option is used (Alias:
--force-download-archive)
--newline                       Output progress bar as new lines
--no-progress                   Do not print progress bar
--progress                      Show progress bar, even if in quiet mode
--console-title                 Display progress in console titlebar
--progress-template [TYPES:]TEMPLATE
Template for progress outputs, optionally
prefixed with one of "download:" (default),
"download-title:" (the console title),
"postprocess:",  or "postprocess-title:".
The video's fields are accessible under the
"info" key and the progress attributes are
accessible under "progress" key. E.g.
--console-title --progress-template
"download-title:%(info.id)s-%(progress.eta)s"
--progress-delta SECONDS        Time between progress output (default: 0)
-v, --verbose                   Print various debugging information
--dump-pages                    Print downloaded pages encoded using base64
to debug problems (very verbose)
--write-pages                   Write downloaded intermediary pages to files
in the current directory to debug problems
--print-traffic                 Display sent and read HTTP traffic