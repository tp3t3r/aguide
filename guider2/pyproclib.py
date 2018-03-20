import ctypes

class Proclib:
    def __init__(self, so='/tmp/libprod-imgproc.so'):
    #def __init__(self, so='/usr/lib/libprod-imgproc.so'):

        self.width = 320
        self.height = 240
        self.resolution = self.width * self.height
        self.buffer_type = ctypes.POINTER(ctypes.c_ubyte * self.resolution)

        self.lib =  ctypes.CDLL(so)

        self.init_image = self.lib.init_image
        self.init_image.argtypes = [ ctypes.c_uint, ctypes.c_uint, self.buffer_type,  ctypes.c_uint]
        self.init_image.restype = None

        self.get_spot_coordinates = self.lib.get_spot_coordinates
        self.get_spot_coordinates.argtypes = [ ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int ]
        self.get_spot_coordinates.restype = None

        self.set_threshold = self.lib.set_threshold
        self.set_threshold.argtypes = [ ctypes.c_int ]
        self.set_threshold.restype = None

        self.get_image_buffer = self.lib.get_image_buffer
        self.get_image_buffer.argtypes = None
        self.get_image_buffer.restype = self.buffer_type

    def initImage(self, data):
        #fixed size and slice size
        self.init_image(320,240, (ctypes.c_ubyte * self.resolution)(*data), 16)

    def getSpotCoordinates(self, locked):
        x = ctypes.c_int()
        y = ctypes.c_int()
        self.get_spot_coordinates(ctypes.byref(x), ctypes.byref(y), locked)
        return (x.value,y.value)

    def setThreshold(self,th):
        self.set_threshold(th)

