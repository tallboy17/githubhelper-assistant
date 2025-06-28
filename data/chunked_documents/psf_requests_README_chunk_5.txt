---
repo: psf/requests
readme_filename: psf_requests_README.md
stars: 52990
forks: 9493
watchers: 52990
contributors_count: 402
license: Apache-2.0
Header 1: Requests
Header 2: Cloning the repository
---
When cloning the Requests repository, you may need to add the `-c
fetch.fsck.badTimezone=ignore` flag to avoid an error about a bad commit timestamp (see
this issue for more background):  
```shell
git clone -c fetch.fsck.badTimezone=ignore 
```  
You can also apply this setting to your global Git config:  
```shell
git config --global fetch.fsck.badTimezone ignore
```  
---  
![Kenneth Reitz]( ![Python Software Foundation](