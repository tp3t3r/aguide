#include "ImageProcessor.h"
#include <stdio.h>
#include <string.h>

ImageProcessor::ImageProcessor(unsigned width, unsigned height, unsigned slice_size, const unsigned char* data) {
    _width = width;
    _height = height;
    _slice_size = slice_size;
    _slice_count = _width / slice_size * _height / slice_size;
    _slice_weights = new unsigned[_slice_count];
    _data = new unsigned char[_width * _height];
    memcpy(_data, data, _width * _height);

}

void ImageProcessor::applyThreshold(unsigned char tval) {
    for(unsigned i = 0; i < _width*_height; i++) {
        _data[i] = *(_data+i) < tval ? *(_data+i):0xFF;
    }
}

void ImageProcessor::getBrightestSlice(int *x_area, int *y_area) {
    unsigned iy, ix;
    //calculate areas
    for(iy = 0; iy<_height; iy++) {
        for(ix = 0; ix<_width; ix++) {
            int area_index = ix/_slice_size + (iy/_slice_size)*(_width/_slice_size);
            unsigned pixel = *(_data+ix+iy*_width);
            _slice_weights[area_index] = *(_slice_weights + area_index) + pixel;
        }
    }
    //finding max
    *x_area = -1;
    *y_area = -1;
    unsigned max_brightness = 0;
    unsigned brightest_idx = 0;
    for(unsigned i=0; i < _slice_count; i++) {
        if(_slice_weights[i] > max_brightness) {
            max_brightness = _slice_weights[i];
            brightest_idx = i;
        }
    }
    //transform index to 2D cooradinate
    *x_area = ( brightest_idx % (_width / _slice_size));
    *y_area = ( brightest_idx / (_width / _slice_size));
}

void ImageProcessor::getSpotCoordinates(int * x, int * y) {
    *x = -1;
    *y = -1;

    int x_area, y_area;
    getBrightestSlice(&x_area, &y_area);
    if ( x < 0 || y < 0) {
        return;
    }
    unsigned x_offset = x_area * _slice_size;
    unsigned y_offset = y_area * _slice_size;
     //center
    *x = x_offset + _slice_size / 2;
    *y = y_offset + _slice_size / 2;

    //iterate over the selected area
    unsigned ix, iy;
    unsigned tl_x = 0;
    unsigned tl_y = 0;
    unsigned br_x = 0;
    unsigned br_y = 0;
    for(iy=y_offset; iy < y_offset + _slice_size; iy++) {
        for(ix=x_offset; ix < x_offset + _slice_size; ix++) {
            unsigned pixel = *(_data+ix+iy*_width);
            if(pixel > 0) {
                //top-left
                if (ix <= tl_x) tl_x = ix;
                if (iy <= tl_y) tl_y = iy;
                //bottom-right
                if (ix >= br_x) br_x = ix;
                if (iy >= br_y) br_y = iy;
            }
        }
    }
    //average
    *x = (br_x - tl_x)/2;
    *y = (br_y - tl_y)/2;
}

const unsigned char* ImageProcessor::getBuffer(void) {
    return const_cast<const unsigned char*>(_data);
}

ImageProcessor::~ImageProcessor() {
    delete [] _data;
    delete [] _slice_weights;
}


