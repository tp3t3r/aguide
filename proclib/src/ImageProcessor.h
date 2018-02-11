#pragma once

typedef unsigned char t_pixel;

class ImageProcessor {
    public:
        ImageProcessor(int width, int height, int slice_size, const t_pixel* data);
        ~ImageProcessor();
        void getBrightestSlice(int *x, int *y);
        void getSpotCoordinates(int * x, int * y, int locked);
        void setThreshold(int th);
        void addFrame(const t_pixel *data);
        const t_pixel* getBuffer(void);

    private:
        t_pixel* _data;
        int _slice_size;
        int _slice_count;
        int _width, _height;
        int _threshold;
        int * _slice_weights;
};

