---
repo: ytdl-org/youtube-dl
readme_filename: ytdl-org_youtube-dl_README.md
stars: 136243
forks: 10379
watchers: 136243
contributors_count: 388
license: Unlicense
Header 1: FAQ
Header 3: HTTP Error 429: Too Many Requests or 402: Payment Required
---
These two error codes indicate that the service is blocking your IP address because of overuse. Usually this is a soft block meaning that you can gain access again after solving CAPTCHA. Just open a browser and solve a CAPTCHA the service suggests you and after that pass cookies to youtube-dl. Note that if your machine has multiple external IPs then you should also pass exactly the same IP you've used for solving CAPTCHA with `--source-address`. Also you may need to pass a `User-Agent` HTTP header of your browser with `--user-agent`.  
If this is not the case (no CAPTCHA suggested to solve by the service) then you can contact the service and ask them to unblock your IP address, or - if you have acquired a whitelisted IP address already - use the `--proxy` or `--source-address` options to select another IP address.