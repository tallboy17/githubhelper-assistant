---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308766
forks: 50890
watchers: 308766
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Reverse proxy (web server)
---



Source: Wikipedia

  
A reverse proxy is a web server that centralizes internal services and provides unified interfaces to the public.  Requests from clients are forwarded to a server that can fulfill it before the reverse proxy returns the server's response to the client.  
Additional benefits include:  
* **Increased security** - Hide information about backend servers, blacklist IPs, limit number of connections per client
* **Increased scalability and flexibility** - Clients only see the reverse proxy's IP, allowing you to scale servers or change their configuration
* **SSL termination** - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations
* Removes the need to install X.509 certificates on each server
* **Compression** - Compress server responses
* **Caching** - Return the response for cached requests
* **Static content** - Serve static content directly
* HTML/CSS/JS
* Photos
* Videos
* Etc