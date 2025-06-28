---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: PLUGINS
Header 2: Developing Plugins
---
See the yt-dlp-sample-plugins repo for a template plugin package and the Plugin Development section of the wiki for a plugin development guide.  
All public classes with a name ending in `IE`/`PP` are imported from each file for extractors and postprocessors respectively. This respects underscore prefix (e.g. `_MyBasePluginIE` is private) and `__all__`. Modules can similarly be excluded by prefixing the module name with an underscore (e.g. `_myplugin.py`).  
To replace an existing extractor with a subclass of one, set the `plugin_name` class keyword argument (e.g. `class MyPluginIE(ABuiltInIE, plugin_name='myplugin')` will replace `ABuiltInIE` with `MyPluginIE`). Since the extractor replaces the parent, you should exclude the subclass extractor from being imported separately by making it private using one of the methods described above.  
If you are a plugin author, add yt-dlp-plugins as a topic to your repository for discoverability.  
See the Developer Instructions on how to write and test an extractor.