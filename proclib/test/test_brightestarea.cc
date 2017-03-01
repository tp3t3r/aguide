#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(32,32,4,img_sample);
    //slices are 4x4
    int area_index = imp.getBrightestArea();
    if (area_index < 0 ) {
        TEST_RESULT("Can't determine brightest area\n");
        return -1;
    }
    if (area_index != 56) {
        TEST_RESULT("We did not expect that.: %d vs %d\n", area_index, 54);
        return -1;
    }
    return 0;
}
