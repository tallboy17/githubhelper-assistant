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
Header 3: RPC and REST calls comparison
---
| Operation | RPC | REST |
|---|---|---|
| Signup    | **POST** /signup | **POST** /persons |
| Resign    | **POST** /resign{"personid": "1234"} | **DELETE** /persons/1234 |
| Read a person | **GET** /readPerson?personid=1234 | **GET** /persons/1234 |
| Read a person’s items list | **GET** /readUsersItemsList?personid=1234 | **GET** /persons/1234/items |
| Add an item to a person’s items | **POST** /addItemToUsersItemsList{"personid": "1234";"itemid": "456"} | **POST** /persons/1234/items{"itemid": "456"} |
| Update an item    | **POST** /modifyItem{"itemid": "456";"key": "value"} | **PUT** /items/456{"key": "value"} |
| Delete an item | **POST** /removeItem{"itemid": "456"} | **DELETE** /items/456 |  

Source: Do you really know why you prefer REST over RPC
  
#### Source(s) and further reading: REST and RPC  
* Do you really know why you prefer REST over RPC
* When are RPC-ish approaches more appropriate than REST?
* REST vs JSON-RPC
* Debunking the myths of RPC and REST
* What are the drawbacks of using REST
* Crack the system design interview
* Thrift
* Why REST for internal use and not RPC