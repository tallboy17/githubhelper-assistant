---
repo: AUTOMATIC1111/stable-diffusion-webui
readme_filename: AUTOMATIC1111_stable-diffusion-webui_README.md
stars: 153957
forks: 28611
watchers: 153957
contributors_count: 429
license: AGPL-3.0
Header 1: Stable Diffusion web UI
Header 2: Features
---
Detailed feature showcase with images:
- Original txt2img and img2img modes
- One click install and run script (but you still must install python and git)
- Outpainting
- Inpainting
- Color Sketch
- Prompt Matrix
- Stable Diffusion Upscale
- Attention, specify parts of text that the model should pay more attention to
- a man in a `((tuxedo))` - will pay more attention to tuxedo
- a man in a `(tuxedo:1.21)` - alternative syntax
- select text and press `Ctrl+Up` or `Ctrl+Down` (or `Command+Up` or `Command+Down` if you're on a MacOS) to automatically adjust attention to selected text (code contributed by anonymous user)
- Loopback, run img2img processing multiple times
- X/Y/Z plot, a way to draw a 3 dimensional plot of images with different parameters
- Textual Inversion
- have as many embeddings as you want and use any names you like for them
- use multiple embeddings with different numbers of vectors per token
- works with half precision floating point numbers
- train embeddings on 8GB (also reports of 6GB working)
- Extras tab with:
- GFPGAN, neural network that fixes faces
- CodeFormer, face restoration tool as an alternative to GFPGAN
- RealESRGAN, neural network upscaler
- ESRGAN, neural network upscaler with a lot of third party models
- SwinIR and Swin2SR (see here), neural network upscalers
- LDSR, Latent diffusion super resolution upscaling
- Resizing aspect ratio options
- Sampling method selection
- Adjust sampler eta values (noise multiplier)
- More advanced noise setting options
- Interrupt processing at any time
- 4GB video card support (also reports of 2GB working)
- Correct seeds for batches
- Live prompt token length validation
- Generation parameters
- parameters you used to generate images are saved with that image
- in PNG chunks for PNG, in EXIF for JPEG
- can drag the image to PNG info tab to restore generation parameters and automatically copy them into UI
- can be disabled in settings
- drag and drop an image/text-parameters to promptbox
- Read Generation Parameters Button, loads parameters in promptbox to UI
- Settings page
- Running arbitrary python code from UI (must run with `--allow-code` to enable)
- Mouseover hints for most UI elements
- Possible to change defaults/mix/max/step values for UI elements via text config
- Tiling support, a checkbox to create images that can be tiled like textures
- Progress bar and live image generation preview
- Can use a separate neural network to produce previews with almost none VRAM or compute requirement
- Negative prompt, an extra text field that allows you to list what you don't want to see in generated image
- Styles, a way to save part of prompt and easily apply them via dropdown later
- Variations, a way to generate same image but with tiny differences
- Seed resizing, a way to generate same image but at slightly different resolution
- CLIP interrogator, a button that tries to guess prompt from an image
- Prompt Editing, a way to change prompt mid-generation, say to start making a watermelon and switch to anime girl midway
- Batch Processing, process a group of files using img2img
- Img2img Alternative, reverse Euler method of cross attention control
- Highres Fix, a convenience option to produce high resolution pictures in one click without usual distortions
- Reloading checkpoints on the fly
- Checkpoint Merger, a tab that allows you to merge up to 3 checkpoints into one
- Custom scripts with many extensions from community
- Composable-Diffusion, a way to use multiple prompts at once
- separate prompts using uppercase `AND`
- also supports weights for prompts: `a cat :1.2 AND a dog AND a penguin :2.2`
- No token limit for prompts (original stable diffusion lets you use up to 75 tokens)
- DeepDanbooru integration, creates danbooru style tags for anime prompts
- xformers, major speed increase for select cards: (add `--xformers` to commandline args)
- via extension: History tab: view, direct and delete images conveniently within the UI
- Generate forever option
- Training tab
- hypernetworks and embeddings options
- Preprocessing images: cropping, mirroring, autotagging using BLIP or deepdanbooru (for anime)
- Clip skip
- Hypernetworks
- Loras (same as Hypernetworks but more pretty)
- A separate UI where you can choose, with preview, which embeddings, hypernetworks or Loras to add to your prompt
- Can select to load a different VAE from settings screen
- Estimated completion time in progress bar
- API
- Support for dedicated inpainting model by RunwayML
- via extension: Aesthetic Gradients, a way to generate images with a specific aesthetic by using clip images embeds (implementation of 
- Stable Diffusion 2.0 support - see wiki for instructions
- Alt-Diffusion support - see wiki for instructions
- Now without any bad letters!
- Load checkpoints in safetensors format
- Eased resolution restriction: generated image's dimensions must be a multiple of 8 rather than 64
- Now with a license!
- Reorder elements in the UI from settings screen
- Segmind Stable Diffusion support