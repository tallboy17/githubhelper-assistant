---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308792
forks: 50893
watchers: 308792
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Communication
Header 3: User datagram protocol (UDP)
---



Source: How to make a multiplayer game
  
UDP is connectionless.  Datagrams (analogous to packets) are guaranteed only at the datagram level.  Datagrams might reach their destination out of order or not at all.  UDP does not support congestion control.  Without the guarantees that TCP support, UDP is generally more efficient.  
UDP can broadcast, sending datagrams to all devices on the subnet.  This is useful with DHCP because the client has not yet received an IP address, thus preventing a way for TCP to stream without the IP address.  
UDP is less reliable but works well in real time use cases such as VoIP, video chat, streaming, and realtime multiplayer games.  
Use UDP over TCP when:  
* You need the lowest latency
* Late data is worse than loss of data
* You want to implement your own error correction  
#### Source(s) and further reading: TCP and UDP  
* Networking for game programming
* Key differences between TCP and UDP protocols
* Difference between TCP and UDP
* Transmission control protocol
* User datagram protocol
* Scaling memcache at Facebook