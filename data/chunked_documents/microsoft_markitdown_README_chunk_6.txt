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
Header 3: Optional Dependencies
---
MarkItDown has optional dependencies for activating various file formats. Earlier in this document, we installed all optional dependencies with the `[all]` option. However, you can also install them individually for more control. For example:  
```bash
pip install 'markitdown[pdf, docx, pptx]'
```  
will install only the dependencies for PDF, DOCX, and PPTX files.  
At the moment, the following optional dependencies are available:  
* `[all]` Installs all optional dependencies
* `[pptx]` Installs dependencies for PowerPoint files
* `[docx]` Installs dependencies for Word files
* `[xlsx]` Installs dependencies for Excel files
* `[xls]` Installs dependencies for older Excel files
* `[pdf]` Installs dependencies for PDF files
* `[outlook]` Installs dependencies for Outlook messages
* `[az-doc-intel]` Installs dependencies for Azure Document Intelligence
* `[audio-transcription]` Installs dependencies for audio transcription of wav and mp3 files
* `[youtube-transcription]` Installs dependencies for fetching YouTube video transcription