#include "imgproc.h"

#include "test_actions.h"
#include "TestFrame.h"

int main(int argc, char** argv) {

    TestFrame tf;
    ImageProcessor imp(32,32,8,tf.getFrame());

    int x,y;
    int x2,y2;
    imp.getSpotCoordinates(&x, &y);
    printf("%d:%d\n", x, y);
    
    imp.lockSpot(true);

    tf.addLargerSpot(22,24);
    imp.addFrame(tf.getFrame());
    imp.getSpotCoordinates(&x2, &y2);
    
    if ((x != x2) || (y != y2)) {
        TEST_RESULT("locking didn't work\n");
        return -1;
    }
    return 0;
}
