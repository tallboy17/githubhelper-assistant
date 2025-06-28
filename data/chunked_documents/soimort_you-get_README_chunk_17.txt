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
Header 3: Proxy settings
---
You may specify an HTTP proxy for `you-get` to use, via the `--http-proxy`/`-x` option:  
```
$ you-get -x 127.0.0.1:8087 '
```  
However, the system proxy setting (i.e. the environment variable `http_proxy`) is applied by default. To disable any proxy, use the `--no-proxy` option.  
**Tips:**  
* If you need to use proxies a lot (in case your network is blocking certain sites), you might want to use `you-get` with proxychains and set `alias you-get="proxychains -q you-get"` (in Bash).
* For some websites (e.g. Youku), if you need access to some videos that are only available in mainland China, there is an option of using a specific proxy to extract video information from the site: `--extractor-proxy`/`-y`.