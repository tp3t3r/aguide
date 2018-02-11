#include "imgproc.h"

#include "test_actions.h"
#include "TestFrame.h"

int main(int argc, char** argv) {

    TestFrame tf;
    ImageProcessor imp(32,32,8,tf.getFrame());

    int startx,starty;
    imp.getSpotCoordinates(&startx, &starty, 0);

    if (startx == -1 || starty == -1) {
        TEST_RESULT("Fail, can't lock");
        return -1;
    }

    int cx=startx;
    int cy=starty;
    int shift_count = 14;
    for (int i=0; i < shift_count; i++) {
        tf.shiftFrame(1,1);
        imp.addFrame(tf.getFrame());
        imp.getSpotCoordinates(&cx, &cy, 1);
        printf("coords: %d,%d\n", cx, cy);
    }
    if ((startx + shift_count != cx) || (starty + shift_count != cy)) {
        TEST_RESULT("Failed to track\n");
        return -1;
    }
    return 0;
}
