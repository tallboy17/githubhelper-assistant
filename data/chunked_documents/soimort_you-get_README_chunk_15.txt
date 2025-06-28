---
repo: soimort/you-get
readme_filename: soimort_you-get_README.md
stars: 55790
forks: 9764
watchers: 55790
contributors_count: 226
license: NOASSERTION
Header 1: You-Get
Header 2: Getting Started
Header 3: Pause and resume a download
---
You may use Ctrl+C to interrupt a download.  
A temporary `.download` file is kept in the output directory. Next time you run `you-get` with the same arguments, the download progress will resume from the last session. In case the file is completely downloaded (the temporary `.download` extension is gone), `you-get` will just skip the download.  
To enforce re-downloading, use the `--force`/`-f` option. (**Warning:** doing so will overwrite any existing file or temporary file with the same name!)