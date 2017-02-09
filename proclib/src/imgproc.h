#pragma once

extern "C" {
    const char* get_lib_version(void);
    unsigned char* apply_threshold(const unsigned char* img, unsigned width, unsigned height, unsigned char tval);
}

