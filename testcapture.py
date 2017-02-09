#!/usr/bin/env python
import time
from image import Capture,FrameProcessor

C = Capture(width=640, height=480, vflip=True, hflip=True)
for v in range(0,255, 30):
    print "start", time.time()
    fp = FrameProcessor(C.getImage(), *(C.getSize()))
    print "--get", time.time()
    fp.applyThreshold(v)
    print "--thold", time.time()
    fp.saveFrame('buffer_' + str(v) + '.png')
    print "--save", time.time()



