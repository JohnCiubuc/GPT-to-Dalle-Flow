#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:54:26 2022

@author: inathero
"""

import openai
from PIL import Image
from docarray import Document

openai_secret_key = 'SECRET KEY HERE'
dalle_server_url = 'grpcs://dalle-flow.dev.jina.ai'

prompt = "generate a dalle wallpaper description"

openai.api_key = openai_secret_key

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompt,
  temperature=0.7,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

prompt = response['choices'][0]['text'].strip()
print(f'DALLE Prompt: {prompt}')
print('Getting goodies from DALLE. This can take like 5 minutes')

da = Document(text=prompt).post(dalle_server_url, parameters={'num_images': 1}).matches
fav = da[0].post(f'{dalle_server_url}/upscale')
tensor_d = fav.load_uri_to_image_tensor()
image = Image.fromarray(tensor_d.tensor)
image = image.resize((1920,1080), resample=Image.BOX)
image.save('dalle_wallpaper.png')