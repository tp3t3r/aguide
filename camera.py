#!/usr/bin/env python

import picamera

camera = picamera.PiCamera()
for i in range(1,10):
    camera.capture('image' + str(i) + '.png')
    print i
