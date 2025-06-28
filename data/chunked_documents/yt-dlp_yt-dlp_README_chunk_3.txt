---
repo: yt-dlp/yt-dlp
readme_filename: yt-dlp_yt-dlp_README.md
stars: 116704
forks: 9228
watchers: 116704
contributors_count: 385
license: Unlicense
Header 1: INSTALLATION
Header 2: RELEASE FILES
---
#### Recommended  
File|Description
:---|:---
yt-dlp|Platform-independent zipimport binary. Needs Python (recommended for **Linux/BSD**)
yt-dlp.exe|Windows (Win8+) standalone x64 binary (recommended for **Windows**)
yt-dlp_macos|Universal MacOS (10.15+) standalone executable (recommended for **MacOS**)  
#### Alternatives  
File|Description
:---|:---
yt-dlp_x86.exe|Windows (Win8+) standalone x86 (32-bit) binary
yt-dlp_linux|Linux standalone x64 binary
yt-dlp_linux_armv7l|Linux standalone armv7l (32-bit) binary
yt-dlp_linux_aarch64|Linux standalone aarch64 (64-bit) binary
yt-dlp_win.zip|Unpackaged Windows executable (no auto-update)
yt-dlp_macos.zip|Unpackaged MacOS (10.15+) executable (no auto-update)
yt-dlp_macos_legacy|MacOS (10.9+) standalone x64 executable  
#### Misc  
File|Description
:---|:---
yt-dlp.tar.gz|Source tarball
SHA2-512SUMS|GNU-style SHA512 sums
SHA2-512SUMS.sig|GPG signature file for SHA512 sums
SHA2-256SUMS|GNU-style SHA256 sums
SHA2-256SUMS.sig|GPG signature file for SHA256 sums  
The public key that can be used to verify the GPG signatures is available here
Example usage:
```
curl -L  | gpg --import
gpg --verify SHA2-256SUMS.sig SHA2-256SUMS
gpg --verify SHA2-512SUMS.sig SHA2-512SUMS
```
  
**Note**: The manpages, shell completion (autocomplete) files etc. are available inside the source tarball