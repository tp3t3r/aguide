#include "imgproc.h"

#include "test_actions.h"
#include "img_sample.h"

int test_spotcoords() {
    init_image(48,32,img_sample, 8);
    int x=-42, y=-412412;
    get_spot_coordinates(&x, &y, 0);
    if (x != 27 && y != 12) {
        TEST_RESULT("wrong coordinates: %d:%d\n", x, y);
        return -1;
    }
    return 0;

}

int main(int argc, char** argv) {
    if (test_spotcoords()){
        return -1;
    }
    return 0;
}
