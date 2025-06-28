---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Big Data
---

Explain what is exactly Big Data  
As defined by Doug Laney:  
* Volume: Extremely large volumes of data
* Velocity: Real time, batch, streams of data
* Variety: Various forms of data, structured, semi-structured and unstructured
* Veracity or Variability: Inconsistent, sometimes inaccurate, varying data
  

What is DataOps? How is it related to DevOps?  
DataOps seeks to reduce the end-to-end cycle time of data analytics, from the origin of ideas to the literal creation of charts, graphs and models that create value.
DataOps combines Agile development, DevOps and statistical process controls and applies them to data analytics.
  

What is Data Architecture?  
An answer from talend.com:  
"Data architecture is the process of standardizing how organizations collect, store, transform, distribute, and use data. The goal is to deliver relevant data to people who need it, when they need it, and help them make sense of it."
  

Explain the different formats of data  
* Structured - data that has defined format and length (e.g. numbers, words)
* Semi-structured - Doesn't conform to a specific format but is self-describing (e.g. XML, SWIFT)
* Unstructured - does not follow a specific format (e.g. images, test messages)
  

What is a Data Warehouse?  
Wikipedia's explanation on Data Warehouse
Amazon's explanation on Data Warehouse
  

What is Data Lake?  
Data Lake - Wikipedia
  

Can you explain the difference between a data lake and a data warehouse?
  

What is "Data Versioning"? What models of "Data Versioning" are there?
  

What is ETL?
  
#### Apache Hadoop  

Explain what is Hadoop  
Apache Hadoop - Wikipedia
  

Explain Hadoop YARN  
Responsible for managing the compute resources in clusters and scheduling users' applications
  

Explain Hadoop MapReduce  
A programming model for large-scale data processing
  

Explain Hadoop Distributed File Systems (HDFS)  
* Distributed file system providing high aggregate bandwidth across the cluster.
* For a user it looks like a regular file system structure but behind the scenes it's distributed across multiple machines in a cluster
* Typical file size is TB and it can scale and supports millions of files
* It's fault tolerant which means it provides automatic recovery from faults
* It's best suited for running long batch operations rather than live analysis
  

What do you know about HDFS architecture?  
HDFS Architecture  
* Master-slave architecture
* Namenode - master, Datanodes - slaves
* Files split into blocks
* Blocks stored on datanodes
* Namenode controls all metadata
