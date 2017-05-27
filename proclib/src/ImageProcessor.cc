#include "ImageProcessor.h"
#include <stdio.h>
#include <string.h>

ImageProcessor::ImageProcessor(unsigned width, unsigned height, unsigned slice_size, const unsigned char* data) {
    _width = width;
    _height = height;
    _slice_size = slice_size;
    _data = new unsigned char[_width * _height];
    memcpy(_data, data, _width * _height);

    _area_count = (_width / _slice_size) * (_height / _slice_size);
    _area_weights = new int[_area_count];
    for (unsigned i = 0; i < _area_count; i++) { _area_weights[i] = 0; }

}

void ImageProcessor::applyThreshold(unsigned char tval) {
    for(unsigned i = 0; i < _width*_height; i++) {
        _data[i] = *(_data+i) < tval ? *(_data+i):0xFF;
    }
}

int ImageProcessor::getBrightestArea() {
   //calculate slice values
    for(unsigned i = 0; i < _width*_height; i++) {
        unsigned c_index = getSliceIndex(i);
        _area_weights[c_index] = *(_data+i) + _area_weights[c_index];
    }

    //finding max
    int ret = -1;
    for (unsigned i = 0; i < _area_count; i++ ) {
        if(_area_weights[i] > ret) {
            ret = i;
        }
    }
    return ret;
}
void ImageProcessor::getSpotCoordinates(int * x, int * y) {
    *x = -1;
    *y = -1;
}

unsigned ImageProcessor::getSliceIndex(unsigned idx) {
    unsigned cx, cy;
    cx = idx % _width;
    cy = idx / _width;
    return cx/_slice_size + (cy/_slice_size)*(_width/_slice_size);
}

const unsigned char* ImageProcessor::getBuffer(void) {
    return const_cast<const unsigned char*>(_data);
}

ImageProcessor::~ImageProcessor() {
    delete [] _data;
    delete [] _area_weights;
}


