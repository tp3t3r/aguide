#include "imgproc.h"

#include "test_actions.h"

int test_thresholding() {
    const char input_data[] = { 10, 20, 30, 40, 200, 201, 202, 200, 200 };
    const char out_data[] =   { 10, 20, 30, 40, 255, 255, 255, 255, 255 };

    init_image(3,3,input_data);
    apply_threshold(200);
    const char* data = get_image_buffer();
    for(int i=0; i<9; i++) {
        if (*(data+i) != out_data[i]) {
            TEST_RESULT("Thresholding failed");
            return -1;
        }
    }
    return 0;

}

int main(int argc, char** argv) {
    if (test_thresholding()){
        return -1;
    }
    if (test_thresholding()){
        return -1;
    }
     if (test_thresholding()){
        return -1;
    }
    return 0;
}
