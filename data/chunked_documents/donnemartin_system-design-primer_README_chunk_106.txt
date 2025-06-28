---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308766
forks: 50890
watchers: 308766
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Appendix
Header 3: Real world architectures
---
> Articles on how real world systems are designed.  



Source: Twitter timelines at scale
  
**Don't focus on nitty gritty details for the following articles, instead:**  
* Identify shared principles, common technologies, and patterns within these articles
* Study what problems are solved by each component, where it works, where it doesn't
* Review the lessons learned  
|Type | System | Reference(s) |
|---|---|---|
| Data processing | **MapReduce** - Distributed data processing from Google | research.google.com |
| Data processing | **Spark** - Distributed data processing from Databricks | slideshare.net |
| Data processing | **Storm** - Distributed data processing from Twitter | slideshare.net |
| | | |
| Data store | **Bigtable** - Distributed column-oriented database from Google | harvard.edu |
| Data store | **HBase** - Open source implementation of Bigtable | slideshare.net |
| Data store | **Cassandra** - Distributed column-oriented database from Facebook | slideshare.net
| Data store | **DynamoDB** - Document-oriented database from Amazon | harvard.edu |
| Data store | **MongoDB** - Document-oriented database | slideshare.net |
| Data store | **Spanner** - Globally-distributed database from Google | research.google.com |
| Data store | **Memcached** - Distributed memory caching system | slideshare.net |
| Data store | **Redis** - Distributed memory caching system with persistence and value types | slideshare.net |
| | | |
| File system | **Google File System (GFS)** - Distributed file system | research.google.com |
| File system | **Hadoop File System (HDFS)** - Open source implementation of GFS | apache.org |
| | | |
| Misc | **Chubby** - Lock service for loosely-coupled distributed systems from Google | research.google.com |
| Misc | **Dapper** - Distributed systems tracing infrastructure | research.google.com
| Misc | **Kafka** - Pub/sub message queue from LinkedIn | slideshare.net |
| Misc | **Zookeeper** - Centralized infrastructure and services enabling synchronization | slideshare.net |
| | Add an architecture | Contribute |