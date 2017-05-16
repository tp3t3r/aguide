#include "imgproc.h"

//globals
ImageProcessor * imp = nullptr;

//meta
const char * get_lib_version() {
    return "imgproc 1.8";
}

void init_image(unsigned width, unsigned height, const unsigned char* data) {
    if (imp) {
        delete imp;
        imp = nullptr;
    }
    unsigned slice = 16; // 16x16 segments
    imp = new ImageProcessor(width, height, slice, data);
}

void apply_threshold(unsigned char tval) {
    if (imp) {
        imp->applyThreshold(tval);
    }
}

int get_brightest_area(void) {
    if (imp) {
        return imp->getBrightestArea();
    }
    return -1;
}

const unsigned char* get_image_buffer(void) {
    if (imp) {
        return imp->getBuffer();
    }
    return nullptr;
}
