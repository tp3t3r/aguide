import pyproclib

from PIL import Image,ImageDraw,ImageOps,ImageFont  

class FrameProcessor():
    def __init__(self, inputfile, outputfile, threshold):
        self.outputfile = outputfile
        self.img = Image.open(inputfile)
        self.proclib = pyproclib.Proclib()
        self.threshold = threshold
        self.locked = False

    def setThreshold(self, value):
        self.threshold = value

    def lockSpot(self, value):
        self.locked = value

    def addRectangle(self, x, y):
        size = 5
        color = "green"

        jpg = self.img.convert('RGB')
        #jpg = ImageOps.invert(jpg)
        jpg_overlay = ImageDraw.Draw(jpg)
        #font = ImageFont.truetype('/home/pi/.font/Pixeland.ttf', 28)
        if (x != -1 and y != -1):
            jpg_overlay.rectangle( ((x-size, y-size), (x+size,y+size)), None, outline = color)
            #if self.locked:
            #    jpg_overlay.text((0, 0),"[locked]",(255,0,0),font=font)
            #else:
            #    jpg_overlay.text((0, 0),"[freerun]",(0,255,0),font=font)
        jpg.save(self.outputfile, quality=99)

    def writeJson(self, x, y, filename='spotdata.json'):
        with open(filename + '.tmp', 'w') as fd:
            fd.write('{ "x": %d, "y": %d }' % (x,y))
        from os import rename
        try:
            rename(filename + '.tmp', filename)
        except: pass

    def getSpotCoordinates(self):
        #luminance data for processing
        imgdata = list(self.img.convert('L').getdata())
        self.proclib.initImage(imgdata)
        self.proclib.setThreshold(self.threshold)
        x,y = self.proclib.getSpotCoordinates()
        self.addRectangle(x,y)
        self.writeJson(x,y)
        return x,y
