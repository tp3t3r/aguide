#include "imgproc.h"
#include "stdio.h"

const char * get_lib_version() {
    return "imgproc 1.0";
}

unsigned char* apply_threshold(const unsigned char* img, unsigned width, unsigned height, unsigned char tval) {
    static unsigned char* buffer;
    if (buffer) {
        delete [] buffer;
    }
    buffer = new unsigned char[width * height];

    if (img) {
        for(unsigned i = 0; i < width*height; i++) {
            buffer[i] = *(img+i) < tval ? *(img+i):0xFF;
        }
        return buffer;
    } else {
        return 0;
    }
}
