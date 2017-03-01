#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(32, 32, 4, img_sample);
    int idx;
    for(int i = 0; i < 32*32; i++) {
        idx = imp.getSliceIndex(i);
    }
    if (idx == 63) {
        return 0;
    } else {
        TEST_RESULT("should be 63 :(");
        return -1;
    }
}
