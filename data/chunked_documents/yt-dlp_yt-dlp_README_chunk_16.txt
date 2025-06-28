---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: USAGE AND OPTIONS
Header 2: General Options:
---
-h, --help                      Print this help text and exit
--version                       Print program version and exit
-U, --update                    Update this program to the latest version
--no-update                     Do not check for updates (default)
--update-to [CHANNEL]@[TAG]     Upgrade/downgrade to a specific version.
CHANNEL can be a repository as well. CHANNEL
and TAG default to "stable" and "latest"
respectively if omitted; See "UPDATE" for
details. Supported channels: stable,
nightly, master
-i, --ignore-errors             Ignore download and postprocessing errors.
The download will be considered successful
even if the postprocessing fails
--no-abort-on-error             Continue with next video on download errors;
e.g. to skip unavailable videos in a
playlist (default)
--abort-on-error                Abort downloading of further videos if an
error occurs (Alias: --no-ignore-errors)
--dump-user-agent               Display the current user-agent and exit
--list-extractors               List all supported extractors and exit
--extractor-descriptions        Output descriptions of all supported
extractors and exit
--use-extractors NAMES          Extractor names to use separated by commas.
You can also use regexes, "all", "default"
and "end" (end URL matching); e.g. --ies
"holodex.*,end,youtube". Prefix the name
with a "-" to exclude it, e.g. --ies
default,-generic. Use --list-extractors for
a list of extractor names. (Alias: --ies)
--default-search PREFIX         Use this prefix for unqualified URLs. E.g.
"gvsearch2:python" downloads two videos from
google videos for the search term "python".
Use the value "auto" to let yt-dlp guess
("auto_warning" to emit a warning when
guessing). "error" just throws an error. The
default value "fixup_error" repairs broken
URLs, but emits an error if this is not
possible instead of searching
--ignore-config                 Don't load any more configuration files
except those given to --config-locations.
For backward compatibility, if this option
is found inside the system configuration
file, the user configuration is not loaded.
(Alias: --no-config)
--no-config-locations           Do not load any custom configuration files
(default). When given inside a configuration
file, ignore all previous --config-locations
defined in the current file
--config-locations PATH         Location of the main configuration file;
either the path to the config or its
containing directory ("-" for stdin). Can be
used multiple times and inside other
configuration files
--plugin-dirs PATH              Path to an additional directory to search
for plugins. This option can be used
multiple times to add multiple directories.
Use "default" to search the default plugin
directories (default)
--no-plugin-dirs                Clear plugin directories to search,
including defaults and those provided by
previous --plugin-dirs
--flat-playlist                 Do not extract a playlist's URL result
entries; some entry metadata may be missing
and downloading may be bypassed
--no-flat-playlist              Fully extract the videos of a playlist
(default)
--live-from-start               Download livestreams from the start.
Currently experimental and only supported
for YouTube and Twitch
--no-live-from-start            Download livestreams from the current time
(default)
--wait-for-video MIN[-MAX]      Wait for scheduled streams to become
available. Pass the minimum number of
seconds (or range) to wait between retries
--no-wait-for-video             Do not wait for scheduled streams (default)
--mark-watched                  Mark videos watched (even with --simulate)
--no-mark-watched               Do not mark videos watched (default)
--color [STREAM:]POLICY         Whether to emit color codes in output,
optionally prefixed by the STREAM (stdout or
stderr) to apply the setting to. Can be one
of "always", "auto" (default), "never", or
"no_color" (use non color terminal
sequences). Use "auto-tty" or "no_color-tty"
to decide based on terminal support only.
Can be used multiple times
--compat-options OPTS           Options that can help keep compatibility
with youtube-dl or youtube-dlc
configurations by reverting some of the
changes made in yt-dlp. See "Differences in
default behavior" for details
--alias ALIASES OPTIONS         Create aliases for an option string. Unless
an alias starts with a dash "-", it is
prefixed with "--". Arguments are parsed
according to the Python string formatting
mini-language. E.g. --alias get-audio,-X "-S
aext:{0},abr -x --audio-format {0}" creates
options "--get-audio" and "-X" that takes an
argument (ARG0) and expands to "-S
aext:ARG0,abr -x --audio-format ARG0". All
defined aliases are listed in the --help
output. Alias options can trigger more
aliases; so be careful to avoid defining
recursive options. As a safety measure, each
alias may be triggered a maximum of 100
times. This option can be used multiple times
-t, --preset-alias PRESET       Applies a predefined set of options. e.g.
--preset-alias mp3. The following presets
are available: mp3, aac, mp4, mkv, sleep.
See the "Preset Aliases" section at the end
for more info. This option can be used
multiple times