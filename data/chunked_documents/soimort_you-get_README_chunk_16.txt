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
Header 3: Set the path and name of downloaded file
---
Use the `--output-dir`/`-o` option to set the path, and `--output-filename`/`-O` to set the name of the downloaded file:  
```
$ you-get -o ~/Videos -O zoo.webm '
```  
**Tips:**  
* These options are helpful if you encounter problems with the default video titles, which may contain special characters that do not play well with your current shell / operating system / filesystem.
* These options are also helpful if you write a script to batch download files and put them into designated folders with designated names.