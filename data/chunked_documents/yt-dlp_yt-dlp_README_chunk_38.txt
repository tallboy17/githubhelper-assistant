---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: FORMAT SELECTION
---
By default, yt-dlp tries to download the best available quality if you **don't** pass any options.
This is generally equivalent to using `-f bestvideo*+bestaudio/best`. However, if multiple audiostreams is enabled (`--audio-multistreams`), the default format changes to `-f bestvideo+bestaudio/best`. Similarly, if ffmpeg is unavailable, or if you use yt-dlp to stream to `stdout` (`-o -`), the default becomes `-f best/bestvideo+bestaudio`.  
**Deprecation warning**: Latest versions of yt-dlp can stream multiple formats to the stdout simultaneously using ffmpeg. So, in future versions, the default for this will be set to `-f bv*+ba/b` similar to normal downloads. If you want to preserve the `-f b/bv+ba` setting, it is recommended to explicitly specify it in the configuration options.  
The general syntax for format selection is `-f FORMAT` (or `--format FORMAT`) where `FORMAT` is a *selector expression*, i.e. an expression that describes format or formats you would like to download.  

**tl;dr:** navigate me to examples.
  
The simplest case is requesting a specific format; e.g. with `-f 22` you can download the format with format code equal to 22. You can get the list of available format codes for particular video using `--list-formats` or `-F`. Note that these format codes are extractor specific.  
You can also use a file extension (currently `3gp`, `aac`, `flv`, `m4a`, `mp3`, `mp4`, `ogg`, `wav`, `webm` are supported) to download the best quality format of a particular file extension served as a single file, e.g. `-f webm` will download the best quality format with the `webm` extension served as a single file.  
You can use `-f -` to interactively provide the format selector *for each video*  
You can also use special names to select particular edge case formats:  
- `all`: Select **all formats** separately
- `mergeall`: Select and **merge all formats** (Must be used with `--audio-multistreams`, `--video-multistreams` or both)
- `b*`, `best*`: Select the best quality format that **contains either** a video or an audio or both (i.e.; `vcodec!=none or acodec!=none`)
- `b`, `best`: Select the best quality format that **contains both** video and audio. Equivalent to `best*[vcodec!=none][acodec!=none]`
- `bv`, `bestvideo`: Select the best quality **video-only** format. Equivalent to `best*[acodec=none]`
- `bv*`, `bestvideo*`: Select the best quality format that **contains video**. It may also contain audio. Equivalent to `best*[vcodec!=none]`
- `ba`, `bestaudio`: Select the best quality **audio-only** format. Equivalent to `best*[vcodec=none]`
- `ba*`, `bestaudio*`: Select the best quality format that **contains audio**. It may also contain video. Equivalent to `best*[acodec!=none]` (Do not use!)
- `w*`, `worst*`: Select the worst quality format that contains either a video or an audio
- `w`, `worst`: Select the worst quality format that contains both video and audio. Equivalent to `worst*[vcodec!=none][acodec!=none]`
- `wv`, `worstvideo`: Select the worst quality video-only format. Equivalent to `worst*[acodec=none]`
- `wv*`, `worstvideo*`: Select the worst quality format that contains video. It may also contain audio. Equivalent to `worst*[vcodec!=none]`
- `wa`, `worstaudio`: Select the worst quality audio-only format. Equivalent to `worst*[vcodec=none]`
- `wa*`, `worstaudio*`: Select the worst quality format that contains audio. It may also contain video. Equivalent to `worst*[acodec!=none]`  
For example, to download the worst quality video-only format you can use `-f worstvideo`. It is, however, recommended not to use `worst` and related options. When your format selector is `worst`, the format which is worst in all respects is selected. Most of the time, what you actually want is the video with the smallest filesize instead. So it is generally better to use `-S +size` or more rigorously, `-S +size,+br,+res,+fps` instead of `-f worst`. See Sorting Formats for more details.  
You can select the n'th best format of a type by using `best.`. For example, `best.2` will select the 2nd best combined format. Similarly, `bv*.3` will select the 3rd best format that contains a video stream.  
If you want to download multiple videos, and they don't have the same formats available, you can specify the order of preference using slashes. Note that formats on the left hand side are preferred; e.g. `-f 22/17/18` will download format 22 if it's available, otherwise it will download format 17 if it's available, otherwise it will download format 18 if it's available, otherwise it will complain that no suitable formats are available for download.  
If you want to download several formats of the same video use a comma as a separator, e.g. `-f 22,17,18` will download all these three formats, of course if they are available. Or a more sophisticated example combined with the precedence feature: `-f 136/137/mp4/bestvideo,140/m4a/bestaudio`.  
You can merge the video and audio of multiple formats into a single file using `-f ++...` (requires ffmpeg installed); e.g. `-f bestvideo+bestaudio` will download the best video-only format, the best audio-only format and mux them together with ffmpeg.  
**Deprecation warning**: Since the *below* described behavior is complex and counter-intuitive, this will be removed and multistreams will be enabled by default in the future. A new operator will be instead added to limit formats to single audio/video  
Unless `--video-multistreams` is used, all formats with a video stream except the first one are ignored. Similarly, unless `--audio-multistreams` is used, all formats with an audio stream except the first one are ignored. E.g. `-f bestvideo+best+bestaudio --video-multistreams --audio-multistreams` will download and merge all 3 given formats. The resulting file will have 2 video streams and 2 audio streams. But `-f bestvideo+best+bestaudio --no-video-multistreams` will download and merge only `bestvideo` and `bestaudio`. `best` is ignored since another format containing a video stream (`bestvideo`) has already been selected. The order of the formats is therefore important. `-f best+bestaudio --no-audio-multistreams` will download only `best` while `-f bestaudio+best --no-audio-multistreams` will ignore `best` and download only `bestaudio`.