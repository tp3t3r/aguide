#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(48,32,8,img_sample3);
    int lx=26; //should be 29:15 
    int ly=11;
    imp.getSpotCoordinates(&lx, &ly, 1);
    if (lx != 29 || ly != 15) {
        TEST_RESULT("Invalid coordiates: %d:%d\n", lx, ly);
        return -1;
    }
    printf("%d,%d\n", lx,ly);
    return 0;
}
