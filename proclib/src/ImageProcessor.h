#pragma once

class ImageProcessor {
    public:
        ImageProcessor(int width, int height, int slice_size, const unsigned char* data);
        ~ImageProcessor();
        void getBrightestSlice(int *x, int *y, int *b);
        void getSpotCoordinates(int * x, int * y);
        void lockSpot(bool);
        void setThreshold(int th);
        void addFrame(const unsigned char *data);
        const unsigned char* getBuffer(void);

    private:
        unsigned char* _data;
        int _slice_size;
        int _slice_count;
        int _width, _height;
        int _threshold;
        bool _locked; 
        int * _slice_weights;
};

