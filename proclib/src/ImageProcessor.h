#pragma once

class ImageProcessor {
    public:
        ImageProcessor(int width, int height, int slice_size, const char* data);
        ~ImageProcessor();
        void applyThreshold(char tvalue);
        void getBrightestSlice(int *x, int *y, int *b);
        void getSpotCoordinates(int * x, int * y);
        const char* getBuffer(void);

    private:
        char* _data;
        int _slice_size;
        //int _slice_count;
        int _width, _height;
        //int * _slice_weights;
};

