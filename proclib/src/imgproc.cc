#include "imgproc.h"
#include <stdio.h>
#include <string.h>

//global image data
unsigned img_width = 0;
unsigned img_height = 0;
unsigned char* img_buffer = 0;

//functions
void init_image(unsigned width, unsigned height, const unsigned char* data) {
    img_width = width;
    img_height = height;
    if (img_buffer) {
        delete [] img_buffer;
    }
    img_buffer = new unsigned char[img_width * img_height];
    memcpy(img_buffer, data, img_width * img_height);
}

void destroy(void) {
    img_width = 0;
    img_height = 0;
    delete [] img_buffer;
    img_buffer = 0;
}

void apply_threshold(unsigned char tval) {
    for(unsigned i = 0; i < img_width*img_height; i++) {
        img_buffer[i] = *(img_buffer+i) < tval ? *(img_buffer+i):0xFF;
    }
}

unsigned get_brightest_area(unsigned slice_size) {
    return 57;
}

unsigned char* get_image_buffer() {
    return img_buffer;
}

//meta
const char * get_lib_version() {
    return "imgproc 1.8";
}


