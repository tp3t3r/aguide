#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(48,32,8,img_sample);
    int x, y, b;
    imp.getBrightestSlice(&x, &y, &b);
    if (x != 3 && y != 1) {
        TEST_RESULT("wrong area: %d:%d. expected: 3:1\n", x,y );
        return -1;
    }
    if (b != 23) {
        TEST_RESULT("invalid brightness value: %d. expected: 23\n", b);
    }
    return 0;
}
