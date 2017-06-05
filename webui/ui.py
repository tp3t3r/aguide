#!/usr/bin/env python
from flask import Flask, render_template, Response
import picamera
from PIL import Image
import sys,time
#from camera import Camera

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ui.html')

def frameFactory():
    with picamera.PiCamera() as camera:
        #camera.resolution=(640,480)
        camera.resolution=(320,240)
        camera.zoom = (0.25,0.25,0.5,0.5)
        camera.vflip = True
        camera.hflip = True
        #camera.led = False
        camera.framerate = 2
        camera.awb_mode = 'sunlight'
        camera.exposure_mode = 'off'
        camera.color_effects = (128,128)
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
            camera.capture('evf.png', use_video_port=True, format='png')
            im = Image.open('evf.png')
            jpg = im.convert('RGB')
            jpg.save('evf.jpg')
            frame = open('evf.jpg').read()
    
            #frame contains jpeg
            yield (b'--frame\r\n' 
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(frameFactory(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)

