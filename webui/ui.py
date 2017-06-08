#!/usr/bin/env python
from flask import Flask, render_template, Response, request
import picamera
from PIL import Image, ImageDraw

import sys,time,signal
import numpy
import json
import ctypes

app = Flask(__name__)

#c wrapper
#processing

lproc = ctypes.CDLL('/tmp/libimgproc.so')
initImage = lproc.init_image
                       # width        #height        #pointer
#imagebuffer pointer
imgbuflen = 320 * 240
bufptr = ctypes.POINTER(ctypes.c_byte * imgbuflen)
initImage.argtypes = [ ctypes.c_uint, ctypes.c_uint, bufptr ]
initImage.restype = None

#void apply_threshold(unsigned char tval);
applyThreshold = lproc.apply_threshold
applyThreshold.argtypes = [ ctypes.c_byte ]
applyThreshold.restype = None

#void get_spot_coordinates(int *x, int *y);
getSpotCoordinates = lproc.get_spot_coordinates
getSpotCoordinates.argtypes = [ ctypes.c_void_p, ctypes.c_void_p ]
getSpotCoordinates.restype = None

getBuffer = lproc.get_image_buffer
getBuffer.argtypes = None
getBuffer.restype = bufptr

getVersion = lproc.get_lib_version
getVersion.argtypes = None
getVersion.restype = ctypes.c_char_p


#globals
stats = {}
stats['name'] = 'siriusguider 9000'

state='running'

@app.route('/')
def index():
    return render_template('ui.html')

@app.route('/shutdown', methods=['POST'])
def shutdown(signal, frame):
    print "shutting down..."
    state='not running'

#signal handlers
signal.signal(signal.SIGINT, shutdown) 

def frameFactory():
    with picamera.PiCamera() as camera:
        camera.resolution=(320,240)
        #camera.zoom = (0.25,0.25,0.5,0.5)
        camera.vflip = True
        camera.hflip = True
        camera.led = False
        camera.framerate = 2
        camera.awb_mode = 'sunlight'
        camera.color_effects = (128,128)
        camera.shutter_speed = 400000
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
            #luminance data for processing
            l_img = im.convert('L')
            imgdata = list(l_img.getdata())
            print 'orig:', len(imgdata), imgdata[0:15]
            

            print "x", type(bufptr)
            print "z", type (ctypes.c_byte * len(imgdata))
            initImage(320,240, (ctypes.c_byte * len(imgdata))(*imgdata) )
            #applyThreshold(200)
            print getVersion()
            imgbuf = getBuffer().contents
            print 'lib: ', len(imgbuf), imgbuf[0:15]
            x = ctypes.c_int()
            y = ctypes.c_int()
            getSpotCoordinates(ctypes.byref(x), ctypes.byref(y))
            print "spot: ", x.value, ":", y.value

            #add overlay
            jpg = im.convert('RGB')
            jpg_overlay = ImageDraw.Draw(jpg)
            jpg_overlay.rectangle(((x.value - 5,y.value - 5 ),(x.value + 5,y.value +5)), None, outline = "green")
            jpg.save('evf.jpg', quality=90)

            #processing stats
            stats['frames'] += 1
            stats['fps'] = "%.2f" % (float(stats['frames']) / (time.time() - now))
            #print stats
    
            #jpeg for live view
            frame = open('evf.jpg').read()
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=False, debug=False)

