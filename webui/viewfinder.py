#!/usr/bin/env python
import picamera
from PIL import Image, ImageDraw

import sys,time
import numpy
import json
import ctypes

#c wrapper
#processing

lproc = ctypes.CDLL('/tmp/libimgproc.so')
initImage = lproc.init_image
                       # width        #height        #pointer
#imagebuffer pointer
imgbuflen = 320 * 240
bufptr = ctypes.POINTER(ctypes.c_ubyte * imgbuflen)
initImage.argtypes = [ ctypes.c_uint, ctypes.c_uint, bufptr ]
initImage.restype = None

#void get_spot_coordinates(int *x, int *y);
getSpotCoordinates = lproc.get_spot_coordinates
getSpotCoordinates.argtypes = [ ctypes.c_void_p, ctypes.c_void_p ]
getSpotCoordinates.restype = None

getBuffer = lproc.get_image_buffer
getBuffer.argtypes = None
getBuffer.restype = bufptr

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

        count = 0
        points = []
        while True:
            camera.capture('evf.png', use_video_port=True, format='png')
            im = Image.open('evf.png')

            #luminance data for processing
            l_img = im.convert('L')
            imgdata = list(l_img.getdata())

            initImage(320,240, (ctypes.c_ubyte * len(imgdata))(*imgdata) )
            #imgbuf = getBuffer().contents

            x = ctypes.c_int()
            y = ctypes.c_int()
            getSpotCoordinates(ctypes.byref(x), ctypes.byref(y))
            print "spot: ", x.value, ":", y.value

            #add overlay
            jpg = im.convert('RGB')
            jpg_overlay = ImageDraw.Draw(jpg)
            if (x.value != -1 and y.value != -1):
                jpg_overlay.rectangle(((x.value - 5,y.value - 5 ),(x.value + 5,y.value +5)), None, outline = "green")
                #add tracer
                if  count % 25 == 0:
                    points.append((x.value, y.value))
                for p in points:        
                    jpg_overlay.point(p, "blue")
                count += 1

            jpg.save('evf.jpg', quality=99)

if __name__ == '__main__':
    frameFactory()

