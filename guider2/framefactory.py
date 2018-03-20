import time
import glob
import shutil

class FrameFactory():
    def __init__(self):
        import picamera
        self.camera = picamera.PiCamera()
        self.camera.resolution=(320,240)
        #self.camera.zoom = (0.125,0.125,0.75,0.75)
        self.camera.vflip = True
        self.camera.hflip = True
        self.camera.led = False
        self.camera.framerate = 1.0
        self.camera.awb_mode = 'sunlight'
        self.camera.color_effects = (128,128)
        self.camera.shutter_speed = 700000
        self.camera.ISO=800
        self.camera.meter_mode = 'average'
        print 'Setting up camera...'
        time.sleep(10)
        print 'OK\n'
        self.camera.exposure_mode = 'off'

    def setShutterSpeed(self, value):
        if abs(value - self.camera.shutter_speed) > 100:
            self.camera.shutter_speed = value
            return self.camera.shutter_speed
        return False

    def capture(self, pngfile):
        self.camera.capture(pngfile, use_video_port=True, format='png')


class CapturedFactory():
    def __init__(self, filepattern):
        self.filepattern = filepattern
        self.filelist = glob.glob(filepattern)
        self.index = 0

    def setShutterSpeed(self, value):
        pass

    def capture(self, pngfile):
        nextfile = None
        if self.filelist:
            nextfile = self.filelist[self.index % len(self.filelist)]
            print "nextfile:", nextfile
            shutil.copyfile(nextfile, pngfile)
            self.index += 1
        time.sleep(0.8)
