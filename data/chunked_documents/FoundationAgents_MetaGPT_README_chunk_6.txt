---
repo: FoundationAgents/MetaGPT
readme_filename: FoundationAgents_MetaGPT_README.md
stars: 56806
forks: 6814
watchers: 56806
contributors_count: 113
license: MIT
Header 1: MetaGPT: The Multi-Agent Framework
Header 2: Get Started
Header 3: Usage
---
After installation, you can use MetaGPT at CLI  
```bash
metagpt "Create a 2048 game"  # this will create a repo in ./workspace
```  
or use it as library  
```python
from metagpt.software_company import generate_repo
from metagpt.utils.project_repo import ProjectRepo

repo: ProjectRepo = generate_repo("Create a 2048 game")  # or ProjectRepo("")
print(repo)  # it will print the repo structure with files
```  
You can also use Data Interpreter to write code:  
```python
import asyncio
from metagpt.roles.di.data_interpreter import DataInterpreter

async def main():
di = DataInterpreter()
await di.run("Run data analysis on sklearn Iris dataset, include a plot")

asyncio.run(main())  # or await main() in a jupyter notebook setting
```