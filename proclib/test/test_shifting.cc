#include "imgproc.h"

#include "test_actions.h"
#include "TestFrame.h"

int main(int argc, char** argv) {

    TestFrame tf;
    ImageProcessor imp(32,32,8,tf.getFrame());

    int xstart,ystart;
    imp.getSpotCoordinates(&xstart, &ystart, 0);
    if (xstart == -1 || ystart == -1) {
        TEST_RESULT("Fail to get spot coordinates\n");
        return -1;
    }
    
    int xnew=xstart;
    int ynew=ystart;
    int xoffset = 3;
    int yoffset = 4;
    tf.shiftFrame(xoffset,yoffset);
    imp.addFrame(tf.getFrame());
    imp.getSpotCoordinates(&xnew, &ynew, 1);

    if ((xnew - xstart != xoffset) || (ynew - ystart) != yoffset) {
        TEST_RESULT("%d:%d is not %d:%d\n", xstart, ystart, xstart+xoffset, ynew+yoffset);
        return -1;
    }
    return 0;
}
