import pyproclib

from PIL import Image,ImageDraw,ImageOps    

class FrameProcessor():
    def __init__(self, inputfile, outputfile, threshold=170):
        self.outputfile = outputfile
        self.img = Image.open(inputfile)
        self.proclib = pyproclib.Proclib()
        self.threshold = 220

    def lockSpot(value):
        if value:
            #lock
            pass
        else:
            #unlock
            pass

    def addRectangle(self, x, y):
        size = 5
        color = "green"

        jpg = self.img.convert('RGB')
        jpg = ImageOps.invert(jpg)
        jpg_overlay = ImageDraw.Draw(jpg)
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
