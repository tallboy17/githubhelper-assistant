---
repo: microsoft/markitdown
readme_filename: microsoft_markitdown_README.md
stars: 59580
forks: 3102
watchers: 59580
contributors_count: 64
license: MIT
Header 1: MarkItDown
Header 2: Usage
Header 3: Python API
---
Basic usage in Python:  
```python
from markitdown import MarkItDown

md = MarkItDown(enable_plugins=False) # Set to True to enable plugins
result = md.convert("test.xlsx")
print(result.text_content)
```  
Document Intelligence conversion in Python:  
```python
from markitdown import MarkItDown

md = MarkItDown(docintel_endpoint="")
result = md.convert("test.pdf")
print(result.text_content)
```  
To use Large Language Models for image descriptions, provide `llm_client` and `llm_model`:  
```python
from markitdown import MarkItDown
from openai import OpenAI

client = OpenAI()
md = MarkItDown(llm_client=client, llm_model="gpt-4o")
result = md.convert("example.jpg")
print(result.text_content)
```