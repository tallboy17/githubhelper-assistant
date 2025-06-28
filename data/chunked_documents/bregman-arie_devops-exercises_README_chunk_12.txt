---
repo: bregman-arie/devops-exercises
readme_filename: bregman-arie_devops-exercises_README.md
stars: 76909
forks: 17266
watchers: 76909
contributors_count: 194
license: NOASSERTION
Header 2: OpenStack
---

What components/projects of OpenStack are you familiar with?
I’m most familiar with several core OpenStack components:  
- Nova for compute resource provisioning, including VM lifecycle management.
- Neutron for networking, focusing on creating and managing networks, subnets, and routers.
- Cinder for block storage, used to attach and manage storage volumes.
- Keystone for identity services, handling authentication and authorization.  
I’ve implemented these in past projects, configuring them for scalability and security to support multi-tenant environments.  
  

Can you tell me what each of the following services/projects is responsible for?:  
- Nova
- Neutron
- Cinder
- Glance
- Keystone  
* Nova - Manage virtual instances
* Neutron - Manage networking by providing Network as a service (NaaS)
* Cinder - Block Storage
* Glance - Manage images for virtual machines and containers (search, get and register)
* Keystone - Authentication service across the cloud
  

Identify the service/project used for each of the following:  
* Copy or snapshot instances
* GUI for viewing and modifying resources
* Block Storage
* Manage virtual instances
  
* Glance - Images Service. Also used for copying or snapshot instances
* Horizon - GUI for viewing and modifying resources
* Cinder - Block Storage
* Nova - Manage virtual instances
  

What is a tenant/project?
  

Determine true or false:  
* OpenStack is free to use
* The service responsible for networking is Glance
* The purpose of tenant/project is to share resources between different projects and users of OpenStack
  

Describe in detail how you bring up an instance with a floating IP
  

You get a call from a customer saying: "I can ping my instance but can't connect (ssh) it". What might be the problem?
  

What types of networks OpenStack supports?
  

How do you debug OpenStack storage issues? (tools, logs, ...)
  

How do you debug OpenStack compute issues? (tools, logs, ...)
  
#### OpenStack Deployment & TripleO  

Have you deployed OpenStack in the past? If yes, can you describe how you did it?
  

Are you familiar with TripleO? How is it different from Devstack or Packstack?  
You can read about TripleO right here
  
#### OpenStack Compute  

Can you describe Nova in detail?  
* Used to provision and manage virtual instances
* It supports Multi-Tenancy in different levels - logging, end-user control, auditing, etc.
* Highly scalable
* Authentication can be done using internal system or LDAP
* Supports multiple types of block storage
* Tries to be hardware and hypervisor agnostice
  

What do you know about Nova architecture and components?  
* nova-api - the server which serves metadata and compute APIs
* the different Nova components communicate by using a queue (Rabbitmq usually) and a database
* a request for creating an instance is inspected by nova-scheduler which determines where the instance will be created and running
* nova-compute is the component responsible for communicating with the hypervisor for creating the instance and manage its lifecycle
  
#### OpenStack Networking (Neutron)  

Explain Neutron in detail  
* One of the core component of OpenStack and a standalone project
* Neutron focused on delivering networking as a service
* With Neutron, users can set up networks in the cloud and configure and manage a variety of network services
* Neutron interacts with:
* Keystone - authorize API calls
* Nova - nova communicates with neutron to plug NICs into a network
* Horizon - supports networking entities in the dashboard and also provides topology view which includes networking details
  

Explain each of the following components:  
- neutron-dhcp-agent
- neutron-l3-agent
- neutron-metering-agent
- neutron-*-agtent
- neutron-server  
* neutron-l3-agent - L3/NAT forwarding (provides external network access for VMs for example)
* neutron-dhcp-agent - DHCP services
* neutron-metering-agent - L3 traffic metering
* neutron-*-agtent - manages local vSwitch configuration on each compute (based on chosen plugin)
* neutron-server - exposes networking API and passes requests to other plugins if required
  

Explain these network types:  
- Management Network
- Guest Network
- API Network
- External Network  
* Management Network - used for internal communication between OpenStack components. Any IP address in this network is accessible only within the datacetner
* Guest Network - used for communication between instances/VMs
* API Network - used for services API communication. Any IP address in this network is publicly accessible
* External Network - used for public communication. Any IP address in this network is accessible by anyone on the internet
  

In which order should you remove the following entities:  
* Network
* Port
* Router
* Subnet  
- Port
- Subnet
- Router
- Network  
There are many reasons for that. One for example: you can't remove router if there are active ports assigned to it.
  

What is a provider network?
  

What components and services exist for L2 and L3?
  

What is the ML2 plug-in? Explain its architecture
  

What is the L2 agent? How does it works and what is it responsible for?
  

What is the L3 agent? How does it works and what is it responsible for?
  

Explain what the Metadata agent is responsible for
  

What networking entities Neutron supports?
  

How do you debug OpenStack networking issues? (tools, logs, ...)
  
#### OpenStack - Glance  

Explain Glance in detail  
* Glance is the OpenStack image service
* It handles requests related to instances disks and images
* Glance also used for creating snapshots for quick instances backups
* Users can use Glance to create new images or upload existing ones
  

Describe Glance architecture  
* glance-api - responsible for handling image API calls such as retrieval and storage. It consists of two APIs: 1. registry-api - responsible for internal requests 2. user API - can be accessed publicly
* glance-registry - responsible for handling image metadata requests (e.g. size, type, etc). This component is private which means it's not available publicly
* metadata definition service - API for custom metadata
* database - for storing images metadata
* image repository - for storing images. This can be a filesystem, swift object storage, HTTP, etc.
  
#### OpenStack - Swift  

