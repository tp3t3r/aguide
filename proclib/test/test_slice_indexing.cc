#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    int size = 4;
    unsigned idx = 0;
    init_image(32, 32, img_sample);
    for(int i = 0; i < 32*32; i++) {
        idx = get_slice_index(i, size);
    }
    if (idx == 63) {
        return 0;
    } else {
        TEST_RESULT("should be 63 :(");
        return -1;
    }
}
