#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:54:26 2022

@author: inathero
"""
import random
import openai
from PIL import Image
from docarray import Document

# ===================
# Setup
# ===================

target_resolution = (1920,1080)

# An optional resampling filter. 
# This can be one of: 
    # Image.NEAREST (use nearest neighbour)
    # Image.BILINEAR (linear interpolation)
    # Image.BICUBIC (cubic spline interpolation)
    # Image.LANCZOS (a high-quality downsampling filter).
# If omitted, or if the image has mode “1” or “P”, it is set PIL.Image.NEAREST.
target_resample = 1

openai_secret_key = 'SECRET-KEY-HERE: https://beta.openai.com/account/api-keys'
dalle_server_url = 'grpcs://dalle-flow.dev.jina.ai'

random_descriptions = []
random_descriptions.append(['abstract', 'realistic', 'waterpainting', 'digital art', 'photography'])
random_descriptions.append(['dark', 'bright', 'light', 'dull', 'colourful'])
random_descriptions.append(['landscape', 'hero', 'anime', 'waterfall', 'immortal'])
random_descriptions.append(['mythical', 'fantasy', 'steampunk', 'science fiction', 'xianxia'])

# ===================
# End Setup
# ===================

descriptions = []
for i in range(len(random_descriptions)):
    descriptions.append(random.choice(random_descriptions[i]))

# Random prompt for GPT
prompt = f'A {descriptions[0]} of a {descriptions[1]} {descriptions[2]} in a {descriptions[3]} setting'

openai.api_key = openai_secret_key
response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompt,
  temperature=1.0,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

prompt = response['choices'][0]['text'].strip()
print(f'DALLE Prompt: {prompt}')
print('Getting goodies from DALLE. This can take like 5 minutes')

# Get a DALLE image
da = Document(text=prompt).post(dalle_server_url, parameters={'num_images': 1}).matches
# Upscale that image to 1024x1024
fav = da[0].post(f'{dalle_server_url}/upscale')
tensor_d = fav.load_uri_to_image_tensor()
image = Image.fromarray(tensor_d.tensor)
# Upscale image to target resolution
image = image.resize(target_resolution, resample=target_resample)
# Save
image.save('dalle_wallpaper.png')