# 442_Project

Ryan Kwon, Emma Cho, Josh Wu

## Overview
* [] Generate Noised Datasets (64x64 or 128x128)
* [] Super resolution (x4) with pre-trained diffusion
    * 64x64 -&gt; 256x256 upsampler: [64_256_upsampler.pt](https://openaipublic.blob.core.windows.net/diffusion/jul-2021/64_256_upsampler.pt)
    * 128x128 -&gt; 512x512 upsampler: [128_512_upsampler.pt](https://openaipublic.blob.core.windows.net/diffusion/jul-2021/128_512_upsampler.pt)
* [] Denoising
    * Gaussian Kernel
    * Salt and Pepper Noise