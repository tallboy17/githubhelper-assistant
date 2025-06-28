---
repo: donnemartin/system-design-primer
readme_filename: donnemartin_system-design-primer_README.md
stars: 308792
forks: 50893
watchers: 308792
contributors_count: 113
license: NOASSERTION
Header 1: The System Design Primer
Header 2: Domain name system
---



Source: DNS security presentation
  
A Domain Name System (DNS) translates a domain name such as www.example.com to an IP address.  
DNS is hierarchical, with a few authoritative servers at the top level.  Your router or ISP provides information about which DNS server(s) to contact when doing a lookup.  Lower level DNS servers cache mappings, which could become stale due to DNS propagation delays.  DNS results can also be cached by your browser or OS for a certain period of time, determined by the time to live (TTL).  
* **NS record (name server)** - Specifies the DNS servers for your domain/subdomain.
* **MX record (mail exchange)** - Specifies the mail servers for accepting messages.
* **A record (address)** - Points a name to an IP address.
* **CNAME (canonical)** - Points a name to another name or `CNAME` (example.com to www.example.com) or to an `A` record.  
Services such as CloudFlare and Route 53 provide managed DNS services.  Some DNS services can route traffic through various methods:  
* Weighted round robin
* Prevent traffic from going to servers under maintenance
* Balance between varying cluster sizes
* A/B testing
* Latency-based
* Geolocation-based