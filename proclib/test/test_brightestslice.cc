#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(48,32,8,img_sample);
    int x, y;
    imp.getBrightestSlice(&x, &y);
    if (x != 3 && y != 1) {
        TEST_RESULT("wrong area: %d:%d. expected: 3:1\n");
        return -1;
    }
    return 0;
}
