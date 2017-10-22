#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(48,32,8,img_sample);
    int x, y;
    imp.getSpotCoordinates(&x, &y, false);
    if (x != 27 && y != 12) {
        TEST_RESULT("wrong spot: %d:%d. expected: 27:12\n", x, y);
        return -1;
    }
    return 0;
}
