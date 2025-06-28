---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: FORMAT SELECTION
Header 2: Filtering Formats
---
You can also filter the video formats by putting a condition in brackets, as in `-f "best[height=720]"` (or `-f "[filesize>10M]"` since filters without a selector are interpreted as `best`).  
The following numeric meta fields can be used with comparisons ``, `>=`, `=` (equals), `!=` (not equals):  
- `filesize`: The number of bytes, if known in advance
- `filesize_approx`: An estimate for the number of bytes
- `width`: Width of the video, if known
- `height`: Height of the video, if known
- `aspect_ratio`: Aspect ratio of the video, if known
- `tbr`: Average bitrate of audio and video in kbps
- `abr`: Average audio bitrate in kbps
- `vbr`: Average video bitrate in kbps
- `asr`: Audio sampling rate in Hertz
- `fps`: Frame rate
- `audio_channels`: The number of audio channels
- `stretched_ratio`: `width:height` of the video's pixels, if not square  
Also filtering work for comparisons `=` (equals), `^=` (starts with), `$=` (ends with), `*=` (contains), `~=` (matches regex) and following string meta fields:  
- `url`: Video URL
- `ext`: File extension
- `acodec`: Name of the audio codec in use
- `vcodec`: Name of the video codec in use
- `container`: Name of the container format
- `protocol`: The protocol that will be used for the actual download, lower-case (`http`, `https`, `rtsp`, `rtmp`, `rtmpe`, `mms`, `f4m`, `ism`, `http_dash_segments`, `m3u8`, or `m3u8_native`)
- `language`: Language code
- `dynamic_range`: The dynamic range of the video
- `format_id`: A short description of the format
- `format`: A human-readable description of the format
- `format_note`: Additional info about the format
- `resolution`: Textual description of width and height  
Any string comparison may be prefixed with negation `!` in order to produce an opposite comparison, e.g. `!*=` (does not contain). The comparand of a string comparison needs to be quoted with either double or single quotes if it contains spaces or special characters other than `._-`.  
**Note**: None of the aforementioned meta fields are guaranteed to be present since this solely depends on the metadata obtained by the particular extractor, i.e. the metadata offered by the website. Any other field made available by the extractor can also be used for filtering.  
Formats for which the value is not known are excluded unless you put a question mark (`?`) after the operator. You can combine format filters, so `-f "bv[height500]"` selects up to 720p videos (or videos where the height is not known) with a bitrate of at least 500 kbps. You can also use the filters with `all` to download all formats that satisfy the filter, e.g. `-f "all[vcodec=none]"` selects all audio-only formats.  
Format selectors can also be grouped using parentheses; e.g. `-f "(mp4,webm)[height<480]"` will download the best pre-merged mp4 and webm formats with a height lower than 480.