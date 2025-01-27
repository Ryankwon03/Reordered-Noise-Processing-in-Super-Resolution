#!/bin/bash

python src/classifier_sample.py \
    --model_path models/256x256_diffusion.pt \
    --classifier_path models/256x256_classifier.pt \
    --attention_resolutions 32,16,8 \
    --class_cond True \
    --diffusion_steps 1000 \
    --image_size 256 \
    --learn_sigma True \
    --noise_schedule linear \
    --num_channels 256 \
    --num_head_channels 64 \
    --num_res_blocks 2 \
    --resblock_updown True \
    --use_fp16 True \
    --use_scale_shift_norm True \
    --classifier_scale 1.0 \
    --batch_size 1 \
    --num_samples 3 \
    --timestep_respacing 250 \
