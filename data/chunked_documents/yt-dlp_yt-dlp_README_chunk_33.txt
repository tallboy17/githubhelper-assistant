---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: CONFIGURATION
---
You can configure yt-dlp by placing any supported command line option in a configuration file. The configuration is loaded from the following locations:  
1. **Main Configuration**:
* The file given to `--config-location`
1. **Portable Configuration**: (Recommended for portable installations)
* If using a binary, `yt-dlp.conf` in the same directory as the binary
* If running from source-code, `yt-dlp.conf` in the parent directory of `yt_dlp`
1. **Home Configuration**:
* `yt-dlp.conf` in the home path given to `-P`
* If `-P` is not given, the current directory is searched
1. **User Configuration**:
* `${XDG_CONFIG_HOME}/yt-dlp.conf`
* `${XDG_CONFIG_HOME}/yt-dlp/config` (recommended on Linux/macOS)
* `${XDG_CONFIG_HOME}/yt-dlp/config.txt`
* `${APPDATA}/yt-dlp.conf`
* `${APPDATA}/yt-dlp/config` (recommended on Windows)
* `${APPDATA}/yt-dlp/config.txt`
* `~/yt-dlp.conf`
* `~/yt-dlp.conf.txt`
* `~/.yt-dlp/config`
* `~/.yt-dlp/config.txt`  
See also: Notes about environment variables
1. **System Configuration**:
* `/etc/yt-dlp.conf`
* `/etc/yt-dlp/config`
* `/etc/yt-dlp/config.txt`  
E.g. with the following configuration file, yt-dlp will always extract the audio, not copy the mtime, use a proxy and save all videos under `YouTube` directory in your home directory:
```
# Lines starting with # are comments

# Always extract audio
-x

# Do not copy the mtime
--no-mtime

# Use this proxy
--proxy 127.0.0.1:3128

# Save all videos under YouTube directory in your home directory
-o ~/YouTube/%(title)s.%(ext)s
```  
**Note**: Options in a configuration file are just the same options aka switches used in regular command line calls; thus there **must be no whitespace** after `-` or `--`, e.g. `-o` or `--proxy` but not `- o` or `-- proxy`. They must also be quoted when necessary, as if it were a UNIX shell.  
You can use `--ignore-config` if you want to disable all configuration files for a particular yt-dlp run. If `--ignore-config` is found inside any configuration file, no further configuration will be loaded. For example, having the option in the portable configuration file prevents loading of home, user, and system configurations. Additionally, (for backward compatibility) if `--ignore-config` is found inside the system configuration file, the user configuration is not loaded.