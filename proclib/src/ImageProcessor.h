#pragma once

class ImageProcessor {
    public:
        ImageProcessor(int width, int height, int slice_size, const char* data);
        ~ImageProcessor();
        void getBrightestSlice(int *x, int *y, int *b);
        void getSpotCoordinates(int * x, int * y);
        void lockSpot(bool);
        void setThreshold(int th);
        void addFrame(const char *data);
        const char* getBuffer(void);

    private:
        char* _data;
        int _slice_size;
        int _slice_count;
        int _width, _height;
        int _threshold;
        bool _locked; 
        int * _slice_weights;
};

