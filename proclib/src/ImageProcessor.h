#pragma once

class ImageProcessor {
    public:
        ImageProcessor(unsigned width, unsigned height, unsigned slice_size, const unsigned char* data);
        ~ImageProcessor();
        void applyThreshold(unsigned char tvalue);
        void getBrightestSlice(int *x, int *y);
        void getSpotCoordinates(int * x, int * y);
        const unsigned char * getBuffer(void);

    private:
        unsigned char* _data;
        unsigned _slice_size;
        unsigned _slice_count;
        unsigned _width, _height;
        unsigned * _slice_weights;
};