Explain Swift in detail  
* Swift is Object Store service and is an highly available, distributed and consistent store designed for storing a lot of data
* Swift is distributing data across multiple servers while writing it to multiple disks
* One can choose to add additional servers to scale the cluster. All while swift maintaining integrity of the information and data replications.
  

Can users store by default an object of 100GB in size?  
Not by default. Object Storage API limits the maximum to 5GB per object but it can be adjusted.
  

Explain the following in regards to Swift:  
* Container
* Account
* Object
  
- Container - Defines a namespace for objects.
- Account - Defines a namespace for containers
- Object - Data content (e.g. image, document, ...)
  

True or False? there can be two objects with the same name in the same container but not in two different containers  
False. Two objects can have the same name if they are in different containers.
  
#### OpenStack - Cinder  

Explain Cinder in detail  
* Cinder is OpenStack Block Storage service
* It basically provides used with storage resources they can consume with other services such as Nova
* One of the most used implementations of storage supported by Cinder is LVM
* From user perspective this is transparent which means the user doesn't know where, behind the scenes, the storage is located or what type of storage is used
  

Describe Cinder's components  
* cinder-api - receives API requests
* cinder-volume - manages attached block devices
* cinder-scheduler - responsible for storing volumes
  
#### OpenStack - Keystone  

Can you describe the following concepts in regards to Keystone?  
- Role
- Tenant/Project
- Service
- Endpoint
- Token
  
- Role - A list of rights and privileges determining what a user or a project can perform
- Tenant/Project - Logical representation of a group of resources isolated from other groups of resources. It can be an account, organization, ...
- Service - An endpoint which the user can use for accessing different resources
- Endpoint - a network address which can be used to access a certain OpenStack service
- Token - Used for access resources while describing which resources can be accessed by using a scope
  

What are the properties of a service? In other words, how a service is identified?  
Using:
- Name
- ID number
- Type
- Description
  

Explain the following:
- PublicURL
- InternalURL
- AdminURL  
- PublicURL - Publicly accessible through public internet
- InternalURL - Used for communication between services
- AdminURL - Used for administrative management
  

What is a service catalog?  
A list of services and their endpoints
  
#### OpenStack Advanced - Services  

Describe each of the following services  
* Swift
* Sahara
* Ironic
* Trove
* Aodh
* Ceilometer
  
* Swift - highly available, distributed, eventually consistent object/blob store
* Sahara - Manage Hadoop Clusters
* Ironic - Bare Metal Provisioning
* Trove - Database as a service that runs on OpenStack
* Aodh - Alarms Service
* Ceilometer - Track and monitor usage
  

Identify the service/project used for each of the following:  
* Database as a service which runs on OpenStack
* Bare Metal Provisioning
* Track and monitor usage
* Alarms Service
* Manage Hadoop Clusters
* highly available, distributed, eventually consistent object/blob store
  
* Database as a service which runs on OpenStack - Trove
* Bare Metal Provisioning - Ironic
* Track and monitor usage - Ceilometer
* Alarms Service - Aodh
* Manage Hadoop Clusters
* Manage Hadoop Clusters - Sahara
* highly available, distributed, eventually consistent object/blob store - Swift
  
#### OpenStack Advanced - Keystone  

Can you describe Keystone service in detail?  
* You can't have OpenStack deployed without Keystone
* It Provides identity, policy and token services
* The authentication provided is for both users and services
* The authorization supported is token-based and user-based.
* There is a policy defined based on RBAC stored in a JSON file and each line in that file defines the level of access to apply
  

Describe Keystone architecture  
* There is a service API and admin API through which Keystone gets requests
* Keystone has four backends:
* Token Backend - Temporary Tokens for users and services
* Policy Backend - Rules management and authorization
* Identity Backend - users and groups (either standalone DB, LDAP, ...)
* Catalog Backend - Endpoints
* It has pluggable environment where you can integrate with:
* LDAP
* KVS (Key Value Store)
* SQL
* PAM
* Memcached
  

Describe the Keystone authentication process  
* Keystone gets a call/request and checks whether it's from an authorized user, using username, password and authURL
* Once confirmed, Keystone provides a token.
* A token contains a list of user's projects so there is no to authenticate every time and a token can submitted instead
  
#### OpenStack Advanced - Compute (Nova)  

What each of the following does?:  
* nova-api
* nova-compuate
* nova-conductor
* nova-cert
* nova-consoleauth
* nova-scheduler
  
* nova-api - responsible for managing requests/calls
* nova-compute - responsible for managing instance lifecycle
* nova-conductor - Mediates between nova-compute and the database so nova-compute doesn't access it directly
  

What types of Nova proxies are you familiar with?  
* Nova-novncproxy - Access through VNC connections
* Nova-spicehtml5proxy - Access through SPICE
* Nova-xvpvncproxy - Access through a VNC connection
  
#### OpenStack Advanced - Networking (Neutron)  

Explain BGP dynamic routing
  

What is the role of network namespaces in OpenStack?
  
#### OpenStack Advanced - Horizon  

Can you describe Horizon in detail?  
* Django-based project focusing on providing an OpenStack dashboard and the ability to create additional customized dashboards
* You can use it to access the different OpenStack services resources - instances, images, networks, ...
* By accessing the dashboard, users can use it to list, create, remove and modify the different resources
* It's also highly customizable and you can modify or add to it based on your needs
  

What can you tell about Horizon architecture?  
* API is backward compatible
* There are three type of dashboards: user, system and settings
* It provides core support for all OpenStack core projects such as Neutron, Nova, etc. (out of the box, no need to install extra packages or plugins)
* Anyone can extend the dashboards and add new components
* Horizon provides templates and core classes from which one can build its own dashboard
