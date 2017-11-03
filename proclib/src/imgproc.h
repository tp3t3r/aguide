#pragma once

#include "ImageProcessor.h"


//A native C wrapper for Python
extern "C" {
    const char* get_lib_version(void);
    void init_image(int width, int height, const char* data);
    void get_spot_coordinates(int *x, int *y);
    int lock_spot(void);
    void set_threshold(int th);
    const char* get_image_buffer(void);
}


