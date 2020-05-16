#!/usr/bin/env python

from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
from time import sleep
i=0
while True:
    img = Image.new('RGBA', (320,240), (0,0,0,255))
    draw = ImageDraw.Draw(img)
    draw.text((2,2), datetime.now().strftime("%d/%m/%Y %H:%M:%S"), (0,160,0))
    diameter = 4
    i=i%200
    draw.ellipse([(10+i,10+i), (10+diameter+i,10+diameter+i)], fill=(255,255,255,255), outline=(100,100,100,255))
    img.save('evf.png')
    i=i+1
    sleep(4.2)
