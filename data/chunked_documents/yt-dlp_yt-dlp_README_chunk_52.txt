---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: CHANGES FROM YOUTUBE-DL
Header 3: Deprecated options
---
These are all the deprecated options and the current alternative to achieve the same effect  
#### Almost redundant options
While these options are almost the same as their new counterparts, there are some differences that prevents them being redundant  
-j, --dump-json                  --print "%()j"
-F, --list-formats               --print formats_table
--list-thumbnails                --print thumbnails_table --print playlist:thumbnails_table
--list-subs                      --print automatic_captions_table --print subtitles_table  
#### Redundant options
While these options are redundant, they are still expected to be used due to their ease of use  
--get-description                --print description
--get-duration                   --print duration_string
--get-filename                   --print filename
--get-format                     --print format
--get-id                         --print id
--get-thumbnail                  --print thumbnail
-e, --get-title                  --print title
-g, --get-url                    --print urls
--match-title REGEX              --match-filters "title ~= (?i)REGEX"
--reject-title REGEX             --match-filters "title !~= (?i)REGEX"
--min-views COUNT                --match-filters "view_count >=? COUNT"
--max-views COUNT                --match-filters "view_count <=? COUNT"
--break-on-reject                Use --break-match-filters
--user-agent UA                  --add-headers "User-Agent:UA"
--referer URL                    --add-headers "Referer:URL"
--playlist-start NUMBER          -I NUMBER:
--playlist-end NUMBER            -I :NUMBER
--playlist-reverse               -I ::-1
--no-playlist-reverse            Default
--no-colors                      --color no_color  
#### Not recommended
While these options still work, their use is not recommended since there are other alternatives to achieve the same  
--force-generic-extractor        --ies generic,default
--exec-before-download CMD       --exec "before_dl:CMD"
--no-exec-before-download        --no-exec
--all-formats                    -f all
--all-subs                       --sub-langs all --write-subs
--print-json                     -j --no-simulate
--autonumber-size NUMBER         Use string formatting, e.g. %(autonumber)03d
--autonumber-start NUMBER        Use internal field formatting like %(autonumber+NUMBER)s
--id                             -o "%(id)s.%(ext)s"
--metadata-from-title FORMAT     --parse-metadata "%(title)s:FORMAT"
--hls-prefer-native              --downloader "m3u8:native"
--hls-prefer-ffmpeg              --downloader "m3u8:ffmpeg"
--list-formats-old               --compat-options list-formats (Alias: --no-list-formats-as-table)
--list-formats-as-table          --compat-options -list-formats [Default] (Alias: --no-list-formats-old)
--youtube-skip-dash-manifest     --extractor-args "youtube:skip=dash" (Alias: --no-youtube-include-dash-manifest)
--youtube-skip-hls-manifest      --extractor-args "youtube:skip=hls" (Alias: --no-youtube-include-hls-manifest)
--youtube-include-dash-manifest  Default (Alias: --no-youtube-skip-dash-manifest)
--youtube-include-hls-manifest   Default (Alias: --no-youtube-skip-hls-manifest)
--geo-bypass                     --xff "default"
--no-geo-bypass                  --xff "never"
--geo-bypass-country CODE        --xff CODE
--geo-bypass-ip-block IP_BLOCK   --xff IP_BLOCK  
#### Developer options
These options are not intended to be used by the end-user  
--test                           Download only part of video for testing extractors
--load-pages                     Load pages dumped by --write-pages
--youtube-print-sig-code         For testing youtube signatures
--allow-unplayable-formats       List unplayable formats also
--no-allow-unplayable-formats    Default  
#### Old aliases
These are aliases that are no longer documented for various reasons  
--avconv-location                --ffmpeg-location
--clean-infojson                 --clean-info-json
--cn-verification-proxy URL      --geo-verification-proxy URL
--dump-headers                   --print-traffic
--dump-intermediate-pages        --dump-pages
--force-write-download-archive   --force-write-archive
--load-info                      --load-info-json
--no-clean-infojson              --no-clean-info-json
--no-split-tracks                --no-split-chapters
--no-write-srt                   --no-write-subs
--prefer-unsecure                --prefer-insecure
--rate-limit RATE                --limit-rate RATE
--split-tracks                   --split-chapters
--srt-lang LANGS                 --sub-langs LANGS
--trim-file-names LENGTH         --trim-filenames LENGTH
--write-srt                      --write-subs
--yes-overwrites                 --force-overwrites  
#### Sponskrub Options
Support for SponSkrub has been deprecated in favor of the `--sponsorblock` options  
--sponskrub                      --sponsorblock-mark all
--no-sponskrub                   --no-sponsorblock
--sponskrub-cut                  --sponsorblock-remove all
--no-sponskrub-cut               --sponsorblock-remove -all
--sponskrub-force                Not applicable
--no-sponskrub-force             Not applicable
--sponskrub-location             Not applicable
--sponskrub-args                 Not applicable  
#### No longer supported
These options may no longer work as intended  
--prefer-avconv                  avconv is not officially supported by yt-dlp (Alias: --no-prefer-ffmpeg)
--prefer-ffmpeg                  Default (Alias: --no-prefer-avconv)
-C, --call-home                  Not implemented
--no-call-home                   Default
--include-ads                    No longer supported
--no-include-ads                 Default
--write-annotations              No supported site has annotations now
--no-write-annotations           Default
--compat-options seperate-video-versions  No longer needed
--compat-options no-youtube-prefer-utc-upload-date  No longer supported  
#### Removed
These options were deprecated since 2014 and have now been entirely removed  
-A, --auto-number                -o "%(autonumber)s-%(id)s.%(ext)s"
-t, -l, --title, --literal       -o "%(title)s-%(id)s.%(ext)s"