---
repo: Textualize/rich
readme_filename: Textualize_rich_README.md
stars: 52598
forks: 1849
watchers: 52598
contributors_count: 260
license: MIT
Header 2: Rich Inspect
---
Rich has an inspect function which can produce a report on any Python object, such as class, instance, or builtin.  
```python
>>> my_list = ["foo", "bar"]
>>> from rich import inspect
>>> inspect(my_list, methods=True)
```  
!Log  
See the inspect docs for details.