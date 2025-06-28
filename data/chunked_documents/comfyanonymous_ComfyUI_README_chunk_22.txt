---
repo: comfyanonymous/ComfyUI
readme_filename: comfyanonymous_ComfyUI_README.md
stars: 80954
forks: 8971
watchers: 80954
contributors_count: 213
license: GPL-3.0
Header 1: Notes
Header 2: How to show high-quality previews?
---
Use ```--preview-method auto``` to enable previews.  
The default installation includes a fast latent preview method that's low-resolution. To enable higher-quality previews with TAESD, download the taesd_decoder.pth, taesdxl_decoder.pth, taesd3_decoder.pth and taef1_decoder.pth and place them in the `models/vae_approx` folder. Once they're installed, restart ComfyUI and launch it with `--preview-method taesd` to enable high-quality previews.