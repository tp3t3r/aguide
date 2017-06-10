#!/usr/bin/env python
import picamera
import time
import numpy

class FrameFactory():
    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution=(320,240)
        #self.camera.zoom = (0.25,0.25,0.5,0.5)
        self.camera.vflip = True
        self.camera.hflip = True
        self.camera.led = False
        self.camera.framerate = 1
        self.camera.awb_mode = 'sunlight'
        self.camera.color_effects = (128,128)
        self.camera.shutter_speed = 500000
        self.camera.ISO=800
        self.camera.meter_mode = 'average'
        time.sleep(7)
        self.camera.exposure_mode = 'off'

        #self.imgproc = pyproclib.Proclib()
        self.framedata = numpy.empty((320 * 240 * 3,), dtype=numpy.uint8)

    def __exit__(self, exc_type, exc_value, traceback):
        return True

    def capture(self, pngfile):
        camera.capture(pngfile, use_video_port=True, format='png')
    '''
    def frameFactory():
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
    '''
