#!/usr/bin/env python

from image import ImageProcessor

try:
    ip = ImageProcessor('./test2-gs.png')
    ip.printMask()
except Exception as e:
    print str(e)
