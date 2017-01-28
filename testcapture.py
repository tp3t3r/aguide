#!/usr/bin/env python

from image import Capture
from PIL import Image

C = Capture()
data = C.getImage()
C.saveBuffer('capture.png')

