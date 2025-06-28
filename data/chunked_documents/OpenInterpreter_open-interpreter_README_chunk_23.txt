---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 1: Access Documentation Offline
---
The full documentation is accessible on-the-go without the need for an internet connection.  
Node is a pre-requisite:  
- Version 18.17.0 or any later 18.x.x version.
- Version 20.3.0 or any later 20.x.x version.
- Any version starting from 21.0.0 onwards, with no upper limit specified.  
Install Mintlify:  
```bash
npm i -g mintlify@latest
```  
Change into the docs directory and run the appropriate command:  
```bash
# Assuming you're at the project's root directory
cd ./docs

# Run the documentation server
mintlify dev
```  
A new browser window should open. The documentation will be available at  as long as the documentation server is running.