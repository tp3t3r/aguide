#pragma once

class TestFrame {
    public:
        TestFrame();
        ~TestFrame();
        void shiftFrame(int x, int y);
        const unsigned char * getFrame(void);
        void addLargerSpot(int x, int y);
        void printFrame(void);
    private:
        unsigned char *_data;
        int _width, _height;
};

