---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: INSTALLATION
Header 2: COMPILE
Header 3: Related scripts
---
* **`devscripts/install_deps.py`** - Install dependencies for yt-dlp.
* **`devscripts/update-version.py`** - Update the version number based on the current date.
* **`devscripts/set-variant.py`** - Set the build variant of the executable.
* **`devscripts/make_changelog.py`** - Create a markdown changelog using short commit messages and update `CONTRIBUTORS` file.
* **`devscripts/make_lazy_extractors.py`** - Create lazy extractors. Running this before building the binaries (any variant) will improve their startup performance. Set the environment variable `YTDLP_NO_LAZY_EXTRACTORS` to something nonempty to forcefully disable lazy extractor loading.  
Note: See their `--help` for more info.