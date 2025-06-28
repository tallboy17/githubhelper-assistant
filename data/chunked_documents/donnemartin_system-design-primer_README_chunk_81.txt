---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308792
forks: 50893
watchers: 308792
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Cache
Header 3: Application caching
---
In-memory caches such as Memcached and Redis are key-value stores between your application and your data storage.  Since the data is held in RAM, it is much faster than typical databases where data is stored on disk.  RAM is more limited than disk, so cache invalidation algorithms such as least recently used (LRU)) can help invalidate 'cold' entries and keep 'hot' data in RAM.  
Redis has the following additional features:  
* Persistence option
* Built-in data structures such as sorted sets and lists  
There are multiple levels you can cache that fall into two general categories: **database queries** and **objects**:  
* Row level
* Query-level
* Fully-formed serializable objects
* Fully-rendered HTML  
Generally, you should try to avoid file-based caching, as it makes cloning and auto-scaling more difficult.