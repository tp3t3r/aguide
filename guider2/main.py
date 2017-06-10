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

def imageProcessor():
    from framefactory import FrameFactory
    with FrameFactory() as cam:
        while Running:
            print "capturing @", time.time()
            cam.capture('/tmp/evf.png')
        

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

    thread_ui.join()
    thread_ch.join()
