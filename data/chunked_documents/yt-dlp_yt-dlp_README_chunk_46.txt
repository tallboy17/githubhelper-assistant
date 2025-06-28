---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: PLUGINS
Header 2: Installing Plugins
---
Plugins can be installed using various methods and locations.  
1. **Configuration directories**:
Plugin packages (containing a `yt_dlp_plugins` namespace folder) can be dropped into the following standard configuration locations:
* **User Plugins**
* `${XDG_CONFIG_HOME}/yt-dlp/plugins//yt_dlp_plugins/` (recommended on Linux/macOS)
* `${XDG_CONFIG_HOME}/yt-dlp-plugins//yt_dlp_plugins/`
* `${APPDATA}/yt-dlp/plugins//yt_dlp_plugins/` (recommended on Windows)
* `${APPDATA}/yt-dlp-plugins//yt_dlp_plugins/`
* `~/.yt-dlp/plugins//yt_dlp_plugins/`
* `~/yt-dlp-plugins//yt_dlp_plugins/`
* **System Plugins**
* `/etc/yt-dlp/plugins//yt_dlp_plugins/`
* `/etc/yt-dlp-plugins//yt_dlp_plugins/`
2. **Executable location**: Plugin packages can similarly be installed in a `yt-dlp-plugins` directory under the executable location (recommended for portable installations):
* Binary: where `/yt-dlp.exe`, `/yt-dlp-plugins//yt_dlp_plugins/`
* Source: where `/yt_dlp/__main__.py`, `/yt-dlp-plugins//yt_dlp_plugins/`  
3. **pip and other locations in `PYTHONPATH`**
* Plugin packages can be installed and managed using `pip`. See yt-dlp-sample-plugins for an example.
* Note: plugin files between plugin packages installed with pip must have unique filenames.
* Any path in `PYTHONPATH` is searched in for the `yt_dlp_plugins` namespace folder.
* Note: This does not apply for Pyinstaller builds.  
`.zip`, `.egg` and `.whl` archives containing a `yt_dlp_plugins` namespace folder in their root are also supported as plugin packages.  
* e.g. `${XDG_CONFIG_HOME}/yt-dlp/plugins/mypluginpkg.zip` where `mypluginpkg.zip` contains `yt_dlp_plugins//myplugin.py`  
Run yt-dlp with `--verbose` to check if the plugin has been loaded.