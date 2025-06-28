---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Puppet
---

What is Puppet? How does it works?  
* Puppet is a configuration management tool ensuring that all systems are configured to a desired and predictable state.


Explain Puppet architecture  
* Puppet has a primary-secondary node architecture. The clients are distributed across the network and communicate with the primary-secondary environment where Puppet modules are present. The client agent sends a certificate with its ID to the server; the server then signs that certificate and sends it back to the client. This authentication allows for secure and verifiable communication between the client and the master.
  

Can you compare Puppet to other configuration management tools? Why did you chose to use Puppet?  
* Puppet is often compared to other configuration management tools like Chef, Ansible, SaltStack, and cfengine. The choice to use Puppet often depends on an organization's needs, such as ease of use, scalability, and community support.
  

Explain the following:  
* Module
* Manifest
* Node
  
* Modules - are a collection of manifests, templates, and files
* Manifests - are the actual codes for configuring the clients
* Node - allows you to assign specific configurations to specific nodes
  

Explain Facter  
* Facter is a standalone tool in Puppet that collects information about a system and its configuration, such as the operating system, IP addresses, memory, and network interfaces. This information can be used in Puppet manifests to make decisions about how resources should be managed, and to customize the behavior of Puppet based on the characteristics of the system. Facter is integrated into Puppet, and its facts can be used within Puppet manifests to make decisions about resource management.
  

What is MCollective?  
* MCollective is a middleware system that integrates with Puppet to provide orchestration, remote execution, and parallel job execution capabilities.
  

Do you have experience with writing modules? Which module have you created and for what?
  

Explain what is Hiera  
* Hiera is a hierarchical data store in Puppet that is used to separate data from code, allowing data to be more easily separated, managed, and reused.
