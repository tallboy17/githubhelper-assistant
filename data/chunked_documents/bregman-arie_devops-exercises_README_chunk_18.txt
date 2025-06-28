---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: HTTP
---

What is HTTP?  
Avinetworks: HTTP stands for Hypertext Transfer Protocol. HTTP uses TCP port 80 to enable internet communication. It is part of the Application Layer (L7) in OSI Model.
  

Describe HTTP request lifecycle  
* Resolve host by request to DNS resolver
* Client SYN
* Server SYN+ACK
* Client SYN
* HTTP request
* HTTP response
  

True or False? HTTP is stateful  
False. It doesn't maintain state for incoming request.
  

How HTTP request looks like?  
It consists of:  
* Request line - request type
* Headers - content info like length, encoding, etc.
* Body (not always included)
  

What HTTP method types are there?  
* GET
* POST
* HEAD
* PUT
* DELETE
* CONNECT
* OPTIONS
* TRACE
  

What HTTP response codes are there?  
* 1xx - informational
* 2xx - Success
* 3xx - Redirect
* 4xx - Error, client fault
* 5xx - Error, server fault
  

What is HTTPS?  
HTTPS is a secure version of the HTTP protocol used to transfer data between a web browser and a web server. It encrypts the communication using SSL/TLS encryption to ensure that the data is private and secure.  
Learn more: 
  

Explain HTTP Cookies  
HTTP is stateless. To share state, we can use Cookies.  
TODO: explain what is actually a Cookie
  

What is HTTP Pipelining?
  

You get "504 Gateway Timeout" error from an HTTP server. What does it mean?  
The server didn't receive a response from another server it communicates with in a timely manner.
  

What is a proxy?  
A proxy is a server that acts as a middleman between a client device and a destination server. It can help improve privacy, security, and performance by hiding the client's IP address, filtering content, and caching frequently accessed data.
- Proxies can be used for load balancing, distributing traffic across multiple servers to help prevent server overload and improve website or application performance. They can also be used for data analysis, as they can log requests and traffic, providing useful insights into user behavior and preferences.
  

What is a reverse proxy?  
A reverse proxy is a type of proxy server that sits between a client and a server, but it is used to manage traffic going in the opposite direction of a traditional forward proxy. In a forward proxy, the client sends requests to the proxy server, which then forwards them to the destination server. However, in a reverse proxy, the client sends requests to the destination server, but the requests are intercepted by the reverse proxy before they reach the server.
- They're commonly used to improve web server performance, provide high availability and fault tolerance, and enhance security by preventing direct access to the back-end server. They are often used in large-scale web applications and high-traffic websites to manage and distribute requests to multiple servers, resulting in improved scalability and reliability.
  

When you publish a project, you usually publish it with a license. What types of licenses are you familiar with and which one do you prefer to use?
  

Explain what is "X-Forwarded-For"  
Wikipedia: "The X-Forwarded-For (XFF) HTTP header field is a common method for identifying the originating IP address of a client connecting to a web server through an HTTP proxy or load balancer."
  
#### Load Balancers  

What is a load balancer?  
A load balancer accepts (or denies) incoming network traffic from a client, and based on some criteria (application related, network, etc.) it distributes those communications out to servers (at least one).
  

Why to used a load balancer?  
* Scalability - using a load balancer, you can possibly add more servers in the backend to handle more requests/traffic from the clients, as opposed to using one server.
* Redundancy - if one server in the backend dies, the load balancer will keep forwarding the traffic/requests to the second server so users won't even notice one of the servers in the backend is down.
  

What load balancer techniques/algorithms are you familiar with?  
* Round Robin
* Weighted Round Robin
* Least Connection
* Weighted Least Connection
* Resource Based
* Fixed Weighting
* Weighted Response Time
* Source IP Hash
* URL Hash
  

What are the drawbacks of round robin algorithm in load balancing?  
* A simple round robin algorithm knows nothing about the load and the spec of each server it forwards the requests to. It is possible, that multiple heavy workloads requests will get to the same server while other servers will got only lightweight requests which will result in one server doing most of the work, maybe even crashing at some point because it unable to handle all the heavy workloads requests by its own.
* Each request from the client creates a whole new session. This might be a problem for certain scenarios where you would like to perform multiple operations where the server has to know about the result of operation so basically, being sort of aware of the history it has with the client. In round robin, first request might hit server X, while second request might hit server Y and ask to continue processing the data that was processed on server X already.
  

