#include "imgproc.h"

const char * get_lib_version() {
    return "imgproc 1.0";
}

char * apply_threshold(const char* img, unsigned width, unsigned height, unsigned char tval) {
    static char* buffer;
    if (buffer) {
        delete [] buffer;
    } else {
        buffer = new char[width * height];
    }

    if (img) {
        for(unsigned i = 0; i < width*height; i++) {
            buffer[i] = *(img+i) < tval ? *(img+i):0xFF;
        }
        return buffer;
    } else {
        return 0;
    }
}
