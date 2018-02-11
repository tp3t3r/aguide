#include "imgproc.h"

#include "test_actions.h"
#include <string.h>

int main(int argc, char** argv) {
    int w=640;
    int h=480;

    t_pixel * empty = new t_pixel[w*h];
    memset(empty, 0, w*h);
    ImageProcessor imp(w,h,16,empty);

    int x, y;
    imp.getSpotCoordinates(&x, &y, 0);
    if (x != -1 || y != -1) {
        TEST_RESULT("should be -1;-1\n");
        return -1;
    }
    return 0;
}
