---
repo: binary-husky/gpt_academic
readme_filename: binary-husky_gpt_academic_README.md
stars: 68842
forks: 8356
watchers: 68842
contributors_count: 101
license: GPL-3.0
Header 1: Advanced Usage
Header 3: I：自定义新的便捷按钮（学术快捷键）
---
现在已可以通过UI中的`界面外观`菜单中的`自定义菜单`添加新的便捷按钮。如果需要在代码中定义，请使用任意文本编辑器打开`core_functional.py`，添加如下条目即可：  
```python
"超级英译中": {
# 前缀，会被加在你的输入之前。例如，用来描述你的要求，例如翻译、解释代码、润色等等
"Prefix": "请翻译把下面一段内容成中文，然后用一个markdown表格逐一解释文中出现的专有名词：\n\n",

# 后缀，会被加在你的输入之后。例如，配合前缀可以把你的输入内容用引号圈起来。
"Suffix": "",
},
```  


