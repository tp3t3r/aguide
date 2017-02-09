from PIL import Image
import time, picamera, numpy

class Capture:
    def __init__(self, width=640, height=480, vflip = False, hflip = False):
        self.width=width
        self.height=height
        self.itype='rgb'
        self.cam = picamera.PiCamera()
        self.cam.resolution=((self.width, self.height))
        self.cam.vflip = vflip
        self.cam.hflip = hflip
        self.cam.framerate = 2
        self.cam.color_effects = (128,128)
        #print self.cam.color_effects
        self.cam.exposure_mode ='verylong'
        #print self.cam.exposure_mode
        self.cam.shutter_speed = 400000
        #print self.cam.shutter_speed
        self.cam.awb_mode = 'tungsten'
        #print self.cam.awb_mode
        self.cam.meter_mode = 'average'
        #print self.cam.meter_mode
        self.cam.ISO = 800
        #print self.cam.ISO
        self.frame = numpy.empty((self.width * self.height * 3,), dtype=numpy.uint8)
        #self.frame_gs = numpy.empty((self.width * self.height,), dtype=numpy.uint8)
        self.frame_gs = []
        time.sleep(2)

    def getSize(self):
        return (self.width,self.height)

    def getImage(self):
        import time
        self.cam.capture(self.frame, self.itype)
        #keep every third value per pixel - it's grayscale anyways...
        self.frame_gs = [ pix for pix in self.frame[::3] ]
        return self.frame_gs

    def saveBuffer(self, filename):
        imggs = Image.new('L', (self.width, self.height))
        imggs.putdata(self.frame_gs)
        imggs.save(filename)

class FrameProcessor:
    def __init__(self, framedata, width, height):
        self.frame = framedata
        self.width = width
        self.height = height

        from proclib import proclib
        self.proclib = proclib()

    #wrapped from proclib
    def applyThreshold(self, tval = 50):
        self.frame = self.proclib.applyThreshold(self.frame, tval)
        #self.frame = [ 255 if x > tval else x for x in self.frame ]

    #wrapped from proclib
    def getLibVersion(self):
        self.proclib.getVer()

    def saveFrame(self, filename):
        img = Image.new('L', (self.width, self.height))
        img.putdata(self.frame)
        img.save(filename)

    def findBrightest(grid = 20):
        if self.width % grid or self.height % grid:
            raise ValueError("invalid width/height")
        maxVal = 0
