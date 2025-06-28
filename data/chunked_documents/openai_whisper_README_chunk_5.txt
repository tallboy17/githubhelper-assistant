---
repo: openai/whisper
readme_filename: openai_whisper_README.md
stars: 84017
forks: 10219
watchers: 84017
contributors_count: 78
license: MIT
Header 1: Whisper
Header 2: Command-line usage
---
The following command will transcribe speech in audio files, using the `turbo` model:  
```bash
whisper audio.flac audio.mp3 audio.wav --model turbo
```  
The default setting (which selects the `turbo` model) works well for transcribing English. However, **the `turbo` model is not trained for translation tasks**. If you need to **translate non-English speech into English**, use one of the **multilingual models** (`tiny`, `base`, `small`, `medium`, `large`) instead of `turbo`.  
For example, to transcribe an audio file containing non-English speech, you can specify the language:  
```bash
whisper japanese.wav --language Japanese
```  
To **translate** speech into English, use:  
```bash
whisper japanese.wav --model medium --language Japanese --task translate
```  
> **Note:** The `turbo` model will return the original language even if `--task translate` is specified. Use `medium` or `large` for the best translation results.  
Run the following to view all available options:  
```bash
whisper --help
```  
See tokenizer.py for the list of all available languages.