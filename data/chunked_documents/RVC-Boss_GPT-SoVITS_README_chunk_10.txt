---
repo: RVC-Boss/GPT-SoVITS
readme_filename: RVC-Boss_GPT-SoVITS_README.md
stars: 48165
forks: 5297
watchers: 48165
contributors_count: 85
license: MIT
Header 2: Pretrained Models
---
**If `install.sh` runs successfully, you may skip No.1,2,3**  
**Users in China can download all these models here.**  
1. Download pretrained models from GPT-SoVITS Models and place them in `GPT_SoVITS/pretrained_models`.  
2. Download G2PW models from G2PWModel.zip(HF)| G2PWModel.zip(ModelScope), unzip and rename to `G2PWModel`, and then place them in `GPT_SoVITS/text`.(Chinese TTS Only)  
3. For UVR5 (Vocals/Accompaniment Separation & Reverberation Removal, additionally), download models from UVR5 Weights and place them in `tools/uvr5/uvr5_weights`.  
- If you want to use `bs_roformer` or `mel_band_roformer` models for UVR5, you can manually download the model and corresponding configuration file, and put them in `tools/uvr5/uvr5_weights`. **Rename the model file and configuration file, ensure that the model and configuration files have the same and corresponding names except for the suffix**. In addition, the model and configuration file names **must include `roformer`** in order to be recognized as models of the roformer class.  
- The suggestion is to **directly specify the model type** in the model name and configuration file name, such as `mel_mand_roformer`, `bs_roformer`. If not specified, the features will be compared from the configuration file to determine which type of model it is. For example, the model `bs_roformer_ep_368_sdr_12.9628.ckpt` and its corresponding configuration file `bs_roformer_ep_368_sdr_12.9628.yaml` are a pair, `kim_mel_band_roformer.ckpt` and `kim_mel_band_roformer.yaml` are also a pair.  
4. For Chinese ASR (additionally), download models from Damo ASR Model, Damo VAD Model, and Damo Punc Model and place them in `tools/asr/models`.  
5. For English or Japanese ASR (additionally), download models from Faster Whisper Large V3 and place them in `tools/asr/models`. Also, other models may have the similar effect with smaller disk footprint.