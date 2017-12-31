#pragma once

#include "ImageProcessor.h"

class TestFrame {
    public:
        TestFrame();
        ~TestFrame();
        void shiftFrame(int x, int y);
        const t_pixel * getFrame(void);
        void addLargerSpot(int x, int y);
        void printFrame(void);
    private:
        t_pixel *_data;
        int _width, _height;
};

