#pragma once

class TestFrame {
    public:
        TestFrame();
        ~TestFrame();
        void shiftFrame(int x, int y);
        const char * getFrame(void);
        void printFrame(void);
    private:
        char *_data;
        int _width, _height;
};

