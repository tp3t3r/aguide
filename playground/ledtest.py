#!/usr/bin/env python

import RPi.GPIO as GPIO ## Import GPIO library
import time, threading, sys

#globals
enableBlink = False
t = None
running = True

#GPIO related
def configure():
    GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
    GPIO.setup(7, GPIO.OUT) ## Setup GPIO Pin 7 to OUT
    GPIO.output(7, GPIO.LOW)
    GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cleanup():
    GPIO.output(7, GPIO.LOW)
    GPIO.cleanup()

#thread specific
def blink():
    global enableBlink
    global running
    while running:
        if enableBlink:
            GPIO.output(7,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(7,GPIO.LOW)
            time.sleep(0.5)


configure()

#working thread
t = threading.Thread(target=blink, )
t.start()

#main thread
try:
    while True:
        state = GPIO.input(11)
        if not state:
            if not enableBlink:
                print "on"
                enableBlink = True
            else:
                print "off"
                enableBlink = False
            time.sleep(1.0)
except KeyboardInterrupt:
    print "exiting"
    running = False
finally:
    #GPIO cleanup
    cleanup()
