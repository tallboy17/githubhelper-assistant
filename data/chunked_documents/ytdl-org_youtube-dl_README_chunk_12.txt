---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: OPTIONS
Header 2: Workarounds:
---
--encoding ENCODING                  Force the specified encoding
(experimental)
--no-check-certificate               Suppress HTTPS certificate validation
--prefer-insecure                    Use an unencrypted connection to
retrieve information about the video.
(Currently supported only for YouTube)
--user-agent UA                      Specify a custom user agent
--referer URL                        Specify a custom referer, use if the
video access is restricted to one
domain
--add-header FIELD:VALUE             Specify a custom HTTP header and its
value, separated by a colon ':'. You
can use this option multiple times
--bidi-workaround                    Work around terminals that lack
bidirectional text support. Requires
bidiv or fribidi executable in PATH
--sleep-interval SECONDS             Number of seconds to sleep before each
download when used alone or a lower
bound of a range for randomized sleep
before each download (minimum possible
number of seconds to sleep) when used
along with --max-sleep-interval.
--max-sleep-interval SECONDS         Upper bound of a range for randomized
sleep before each download (maximum
possible number of seconds to sleep).
Must only be used along with --min-
sleep-interval.