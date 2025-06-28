---
repo: OpenInterpreter/open-interpreter
readme_filename: OpenInterpreter_open-interpreter_README.md
stars: 59793
forks: 5090
watchers: 59793
contributors_count: 122
license: AGPL-3.0
Header 2: Commands
Header 3: Configuration / Profiles
---
Open Interpreter allows you to set default behaviors using `yaml` files.  
This provides a flexible way to configure the interpreter without changing command-line arguments every time.  
Run the following command to open the profiles directory:  
```
interpreter --profiles
```  
You can add `yaml` files there. The default profile is named `default.yaml`.  
#### Multiple Profiles  
Open Interpreter supports multiple `yaml` files, allowing you to easily switch between configurations:  
```
interpreter --profile my_profile.yaml
```