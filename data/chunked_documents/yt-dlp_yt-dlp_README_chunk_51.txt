---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: CHANGES FROM YOUTUBE-DL
Header 3: Differences in default behavior
---
Some of yt-dlp's default options are different from that of youtube-dl and youtube-dlc:  
* yt-dlp supports only Python 3.9+, and will remove support for more versions as they become EOL; while youtube-dl still supports Python 2.6+ and 3.2+
* The options `--auto-number` (`-A`), `--title` (`-t`) and `--literal` (`-l`), no longer work. See removed options for details
* `avconv` is not supported as an alternative to `ffmpeg`
* yt-dlp stores config files in slightly different locations to youtube-dl. See CONFIGURATION for a list of correct locations
* The default output template is `%(title)s [%(id)s].%(ext)s`. There is no real reason for this change. This was changed before yt-dlp was ever made public and now there are no plans to change it back to `%(title)s-%(id)s.%(ext)s`. Instead, you may use `--compat-options filename`
* The default format sorting is different from youtube-dl and prefers higher resolution and better codecs rather than higher bitrates. You can use the `--format-sort` option to change this to any order you prefer, or use `--compat-options format-sort` to use youtube-dl's sorting order. Older versions of yt-dlp preferred VP9 due to its broader compatibility; you can use `--compat-options prefer-vp9-sort` to revert to that format sorting preference. These two compat options cannot be used together
* The default format selector is `bv*+ba/b`. This means that if a combined video + audio format that is better than the best video-only format is found, the former will be preferred. Use `-f bv+ba/b` or `--compat-options format-spec` to revert this
* Unlike youtube-dlc, yt-dlp does not allow merging multiple audio/video streams into one file by default (since this conflicts with the use of `-f bv*+ba`). If needed, this feature must be enabled using `--audio-multistreams` and `--video-multistreams`. You can also use `--compat-options multistreams` to enable both
* `--no-abort-on-error` is enabled by default. Use `--abort-on-error` or `--compat-options abort-on-error` to abort on errors instead
* When writing metadata files such as thumbnails, description or infojson, the same information (if available) is also written for playlists. Use `--no-write-playlist-metafiles` or `--compat-options no-playlist-metafiles` to not write these files
* `--add-metadata` attaches the `infojson` to `mkv` files in addition to writing the metadata when used with `--write-info-json`. Use `--no-embed-info-json` or `--compat-options no-attach-info-json` to revert this
* Some metadata are embedded into different fields when using `--add-metadata` as compared to youtube-dl. Most notably, `comment` field contains the `webpage_url` and `synopsis` contains the `description`. You can use `--parse-metadata` to modify this to your liking or use `--compat-options embed-metadata` to revert this
* `playlist_index` behaves differently when used with options like `--playlist-reverse` and `--playlist-items`. See #302 for details. You can use `--compat-options playlist-index` if you want to keep the earlier behavior
* The output of `-F` is listed in a new format. Use `--compat-options list-formats` to revert this
* Live chats (if available) are considered as subtitles. Use `--sub-langs all,-live_chat` to download all subtitles except live chat. You can also use `--compat-options no-live-chat` to prevent any live chat/danmaku from downloading
* YouTube channel URLs download all uploads of the channel. To download only the videos in a specific tab, pass the tab's URL. If the channel does not show the requested tab, an error will be raised. Also, `/live` URLs raise an error if there are no live videos instead of silently downloading the entire channel. You may use `--compat-options no-youtube-channel-redirect` to revert all these redirections
* Unavailable videos are also listed for YouTube playlists. Use `--compat-options no-youtube-unavailable-videos` to remove this
* The upload dates extracted from YouTube are in UTC.
* If `ffmpeg` is used as the downloader, the downloading and merging of formats happen in a single step when possible. Use `--compat-options no-direct-merge` to revert this
* Thumbnail embedding in `mp4` is done with mutagen if possible. Use `--compat-options embed-thumbnail-atomicparsley` to force the use of AtomicParsley instead
* Some internal metadata such as filenames are removed by default from the infojson. Use `--no-clean-infojson` or `--compat-options no-clean-infojson` to revert this
* When `--embed-subs` and `--write-subs` are used together, the subtitles are written to disk and also embedded in the media file. You can use just `--embed-subs` to embed the subs and automatically delete the separate file. See #630 (comment) for more info. `--compat-options no-keep-subs` can be used to revert this
* `certifi` will be used for SSL root certificates, if installed. If you want to use system certificates (e.g. self-signed), use `--compat-options no-certifi`
* yt-dlp's sanitization of invalid characters in filenames is different/smarter than in youtube-dl. You can use `--compat-options filename-sanitization` to revert to youtube-dl's behavior
* ~~yt-dlp tries to parse the external downloader outputs into the standard progress output if possible (Currently implemented: aria2c). You can use `--compat-options no-external-downloader-progress` to get the downloader output as-is~~
* yt-dlp versions between 2021.09.01 and 2023.01.02 applies `--match-filters` to nested playlists. This was an unintentional side-effect of 8f18ac and is fixed in d7b460. Use `--compat-options playlist-match-filter` to revert this
* yt-dlp versions between 2021.11.10 and 2023.06.21 estimated `filesize_approx` values for fragmented/manifest formats. This was added for convenience in f2fe69, but was reverted in 0dff8e due to the potentially extreme inaccuracy of the estimated values. Use `--compat-options manifest-filesize-approx` to keep extracting the estimated values
* yt-dlp uses modern http client backends such as `requests`. Use `--compat-options prefer-legacy-http-handler` to prefer the legacy http handler (`urllib`) to be used for standard http requests.
* The sub-modules `swfinterp`, `casefold` are removed.
* Passing `--simulate` (or calling `extract_info` with `download=False`) no longer alters the default format selection. See #9843 for details.  
For ease of use, a few more compat options are available:  
* `--compat-options all`: Use all compat options (**Do NOT use this!**)
* `--compat-options youtube-dl`: Same as `--compat-options all,-multistreams,-playlist-match-filter,-manifest-filesize-approx,-allow-unsafe-ext,-prefer-vp9-sort`
* `--compat-options youtube-dlc`: Same as `--compat-options all,-no-live-chat,-no-youtube-channel-redirect,-playlist-match-filter,-manifest-filesize-approx,-allow-unsafe-ext,-prefer-vp9-sort`
* `--compat-options 2021`: Same as `--compat-options 2022,no-certifi,filename-sanitization`
* `--compat-options 2022`: Same as `--compat-options 2023,playlist-match-filter,no-external-downloader-progress,prefer-legacy-http-handler,manifest-filesize-approx`
* `--compat-options 2023`: Same as `--compat-options 2024,prefer-vp9-sort`
* `--compat-options 2024`: Currently does nothing. Use this to enable all future compat options  
The following compat options restore vulnerable behavior from before security patches:  
* `--compat-options allow-unsafe-ext`: Allow files with any extension (including unsafe ones) to be downloaded ([GHSA-79w7-vh3h-8g4j]())  
> :warning: Only use if a valid file download is rejected because its extension is detected as uncommon
>
> **This option can enable remote code execution! Consider [opening an issue]() instead!**