#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 19:34:00 2022

@author: inathero
"""

import pickle
from docarray import Document

from PIL import Image

with open('main.pckl', 'rb') as in_file:
  darry = pickle.load(in_file) #why doesn't this just save, annoying
a = darry[0]
b = a.load_uri_to_image_tensor()
c = Image.fromarray(b.tensor)
d = c.resize((1920,1080), resample=Image.BOX)
d.save('tester.png')
# a.save_image_tensor_to_file