from PIL import Image
import time, picamera, numpy

class Capture:
    def __init__(self, width=640, height=480, vflip = False, hflip = False):
        self.width=width
        self.height=height
        self.itype='rgb'
        self.cam = picamera.PiCamera()
        self.cam.resolution=((self.width, self.height))
        self.cam.awb_mode = 'auto'
        self.cam.vflip = vflip
        self.cam.hflip = hflip
        self.cam.color_effects = (128,128)
        self.cam.exposure_mode ='nightpreview'
        #self.cam.shutter_speed = 1000000
        self.cam.meter_mode = 'average'
        self.cam.ISO = 800
        self.frame = numpy.empty((self.width * self.height * 3,), dtype=numpy.uint8)
        #self.frame_gs = numpy.empty((self.width * self.height,), dtype=numpy.uint8)
        self.frame_gs = []
        time.sleep(2)

    def getSize(self):
        return (self.width,self.height)

    def getImage(self):
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

    def findBrightest(grid = 20):
        if self.width % grid or self.height % grid:
            raise ValueError("invalid width/height")
        maxVal = 0
