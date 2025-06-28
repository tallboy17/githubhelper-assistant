---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: INSTALLATION
Header 2: DEPENDENCIES
Header 3: Networking
---
* **certifi**\* - Provides Mozilla's root certificate bundle. Licensed under MPLv2
* **brotli**\* or **brotlicffi** - Brotli content encoding support. Both licensed under MIT 1 2 
* **websockets**\* - For downloading over websocket. Licensed under BSD-3-Clause
* **requests**\* - HTTP library. For HTTPS proxy and persistent connections support. Licensed under Apache-2.0  
#### Impersonation  
The following provide support for impersonating browser requests. This may be required for some sites that employ TLS fingerprinting.  
* **curl_cffi** (recommended) - Python binding for curl-impersonate. Provides impersonation targets for Chrome, Edge and Safari. Licensed under MIT
* Can be installed with the `curl-cffi` group, e.g. `pip install "yt-dlp[default,curl-cffi]"`
* Currently included in `yt-dlp.exe`, `yt-dlp_linux` and `yt-dlp_macos` builds