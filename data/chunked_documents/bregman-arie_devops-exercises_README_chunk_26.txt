---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Ceph
---

Explain what is Ceph
Ceph is an Open-Source Distributed Storage System designed to provide excellent performance, reliability, and scalability. It's often used in cloud computing environments and Data Centers.
  

True or False? Ceph favor consistency and correctness over performances
True
  

Which services or types of storage Ceph supports?  
* Object (RGW)
* Block (RBD)
* File (CephFS)
  

What is RADOS?  
* Reliable Autonomic Distributed Object Storage
* Provides low-level data object storage service
* Strong Consistency
* Simplifies design and implementation of higher layers (block, file, object)
  

Describe RADOS software components  
* Monitor
* Central authority for authentication, data placement, policy
* Coordination point for all other cluster components
* Protect critical cluster state with Paxos
* Manager
* Aggregates real-time metrics (throughput, disk usage, etc.)
* Host for pluggable management functions
* 1 active, 1+ standby per cluster
* OSD (Object Storage Daemon)
* Stores data on an HDD or SSD
* Services client IO requests
  

What is the workflow of retrieving data from Ceph?
The work flow is as follows:  
1. The client sends a request to the ceph cluster to retrieve data:
> **Client could be any of the following**
>> * Ceph Block Device
>> * Ceph Object Gateway
>> * Any third party ceph client  
2. The client retrieves the latest cluster map from the Ceph Monitor
3. The client uses the CRUSH algorithm to map the object to a placement group. The placement group is then assigned to a OSD.
4. Once the placement group and the OSD Daemon are determined, the client can retrieve the data from the appropriate OSD  
  

What is the workflow of writing data to Ceph?
The work flow is as follows:  
1. The client sends a request to the ceph cluster to retrieve data
2. The client retrieves the latest cluster map from the Ceph Monitor
3. The client uses the CRUSH algorithm to map the object to a placement group. The placement group is then assigned to a Ceph OSD Daemon dynamically.
4. The client sends the data to the primary OSD of the determined placement group. If the data is stored in an erasure-coded pool, the primary OSD is responsible for encoding the object into data chunks and coding chunks, and distributing them to the other OSDs.  
  

What are "Placement Groups"?
  

Describe in the detail the following: Objects -> Pool -> Placement Groups -> OSDs
  

What is OMAP?
  

What is a metadata server? How it works?
