#include "imgproc.h"

void apply_threshold(unsigned char* img, unsigned width, unsigned height, unsigned char tval) {
    if (img) {
        for(unsigned i = 0; i < width*height; i++) {
            *(img+i) = *(img+i) <= tval ? 0x00:0xFF;
        }
    }
}
