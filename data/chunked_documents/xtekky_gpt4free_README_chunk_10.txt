---
repo: xtekky/gpt4free
readme_filename: xtekky_gpt4free_README.md
stars: 64522
forks: 13656
watchers: 64522
contributors_count: 240
license: GPL-3.0
Header 2: 💡 Usage
Header 3: 🎨  Image Generation
---
```python
from g4f.client import Client

client = Client()
response = client.images.generate(
model="flux",
prompt="a white siamese cat",
response_format="url"
)

print(f"Generated image URL: {response.data[0].url}")
```
![Image with cat](