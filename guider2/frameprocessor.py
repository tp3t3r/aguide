import pyproclib

from PIL import Image,ImageDraw,ImageOps,ImageFont  

class FrameProcessor():
    def __init__(self, inputfile, outputfile, threshold):
        self.outputfile = outputfile
        self.img = Image.open(inputfile)
        self.proclib = pyproclib.Proclib()
        self.threshold = threshold

    def setThreshold(self, value):
        self.threshold = value

    def lockSpot(self, value):
        print "+++ locking: ", value
        self.proclib.lockSpot(value)

    def addRectangle(self, x, y):
        size = 5
        color = "green"

        jpg = self.img.convert('RGB')
        #jpg = ImageOps.invert(jpg)
        jpg_overlay = ImageDraw.Draw(jpg)
        #font = ImageFont.truetype('/home/pi/.font/Pixeland.ttf', 28)
        if (x != -1 and y != -1):
            jpg_overlay.rectangle( ((x-size, y-size), (x+size,y+size)), None, outline = color)
        jpg.save(self.outputfile, quality=99)

    def getSpotCoordinates(self):
        #luminance data for processing
        imgdata = list(self.img.convert('L').getdata())
        self.proclib.initImage(imgdata)
        self.proclib.setThreshold(self.threshold)
        x,y = self.proclib.getSpotCoordinates()
        self.addRectangle(x,y)
        return x,y
