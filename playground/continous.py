#!/usr/bin/env python
import time
import picamera
with picamera.PiCamera() as camera:
    camera.framerate = 20
    camera.shutter_speed = 100000
    camera.width = 320
    camera.height = 240
    camera.start_preview()
    try:
        data = None
        for i,x in enumerate(camera.capture_continuous(data, 'rgb')):
            print i, time.time()
            if i == 5:
                break
        print repr(data)
    finally:
        camera.stop_preview()
