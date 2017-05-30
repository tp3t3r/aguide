#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(48,32,8,img_sample);

    int x, y, x2, y2;

    imp.getSpotCoordinates(&x, &y);

    imp.addFrame(img_sample2);
    imp.getSpotCoordinates(&x2, &y2);

    int diffx = x2 - x;
    int diffy = y2 -y; 

    if (diffx != -8 && diffy != 5) {
        TEST_RESULT("move %d,%d -> %d,%d\n", x, y, x2, y2);
        return -1;
    }
    
    return 0;
}
