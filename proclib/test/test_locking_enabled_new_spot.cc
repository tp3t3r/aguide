#include "imgproc.h"

#include "test_actions.h"
#include "TestFrame.h"

int main(int argc, char** argv) {

    TestFrame tf;
    ImageProcessor imp(32,32,8,tf.getFrame());

    int x,y;
    int x2,y2;
    imp.getSpotCoordinates(&x, &y, false);
    printf("%d:%d\n", x, y);
    
    tf.addLargerSpot(12,14);
    imp.addFrame(tf.getFrame());
    imp.getSpotCoordinates(&x2, &y2, true);
    
    if ((x != x2) || (y != y2)) {
        TEST_RESULT("locking didn't work\n");
        return -1;
    }
    return 0;
}
