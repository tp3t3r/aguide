#include "imgproc.h"

int test_thresholding() {
    const unsigned char input_data[] = { 10, 20, 30, 40, 200, 201, 202, 200, 200 };
    const unsigned char out_data[] =   { 10, 20, 30, 40, 255, 255, 255, 255, 255 };
    init_image(3,3, input_data);
    apply_threshold(200);
    unsigned char* imgbuf = get_image_buffer();
    for(int i=0; i<9; i++) {
        if (*(imgbuf+i) != out_data[i]) {
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
