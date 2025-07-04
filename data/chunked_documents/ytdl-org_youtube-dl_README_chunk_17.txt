---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: OPTIONS
Header 2: Post-processing Options:
---
-x, --extract-audio                  Convert video files to audio-only files
(requires ffmpeg/avconv and
ffprobe/avprobe)
--audio-format FORMAT                Specify audio format: "best", "aac",
"flac", "mp3", "m4a", "opus", "vorbis",
or "wav"; "best" by default; No effect
without -x
--audio-quality QUALITY              Specify ffmpeg/avconv audio quality,
insert a value between 0 (better) and 9
(worse) for VBR or a specific bitrate
like 128K (default 5)
--recode-video FORMAT                Encode the video to another format if
necessary (currently supported:
mp4|flv|ogg|webm|mkv|avi)
--postprocessor-args ARGS            Give these arguments to the
postprocessor
-k, --keep-video                     Keep the video file on disk after the
post-processing; the video is erased by
default
--no-post-overwrites                 Do not overwrite post-processed files;
the post-processed files are
overwritten by default
--embed-subs                         Embed subtitles in the video (only for
mp4, webm and mkv videos)
--embed-thumbnail                    Embed thumbnail in the audio as cover
art
--add-metadata                       Write metadata to the video file
--metadata-from-title FORMAT         Parse additional metadata like song
title / artist from the video title.
The format syntax is the same as
--output. Regular expression with named
capture groups may also be used. The
parsed parameters replace existing
values. Example: --metadata-from-title
"%(artist)s - %(title)s" matches a
title like "Coldplay - Paradise".
Example (regex): --metadata-from-title
"(?P.+?) - (?P.+)"
--xattrs                             Write metadata to the video file's
xattrs (using dublin core and xdg
standards)
--fixup POLICY                       Automatically correct known faults of
the file. One of never (do nothing),
warn (only emit a warning),
detect_or_warn (the default; fix file
if we can, warn otherwise)
--prefer-avconv                      Prefer avconv over ffmpeg for running
the postprocessors
--prefer-ffmpeg                      Prefer ffmpeg over avconv for running
the postprocessors (default)
--ffmpeg-location PATH               Location of the ffmpeg/avconv binary;
either the path to the binary or its
containing directory.
--exec CMD                           Execute a command on the file after
downloading and post-processing,
similar to find's -exec syntax.
Example: --exec 'adb push {}
/sdcard/Music/ && rm {}'
--convert-subs FORMAT                Convert the subtitles to other format
(currently supported: srt|ass|vtt|lrc)