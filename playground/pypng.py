#!/usr/bin/env python

import png

image = png.Reader("../testimage.png")
try:
    data = image.read()
    print data[0], data[1]
    print data[3]
    for line in data:
        pass
        #for pixel in line:
        #    print pixel
except:
    print "shit."
