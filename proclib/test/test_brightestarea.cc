#include "imgproc.h"

<<<<<<< HEAD
=======
#include "test_actions.h"
>>>>>>> [Test] brightest area finder testcase added
#include "img_sample.h"

int main(int argc, char** argv) {
    init_image(32,32, img_sample);
    //slices are 4x4
    unsigned slicesize = 4;
    int area_index = get_brightest_area(slicesize);
    if (area_index < 0 ) {
        TEST_RESULT("Can't determine brightest area\n");
        return -1;
    }
    if (area_index != 54) {
        TEST_RESULT("We did not expect that.: %d vs %d\n", area_index, 54);
        return -1;
    }
    return 0;
}
