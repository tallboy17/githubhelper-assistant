---
repo: microsoft/markitdown
readme_filename: microsoft_markitdown_README.md
stars: 59580
forks: 3102
watchers: 59580
contributors_count: 64
license: MIT
Header 1: MarkItDown
Header 2: Contributing
Header 3: Running Tests and Checks
---
- Navigate to the MarkItDown package:  
```sh
cd packages/markitdown
```  
- Install `hatch` in your environment and run tests:  
```sh
pip install hatch  # Other ways of installing hatch: 
hatch shell
hatch test
```  
(Alternative) Use the Devcontainer which has all the dependencies installed:  
```sh
# Reopen the project in Devcontainer and run:
hatch test
```  
- Run pre-commit checks before submitting a PR: `pre-commit run --all-files`