What is an Application Load Balancer?
  

In which scenarios would you use ALB?
  

At what layers a load balancer can operate?  
L4 and L7
  

Can you perform load balancing without using a dedicated load balancer instance?  
Yes, you can use DNS for performing load balancing.
  

What is DNS load balancing? What its advantages? When would you use it?
  
#### Load Balancers - Sticky Sessions  

What are sticky sessions? What are their pros and cons?  
Recommended read:
* Red Hat Article  
Cons:
* Can cause uneven load on instance (since requests routed to the same instances)
Pros:
* Ensures in-proc sessions are not lost when a new request is created
  

Name one use case for using sticky sessions  
You would like to make sure the user doesn't lose the current session data.
  

What sticky sessions use for enabling the "stickiness"?  
Cookies. There are application based cookies and duration based cookies.
  

Explain application-based cookies  
* Generated by the application and/or the load balancer
* Usually allows to include custom data
  

Explain duration-based cookies  
* Generated by the load balancer
* Session is not sticky anymore once the duration elapsed
  
#### Load Balancers - Load Balancing Algorithms  

Explain each of the following load balancing techniques  
* Round Robin
* Weighted Round Robin
* Least Connection
* Weighted Least Connection
* Resource Based
* Fixed Weighting
* Weighted Response Time
* Source IP Hash
* URL Hash

  

Explain use case for connection draining?
To ensure that a Classic Load Balancer stops sending requests to instances that are de-registering or unhealthy, while keeping the existing connections open, use connection draining. This enables the load balancer to complete in-flight requests made to instances that are de-registering or unhealthy.  
The maximum timeout value can be set between 1 and 3,600 seconds on both GCP and AWS.  
  
#### Licenses  

Are you familiar with "Creative Commons"? What do you know about it?  
The Creative Commons license is a set of copyright licenses that allow creators to share their work with the public while retaining some control over how it can be used. The license was developed as a response to the restrictive standards of traditional copyright laws, which limited access of creative works. Its creators to choose the terms under which their works can be shared, distributed, and used by others. They're six main types of Creative Commons licenses, each with different levels of restrictions and permissions, the six licenses are:  
* Attribution (CC BY): Allows others to distribute, remix, and build upon the work, even commercially, as long as they credit the original creator.
* Attribution-ShareAlike (CC BY-SA): Allows others to remix and build upon the work, even commercially, as long as they credit the original creator and release any new creations under the same license.
* Attribution-NoDerivs (CC BY-ND): Allows others to distribute the work, even commercially, but they cannot remix or change it in any way and must credit the original creator.
* Attribution-NonCommercial (CC BY-NC): Allows others to remix and build upon the work, but they cannot use it commercially and must credit the original creator.
* Attribution-NonCommercial-ShareAlike (CC BY-NC-SA): Allows others to remix and build upon the work, but they cannot use it commercially, must credit the original creator, and must release any new creations under the same license.
* Attribution-NonCommercial-NoDerivs (CC BY-NC-ND): Allows others to download and share the work, but they cannot use it commercially, remix or change it in any way, and must credit the original creator.  
Simply stated, the Creative Commons licenses are a way for creators to share their work with the public while retaining some control over how it can be used. The licenses promote creativity, innovation, and collaboration, while also respecting the rights of creators while still encouraging the responsible use of creative works.  
More information: 
  

Explain the differences between copyleft and permissive licenses  
In Copyleft, any derivative work must use the same licensing while in permissive licensing there are no such condition. GPL-3 is an example of copyleft license while BSD is an example of permissive license.
  
#### Random  

How a search engine works?
  

How auto completion works?
  

What is faster than RAM?  
CPU cache.
Source
  

What is a memory leak?  
A memory leak is a programming error that occurs when a program fails to release memory that is no longer needed, causing the program to consume increasing amounts of memory over time.  
The leaks can lead to a variety of problems, including system crashes, performance degradation, and instability. Usually occurring after failed maintenance on older systems and compatibility with new components over time.
  

What is your favorite protocol?  
SSH
HTTP
DHCP
DNS
...
  

What is Cache API?
  

What is the C10K problem? Is it relevant today?  

