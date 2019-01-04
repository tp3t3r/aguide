#!/usr/bin/env python

import RPi.GPIO as GPIO ## Import GPIO library
import time, threading, sys

used_pins=[12,16,20,21]

#stepper motor wiring:
#out
#L298 header VCC/NC A/RED B/GREEN C/BLUE D/BLACK

#in
#INA/PUPRLE INB/BLUE INC/GREEN IND/YELLOW

#common
#G on raspi is connected to driver's common

# on raspi:
# 2  4  6  8 10 12 14 16 18 20 22 24 26 18 30 32 34 36 38 40
|  |  |G |  |  |P |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
=============================================================
|  |  |  |  |  |B |Y |G |  |  |  |  |  |  |  |  |  |  |  |  |


#GPIO related
def configure():
    GPIO.setmode(GPIO.BCM) ## Use board pin numbering
    print used_pins
    for p in used_pins:
        GPIO.setup(p, GPIO.OUT)
        GPIO.output(p, GPIO.LOW)

def setValue(p1,p2,p3,p4):
    if p1:
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(12, GPIO.LOW)
    if p2:
        GPIO.output(16, GPIO.HIGH)
    else:
        GPIO.output(16, GPIO.LOW)

    if p3:
        GPIO.output(20, GPIO.HIGH)
    else:
        GPIO.output(20, GPIO.LOW)
    if p4:
        GPIO.output(21, GPIO.HIGH)
    else:
        GPIO.output(21, GPIO.LOW)


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
        time.sleep(2)

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
except IndexError:
    print "step count has to be provided"
    sys.exit(1)
finally:
    #GPIO cleanup
    cleanup()

