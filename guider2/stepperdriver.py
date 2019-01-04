import time
import RPi.GPIO as GPIO ## Import GPIO library

#type
# 17hd34008-22b

#stepper motor wiring:
#out
#L298 header VCC/NC A/RED B/GREEN C/BLUE D/BLACK

#in
#INA/PUPRLE INB/BLUE INC/GREEN IND/YELLOW

#common
#G on raspi is connected to driver's common

# on raspi:
# 2  4  6  8 10 12 14 16 18 20 22 24 26 18 30 32 34 36 38 40
#|  |  |G |  |  |P |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
#=============================================================
#|  |  |  |  |  |B |Y |G |  |  |  |  |  |  |  |  |  |  |  |  |

class StepperDriver():
    def __init__(self):
        GPIO.setmode(GPIO.BCM) ## Use board pin numbering
        self.used_pins = [17, 18, 27, 22]
        self.sequence = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.delay = 0.05

        for pin in self.used_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)

    def __enter__(self):
        pass

    def __exit__(self, *args):
        for pin in self.used_pins:
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()

    def doStep(self, count):
        if count > 0:
            while count:
                count -= 1
                for step in self.sequence:
                    self.setPins(step[0], step[1], step[2], step[3])
                    time.sleep(self.delay)
        else:
            while count:
                count += 1
                for step in self.sequence[::-1]:
                    self.setPins(step[0], step[1], step[2], step[3])
                    time.sleep(self.delay)

    def setPins(self, p1, p2, p3, p4):
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
