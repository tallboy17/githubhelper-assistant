---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308766
forks: 50890
watchers: 308766
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Cache
Header 3: Caching at the database query level
---
Whenever you query the database, hash the query as a key and store the result to the cache.  This approach suffers from expiration issues:  
* Hard to delete a cached result with complex queries
* If one piece of data changes such as a table cell, you need to delete all cached queries that might include the changed cell