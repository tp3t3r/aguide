#!/usr/bin/env python
import time
from image import Capture

C = Capture(width=1280, height=960, vflip=True, hflip=True)
C.getImage()
C.saveBuffer('capture.png')


