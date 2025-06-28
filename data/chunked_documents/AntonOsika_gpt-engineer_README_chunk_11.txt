---
repo: AntonOsika/gpt-engineer
readme_filename: AntonOsika_gpt-engineer_README.md
stars: 54377
forks: 7182
watchers: 54377
contributors_count: 101
license: MIT
Header 1: gpt-engineer
Header 2: Features
Header 3: Vision
---
By default, gpt-engineer expects text input via a `prompt` file. It can also accept image inputs for vision-capable models. This can be useful for adding UX or architecture diagrams as additional context for GPT Engineer. You can do this by specifying an image directory with the `—-image_directory` flag and setting a vision-capable model in the second CLI argument.  
E.g. `gpte projects/example-vision gpt-4-vision-preview --prompt_file prompt/text --image_directory prompt/images -i`