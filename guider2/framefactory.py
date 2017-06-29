#!/usr/bin/env python
import picamera
import time
import numpy

class FrameFactory():
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution=(320,240)
        #self.camera.zoom = (0.125,0.125,0.75,0.75)
        self.camera.vflip = True
        self.camera.hflip = True
        self.camera.led = False
        self.camera.framerate = 0.5
        self.camera.awb_mode = 'sunlight'
        self.camera.color_effects = (128,128)
        self.camera.shutter_speed = 800000
        self.camera.ISO=800
        self.camera.meter_mode = 'average'
        print 'Setting up camera...'
        time.sleep(10)
        print 'OK\n'
        self.camera.exposure_mode = 'off'
        self.framedata = numpy.empty((320 * 240 * 3,), dtype=numpy.uint8)

    def capture(self, pngfile):
        self.camera.capture(pngfile, use_video_port=True, format='png')
