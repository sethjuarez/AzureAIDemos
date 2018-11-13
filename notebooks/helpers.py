import os
import json
import requests
import numpy as np
from io import BytesIO
from IPython.display import display
from PIL import Image, ImageDraw, ImageFont

def get_image(location):
    if location.startswith('http'):
        r = requests.get(location)
        im = Image.open(BytesIO(r.content))
        return im
    else:
        return Image.open(location)

def draw_faces(im, items, caption=None):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', 16, encoding='unic')
    for item in items:
        rect = item['faceRectangle']
        r =[rect['left'], rect['top'], rect['left']+rect['width'], rect['top']+rect['height']]
        draw.rectangle(r, outline='#FF0000')
                        
        s = '{0} ({1})'.format(item['gender'], item['age'])
        draw.text((rect['left'], rect['top']), s, 
                  font=font, fill=(0, 0, 0, 255))
        
    if caption != None:
        font = ImageFont.truetype('arial.ttf', 24, encoding='unic')
        draw.text((10, 10), caption, font=font, fill=(255, 255, 255, 255))
    del draw
    return im