---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308792
forks: 50893
watchers: 308792
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Database
Header 3: SQL or NoSQL
---



Source: Transitioning from RDBMS to NoSQL
  
Reasons for **SQL**:  
* Structured data
* Strict schema
* Relational data
* Need for complex joins
* Transactions
* Clear patterns for scaling
* More established: developers, community, code, tools, etc
* Lookups by index are very fast  
Reasons for **NoSQL**:  
* Semi-structured data
* Dynamic or flexible schema
* Non-relational data
* No need for complex joins
* Store many TB (or PB) of data
* Very data intensive workload
* Very high throughput for IOPS  
Sample data well-suited for NoSQL:  
* Rapid ingest of clickstream and log data
* Leaderboard or scoring data
* Temporary data, such as a shopping cart
* Frequently accessed ('hot') tables
* Metadata/lookup tables  
##### Source(s) and further reading: SQL or NoSQL  
* Scaling up to your first 10 million users
* SQL vs NoSQL differences