#include "imgproc.h"

#include "test_actions.h"
#include "TestFrame.h"

int main(int argc, char** argv) {

    TestFrame tf;
    ImageProcessor imp(32,32,8,tf.getFrame());

    int xstart,ystart;
    imp.getSpotCoordinates(&xstart, &ystart);

    int xnew,ynew;

    for (int i=0; i < 30; i++) {
        tf.shiftFrame(1,1);
        imp.addFrame(tf.getFrame());
        imp.getSpotCoordinates(&xnew, &ynew);
        printf("diff: %d,%d\n", xnew-xstart, ynew-ystart);
    }

    
    return 0;
}
