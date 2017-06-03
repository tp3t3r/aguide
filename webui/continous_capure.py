#!/usr/bin/env python

import time,sys
import picamera

def filenames():
    frame = 0
    while True:
        frame = frame + 1
        filename = 'image%02d.png' % (frame % 2)
        time.sleep(0.5)
        yield filename


try:
    with picamera.PiCamera() as camera:
        camera.resolution=(640,480)
        camera.vflip = True
        camera.hflip = True
        #camera.led = False
        camera.framerate = 1
        camera.exposure_mode ='off'
        camera.color_effects = (128,128)
        camera.shutter_speed = 400000
        camera.ISO=800
        camera.meter_mode = 'average'
        print "getting ready..."
        time.sleep(5)
        print "go!"
        camera.capture_sequence(filenames(), use_video_port=True, format='png')
except KeyboardInterrupt:
    print "exiting..."
    sys.exit()
except:
    print "terrible thing happened"
    sys.exit()

