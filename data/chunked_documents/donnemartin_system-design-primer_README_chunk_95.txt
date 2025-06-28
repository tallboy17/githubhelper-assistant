---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308766
forks: 50890
watchers: 308766
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Communication
Header 3: Transmission control protocol (TCP)
---



Source: How to make a multiplayer game
  
TCP is a connection-oriented protocol over an IP network.  Connection is established and terminated using a handshake.  All packets sent are guaranteed to reach the destination in the original order and without corruption through:  
* Sequence numbers and checksum fields for each packet
* Acknowledgement) packets and automatic retransmission  
If the sender does not receive a correct response, it will resend the packets.  If there are multiple timeouts, the connection is dropped.  TCP also implements flow control) and congestion control.  These guarantees cause delays and generally result in less efficient transmission than UDP.  
To ensure high throughput, web servers can keep a large number of TCP connections open, resulting in high memory usage.  It can be expensive to have a large number of open connections between web server threads and say, a memcached server.  Connection pooling can help in addition to switching to UDP where applicable.  
TCP is useful for applications that require high reliability but are less time critical.  Some examples include web servers, database info, SMTP, FTP, and SSH.  
Use TCP over UDP when:  
* You need all of the data to arrive intact
* You want to automatically make a best estimate use of the network throughput