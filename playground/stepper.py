#!/usr/bin/env python

import RPi.GPIO as GPIO ## Import GPIO library
import time, threading, sys

used_pins=[17,18,27,22]

#stepper motor wiring:
#L298 header VCC/NC A/RED B/GREEN C/BLUE D/BLACK

#GPIO related
def configure():
    GPIO.setmode(GPIO.BCM) ## Use board pin numbering
    print used_pins
    for p in used_pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

def setValue(p1,p2,p3,p4):
    if p1:
        GPIO.output(17, GPIO.HIGH)
    else:
        GPIO.output(17, GPIO.LOW)
    if p2:
        GPIO.output(18, GPIO.HIGH)
    else:
        GPIO.output(18, GPIO.LOW)

    if p3:
        GPIO.output(27, GPIO.HIGH)
    else:
        GPIO.output(27, GPIO.LOW)
    if p4:
        GPIO.output(22, GPIO.HIGH)
    else:
        GPIO.output(22, GPIO.LOW)


def cleanup():
    for p in used_pins:
        GPIO.output(p, GPIO.LOW)
    GPIO.cleanup()


sequence = [
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]
]


try:
    def doStep(step):
        print step
        setValue(step[0], step[1], step[2], step[3])
        time.sleep(.01)

    nos = int(sys.argv[1])
    configure()

    if nos > 0:
        while nos:
            nos -= 1
            for step in sequence:
                doStep(step)
    else:
        while nos:
            nos += 1
            for step in sequence[::-1]:
                doStep(step)

except KeyboardInterrupt:
    print "exiting"
finally:
    #GPIO cleanup
    cleanup()

