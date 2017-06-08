import ctypes

#globals
imgbuflen = 320 * 240
bufptr = ctypes.POINTER(ctypes.c_ubyte * imgbuflen)

class proclib():
    def __init__(self, so = "/tmp/libimgproc.so"):
        self.lib = ctypes.CDLL(so)

        self.initImage = self.lib.init_image
        self.initImage.argtypes = [ ctypes.c_uint, ctypes.c_uint, bufptr ]
        self.initImage.restype = None

        self.applyThreshold = self.lib.apply_threshold
        self.applyThreshold.argtypes = [ ctypes.c_ubyte ]
        self.applyThreshold.restype = None

        #void get_spot_coordinates(int *x, int *y);
        self.getSpotCoordinates = self.lib.get_spot_coordinates
        self.getSpotCoordinates.argtypes = [ ctypes.c_void_p, ctypes.c_void_p ]
        self.getSpotCoordinates.restype = None

        self.getBuffer = self.lib.get_image_buffer
        self.getBuffer.argtypes = None
        #self.getBuffer.restype = bufptr
        self.getBuffer.restype =  ctypes.POINTER(ctypes.c_ubyte)

from PIL import Image
import sys
testimage = Image.open(sys.argv[1])
tlum = testimage.convert('L')
data = list(tlum.getdata())

plib = proclib()
plib.initImage(320,240,(ctypes.c_ubyte * len(data))(*data) )        
buffer1 = plib.getBuffer()
plib.applyThreshold(220)
print buffer2[100:130]

x = ctypes.c_int() 
y = ctypes.c_int()
plib.getSpotCoordinates(ctypes.byref(x), ctypes.byref(y))
plib.getSpotCoordinates(ctypes.byref(x), ctypes.byref(y))

plib.getSpotCoordinates(ctypes.byref(x), ctypes.byref(y))

plib.getSpotCoordinates(ctypes.byref(x), ctypes.byref(y))

plib.getSpotCoordinates(ctypes.byref(x), ctypes.byref(y))


print "spot: ", x.value, ":", y.value
