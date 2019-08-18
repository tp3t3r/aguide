#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(48,32,8,img_sample3);
    int lx=40; //should be 29:15 
    int ly=8;
    imp.getSpotCoordinates(&lx, &ly, 1);
    if (lx != -1 || ly != -1) {
        TEST_RESULT("Invalid coordiates: %d:%d\n", lx, ly);
        return -1;
    }
    printf("unlocked. %d,%d\n", lx,ly);
    return 0;
}
