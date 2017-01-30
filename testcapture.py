#!/usr/bin/env python
import time
from image import Capture

C = Capture()
C.getImage()
C.saveBuffer('capture.png')


