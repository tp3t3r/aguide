#!/usr/bin/env python
import time
from image import Capture,FrameProcessor

C = Capture(width=640, height=480, vflip=True, hflip=True)
fp = FrameProcessor(C.getImage(), *(C.getSize()))
fp.getLibVersion()
fp.applyThreshold()
fp.saveBuffer('buffer.png')



