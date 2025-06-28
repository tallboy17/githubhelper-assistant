---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Virtualization
---

What is Virtualization?  
Virtualization uses software to create an abstraction layer over computer hardware, that allows the hardware elements of a single computer - processors, memory, storage and more - to be divided into multiple virtual computers, commonly called virtual machines (VMs).
  

What is a hypervisor?  
Red Hat: "A hypervisor is software that creates and runs virtual machines (VMs). A hypervisor, sometimes called a virtual machine monitor (VMM), isolates the hypervisor operating system and resources from the virtual machines and enables the creation and management of those VMs."  
Read more here
  

What types of hypervisors are there?  
Hosted hypervisors and bare-metal hypervisors.
  

What are the advantages and disadvantges of bare-metal hypervisor over a hosted hypervisor?  
Due to having its own drivers and a direct access to hardware components, a baremetal hypervisor will often have better performances along with stability and scalability.  
On the other hand, there will probably be some limitation regarding loading (any) drivers so a hosted hypervisor will usually benefit from having a better hardware compatibility.
  

What types of virtualization are there?  
Operating system virtualization
Network functions virtualization
Desktop virtualization
  

Is containerization is a type of Virtualization?  
Yes, it's a operating-system-level virtualization, where the kernel is shared and allows to use multiple isolated user-spaces instances.
  

How the introduction of virtual machines changed the industry and the way applications were deployed?  
The introduction of virtual machines allowed companies to deploy multiple business applications on the same hardware, while each application is separated from each other in secured way, where each is running on its own separate operating system.
  
#### Virtual Machines  

Do we need virtual machines in the age of containers? Are they still relevant?  
Yes, virtual machines are still relevant even in the age of containers. While containers provide a lightweight and portable alternative to virtual machines, they do have certain limitations. Virtual machines still matter because they offer isolation and security, can run different operating systems, and are good for legacy apps. Containers limitations for example are sharing the host kernel.
