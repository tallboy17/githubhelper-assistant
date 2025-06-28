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
Header 3: Eventual consistency
---
After a write, reads will eventually see it (typically within milliseconds).  Data is replicated asynchronously.  
This approach is seen in systems such as DNS and email.  Eventual consistency works well in highly available systems.