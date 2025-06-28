---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: CHANGES FROM YOUTUBE-DL
Header 3: New features
---
* Forked from **yt-dlc@f9401f2** and merged with **youtube-dl@a08f2b7** (exceptions)  
* **SponsorBlock Integration**: You can mark/remove sponsor sections in YouTube videos by utilizing the SponsorBlock API  
* **Format Sorting**: The default format sorting options have been changed so that higher resolution and better codecs will be now preferred instead of simply using larger bitrate. Furthermore, you can now specify the sort order using `-S`. This allows for much easier format selection than what is possible by simply using `--format` (examples)  
* **Merged with animelover1984/youtube-dl**: You get most of the features and improvements from animelover1984/youtube-dl including `--write-comments`, `BiliBiliSearch`, `BilibiliChannel`, Embedding thumbnail in mp4/ogg/opus, playlist infojson etc. See #31 for details.  
* **YouTube improvements**:
* Supports Clips, Stories (`ytstories:`), Search (including filters)**\***, YouTube Music Search, Channel-specific search, Search prefixes (`ytsearch:`, `ytsearchdate:`)**\***, Mixes, and Feeds (`:ytfav`, `:ytwatchlater`, `:ytsubs`, `:ythistory`, `:ytrec`, `:ytnotif`)
* Fix for n-sig based throttling **\***
* Download livestreams from the start using `--live-from-start` (*experimental*)
* Channel URLs download all uploads of the channel, including shorts and live
* Support for logging in with OAuth  
* **Cookies from browser**: Cookies can be automatically extracted from all major web browsers using `--cookies-from-browser BROWSER[+KEYRING][:PROFILE][::CONTAINER]`  
* **Download time range**: Videos can be downloaded partially based on either timestamps or chapters using `--download-sections`  
* **Split video by chapters**: Videos can be split into multiple files based on chapters using `--split-chapters`  
* **Multi-threaded fragment downloads**: Download multiple fragments of m3u8/mpd videos in parallel. Use `--concurrent-fragments` (`-N`) option to set the number of threads used  
* **Aria2c with HLS/DASH**: You can use `aria2c` as the external downloader for DASH(mpd) and HLS(m3u8) formats  
* **New and fixed extractors**: Many new extractors have been added and a lot of existing ones have been fixed. See the changelog or the list of supported sites  
* **New MSOs**: Philo, Spectrum, SlingTV, Cablevision, RCN etc.  
* **Subtitle extraction from manifests**: Subtitles can be extracted from streaming media manifests. See commit/be6202f for details  
* **Multiple paths and output templates**: You can give different output templates and download paths for different types of files. You can also set a temporary path where intermediary files are downloaded to using `--paths` (`-P`)  
* **Portable Configuration**: Configuration files are automatically loaded from the home and root directories. See CONFIGURATION for details  
* **Output template improvements**: Output templates can now have date-time formatting, numeric offsets, object traversal etc. See output template for details. Even more advanced operations can also be done with the help of `--parse-metadata` and `--replace-in-metadata`  
* **Other new options**: Many new options have been added such as `--alias`, `--print`, `--concat-playlist`, `--wait-for-video`, `--retry-sleep`, `--sleep-requests`, `--convert-thumbnails`, `--force-download-archive`, `--force-overwrites`, `--break-match-filters` etc  
* **Improvements**: Regex and other operators in `--format`/`--match-filters`, multiple `--postprocessor-args` and `--downloader-args`, faster archive checking, more format selection options, merge multi-video/audio, multiple `--config-locations`, `--exec` at different stages, etc  
* **Plugins**: Extractors and PostProcessors can be loaded from an external file. See plugins for details  
* **Self updater**: The releases can be updated using `yt-dlp -U`, and downgraded using `--update-to` if required  
* **Automated builds**: Nightly/master builds can be used with `--update-to nightly` and `--update-to master`  
See changelog or commits for the full list of changes  
Features marked with a **\*** have been back-ported to youtube-dl