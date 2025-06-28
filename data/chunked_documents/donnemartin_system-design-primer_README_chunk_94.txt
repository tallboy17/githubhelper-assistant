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
Header 3: Hypertext transfer protocol (HTTP)
---
HTTP is a method for encoding and transporting data between a client and a server.  It is a request/response protocol: clients issue requests and servers issue responses with relevant content and completion status info about the request.  HTTP is self-contained, allowing requests and responses to flow through many intermediate routers and servers that perform load balancing, caching, encryption, and compression.  
A basic HTTP request consists of a verb (method) and a resource (endpoint).  Below are common HTTP verbs:  
| Verb | Description | Idempotent* | Safe | Cacheable |
|---|---|---|---|---|
| GET | Reads a resource | Yes | Yes | Yes |
| POST | Creates a resource or trigger a process that handles data | No | No | Yes if response contains freshness info |
| PUT | Creates or replace a resource | Yes | No | No |
| PATCH | Partially updates a resource | No | No | Yes if response contains freshness info |
| DELETE | Deletes a resource | Yes | No | No |  
*Can be called many times without different outcomes.  
HTTP is an application layer protocol relying on lower-level protocols such as **TCP** and **UDP**.  
#### Source(s) and further reading: HTTP  
* What is HTTP?
* Difference between HTTP and TCP
* Difference between PUT and PATCH