#!/usr/bin/env python

import time,sys,os
import picamera

try:
    with picamera.PiCamera() as camera:

        camera.resolution=(640,480)
        #camera.zoom = (0.25,0.25,0.125,0.125)
        camera.vflip = True
        camera.hflip = True
        #camera.led = False
        camera.framerate = 2
        camera.awb_mode = 'sunlight'
        
        '''
        camera.exposure_mode = 'off'
        camera.color_effects = (128,128)
        camera.shutter_speed = 400000
        camera.ISO=800
        camera.meter_mode = 'average'
        '''
        print "getting ready..."
        time.sleep(3)
        print "go!"
       

        fname='evf.png'
        fname_tmp='.evf.png' 
        while True:
            print time.time()
            camera.capture('.evf.png', use_video_port=True, format='png')
            os.rename('.evf.png', 'evf.png')
except KeyboardInterrupt:
    print "exiting..."
    sys.exit()
except Exception as e:
    print "terrible thing happened"
    print e
    sys.exit()

