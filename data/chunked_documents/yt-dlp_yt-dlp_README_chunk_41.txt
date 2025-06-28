---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: FORMAT SELECTION
Header 2: Format Selection examples
---
```bash
# Download and merge the best video-only format and the best audio-only format,
# or download the best combined format if video-only format is not available
$ yt-dlp -f "bv+ba/b"

# Download best format that contains video,
# and if it doesn't already have an audio stream, merge it with best audio-only format
$ yt-dlp -f "bv*+ba/b"

# Same as above
$ yt-dlp

# Download the best video-only format and the best audio-only format without merging them
# For this case, an output template should be used since
# by default, bestvideo and bestaudio will have the same file name.
$ yt-dlp -f "bv,ba" -o "%(title)s.f%(format_id)s.%(ext)s"

# Download and merge the best format that has a video stream,
# and all audio-only formats into one file
$ yt-dlp -f "bv*+mergeall[vcodec=none]" --audio-multistreams

# Download and merge the best format that has a video stream,
# and the best 2 audio-only formats into one file
$ yt-dlp -f "bv*+ba+ba.2" --audio-multistreams


# The following examples show the old method (without -S) of format selection
# and how to use -S to achieve a similar but (generally) better result

# Download the worst video available (old method)
$ yt-dlp -f "wv*+wa/w"

# Download the best video available but with the smallest resolution
$ yt-dlp -S "+res"

# Download the smallest video available
$ yt-dlp -S "+size,+br"



# Download the best mp4 video available, or the best video if no mp4 available
$ yt-dlp -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b"

# Download the best video with the best extension
# (For video, mp4 > mov > webm > flv. For audio, m4a > aac > mp3 ...)
$ yt-dlp -S "ext"



# Download the best video available but no better than 480p,
# or the worst video if there is no video under 480p
$ yt-dlp -f "bv*[height http/ftp > m3u8_native > m3u8 > http_dash_segments ...)
$ yt-dlp -S "proto"



# Download the best video with either h264 or h265 codec,
# or the best video if there is no such video
$ yt-dlp -f "(bv*[vcodec~='^((he|a)vc|h26[45])']+ba) / (bv*+ba/b)"

# Download the best video with best codec no better than h264,
# or the best video with worst codec if there is no such video
$ yt-dlp -S "codec:h264"

# Download the best video with worst codec no worse than h264,
# or the best video with best codec if there is no such video
$ yt-dlp -S "+codec:h264"



# More complex examples

# Download the best video no better than 720p preferring framerate greater than 30,
# or the worst video (still preferring framerate greater than 30) if there is no such video
$ yt-dlp -f "((bv*[fps>30]/bv*)[height30]/wv*)) + ba / (b[fps>30]/b)[height30]/w)"

# Download the video with the largest resolution no better than 720p,
# or the video with the smallest resolution available if there is no such video,
# preferring larger framerate for formats with the same resolution
$ yt-dlp -S "res:720,fps"



# Download the video with smallest resolution no worse than 480p,
# or the video with the largest resolution available if there is no such video,
# preferring better codec and then larger total bitrate for the same resolution
$ yt-dlp -S "+res:480,codec,br"
```