#include "ImageProcessor.h"
#include <stdio.h>
#include <string.h>

ImageProcessor::ImageProcessor(int width, int height, int slice_size, const unsigned char* data) {
#ifndef PRODUCTION_BUILD
    _width = width;
    _height = height;
    _slice_size = slice_size;
#else
    _width = 320;
    _height = 240;
    _slice_size = 16;
#endif

    _slice_count = _width / _slice_size * _height / _slice_size;
    _threshold = 85; //default
    _slice_weights = new int[_slice_count];
    _locked = false;
     
    _data = new unsigned char[_width * _height];
    addFrame(data);
}

void ImageProcessor::addFrame(const unsigned char* data) {
    if (data) {
        memcpy(_data, data,  _width * _height);
    }
}

void ImageProcessor::setThreshold(int th) {
    _threshold = th;
}
void ImageProcessor::lockSpot(bool enable) {
    _locked = enable;
}
void ImageProcessor::getBrightestSlice(int *x_area, int *y_area, int *brightness) {
    memset(_slice_weights, 0, _slice_count*sizeof(_slice_count));
    int iy, ix;
    //calculate area
    for(iy = 0; iy<_height; iy++) {
        for(ix = 0; ix<_width; ix++) {
            int area_index = ix/_slice_size + (iy/_slice_size)*(_width/_slice_size);
            int pixel = *(_data+ix+iy*_width);
            if (pixel > _threshold) {
                _slice_weights[area_index]++;
            }
        }
    }
    //finding max - skip the edges (thickness: _slice_size)
    *x_area = -1;
    *y_area = -1;
    *brightness = -1;
    int brightest_idx = 0;
    for(int i=0; i < _slice_count; i++) {
        int slice_per_line = _width / _slice_size;
        if (i < slice_per_line) continue; // skip the first lines
        if (i > _slice_count - slice_per_line) continue; //skip the last line
        if ((i % slice_per_line == 0) || (i % slice_per_line == slice_per_line - 1)) continue; //skip the left and right sides
        if(_slice_weights[i] > *brightness) {
            *brightness = _slice_weights[i];
            brightest_idx = i;
        }
        //printf("sw[%d]: %d\n", i, _slice_weights[i]);
    }
    //transform index to 2D cooradinate
    *x_area = ( brightest_idx % (_width / _slice_size));
    *y_area = ( brightest_idx / (_width / _slice_size));

}

void ImageProcessor::getSpotCoordinates(int * x, int * y) {
    *x = -1;
    *y = -1;

    static int x_area, y_area, brightness;
    if ( !_locked) {
        getBrightestSlice(&x_area, &y_area, &brightness);
        if ( x_area < 0 || y_area < 0 || brightness < 1) {
            //printf("not bright spot");
            return;
        }
    }
    int iy,ix;
    int x_offset = x_area * _slice_size;
    int y_offset = y_area * _slice_size;
    int sumx = 0;
    int sumy = 0;

    //iterate over the selected area, calculate coordinate averages
    for(iy=y_offset; iy < y_offset + _slice_size; iy++) {
        for(ix=x_offset; ix < x_offset + _slice_size; ix++) {
            int pixel = *(_data+ix+iy*_width);
            //printf("%03d ", pixel);
            if(pixel > _threshold) {
                sumx += ix;
                sumy += iy;
            }
        }
        //printf("\n");
    }
    //printf("spot: %d:%d [%d]\n", sumx/brightness, sumy/brightness, brightness);
    *x = sumx/brightness;
    *y = sumy/brightness;
}

const unsigned char* ImageProcessor::getBuffer(void) {
    return const_cast<const unsigned char*>(_data);
}

ImageProcessor::~ImageProcessor() {
    delete [] _data;
    delete [] _slice_weights;
}
