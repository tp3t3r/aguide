#include "imgproc.h"
#include <stdio.h>
#include <string.h>

//global image data
unsigned img_width = 0;
unsigned img_height = 0;
unsigned char* img_buffer = nullptr;
unsigned int area_count = 0;
int* area_weights = nullptr;

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
    img_buffer = nullptr;
    delete [] area_weights;
    area_weights = nullptr;
    area_count = 0;
}

void apply_threshold(unsigned char tval) {
    for(unsigned i = 0; i < img_width*img_height; i++) {
        img_buffer[i] = *(img_buffer+i) < tval ? *(img_buffer+i):0xFF;
    }
}

int get_brightest_area(unsigned slice_size) {
    area_count = (img_width / slice_size) * (img_height / slice_size);
    area_weights = new int[area_count];
    for (unsigned i = 0; i < area_count; i++) { area_weights[i] = 0; }

    //calculate slice values
    for(unsigned i = 0; i < img_width*img_height; i++) {
        unsigned c_index = (i % img_width)/slice_size + (i/(img_width*slice_size))*slice_size;
        area_weights[c_index] = *(img_buffer+i) + area_weights[c_index];
    }

    //finding max
    int ret = -1;
    for (unsigned i = 0; i < area_count; i++ ) {
        if(area_weights[i] > ret) {
            ret = i;
        }
    }
    return ret;
}

unsigned char* get_image_buffer() {
    return img_buffer;
}

//meta
const char * get_lib_version() {
    return "imgproc 1.8";
}


