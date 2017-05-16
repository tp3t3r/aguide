#!/usr/bin/env python
import time
from image import Capture,FrameProcessor

C = Capture(width=640, height=480, vflip=True, hflip=True)
print "start", time.time()
data = C.getImage()
fp = FrameProcessor(data, *(C.getSize()))
print "--get", time.time()
fp.applyThreshold(50)
print "--thold", time.time()
fp.saveFrame('buffer_.png')
print "--save", time.time()



