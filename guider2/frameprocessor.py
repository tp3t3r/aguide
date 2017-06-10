import pyproclib

from PIL import Image,ImageDraw

class FrameProcessor():
    def __init__(self, inputfile, outputfile, threshold=170):
        self.outputfile = outputfile
        self.img = Image.open(inputfile)

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

        jpg = img.convert('RGB')
        jpg_overlay = ImageDraw.Draw(jpg)
        if (x != -1 and y != -1):
            jpg_overlay.rectangle( ((x-size, y-size), (x+size,y+size)), None, outline = color)
        jpg.save('evf.jpg', quality=99)


    def getSpotCoordinates(self):
        #luminance data for processing
        imgdata = list(img.convert('L').getdata())
        imgproc.initImage(imgdata)
        imgproc.setThreshold(threshold)
        x,y = imgproc.getSpotCoordinates()
        self.addRectangle(x,y)
        return x,y
