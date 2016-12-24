#!/usr/bin/env python

#Capture: implements rpi camera interface
#Processor: does the image processing part
from image import Capture, Processor

#stepperDriver uses GPIO
from stepperDriver import stepperDriver

def main():
    #get an image
    cpt = Capture()
    skyline = cpt.getImage()

    #find the brightest spot
    proc = Processor()
    base_area = proc.findBrightest(skyline)

    #stepper's command
    threshold = 2
    stepper = stepperDriver(threshold)
    move = 0
    while True:
        #get another image - from the same area
        new_area = proc.crop(cpt.getImage(), base_area)

        #calcuate delta
        command = proc.getDelta(new_area, base_area)

        #actuation
        stepper.act(command)

        #start over the whole loop after a while
        base_area = new_area
        #time.sleep...

#let the magic begin
if __name__ == '__main__':
    main()
