import png

class Capture:
    def __init__(self):
        pass
    def getImage(self):
        pass

class Processor:
    def __init__(self):
        pass
    def crop(self, image, basearea):
        pass
    def findBrightest(self, image):
        pass
    def getDelta(self, newarea, basearea):
        delta = 0
        return delta

class ImageProcessor:
    def __init__(self, pngfile, border=25, thold=0.9):
        self.img = pngfile
        self.data = []
        self.border = border # pixels
        self.lights = []
        self.thold = thold # factor
        imagedata = None
        try:
            reader = png.Reader(pngfile)
            imagedata = reader.read()
        except:
            raise Exception("File can't be opened")
        print imagedata[3]
        if imagedata[3]['bitdepth'] != 8:
            raise ValueError("Only 8-bit images are supported")
        self.width = imagedata[0]
        self.height = imagedata[1]
        for line in imagedata[2]:
            self.data.append(line)

    def checkTreshold(self, pixel):
        if pixel > 255 * self.thold:
            return True
        return False

    def printMask(self, output="mask.png"):
        writer = png.Writer(self.width, self.height, greyscale=True)
        data = []
        mask_color = 255
        for y in range(self.height):
            line = []
            for x in range(self.width):
                pixel = self.data[y][x]
                '''
                if self.checkTreshold(pixel):
                    pixel = mask_color
                else:
                    pixel = 0
                '''
                line.append(pixel)
                line.append(pixel)
                line.append(pixel)
            data.append(line)
        try:
            mfd = open(output, 'wb')
            writer.write(mfd, data)
        except:
            raise Exception('Can\'t write mask file: %s' % str(output))

    def seekByThreshold(self):
        def checkCoords(x,y):
            if x > self.border and x < self.width - self.border:
                if y > self.border and y < self.height - self.border:
                    return True
            return False

        for y,l in enumerate(self.data):
            for x,p in enumerate(l):
                coords = (x,y)
                if p > 255 * self.thold and checkCoords(x,y):
                    self.lights.append((coords,p))


