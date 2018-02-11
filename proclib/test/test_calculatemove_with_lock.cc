#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int main(int argc, char** argv) {
    ImageProcessor imp(48,32,8,img_sample);

    int x, y;

    imp.getSpotCoordinates(&x, &y, 0);
    if (x == -1 || y == -1) {
        TEST_RESULT("Fail, can't find spot\n");
        return -1;
    }

    imp.addFrame(img_sample3);
    
    int x2=x;
    int y2=y;
    //locked
    imp.getSpotCoordinates(&x2, &y2, 1);

    int diffx = x2 - x;
    int diffy = y2 - y; 

    if (diffx != 2 && diffy != 3) {
        TEST_RESULT("move %d,%d -> %d,%d\n", x, y, x2, y2);
        return -1;
    }
    
    return 0;
}
