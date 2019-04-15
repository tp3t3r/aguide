import time
import RPi.GPIO as GPIO ## Import GPIO library

#type
# 17hd34008-22b

# on raspi:
# GN - ground
# DR - direction
# ST = step
# 2  4  6  8  10 12 14 16 18 20 22 24 26 18 30 32 34 36 38 40
#|  |+5|GN|ST|DR|  |  |  |  |  |  |  |  |  |  |  |  |M1|M2|M3|
#=============================================================
#|  |  |  |  |GN|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

class StepperDriver():
    def __init__(self):
        GPIO.setmode(GPIO.BCM) ## Use board pin numberinga

        # half steps
        GPIO.setup(16, GPIO.OUT)
        GPIO.output(16, GPIO.HIGH)

        GPIO.setup(20, GPIO.OUT)
        GPIO.output(20, GPIO.LOW)

        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21, GPIO.LOW)

        # direction and step
        self.used_pins = [14, 15]
        for pin in self.used_pins:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.LOW)
        self.delay = 0.8

    def __enter__(self):
        return self

    def __exit__(self, *args):
        for pin in self.used_pins + [16, 20, 21]:
            GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup()

    def doStep(self, count):
        if count > 0:
            while count:
                self.setPins(0, 0)
                time.sleep(self.delay)
                self.setPins(0, 1)
                count -= 1
        else:
            while count:
                self.setPins(1, 0)
                time.sleep(self.delay)
                self.setPins(1, 1)
                count += 1

    def setPins(self, p_dir, p_step):
        if p_dir:
            GPIO.output(15, GPIO.HIGH)
        else:
            GPIO.output(15, GPIO.LOW)
        if p_step:
            GPIO.output(14, GPIO.HIGH)
        else:
            GPIO.output(14, GPIO.LOW)


# with StepperDriver() as st:
#    st.doStep(100)
