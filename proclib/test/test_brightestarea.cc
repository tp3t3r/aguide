#include "imgproc.h"

#include "img_sample.h"

int main(int argc, char** argv) {
    init_image(32,32, img_sample);
    //slices are 4x4
    unsigned slicesize = 4;
    unsigned area_index = get_brightest_area(slicesize);
    if (area_index != 57) {
        return -1;
    }
    return 0;

}
