#!/usr/bin/env python
import picamera
from PIL import Image, ImageDraw

import sys,time
import numpy
import json
import ctypes
import pyproclib

def frameFactory():
    with picamera.PiCamera() as camera:
        camera.resolution=(320,240)
        #camera.zoom = (0.25,0.25,0.5,0.5)
        camera.vflip = True
        camera.hflip = True
        camera.led = False
        camera.framerate = 1
        camera.awb_mode = 'sunlight'
        camera.color_effects = (128,128)
        camera.shutter_speed = 500000
        camera.ISO=800
        camera.meter_mode = 'average'
        print "getting ready..."
        time.sleep(5)
        camera.exposure_mode = 'off'
        print "go!"

        framedata = numpy.empty((320 * 240 * 3,), dtype=numpy.uint8)

        imgproc = pyproclib.Proclib()

        while True:
            camera.capture('evf.png', use_video_port=True, format='png')
            im = Image.open('evf.png')

            #luminance data for processing
            imgdata = list(im.convert('L').getdata())

            imgproc.initImage(imgdata)
            #imgproc.setThreshold(40)

            x,y = imgproc.getSpotCoordinates()

            #add overlay
            jpg = im.convert('RGB')
            jpg_overlay = ImageDraw.Draw(jpg)
            if (x != -1 and y != -1):
                jpg_overlay.rectangle( ((x-5, y-5), (x+5,y+5)), None, outline = "green")

            jpg.save('evf.jpg', quality=99)

if __name__ == '__main__':
    frameFactory()

