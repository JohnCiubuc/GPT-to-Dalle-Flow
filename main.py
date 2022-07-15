#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 18:54:26 2022

@author: inathero
"""

openai_secret_key = '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'

import os
import openai

openai.api_key = os.getenv(openai_secret_key)

response = openai.Completion.create(
  model="text-davinci-002",
  prompt="",
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)


server_url = 'grpcs://dalle-flow.dev.jina.ai'
prompt = 'an oil painting of a humanoid robot playing chess in the style of Matisse'
from docarray import Document

da = Document(text=prompt).post(server_url, parameters={'num_images': 2}).matches

da.plot_image_sprites(fig_size=(10,10), show_index=True)
fav_id = 3

fav = da[fav_id]

fav.display()

diffused = fav.post(f'{server_url}', parameters={'skip_rate': 0.6, 'num_images': 4}, target_executor='diffusion').matches

diffused.plot_image_sprites(fig_size=(10,10), show_index=True)


dfav_id = 2

fav = diffused[dfav_id]

fav.display()


fav = fav.post(f'{server_url}/upscale')
fav.display()