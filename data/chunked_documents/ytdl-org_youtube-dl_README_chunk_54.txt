---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: DEVELOPER INSTRUCTIONS
Header 2: youtube-dl coding conventions
---
This section introduces guidelines for writing idiomatic, robust and future-proof extractor code.  
Extractors are very fragile by nature since they depend on the layout of the source data provided by 3rd party media hosters out of your control and this layout tends to change. As an extractor implementer your task is not only to write code that will extract media links and metadata correctly but also to minimize dependency on the source's layout and even to make the code foresee potential future changes and be ready for that. This is important because it will allow the extractor not to break on minor layout changes thus keeping old youtube-dl versions working. Even though this breakage issue is easily fixed by emitting a new version of youtube-dl with a fix incorporated, all the previous versions become broken in all repositories and distros' packages that may not be so prompt in fetching the update from us. Needless to say, some non rolling release distros may never receive an update at all.