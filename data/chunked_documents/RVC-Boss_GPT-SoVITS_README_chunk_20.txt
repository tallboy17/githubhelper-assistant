---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: (Additional) Method for running from the command line
---
Use the command line to open the WebUI for UVR5  
```bash
python tools/uvr5/webui.py ""  
```  
  
This is how the audio segmentation of the dataset is done using the command line  
```bash
python audio_slicer.py \
--input_path "" \
--output_root "" \
--threshold  \
--min_length  \
--min_interval 
--hop_size 
```  
This is how dataset ASR processing is done using the command line(Only Chinese)  
```bash
python tools/asr/funasr_asr.py -i  -o 
```  
ASR processing is performed through Faster_Whisper(ASR marking except Chinese)  
(No progress bars, GPU performance may cause time delays)  
```bash
python ./tools/asr/fasterwhisper_asr.py -i  -o  -l  -p 
```  
A custom list save path is enabled