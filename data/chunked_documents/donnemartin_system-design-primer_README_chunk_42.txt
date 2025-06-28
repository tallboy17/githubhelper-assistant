---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308792
forks: 50893
watchers: 308792
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Consistency patterns
Header 3: Strong consistency
---
After a write, reads will see it.  Data is replicated synchronously.  
This approach is seen in file systems and RDBMSes.  Strong consistency works well in systems that need transactions.