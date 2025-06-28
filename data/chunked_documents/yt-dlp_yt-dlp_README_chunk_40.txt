---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: FORMAT SELECTION
Header 2: Sorting Formats
---
You can change the criteria for being considered the `best` by using `-S` (`--format-sort`). The general format for this is `--format-sort field1,field2...`.  
The available fields are:  
- `hasvid`: Gives priority to formats that have a video stream
- `hasaud`: Gives priority to formats that have an audio stream
- `ie_pref`: The format preference
- `lang`: The language preference as determined by the extractor (e.g. original language preferred over audio description)
- `quality`: The quality of the format
- `source`: The preference of the source
- `proto`: Protocol used for download (`https`/`ftps` > `http`/`ftp` > `m3u8_native`/`m3u8` > `http_dash_segments`> `websocket_frag` > `mms`/`rtsp` > `f4f`/`f4m`)
- `vcodec`: Video Codec (`av01` > `vp9.2` > `vp9` > `h265` > `h264` > `vp8` > `h263` > `theora` > other)
- `acodec`: Audio Codec (`flac`/`alac` > `wav`/`aiff` > `opus` > `vorbis` > `aac` > `mp4a` > `mp3` > `ac4` > `eac3` > `ac3` > `dts` > other)
- `codec`: Equivalent to `vcodec,acodec`
- `vext`: Video Extension (`mp4` > `mov` > `webm` > `flv` > other). If `--prefer-free-formats` is used, `webm` is preferred.
- `aext`: Audio Extension (`m4a` > `aac` > `mp3` > `ogg` > `opus` > `webm` > other). If `--prefer-free-formats` is used, the order changes to `ogg` > `opus` > `webm` > `mp3` > `m4a` > `aac`
- `ext`: Equivalent to `vext,aext`
- `filesize`: Exact filesize, if known in advance
- `fs_approx`: Approximate filesize
- `size`: Exact filesize if available, otherwise approximate filesize
- `height`: Height of video
- `width`: Width of video
- `res`: Video resolution, calculated as the smallest dimension.
- `fps`: Framerate of video
- `hdr`: The dynamic range of the video (`DV` > `HDR12` > `HDR10+` > `HDR10` > `HLG` > `SDR`)
- `channels`: The number of audio channels
- `tbr`: Total average bitrate in kbps
- `vbr`: Average video bitrate in kbps
- `abr`: Average audio bitrate in kbps
- `br`: Average bitrate in kbps, `tbr`/`vbr`/`abr`
- `asr`: Audio sample rate in Hz  
**Deprecation warning**: Many of these fields have (currently undocumented) aliases, that may be removed in a future version. It is recommended to use only the documented field names.  
All fields, unless specified otherwise, are sorted in descending order. To reverse this, prefix the field with a `+`. E.g. `+res` prefers format with the smallest resolution. Additionally, you can suffix a preferred value for the fields, separated by a `:`. E.g. `res:720` prefers larger videos, but no larger than 720p and the smallest video if there are no videos less than 720p. For `codec` and `ext`, you can provide two preferred values, the first for video and the second for audio. E.g. `+codec:avc:m4a` (equivalent to `+vcodec:avc,+acodec:m4a`) sets the video codec preference to `h264` > `h265` > `vp9` > `vp9.2` > `av01` > `vp8` > `h263` > `theora` and audio codec preference to `mp4a` > `aac` > `vorbis` > `opus` > `mp3` > `ac3` > `dts`. You can also make the sorting prefer the nearest values to the provided by using `~` as the delimiter. E.g. `filesize~1G` prefers the format with filesize closest to 1 GiB.  
The fields `hasvid` and `ie_pref` are always given highest priority in sorting, irrespective of the user-defined order. This behavior can be changed by using `--format-sort-force`. Apart from these, the default order used is: `lang,quality,res,fps,hdr:12,vcodec,channels,acodec,size,br,asr,proto,ext,hasaud,source,id`. The extractors may override this default order, but they cannot override the user-provided order.  
Note that the default for hdr is `hdr:12`; i.e. Dolby Vision is not preferred. This choice was made since DV formats are not yet fully compatible with most devices. This may be changed in the future.  
If your format selector is `worst`, the last item is selected after sorting. This means it will select the format that is worst in all respects. Most of the time, what you actually want is the video with the smallest filesize instead. So it is generally better to use `-f best -S +size,+br,+res,+fps`.  
**Tip**: You can use the `-v -F` to see how the formats have been sorted (worst to best).