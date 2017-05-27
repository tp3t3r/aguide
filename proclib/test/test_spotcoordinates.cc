#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(32,32,4,img_sample);
    //slices are 4x4
    int area_index = imp.getBrightestArea();
    //should be 56
    int x,y;
    imp.getSpotCoordinates(&x, &y);
    if (x < 0 || y < 0) {
        TEST_RESULT("Can't get coordinates\n");
        return -1;
    }
    return 0;
}
