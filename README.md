# Reordered Noise Processing in Super-Resolution

Ryan Kwon

## Overview
* [v] Generate Noised Datasets (64x64 or 128x128)
* [v] Super resolution (x4) with pre-trained diffusion
    * OpenAI
        * 64x64 -&gt; 256x256 upsampler: [64_256_upsampler.pt](https://openaipublic.blob.core.windows.net/diffusion/jul-2021/64_256_upsampler.pt)
        * 128x128 -&gt; 512x512 upsampler: [128_512_upsampler.pt](https://openaipublic.blob.core.windows.net/diffusion/jul-2021/128_512_upsampler.pt)
        * 256x256 classifier: [256x256_classifier.pt](https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_classifier.pt)
        * 256x256 diffusion: [256x256_diffusion.pt](https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_diffusion.pt)
        * 256x256 diffusion (unconditional): [256x256_diffusion_uncond.pt](https://openaipublic.blob.core.windows.net/diffusion/jul-2021/256x256_diffusion_uncond.pt)
    * Stability AI
        * [Stable Diffusion x4 scaler](https://huggingface.co/stabilityai/stable-diffusion-x4-upscaler)

* [] Denoising
    * Gaussian Noise
    * Poisson Noise
    * Salt and Pepper Noise

* [] Diffusion

## References
* [OpenAI/guided-diffusion](https://github.com/openai/guided-diffusion)


## Brainstorming
* [Google Slides](https://docs.google.com/presentation/d/1jNjpgHjSUmP9twyLtgJW9e-mBIeoYHoweL0xOzGpVQk/edit#slide=id.p)


Credit to: Emma Cho, Josh Wu