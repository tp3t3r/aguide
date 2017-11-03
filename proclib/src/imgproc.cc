#include "imgproc.h"

//globals
ImageProcessor * imp = nullptr;

//meta
const char * get_lib_version() {
    return "imgproc 1.8";
}

void init_image(int width, int height, const char* data) {
    if (imp) {
        delete imp;
        imp = nullptr;
    }
    unsigned slice = 16; // 16x16 segments

    imp = new ImageProcessor(width, height, slice, data);
}

void get_spot_coordinates(int *x, int *y) {
    if (imp) {
        imp->getSpotCoordinates(x, y);
    }
}

int lock_spot(void) {
    //todo
}

void set_threshold(int th) {
    if (imp) {
        imp->setThreshold(th);
    }
}

const char* get_image_buffer(void) {
    if (imp) {
        return imp->getBuffer();
    }
    return nullptr;
}

