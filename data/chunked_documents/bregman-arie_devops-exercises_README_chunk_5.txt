---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: Operating System
Header 3: Operating System - Self Assessment
---

What is an operating system?  
From the book "Operating Systems: Three Easy Pieces":  
"responsible for making it easy to run programs (even allowing you to seemingly run many at the same time), allowing programs to share memory, enabling programs to interact with devices, and other fun stuff like that".
  
#### Operating System - Process  

Can you explain what is a process?  
A process is a running program. A program is one or more instructions and the program (or process) is executed by the operating system.
  

If you had to design an API for processes in an operating system, what would this API look like?  
It would support the following:  
* Create - allow to create new processes
* Delete - allow to remove/destroy processes
* State - allow to check the state of the process, whether it's running, stopped, waiting, etc.
* Stop - allow to stop a running process
  

How a process is created?  
* The OS is reading program's code and any additional relevant data
* Program's code is loaded into the memory or more specifically, into the address space of the process.
* Memory is allocated for program's stack (aka run-time stack). The stack also initialized by the OS with data like argv, argc and parameters to main()
* Memory is allocated for program's heap which is required for dynamically allocated data like the data structures linked lists and hash tables
* I/O initialization tasks are performed, like in Unix/Linux based systems, where each process has 3 file descriptors (input, output and error)
* OS is running the program, starting from main()
  

True or False? The loading of the program into the memory is done eagerly (all at once)  
False. It was true in the past but today's operating systems perform lazy loading, which means only the relevant pieces required for the process to run are loaded first.
  

What are different states of a process?  
* Running - it's executing instructions
* Ready - it's ready to run, but for different reasons it's on hold
* Blocked - it's waiting for some operation to complete, for example I/O disk request
  

What are some reasons for a process to become blocked?  
- I/O operations (e.g. Reading from a disk)
- Waiting for a packet from a network
  

What is Inter Process Communication (IPC)?  
Inter-process communication (IPC) refers to the mechanisms provided by an operating system that allow processes to manage shared data.
  

What is "time sharing"?  
Even when using a system with one physical CPU, it's possible to allow multiple users to work on it and run programs. This is possible with time sharing, where computing resources are shared in a way it seems to the user, the system has multiple CPUs, but in fact it's simply one CPU shared by applying multiprogramming and multi-tasking.
  

What is "space sharing"?  
Somewhat the opposite of time sharing. While in time sharing a resource is used for a while by one entity and then the same resource can be used by another resource, in space sharing the space is shared by multiple entities but in a way where it's not being transferred between them.
It's used by one entity, until this entity decides to get rid of it. Take for example storage. In storage, a file is yours, until you decide to delete it.
  

What component determines which process runs at a given moment in time?  
CPU scheduler
  
#### Operating System - Memory  

What is "virtual memory" and what purpose does serve?  
Virtual memory combines your computer's RAM with temporary space on your hard disk. When RAM runs low, virtual memory helps to move data from RAM to a space called a paging file. Moving data to paging file can free up the RAM, so your computer can complete its work. In general, the more RAM your computer has, the faster the programs run.

  

What is demand paging?  
Demand paging is a memory management technique where pages are loaded into physical memory only when accessed by a process. It optimizes memory usage by loading pages on demand, reducing startup latency and space overhead. However, it introduces some latency when accessing pages for the first time. Overall, it’s a cost-effective approach for managing memory resources in operating systems.
  

What is copy-on-write?
Copy-on-write (COW) is a resource management concept, with the goal to reduce unnecessary copying of information. It is a concept, which is implemented for instance within the POSIX fork syscall, which creates a duplicate process of the calling process.  
The idea:
1. If resources are shared between 2 or more entities (for example shared memory segments between 2 processes), the resources don't need to be copied for every entity, but rather every entity has a READ operation access permission on the shared resource. (the shared segments are marked as read-only)
(Think of every entity having a pointer to the location of the shared resource, which can be dereferenced to read its value)
2. If one entity would perform a WRITE operation on a shared resource, a problem would arise, since the resource also would be permanently changed for ALL other entities sharing it.
(Think of a process modifying some variables on the stack, or allocatingy some data dynamically on the heap, these changes to the shared resource would also apply for ALL other processes, this is definitely an undesirable behaviour)
3. As a solution only, if a WRITE operation is about to be performed on a shared resource, this resource gets COPIED first and then the changes are applied.
  

What is a kernel, and what does it do?  
The kernel is part of the operating system and is responsible for tasks like:  
* Allocating memory
* Schedule processes
* Control CPU
  

True or False? Some pieces of the code in the kernel are loaded into protected areas of the memory so applications can't overwrite them.  
True
  

What is POSIX?  
POSIX (Portable Operating System Interface) is a set of standards that define the interface between a Unix-like operating system and application programs.
  

Explain what is Semaphore and what its role in operating systems.  
A semaphore is a synchronization primitive used in operating systems and concurrent programming to control access to shared resources. It's a variable or abstract data type that acts as a counter or a signaling mechanism for managing access to resources by multiple processes or threads.
  

What is cache? What is buffer?  
Cache: Cache is usually used when processes are reading and writing to the disk to make the process faster, by making similar data used by different programs easily accessible.
Buffer: Reserved place in RAM, which is used to hold data for temporary purposes.
