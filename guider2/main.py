#!/usr/bin/env python

import threading
import time
import signal
import sys


#redirect
sys.stderr = sys.stdout

Running = True
def shutdown(signal, frame):
    print "Shutting down..."
    global Running
    Running = False;

signal.signal(signal.SIGINT, shutdown)
signal.signal(signal.SIGTERM, shutdown)

#globals
lock = threading.RLock()
spotx = -1
spoty = -1

def imageProcessor():
    from framefactory import FrameFactory
    from frameprocessor import FrameProcessor

    infile = 'evf.png'
    evffile = 'evf.jpg'

    cam = FrameFactory()
    while Running:
        print "capturing @", time.time()
        cam.capture(infile)
        proc = FrameProcessor(infile, evffile)
        x,y = proc.getSpotCoordinates()
        with lock:
            spotx = x
            spoty = y
        

def uiHandler():
        while Running:
            print "webserver"
            time.sleep(5)
    
if __name__ == "__main__":            
    thread_ui = threading.Thread(target=uiHandler)
    thread_ch = threading.Thread(target=imageProcessor)

    thread_ui.start()
    thread_ch.start()

    while Running:
        print "main thread"
        time.sleep(2)

    #exiting
    thread_ui.join()
    thread_ch.join()

