#!/usr/bin/env python
import time
from image import Capture,FrameProcessor

C = Capture(width=640, height=480, vflip=True, hflip=True)
for i in range(10):
    print "start", time.time()
    data = C.getImage()
    fp = FrameProcessor(data, *(C.getSize()))
    fpo = FrameProcessor(data, *(C.getSize()))
    print "--get", time.time()
    fp.applyThreshold(50)
    fpo.applyThreshold(255)
    print "--thold", time.time()
    fp.saveFrame('buffer_' + str(i) + '.png')
    fpo.saveFrame('buffer_orig_' + str(i) + '.png')
    print "--save", time.time()
    time.sleep(10);



