#pragma once

#include "ImageProcessor.h"


//A native C wrapper for Python
extern "C" {
    const char* get_lib_version(void);
    void init_image(unsigned width, unsigned height, const unsigned char* data);
    void apply_threshold(unsigned char tval);
    int get_brightest_area(unsigned slice_size);
    const unsigned char* get_image_buffer(void);
}


