#include "imgproc.h"

#include "test_actions.h"
#include <string.h>

int main(int argc, char** argv) {
    int w=640;
    int h=480;

    unsigned char * empty = new unsigned char[w*h];
    memset(empty, 0, w*h);
    ImageProcessor imp(w,h,16,empty);
    int x,y,b;
    imp.getBrightestSlice(&x,&y,&b);
    printf("%d,%d,%d\n", x, y, b);
    
    imp.getSpotCoordinates(&x, &y);
    return 0;
}
