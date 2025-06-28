---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308766
forks: 50890
watchers: 308766
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Application layer
Header 3: Service Discovery
---
Systems such as Consul, Etcd, and Zookeeper can help services find each other by keeping track of registered names, addresses, and ports.  Health checks help verify service integrity and are often done using an HTTP endpoint.  Both Consul and Etcd have a built in key-value store that can be useful for storing config values and other shared data.