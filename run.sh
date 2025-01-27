#!/bin/bash

python src/super_res_upsample.py \
    --model_path models/64_256_upsampler.pt \
    --base_samples data/low_res_input_09.npz \
    --attention_resolutions 32,16,8 \
    --class_cond True \
    --diffusion_steps 750 \
    --large_size 256 \
    --small_size 64 \
    --learn_sigma True \
    --noise_schedule linear \
    --num_channels 192 \
    --num_heads 4 \
    --num_res_blocks 2 \
    --resblock_updown True \
    --use_fp16 True \
    --use_scale_shift_norm True \
    --batch_size 1 \
    --num_samples 3 \
    --timestep_respacing 250 \

