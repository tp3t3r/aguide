#include "imgproc.h"

#include "test_actions.h"
#include "TestFrame.h"

int main(int argc, char** argv) {

    TestFrame tf;
    ImageProcessor imp(32,32,8,tf.getFrame());

    int xstart,ystart;
    imp.getSpotCoordinates(&xstart, &ystart);
    
    int xnew,ynew;
    int xoffset = 10;
    int yoffset = 13;
    tf.shiftFrame(xoffset,yoffset);
    imp.addFrame(tf.getFrame());
    imp.getSpotCoordinates(&xnew, &ynew);

    if ((xnew - xstart != xoffset) || (ynew - ystart) != yoffset) {
        TEST_RESULT("%d:%d is not %d:%d\n", xstart, ystart, xstart+xoffset, ynew+yoffset);
        return -1;
    }
    return 0;
}
