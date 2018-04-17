#!/usr/bin/env python

from PIL import Image, ImageDraw

for i in range(100):
    img = Image.new('RGBA', (320,240), (0,0,0,255))
    draw = ImageDraw.Draw(img)

    diameter = 2.5
    draw.ellipse([(10+i,10+i), (10+diameter+i,10+diameter+i)], fill=(255,255,255,255), outline=(100,100,100,255))
    img.save('test_frame_%03d.png' % i)
