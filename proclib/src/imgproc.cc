#include "imgproc.h"

//globals
ImageProcessor * imp = nullptr;

//meta
const char * get_lib_version() {
    return "imgproc 1.8";
}

void init_image(int width, int height, const t_pixel* data, unsigned slice_size) {
    if (imp) {
        delete imp;
        imp = nullptr;
    }
    imp = new ImageProcessor(width, height, slice_size, data);
}

void get_spot_coordinates(int *x, int *y, int locked) {
    if (imp) {
        imp->getSpotCoordinates(x, y, locked);
    }
}

void set_threshold(int th) {
    if (imp) {
        imp->setThreshold(th);
    }
}

const t_pixel* get_image_buffer(void) {
    if (imp) {
        return imp->getBuffer();
    }
    return nullptr;
}

