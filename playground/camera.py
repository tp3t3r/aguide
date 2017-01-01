#!/usr/bin/env python

import picamera
import time

camera = picamera.PiCamera()
camera.resolution = (640,480)
camera.exposure_mode = 'night'
camera.shutter_speed = 200000
camera.ISO = 800
#camera.shutter_speed = 30000000
#print camera.EXPOSURE_MODES
for i in range(100):
    camera.capture('capture_' + str(i+100) + '.png')
    print 'captured: ' + str(i)
    time.sleep(30)
