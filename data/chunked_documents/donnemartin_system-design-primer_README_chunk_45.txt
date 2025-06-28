---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308766
forks: 50890
watchers: 308766
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Availability patterns
Header 3: Fail-over
---
#### Active-passive  
With active-passive fail-over, heartbeats are sent between the active and the passive server on standby.  If the heartbeat is interrupted, the passive server takes over the active's IP address and resumes service.  
The length of downtime is determined by whether the passive server is already running in 'hot' standby or whether it needs to start up from 'cold' standby.  Only the active server handles traffic.  
Active-passive failover can also be referred to as master-slave failover.  
#### Active-active  
In active-active, both servers are managing traffic, spreading the load between them.  
If the servers are public-facing, the DNS would need to know about the public IPs of both servers.  If the servers are internal-facing, application logic would need to know about both servers.  
Active-active failover can also be referred to as master-master failover.