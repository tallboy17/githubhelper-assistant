---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308792
forks: 50893
watchers: 308792
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Reverse proxy (web server)
Header 3: Disadvantage(s): reverse proxy
---
* Introducing a reverse proxy results in increased complexity.
* A single reverse proxy is a single point of failure, configuring multiple reverse proxies (ie a failover) further increases complexity.