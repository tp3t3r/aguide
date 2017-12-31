#include "TestFrame.h"
#include <stdio.h>
#include <string.h>

//global
#define O 0x00
#define X 0xFF
const unsigned char sampleFrame[] = {
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
 
    O,O,O,O,O,O,O,O, X,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,X,X,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,X,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,

    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O,
    O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O, O,O,O,O,O,O,O,O
};
TestFrame::TestFrame() {
    _width = 32;
    _height = 32;
    _data = new unsigned char[_width*_height];
    memcpy(_data, sampleFrame, _width*_height);
}

void TestFrame::printFrame(void) {
    int h,w;
    for(h=0; h<_height; h++) {
        for(w=0; w<_width; w++) {
            printf("%02x ", *(_data+w+h*_width));
        }
        printf("\n");
    }
    printf("\n");
}

TestFrame::~TestFrame() {
    delete [] _data;
}

void TestFrame::shiftFrame(int xoffset, int yoffset) {
    //move x - every line
    int linesize = _width;
    unsigned char * newline = new unsigned char[linesize];
    if (0 < xoffset && xoffset < linesize) {
        for(int h=0; h < _height; h++) {
            memset(newline, 0, linesize);
            memcpy(newline+xoffset, _data+h*linesize, linesize-xoffset);
            memcpy(_data+h*linesize, newline, linesize);
        }
    }
    delete [] newline;

    //move y - every column
    if (0 < yoffset && yoffset < _height) {
        for(int h=_height-1; h >= yoffset; h--) {
            memcpy(_data+h*linesize, _data+(h-yoffset)*linesize, linesize);
        }
        //then fill the new lines
        for(int i=0; i<yoffset; i++) {
            memset(_data+i*linesize, 0, linesize);
        }
        //printFrame();
    }
}

void TestFrame::addLargerSpot(int x, int y) {
    int size = 5;
    int linesize = _width;
    for(int i=0; i < size; i++) {
        memset(_data+(y+i)*linesize+x, 0xFF, size);
    }
}

const unsigned char * TestFrame::getFrame(void) {
    return const_cast<const unsigned char*>(_data);
}
