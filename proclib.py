import ctypes

class proclib():
    def __init__(self, so = "/home/pi/autoguider/proclib/build/src/libimgproc.so"):
        self.lib = ctypes.CDLL(so)

        self.get_lib_version = self.lib.get_lib_version
        self.get_lib_version.argtypes = None
        self.get_lib_version.restype = ctypes.c_char_p

        #apply_threshold(char* img, unsigned width, unsigned height, unsigned char tval);
        self.apply_threshold = self.lib.apply_threshold
        self.apply_threshold.argtypes = [ ctypes.POINTER(ctypes.c_ubyte), ctypes.c_uint, ctypes.c_uint, ctypes.c_ubyte ]
        self.apply_threshold.restype = ctypes.c_void_p

    def getVer(self):
        return self.get_lib_version()

    def applyThreshold(self, imagedata, tval = 200):
        raw_data_ptr = (ctypes.c_ubyte * len(imagedata))(*imagedata)
        width=640
        height=480
        dataptr = self.apply_threshold(raw_data_ptr, width, height, tval)
        dataptr = ctypes.cast(dataptr, ctypes.POINTER(ctypes.c_ubyte))
        return [dataptr[i] for i in range(width*height)]
        '''
        print type(x)
        print repr(x)
        print len(x)
        '''
        


