import ctypes

class proclib():
    def __init__(self, so = "/tmp/libimgproc.so"):
        self.lib = ctypes.CDLL(so)

        self.get_lib_version = self.lib.get_lib_version
        self.get_lib_version.argtypes = None
        self.get_lib_version.restype = ctypes.c_char_p

        #void init_image(unsigned width, unsigned height, const unsigned char* data);
        self.init_image = self.lib.init_image
        self.init_image.argtypes = [ ctypes.c_uint, ctypes.c_uint, ctypes.c_char_p ]
        self.init_image.restype = None

        #void apply_threshold(unsigned char tval);
        self.apply_threshold = self.lib.apply_threshold
        self.apply_threshold.argtypes = [ ctypes.c_ubyte ]
        self.apply_threshold.restype = None

        #void get_spot_coordinates(int *x, int *y);
        self.get_spot_coordinates = self.lib.get_spot_coordinates
        self.get_spot_coordinates.argtypes = [ ctypes.c_void_p, ctypes.c_void_p ]
        self.get_spot_coordinates.restype = None

        #const unsigned char* get_image_buffer(void);
        self.get_image_buffer = self.lib.get_image_buffer
        self.get_image_buffer.argtypes = None
        self.apply_threshold.restype = ctypes.c_char_p


    def getVer(self):
        return self.get_lib_version()

    def getSpotCoordinates(self):
        x = ctypes.c_void_p()
        y = ctypes.c_void_p()
        self.get_spot_coordinates(x, y)
        return x.contents, y.contents

    def applyThreshold(self, imagedata, tval = 200):
        raw_data_ptr = (ctypes.c_ubyte * len(imagedata))(*imagedata)
        width=640
        height=480
        dataptr = self.apply_threshold(raw_data_ptr, width, height, tval)
        dataptr = ctypes.cast(dataptr, ctypes.POINTER(ctypes.c_ubyte))
        return [dataptr[i] for i in range(width*height)]


