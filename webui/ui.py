#!/usr/bin/env python
from flask import Flask, render_template, Response
import picamera
from PIL import Image

import sys,time,signal
import numpy
import json

app = Flask(__name__)

#globals
stats = {}
stats['name'] = 'siriusguider 9000'
state='running'

@app.route('/')
def index():
    return render_template('ui.html')

def frameFactory():
    with picamera.PiCamera() as camera:
        #camera.resolution=(640,480)
        camera.resolution=(320,240)
        #camera.zoom = (0.25,0.25,0.5,0.5)
        camera.vflip = True
        camera.hflip = True
        camera.led = False
        camera.framerate = .1
        camera.awb_mode = 'sunlight'
        camera.exposure_mode = 'off'
        camera.color_effects = (128,128)
        camera.shutter_speed = 500000
        camera.ISO=800
        camera.meter_mode = 'average'
        print "getting ready..."
        time.sleep(5)
        camera.exposure_mode = 'off'
        print "go!"

        stats['frames'] = 0
        now = time.time()

        framedata = numpy.empty((320 * 240 * 3,), dtype=numpy.uint8)
        stats['fps'] = 0.0

        while True and state == 'running':
            '''
            #new way
            camera.capture(framedata, use_video_port=True, format='rgb')
            jpg = Image.new('RGB', (320,240))
            it = iter(framedata)
            framedata_tuples = zip(it,it,it) # R,G,B pixels as a tuple
            jpg.putdata(framedata_tuples) # should be 'L' for grayscale
            jpg.save('evf.jpg')

            it = None
            '''
            #traditional way
            camera.capture('evf.png', use_video_port=True, format='png')
            im = Image.open('evf.png')

            #jpeg for live view
            jpg = im.convert('RGB')
            jpg.save('evf.jpg')
            frame = open('evf.jpg').read()

            #luminance data for processing
            l_img = im.convert('L')
            stats['frames'] += 1
            stats['fps'] = "%.2f" % (float(stats['frames']) / (time.time() - now))
    
            #frame contains jpeg
            yield (b'--frame\r\n' 
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(frameFactory(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/stats.json')
def proc_stats_data():
    data = json.dumps(stats)
    #print data
    return(data)

@app.route('/stats.js')
def proc_stats_reader():
    return app.send_static_file('stats.js')


def shutdown(signal, frame):
    print "shutting down..."
    state='not running anymore'

signal.signal(signal.SIGINT, shutdown)

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True, debug=False)

