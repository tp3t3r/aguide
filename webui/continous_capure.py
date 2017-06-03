#!/usr/bin/env python

import time
import picamera

def filenames():
    frame = 0
    while True:
        time.sleep(0.5)
        yield 'image00.png'

with picamera.PiCamera(framerate=2) as camera:
    time.sleep(2)
    camera.resolution=(640,480)
    camera.vflip=True
    camera.hflip=True   
    camera.framerate=2
    camera.color_effects = (128,128)
    camera.ISO=200
    camera.meter_mode = 'average'

    camera.capture_sequence(filenames(), use_video_port=True, format='png')

