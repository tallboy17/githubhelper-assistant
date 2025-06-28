---
repo: openai/whisper
readme_filename: openai_whisper_README.md
stars: 84017
forks: 10219
watchers: 84017
contributors_count: 78
license: MIT
Header 1: Whisper
Header 2: Approach
---
!Approach  
A Transformer sequence-to-sequence model is trained on various speech processing tasks, including multilingual speech recognition, speech translation, spoken language identification, and voice activity detection. These tasks are jointly represented as a sequence of tokens to be predicted by the decoder, allowing a single model to replace many stages of a traditional speech-processing pipeline. The multitask training format uses a set of special tokens that serve as task specifiers or classification targets.