---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: Video URL contains an ampersand and I'm getting some strange output `[1] 2839` or `'v' is not recognized as an internal or external command`
---
That's actually the output from your shell. Since ampersand is one of the special shell characters it's interpreted by the shell preventing you from passing the whole URL to youtube-dl. To disable your shell from interpreting the ampersands (or any other special characters) you have to either put the whole URL in quotes or escape them with a backslash (which approach will work depends on your shell).  
For example if your URL is  you should end up with following command:  
```youtube-dl '  
or  
```youtube-dl   
For Windows you have to use the double quotes:  
```youtube-dl "