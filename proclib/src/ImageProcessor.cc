#include "ImageProcessor.h"
#include <stdio.h>
#include <string.h>

ImageProcessor::ImageProcessor(int width, int height, int slice_size, const char* data) {
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
     
    _data = new char[_width * _height];
    addFrame(data);
}

void ImageProcessor::addFrame(const char* data) {
    if (data) {
        memcpy(_data, data,  _width * _height);
    }
}

void ImageProcessor::setThreshold(int th) {
    _threshold = th;
}

void ImageProcessor::getBrightestSlice(int *x_area, int *y_area, int *brightness) {
    memset(_slice_weights, 0, _slice_count*sizeof(_slice_count));
    int iy, ix;
    //calculate area
    int maxpix = 0;
    for(iy = 0; iy<_height; iy++) {
        for(ix = 0; ix<_width; ix++) {
            int area_index = ix/_slice_size + (iy/_slice_size)*(_width/_slice_size);
            int pixel = *(_data+ix+iy*_width);
            if (pixel > maxpix) {
                maxpix = pixel;
            }
            if (pixel > _threshold) {
                _slice_weights[area_index]++;
            }
        }
    }
    //printf("max value: %d\n", maxpix);

    //finding max
    *x_area = -1;
    *y_area = -1;
    *brightness = -1;
    int brightest_idx = 0;
    for(int i=0; i < _slice_count; i++) {
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

void ImageProcessor::getSpotCoordinates(int * x, int * y, bool isLocked) {
    int ix, iy;
    int x_offset, y_offset;
    int sumx=0;
    int sumy=0;
    int pixelCount = 0; //above threshold

    if (!isLocked) {
        int x_area, y_area, brightness;
        //get the brightest part first
        getBrightestSlice(&x_area, &y_area, &brightness);
        if ( x_area < 0 || y_area < 0 || brightness < 1) {
            //printf("not bright spot");
            return;
        }
        pixelCount = brightness;
        x_offset = x_area * _slice_size;
        y_offset = y_area * _slice_size;
    } else {
        //not locked, check the neighbors of (given) X:Y
        //TODO: check if they're on the edge of the frame
        x_offset = *x - _slice_size / 2;
        y_offset = *y - _slice_size / 2;
    }
    //iterate over the selected area, calculate coordinate averages
    for(iy=y_offset; iy < y_offset + _slice_size; iy++) {
        for(ix=x_offset; ix < x_offset + _slice_size; ix++) {
            int pixel = *(_data+ix+iy*_width);
            //printf("%03d ", pixel);
            if(pixel > _threshold) {
                if (isLocked) {
                    pixelCount++;
                }
                sumx += ix;
                sumy += iy;
            }
        }
        //printf("\n");
    }
    //printf("spot: %d:%d [%d]\n", sumx/pixelCount, sumy/pixelCount, pixelCount);
    *x = sumx/pixelCount;
    *y = sumy/pixelCount;
}

const char* ImageProcessor::getBuffer(void) {
    return const_cast<const char*>(_data);
}

ImageProcessor::~ImageProcessor() {
    delete [] _data;
    delete [] _slice_weights;
}
