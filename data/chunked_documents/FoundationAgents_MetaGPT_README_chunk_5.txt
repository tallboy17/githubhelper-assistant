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
Header 3: Configuration
---
You can init the config of MetaGPT by running the following command, or manually create `~/.metagpt/config2.yaml` file:
```bash
# Check  for more details
metagpt --init-config  # it will create ~/.metagpt/config2.yaml, just modify it to your needs
```  
You can configure `~/.metagpt/config2.yaml` according to the example and doc:  
```yaml
llm:
api_type: "openai"  # or azure / ollama / groq etc. Check LLMType for more options
model: "gpt-4-turbo"  # or gpt-3.5-turbo
base_url: "  # or forward url / other llm url
api_key: "YOUR_API_KEY"
```