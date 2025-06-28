---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: USAGE AND OPTIONS
Header 2: Workarounds:
---
--encoding ENCODING             Force the specified encoding (experimental)
--legacy-server-connect         Explicitly allow HTTPS connection to servers
that do not support RFC 5746 secure
renegotiation
--no-check-certificates         Suppress HTTPS certificate validation
--prefer-insecure               Use an unencrypted connection to retrieve
information about the video (Currently
supported only for YouTube)
--add-headers FIELD:VALUE       Specify a custom HTTP header and its value,
separated by a colon ":". You can use this
option multiple times
--bidi-workaround               Work around terminals that lack
bidirectional text support. Requires bidiv
or fribidi executable in PATH
--sleep-requests SECONDS        Number of seconds to sleep between requests
during data extraction
--sleep-interval SECONDS        Number of seconds to sleep before each
download. This is the minimum time to sleep
when used along with --max-sleep-interval
(Alias: --min-sleep-interval)
--max-sleep-interval SECONDS    Maximum number of seconds to sleep. Can only
be used along with --min-sleep-interval
--sleep-subtitles SECONDS       Number of seconds to sleep before each
subtitle download