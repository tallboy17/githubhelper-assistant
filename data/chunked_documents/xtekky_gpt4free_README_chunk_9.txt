---
repo: xtekky/gpt4free
readme_filename: xtekky_gpt4free_README.md
stars: 64522
forks: 13656
watchers: 64522
contributors_count: 240
license: GPL-3.0
Header 2: 💡 Usage
Header 3: 📝 Text Generation
---
```python
from g4f.client import Client

client = Client()
response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[{"role": "user", "content": "Hello"}],
web_search=False
)
print(response.choices[0].message.content)
```
```
Hello! How can I assist you today?
```