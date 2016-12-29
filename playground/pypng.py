#!/usr/bin/env python

import png

image = png.Reader("../testimage.png")
try:
    data = image.read()[2]
    for line in data:
        for pixel in line:
            print pixel
except:
    print "shit."
