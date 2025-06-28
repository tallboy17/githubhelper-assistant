---
repo: comfyanonymous/ComfyUI
readme_filename: comfyanonymous_ComfyUI_README.md
stars: 80954
forks: 8971
watchers: 80954
contributors_count: 213
license: GPL-3.0
Header 1: ComfyUI
Header 2: Features
---
- Nodes/graph/flowchart interface to experiment and create complex Stable Diffusion workflows without needing to code anything.
- Image Models
- SD1.x, SD2.x,
- SDXL, SDXL Turbo
- Stable Cascade
- SD3 and SD3.5
- Pixart Alpha and Sigma
- AuraFlow
- HunyuanDiT
- Flux
- Lumina Image 2.0
- HiDream
- Cosmos Predict2
- Image Editing Models
- Omnigen 2
- Flux Kontext
- Video Models
- Stable Video Diffusion
- Mochi
- LTX-Video
- Hunyuan Video
- Nvidia Cosmos and Cosmos Predict2
- Wan 2.1
- Audio Models
- Stable Audio
- ACE Step
- 3D Models
- Hunyuan3D 2.0
- Asynchronous Queue system
- Many optimizations: Only re-executes the parts of the workflow that changes between executions.
- Smart memory management: can automatically run models on GPUs with as low as 1GB vram.
- Works even if you don't have a GPU with: ```--cpu``` (slow)
- Can load ckpt, safetensors and diffusers models/checkpoints. Standalone VAEs and CLIP models.
- Embeddings/Textual inversion
- Loras (regular, locon and loha)
- Hypernetworks
- Loading full workflows (with seeds) from generated PNG, WebP and FLAC files.
- Saving/Loading workflows as Json files.
- Nodes interface can be used to create complex workflows like one for Hires fix or much more advanced ones.
- Area Composition
- Inpainting with both regular and inpainting models.
- ControlNet and T2I-Adapter
- Upscale Models (ESRGAN, ESRGAN variants, SwinIR, Swin2SR, etc...)
- unCLIP Models
- GLIGEN
- Model Merging
- LCM models and Loras
- Latent previews with TAESD
- Starts up very fast.
- Works fully offline: core will never download anything unless you want to.
- Optional API nodes to use paid models from external providers through the online Comfy API.
- Config file to set the search paths for models.  
Workflow examples can be found on the Examples page