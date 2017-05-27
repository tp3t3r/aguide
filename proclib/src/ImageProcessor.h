#pragma once

class ImageProcessor {
    public:
        ImageProcessor(unsigned width, unsigned height, unsigned slice_size, const unsigned char* data);
        ~ImageProcessor();
        void applyThreshold(unsigned char tvalue);
        int getBrightestArea(void);
        void getSpotCoordinates(int * x, int * y);
        const unsigned char * getBuffer(void);
        unsigned getSliceIndex(unsigned idx);

    private:
        //data
        unsigned _area_count;
        int * _area_weights;

        unsigned char* _data;
        unsigned _slice_size;
        unsigned _width, _height;
};

