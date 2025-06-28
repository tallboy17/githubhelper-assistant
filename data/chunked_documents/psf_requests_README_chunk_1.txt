---
repo: psf/requests
readme_filename: psf_requests_README.md
stars: 52990
forks: 9493
watchers: 52990
contributors_count: 402
license: Apache-2.0
Header 1: Requests
---
**Requests** is a simple, yet elegant, HTTP library.  
```python
>>> import requests
>>> r = requests.get(' auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
'{"authenticated": true, ...'
>>> r.json()
{'authenticated': True, ...}
```  
Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your `PUT` & `POST` data — but nowadays, just use the `json` method!  
Requests is one of the most downloaded Python packages today, pulling in around `30M downloads / week`— according to GitHub, Requests is currently depended upon by `1,000,000+` repositories. You may certainly put your trust in this code.  
![Downloads](
![Supported Versions](
![Contributors](