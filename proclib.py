import ctypes

class proclib():
    def __init__(self, so = "/home/pi/autoguider/proclib/build/src/libimgproc.so"):
        self.lib = ctypes.CDLL(so)

        self.get_lib_version = self.lib.get_lib_version
        self.get_lib_version.argtypes = None
        self.get_lib_version.restype = ctypes.c_char_p

        #apply_threshold(char* img, unsigned width, unsigned height, unsigned char tval);
        self.apply_threshold = self.lib.apply_threshold
        self.apply_threshold.argtypes = [ ctypes.c_void_p, ctypes.c_uint, ctypes.c_uint, ctypes.c_ubyte ]
        self.apply_threshold.restype = ctypes.c_void_p

    def getVer(self):
        return self.get_lib_version()

    def applyThreshold(self, imagedata, tval = 200):
        return self.apply_threshold(imagedata, 640, 480, tval)

